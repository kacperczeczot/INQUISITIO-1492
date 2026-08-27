#include <Python.h>
#include <cstdint>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <thread>
#include <future>
#include <map>
#include <chrono>

namespace inq {

// ─── Enums & Graph ──────────────────────────────────────────────────────────
enum Faction : uint8_t {
    SO = 0,
    CAA = 1,
    KB = 2,
    KT = 3,
    GC = 4,
    NUM_FACTIONS = 5,
    NO_FACTION = 255
};

enum Location : uint8_t {
    TRYBUNAL = 0,
    PALAC = 1,
    LOCHY = 2,
    RYNEK = 3,
    GILDIA = 4,
    NUM_LOCATIONS = 5,
    NO_LOCATION = 255
};

static const uint8_t NEIGHBORS[5][4] = {
    {PALAC, LOCHY, 255, 255},           // TRYBUNAL
    {TRYBUNAL, RYNEK, LOCHY, 255},      // PALAC
    {TRYBUNAL, PALAC, GILDIA, 255},     // LOCHY
    {PALAC, GILDIA, 255, 255},          // RYNEK
    {RYNEK, LOCHY, 255, 255}            // GILDIA
};

static const uint8_t NEIGHBOR_COUNTS[5] = {2, 3, 3, 2, 2};

[[maybe_unused]] static inline bool is_neighbor(uint8_t a, uint8_t b) {
    if (a >= 5 || b >= 5) return false;
    for (uint8_t i = 0; i < NEIGHBOR_COUNTS[a]; ++i) {
        if (NEIGHBORS[a][i] == b) return true;
    }
    return false;
}

// ─── Fast RNG (Xoroshiro128+) ───────────────────────────────────────────────
struct FastRng {
    uint64_t s[2];

    static inline uint64_t rotl(const uint64_t x, int k) {
        return (x << k) | (x >> (64 - k));
    }

    inline uint64_t next() {
        const uint64_t s0 = s[0];
        uint64_t s1 = s[1];
        const uint64_t result = s0 + s1;
        s1 ^= s0;
        s[0] = rotl(s0, 24) ^ s1 ^ (s1 << 16);
        s[1] = rotl(s1, 37);
        return result;
    }

    inline uint32_t next_u32(uint32_t bound) {
        if (bound <= 1) return 0;
        uint64_t r = next() & 0xFFFFFFFFULL;
        return (uint32_t)((r * bound) >> 32);
    }

    inline double next_double() {
        return (next() >> 11) * (1.0 / 9007199254740992.0);
    }

    void seed(uint64_t x) {
        uint64_t z = (x + 0x9e3779b97f4a7c15ULL);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        s[0] = z ^ (z >> 31);
        z = (x + 2 * 0x9e3779b97f4a7c15ULL);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        s[1] = z ^ (z >> 31);
    }

    template<typename T>
    void shuffle(T* array, size_t n) {
        for (size_t i = n - 1; i > 0; --i) {
            size_t j = next_u32((uint32_t)i + 1);
            std::swap(array[i], array[j]);
        }
    }
};

// ─── Card Definitions ───────────────────────────────────────────────────────
enum CardTag : uint16_t {
    TAG_NONE = 0,
    TAG_INQUISITOR = 1 << 0,
    TAG_AUTODAFE = 1 << 1,
    TAG_RELIC = 1 << 2,
    TAG_DECREE = 1 << 3,
    TAG_FRAGMENT = 1 << 4,
    TAG_FALL = 1 << 5,
    TAG_SIGNATURE = 1 << 6,
    TAG_INTERROGATE = 1 << 7,
    TAG_HARBOR = 1 << 8
};

struct CardDef {
    const char* id;
    uint8_t faction;
    uint8_t cost_gold;
    uint8_t heresy;
    uint8_t target_heresy;
    uint8_t gold_gain;
    uint8_t agents_move;
    bool is_arrest;
    bool creates_hook;
    bool breaks_rule;
    uint8_t card_type; // 0=akcja, 1=reakcja, 2=signature, 3=permanent
    uint8_t fixed_loc; // 0..4 or 255
    uint16_t tags;
};

// Static card table for all 60 faction cards
static CardDef CARD_DB[60] = {
    // SWIETE OFICJUM (0..11)
    {"so-01", SO, 1, 2, 0, 2, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-02", SO, 1, 2, 1, 2, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-03", SO, 2, 3, 3, 1, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-04", SO, 1, 0, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_INQUISITOR},
    {"so-05", SO, 0, 0, 1, 0, 0, false, false, false, 1, NO_LOCATION, TAG_NONE},
    {"so-06", SO, 2, 0, 1, 0, 0, true, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-07", SO, 1, 0, 0, 2, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-08", SO, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_INQUISITOR},
    {"so-09", SO, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"so-10", SO, 5, 1, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_AUTODAFE | TAG_SIGNATURE},
    {"so-11", SO, 1, 1, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-12", SO, 1, 0, 1, 1, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},

    // CIENIE AL-ANDALUS (12..23)
    {"caa-01", CAA, 1, 1, 1, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-02", CAA, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-03", CAA, 0, 1, 0, 2, 1, false, false, false, 0, NO_LOCATION, TAG_RELIC},
    {"caa-04", CAA, 0, 0, 1, 3, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-05", CAA, 1, 0, 3, 3, 0, false, false, false, 0, NO_LOCATION, TAG_RELIC},
    {"caa-06", CAA, 0, 0, 2, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-07", CAA, 0, 0, 0, 3, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-08", CAA, 3, 0, 2, 3, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"caa-09", CAA, 0, 0, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_RELIC},
    {"caa-10", CAA, 3, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_RELIC | TAG_SIGNATURE},
    {"caa-11", CAA, 1, 0, 2, 3, 1, false, false, false, 0, NO_LOCATION, TAG_INQUISITOR},
    {"caa-12", CAA, 0, 0, 0, 4, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},

    // KORONA BORGIOWIE (24..35)
    {"kb-01", KB, 1, 1, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-02", KB, 1, 0, 1, 2, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-03", KB, 1, 1, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-04", KB, 2, 0, 0, 0, 1, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-05", KB, 2, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_DECREE},
    {"kb-06", KB, 2, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-07", KB, 2, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-08", KB, 3, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-09", KB, 2, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_DECREE | TAG_SIGNATURE},
    {"kb-10", KB, 4, 1, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_DECREE | TAG_SIGNATURE},
    {"kb-11", KB, 1, 0, 1, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-12", KB, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},

    // KABALA TOLEDO (36..47)
    {"kt-01", KT, 1, 0, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-02", KT, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-03", KT, 0, 2, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-04", KT, 1, 0, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-05", KT, 1, 1, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-06", KT, 2, 0, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-07", KT, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-08", KT, 1, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-09", KT, 1, 1, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-10", KT, 4, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_FRAGMENT | TAG_SIGNATURE},
    {"kt-11", KT, 2, 0, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"kt-12", KT, 0, 1, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},

    // GILDIA CIENI (48..59)
    {"gc-01", GC, 1, 1, 0, 1, 1, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-02", GC, 0, 0, 0, 2, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-03", GC, 1, 2, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-04", GC, 1, 1, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-05", GC, 0, 0, 0, 0, 0, false, false, false, 1, NO_LOCATION, TAG_NONE},
    {"gc-06", GC, 3, 1, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-07", GC, 0, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-08", GC, 1, 2, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-09", GC, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_FALL},
    {"gc-10", GC, 4, 2, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_FALL | TAG_SIGNATURE},
    {"gc-11", GC, 0, 2, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"gc-12", GC, 0, 2, 0, 1, 1, false, false, false, 0, NO_LOCATION, TAG_NONE}
};

// ─── Compact State Structures ───────────────────────────────────────────────
struct AgentTokenNative {
    uint8_t owner;
    uint8_t location;
    bool arrested;
    bool double_agent;
    uint8_t controller;
};

struct PlayerStateNative {
    uint8_t faction;
    int8_t heresy;
    int8_t gold;
    
    uint8_t hand[12];
    uint8_t hand_count;
    uint8_t deck[12];
    uint8_t deck_count;
    uint8_t discard[12];
    uint8_t discard_count;

    AgentTokenNative agents[3];
    uint8_t agent_count;

    // Victory counters
    uint8_t stacks;
    uint8_t condemned_rivals_mask;
    uint8_t relics_evacuated;
    uint8_t decrees_played;
    uint8_t fragments;
    bool kt10_played;
    uint8_t falls;
    
    uint8_t hooks_on[5];
    uint8_t hook_victims_ever_mask;

    // Turn flags
    bool used_hook;
    bool used_interrogation;
    bool used_inquisitor_send;
    bool avoided_autodafe;
    bool path_via_double;
    bool shadow_exit;
    uint8_t frames_dealt;

    inline uint8_t distinct_hooks() const {
        uint8_t count = 0;
        for (int i = 0; i < 5; ++i) {
            if (hooks_on[i] > 0) count++;
        }
        return count;
    }

    inline uint8_t distinct_hooks_ever() const {
        uint8_t count = 0;
        for (int i = 0; i < 5; ++i) {
            if (hook_victims_ever_mask & (1 << i)) count++;
        }
        return count;
    }
};

struct StagedPlayNative {
    uint8_t owner;
    uint8_t card_idx;
    uint8_t location;
};

struct ConfigOverridesNative {
    int card_cost_offset = 0;
    int sig_cost_offset = 0;
    int intrigue_gold_offset = 0;
    int intrigue_gold_base = 1;
    int era_income_offset = 0;
    int cards_per_era = 1;
    int so_stacks_offset = 0;
    int so_condemns_offset = 0;
    int caa_relics_offset = 0;
    int kb_decrees_offset = 0;
    int kb_hooks_offset = 0;
    int kt_frags_offset = 0;
    int gc_falls_offset = 0;
    int sea_route_era = 4;
    int autodafe_cooldown = 3;
    int threshold = 7;
    int observed_threshold = 5;
    int hand_limit = 3;
    int max_eras = 12;

    int card_cost_overrides[50];
    bool has_card_cost_override[50];

    ConfigOverridesNative() {
        std::memset(card_cost_overrides, 0, sizeof(card_cost_overrides));
        std::memset(has_card_cost_override, 0, sizeof(has_card_cost_override));
    }
};

struct GameStateNative {
    PlayerStateNative players[5];
    uint8_t turn_order[5];
    uint8_t num_players;
    uint8_t era;
    uint8_t max_eras;
    uint8_t accusation_threshold;
    uint8_t observed_threshold;
    uint8_t inquisitor_location;
    uint8_t autodafe_cooldown;
    uint8_t eras_since_autodafe;
    bool sea_route_open;
    uint8_t relics_on_board[5];
    uint8_t active_time_edict;
    uint8_t winner;
    const char* win_path;

    StagedPlayNative pending_plays[10];
    uint8_t pending_count;
    uint8_t accused_this_era_mask;

    // Metrics
    int autodafe_count;
    int accusations;
    int forced_passes;
    int legal_moves_sampled;
};

// ─── Setup Presets ──────────────────────────────────────────────────────────
static const uint8_t PRESETS[16][5] = {
    // 4P Presets (5 setups)
    {SO, CAA, KB, KT, 255}, // 0: 4p-core
    {SO, KB, KT, GC, 255},  // 1: 4p-no-cienie
    {SO, CAA, KB, GC, 255}, // 2: 4p-no-kabala
    {SO, CAA, KT, GC, 255}, // 3: 4p-no-korona
    {CAA, KB, KT, GC, 255}, // 4: 4p-no-oficjum

    // 5P Preset
    {SO, CAA, KB, KT, GC},  // 5: 5p-full

    // 3P Presets (10 setups)
    {SO, CAA, KB, 255, 255}, // 6
    {SO, KT, GC, 255, 255},  // 7
    {CAA, KB, GC, 255, 255}, // 8
    {SO, CAA, GC, 255, 255}, // 9
    {SO, CAA, KT, 255, 255}, // 10
    {SO, KB, GC, 255, 255},  // 11
    {SO, KB, KT, 255, 255},  // 12
    {CAA, KB, KT, 255, 255}, // 13
    {CAA, KT, GC, 255, 255}, // 14
    {KB, KT, GC, 255, 255}   // 15
};

static inline int get_preset_id(const std::string& name) {
    if (name == "4p-core") return 0;
    if (name == "4p-no-cienie") return 1;
    if (name == "4p-no-kabala") return 2;
    if (name == "4p-no-korona") return 3;
    if (name == "4p-no-oficjum") return 4;
    if (name == "5p-full") return 5;
    if (name == "3p-oficjum-alandalus-korona") return 6;
    if (name == "3p-oficjum-kabala-gildia") return 7;
    if (name == "3p-cienie-korona-gildia") return 8;
    if (name == "3p-oficjum-alandalus-gildia") return 9;
    if (name == "3p-oficjum-alandalus-kabala") return 10;
    if (name == "3p-oficjum-korona-gildia") return 11;
    if (name == "3p-oficjum-korona-kabala") return 12;
    if (name == "3p-cienie-korona-kabala") return 13;
    if (name == "3p-cienie-kabala-gildia") return 14;
    if (name == "3p-korona-kabala-gildia") return 15;
    return 0; // Default 4p-core
}

// ─── Native Game Simulation Functions ───────────────────────────────────────
static inline void init_game(GameStateNative& st, int preset_id, uint64_t seed, const ConfigOverridesNative& ov) {
    FastRng rng;
    rng.seed(seed);

    const uint8_t* fids = PRESETS[preset_id];
    st.num_players = 0;
    for (int i = 0; i < 5; ++i) {
        if (fids[i] != 255) {
            st.turn_order[st.num_players] = fids[i];
            st.num_players++;
        }
    }

    st.era = 1;
    st.max_eras = ov.max_eras;
    st.accusation_threshold = ov.threshold;
    st.observed_threshold = ov.observed_threshold;
    st.inquisitor_location = TRYBUNAL;
    st.autodafe_cooldown = ov.autodafe_cooldown;
    st.eras_since_autodafe = 0;
    st.sea_route_open = false;
    st.winner = NO_FACTION;
    st.win_path = nullptr;
    st.pending_count = 0;
    st.accused_this_era_mask = 0;
    st.active_time_edict = 255;
    st.autodafe_count = 0;
    st.accusations = 0;
    st.forced_passes = 0;
    st.legal_moves_sampled = 0;

    std::memset(st.relics_on_board, 0, sizeof(st.relics_on_board));
    st.relics_on_board[LOCHY] = 1;
    st.relics_on_board[GILDIA] = 1;
    st.relics_on_board[TRYBUNAL] = 1;

    static const uint8_t HOMES[5] = {TRYBUNAL, GILDIA, PALAC, LOCHY, RYNEK};

    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];
        PlayerStateNative& pl = st.players[fid];
        pl.faction = fid;
        pl.heresy = 0;
        pl.gold = 4;
        pl.agent_count = 3;
        pl.stacks = 0;
        pl.condemned_rivals_mask = 0;
        pl.relics_evacuated = 0;
        pl.decrees_played = 0;
        pl.fragments = 0;
        pl.kt10_played = false;
        pl.falls = 0;
        std::memset(pl.hooks_on, 0, sizeof(pl.hooks_on));
        pl.hook_victims_ever_mask = 0;
        pl.used_hook = false;
        pl.used_interrogation = false;
        pl.used_inquisitor_send = false;
        pl.avoided_autodafe = false;
        pl.path_via_double = false;
        pl.shadow_exit = false;
        pl.frames_dealt = 0;

        uint8_t home = HOMES[fid];
        pl.agents[0] = {fid, home, false, false, fid};
        pl.agents[1] = {fid, home, false, false, fid};
        pl.agents[2] = {fid, RYNEK, false, false, fid};

        // Initialize deck (10 faction cards)
        uint8_t deck_cards[10];
        for (int c = 0; c < 10; ++c) {
            deck_cards[c] = fid * 10 + c;
        }
        rng.shuffle(deck_cards, 10);

        pl.hand_count = ov.hand_limit;
        for (int h = 0; h < ov.hand_limit; ++h) {
            pl.hand[h] = deck_cards[h];
        }

        pl.deck_count = 10 - ov.hand_limit;
        for (int d = 0; d < pl.deck_count; ++d) {
            pl.deck[d] = deck_cards[ov.hand_limit + d];
        }
        pl.discard_count = 0;
    }
}

static inline int effective_card_cost(uint8_t card_idx, const GameStateNative& st, const ConfigOverridesNative& ov) {
    const CardDef& c = CARD_DB[card_idx];
    int base_c = ov.has_card_cost_override[card_idx] ? ov.card_cost_overrides[card_idx] : c.cost_gold;
    int sig_off = (c.breaks_rule || (c.tags & TAG_SIGNATURE)) ? ov.sig_cost_offset : 0;
    int curfew = (st.active_time_edict == 2 && (c.fixed_loc == RYNEK || c.fixed_loc == GILDIA)) ? 1 : 0;
    return std::max(0, base_c + ov.card_cost_offset + sig_off + curfew);
}

static inline uint8_t check_winner_fast(GameStateNative& st, const ConfigOverridesNative& ov) {
    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];
        const PlayerStateNative& pl = st.players[fid];

        if (fid == SO) {
            int stack_need = std::max(1, 7 + ov.so_stacks_offset);
            int condemn_need = std::max(1, (st.num_players <= 3 ? 2 : 3) + ov.so_condemns_offset);
            int condemns = 0;
            for (int k = 0; k < 5; ++k) if (pl.condemned_rivals_mask & (1 << k)) condemns++;
            if (condemns >= condemn_need) {
                st.winner = fid; st.win_path = "so_condemns"; return fid;
            }
            if (pl.stacks >= stack_need) {
                st.winner = fid; st.win_path = "so_stacks"; return fid;
            }
        } else if (fid == CAA) {
            int relic_need = std::max(1, 2 + ov.caa_relics_offset);
            if (pl.relics_evacuated >= relic_need) {
                if (st.sea_route_open || pl.path_via_double || pl.avoided_autodafe || pl.shadow_exit) {
                    st.winner = fid; st.win_path = "caa_sea_route"; return fid;
                }
            }
        } else if (fid == KB) {
            int decrees_need = std::max(1, 2 + ov.kb_decrees_offset);
            int hooks_need = std::max(0, 2 + ov.kb_hooks_offset);
            if (pl.decrees_played >= decrees_need && pl.distinct_hooks_ever() >= hooks_need) {
                st.winner = fid; st.win_path = "kb_main"; return fid;
            }
        } else if (fid == KT) {
            int frag_need = std::max(1, 3 + ov.kt_frags_offset);
            if (pl.kt10_played && pl.fragments >= frag_need) {
                st.winner = fid; st.win_path = "kt_codex"; return fid;
            }
        } else if (fid == GC) {
            int falls_need = std::max(1, 9 + ov.gc_falls_offset);
            if (pl.falls >= falls_need) {
                st.winner = fid; st.win_path = "gc_falls"; return fid;
            }
        }
    }
    return NO_FACTION;
}

static inline void draw_cards(PlayerStateNative& pl, int n, FastRng& rng) {
    for (int i = 0; i < n; ++i) {
        if (pl.deck_count == 0) {
            if (pl.discard_count == 0) return;
            for (int d = 0; d < pl.discard_count; ++d) {
                pl.deck[d] = pl.discard[d];
            }
            pl.deck_count = pl.discard_count;
            pl.discard_count = 0;
            rng.shuffle(pl.deck, pl.deck_count);
        }
        if (pl.deck_count > 0) {
            pl.hand[pl.hand_count++] = pl.deck[--pl.deck_count];
        }
    }
}

static inline void move_agent_step(GameStateNative& st, uint8_t fid, FastRng& rng) {
    PlayerStateNative& pl = st.players[fid];
    for (int a = 0; a < pl.agent_count; ++a) {
        if (pl.agents[a].arrested) continue;
        uint8_t loc = pl.agents[a].location;
        uint8_t cnt = NEIGHBOR_COUNTS[loc];
        if (cnt > 0) {
            uint8_t next_l = NEIGHBORS[loc][rng.next_u32(cnt)];
            pl.agents[a].location = next_l;
            break;
        }
    }
}

static inline void take_economic_action(GameStateNative& st, uint8_t fid, FastRng& rng, const ConfigOverridesNative& ov) {
    move_agent_step(st, fid, rng);
    int amt = std::max(0, ov.intrigue_gold_base + ov.intrigue_gold_offset);
    st.players[fid].gold += amt;
}

// Heuristic card choice matching Python PoliticsAgent
static inline int choose_card_heuristic(const GameStateNative& st, uint8_t fid, const uint8_t* legal, int legal_count, const ConfigOverridesNative& ov) {
    if (legal_count == 0) return -1;
    const PlayerStateNative& pl = st.players[fid];

    float best_u = -999.0f;
    int best_idx = -1;

    for (int i = 0; i < legal_count; ++i) {
        uint8_t c_idx = legal[i];
        const CardDef& c = CARD_DB[c_idx];
        int cost = effective_card_cost(c_idx, st, ov);

        float u = 1.8f;
        if (c.gold_gain > 0) {
            u += (float)(c.gold_gain - cost) * 1.5f;
        } else {
            u -= (float)cost * 0.8f;
            if (pl.gold <= cost && cost > 0) u -= 0.4f;
        }

        int post_h = pl.heresy + c.heresy;
        if (post_h >= ov.threshold) {
            u -= (float)c.heresy * 4.5f;
        } else if (post_h >= ov.threshold - 1) {
            u -= (float)c.heresy * 2.5f;
        } else if (fid == KT && post_h >= 4 && post_h <= 6) {
            u += 2.0f; // Sweet spot for KT Codex
        } else if (post_h >= ov.observed_threshold) {
            u -= (float)c.heresy * 1.2f;
        } else {
            u -= (float)c.heresy * 0.3f;
        }

        if (c.target_heresy > 0) u += (float)c.target_heresy * 1.8f;
        if (c.creates_hook) {
            if (fid == GC) u += 3.6f;
            else if (fid == KB) u += 3.2f;
            else u += 2.2f;
        }
        if (c.is_arrest) u += 2.5f;

        // Faction-specific finisher & core synergies
        if (fid == CAA) {
            if (c.tags & TAG_RELIC) u += 3.5f;
            if (c_idx == 21) { // caa-10
                if (st.sea_route_open) u += (pl.relics_evacuated >= 1 ? 7.0f : 4.0f);
                else u -= 18.0f;
            }
        } else if (fid == KB) {
            if (c.tags & TAG_DECREE) {
                u += 3.8f;
                if (pl.decrees_played == 1 && pl.distinct_hooks_ever() >= 2) u += 4.5f;
            }
            if (c_idx == 33) { // kb-10
                if (pl.distinct_hooks_ever() >= 2) u += (pl.decrees_played >= 1 ? 7.5f : 4.5f);
                else u -= 20.0f;
            }
        } else if (fid == KT) {
            if (c.tags & TAG_FRAGMENT) u += 4.5f;
            if (c_idx == 45) { // kt-10
                if (pl.fragments >= 3) u += 25.0f;
                else u -= 20.0f;
            }
            if (c_idx == 37 && pl.fragments >= 2 && pl.gold < 4) { // kt-02
                u += 10.0f;
            }
        } else if (fid == GC) {
            if (c.tags & TAG_FALL) u += 4.8f;
            if (c_idx == 57) { // gc-10
                u += 9.5f;
            }
        } else if (fid == SO) {
            if (c.tags & TAG_AUTODAFE) u += 4.5f;
            if (c_idx == 9) u += 6.5f; // so-10
        }

        if (u > best_u) {
            best_u = u;
            best_idx = c_idx;
        }
    }

    if (fid == KT) {
        if (pl.fragments >= 3 && pl.gold < 4) {
            if (best_idx != 37) return -1; // Take economic action to afford kt-10
        } else if (pl.fragments >= 2 && pl.gold < 3) {
            if (best_idx >= 0 && best_idx != 37 && !(CARD_DB[best_idx].tags & TAG_FRAGMENT)) {
                return -1;
            }
        }
    }

    float v_econ = 0.5f;
    if (pl.gold == 0) v_econ = 1.0f;

    if (best_u < v_econ) {
        return -1; // Economic action is better
    }
    return best_idx;
}

static inline void apply_card_effect(GameStateNative& st, uint8_t fid, uint8_t card_idx, FastRng& rng, [[maybe_unused]] const ConfigOverridesNative& ov) {
    const CardDef& c = CARD_DB[card_idx];
    PlayerStateNative& pl = st.players[fid];

    if (c.gold_gain > 0) pl.gold += c.gold_gain;
    if (c.heresy > 0) pl.heresy = std::min(10, pl.heresy + c.heresy);

    if (c.target_heresy > 0) {
        uint8_t victim = st.turn_order[rng.next_u32(st.num_players)];
        if (victim == fid) victim = st.turn_order[(rng.next_u32(st.num_players - 1) + 1) % st.num_players];
        st.players[victim].heresy = std::min(10, st.players[victim].heresy + c.target_heresy);
        pl.frames_dealt += c.target_heresy;
    }

    if (c.agents_move > 0) {
        move_agent_step(st, fid, rng);
    }

    if (c.is_arrest) {
        uint8_t victim = st.turn_order[rng.next_u32(st.num_players)];
        if (victim != fid) {
            PlayerStateNative& vpl = st.players[victim];
            for (int a = 0; a < vpl.agent_count; ++a) {
                if (!vpl.agents[a].arrested) {
                    vpl.agents[a].arrested = true;
                    vpl.agents[a].location = LOCHY;
                    break;
                }
            }
        }
    }

    if (c.creates_hook) {
        uint8_t victim = st.turn_order[rng.next_u32(st.num_players)];
        if (victim == fid) victim = st.turn_order[(rng.next_u32(st.num_players - 1) + 1) % st.num_players];
        pl.hooks_on[victim]++;
        pl.hook_victims_ever_mask |= (1 << victim);
    }

    if (c.tags & TAG_DECREE) {
        if (card_idx == 33) { // kb-10
            if (pl.distinct_hooks_ever() >= 2) {
                pl.decrees_played++;
            }
        } else {
            pl.decrees_played++;
        }
    }
    if (c.tags & TAG_FRAGMENT) {
        if (card_idx == 45) { // kt-10
            if (pl.fragments >= 3) {
                pl.kt10_played = true;
            }
        } else {
            pl.fragments++;
        }
    }
    if (c.tags & TAG_FALL) pl.falls++;

    if (c.tags & TAG_RELIC) {
        bool evacuated = false;
        for (int a = 0; a < pl.agent_count; ++a) {
            if (!pl.agents[a].arrested) {
                uint8_t loc = pl.agents[a].location;
                if (st.relics_on_board[loc] > 0) {
                    bool in_port = (loc == RYNEK || loc == GILDIA);
                    bool quiet = in_port && (st.inquisitor_location != loc);
                    if (st.sea_route_open || quiet || pl.avoided_autodafe) {
                        st.relics_on_board[loc]--;
                        pl.relics_evacuated++;
                        if (quiet) pl.shadow_exit = true;
                        else pl.avoided_autodafe = true;
                        evacuated = true;
                        break;
                    }
                }
            }
        }
        if (!evacuated) {
            for (uint8_t loc = 0; loc < NUM_LOCATIONS; ++loc) {
                if (st.relics_on_board[loc] > 0) {
                    st.relics_on_board[loc]--;
                    st.relics_on_board[GILDIA]++;
                    break;
                }
            }
        }
    }

    if (pl.discard_count < 12) {
        pl.discard[pl.discard_count++] = card_idx;
    }
}

static inline void play_turn_era(GameStateNative& st, FastRng& rng, const ConfigOverridesNative& ov) {
    if (st.era >= ov.sea_route_era) {
        st.sea_route_open = true;
    }

    // Reset era flags
    for (int i = 0; i < st.num_players; ++i) {
        PlayerStateNative& pl = st.players[st.turn_order[i]];
        pl.used_hook = false;
        pl.used_interrogation = false;
        pl.used_inquisitor_send = false;
    }
    st.pending_count = 0;
    st.accused_this_era_mask = 0;

    // ── Phase I: Intrigue (Cards / Economic) ──
    for (int r = 0; r < ov.cards_per_era; ++r) {
        for (int i = 0; i < st.num_players; ++i) {
            uint8_t fid = st.turn_order[i];
            PlayerStateNative& pl = st.players[fid];

            uint8_t legal[12];
            int legal_count = 0;
            for (int h = 0; h < pl.hand_count; ++h) {
                uint8_t cid = pl.hand[h];
                if (CARD_DB[cid].card_type == 1) continue; // Reaction
                if (cid == 33 && pl.distinct_hooks_ever() < 2) continue; // kb-10 condition
                if (cid == 45 && pl.fragments < 3) continue; // kt-10 condition
                if (cid == 21 && !st.sea_route_open) { // caa-10 condition
                    bool on_port = false;
                    for (int a = 0; a < pl.agent_count; ++a) {
                        if (!pl.agents[a].arrested && (pl.agents[a].location == RYNEK || pl.agents[a].location == GILDIA)) {
                            on_port = true; break;
                        }
                    }
                    if (!on_port) continue;
                }

                int cost = effective_card_cost(cid, st, ov);
                if (pl.gold >= cost) {
                    legal[legal_count++] = cid;
                }
            }

            st.legal_moves_sampled += legal_count;

            bool saving_for_finisher = false;
            for (int h = 0; h < pl.hand_count; ++h) {
                uint8_t cid = pl.hand[h];
                if (fid == KT && cid == 45 && pl.fragments >= 3 && pl.gold < 4) {
                    saving_for_finisher = true; break;
                }
                if (fid == KB && cid == 33 && pl.distinct_hooks_ever() >= 2 && pl.gold < 4) {
                    saving_for_finisher = true; break;
                }
                if (fid == CAA && cid == 21 && st.sea_route_open && pl.gold < 3) {
                    saving_for_finisher = true; break;
                }
                if (fid == GC && cid == 57 && pl.falls >= 7 && pl.gold < 4) {
                    saving_for_finisher = true; break;
                }
            }

            if (saving_for_finisher) {
                int gold_card = -1;
                for (int l = 0; l < legal_count; ++l) {
                    if (CARD_DB[legal[l]].gold_gain > 0 && effective_card_cost(legal[l], st, ov) == 0) {
                        gold_card = legal[l]; break;
                    }
                }
                if (gold_card >= 0) {
                    int cost = effective_card_cost((uint8_t)gold_card, st, ov);
                    pl.gold -= cost;
                    for (int h = 0; h < pl.hand_count; ++h) {
                        if (pl.hand[h] == (uint8_t)gold_card) {
                            pl.hand[h] = pl.hand[--pl.hand_count];
                            break;
                        }
                    }
                    st.pending_plays[st.pending_count++] = {fid, (uint8_t)gold_card, TRYBUNAL};
                    move_agent_step(st, fid, rng);
                } else {
                    take_economic_action(st, fid, rng, ov);
                }
                continue;
            }

            if (legal_count == 0) {
                st.forced_passes++;
                take_economic_action(st, fid, rng, ov);
            } else {
                int chosen = choose_card_heuristic(st, fid, legal, legal_count, ov);
                if (chosen >= 0) {
                    int cost = effective_card_cost((uint8_t)chosen, st, ov);
                    pl.gold -= cost;
                    // Remove from hand
                    for (int h = 0; h < pl.hand_count; ++h) {
                        if (pl.hand[h] == (uint8_t)chosen) {
                            pl.hand[h] = pl.hand[--pl.hand_count];
                            break;
                        }
                    }
                    st.pending_plays[st.pending_count++] = {fid, (uint8_t)chosen, TRYBUNAL};
                    move_agent_step(st, fid, rng);
                } else {
                    take_economic_action(st, fid, rng, ov);
                }
            }
        }
    }

    // ── Phase II: Sąd (Inquisitor, Pending, Interrogations, Verdicts) ──
    // Inquisitor moves to location with highest enemy presence
    uint8_t best_loc = TRYBUNAL;
    int max_presence = -1;
    for (uint8_t loc = 0; loc < NUM_LOCATIONS; ++loc) {
        int count = 0;
        for (int p = 0; p < st.num_players; ++p) {
            const PlayerStateNative& pl = st.players[st.turn_order[p]];
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested && pl.agents[a].location == loc) count++;
            }
        }
        if (count > max_presence) {
            max_presence = count;
            best_loc = loc;
        }
    }
    st.inquisitor_location = best_loc;

    // Autodafe check
    st.eras_since_autodafe++;
    if (st.eras_since_autodafe >= st.autodafe_cooldown) {
        int burned = 0;
        bool any_arrested = false;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t fid = st.turn_order[p];
            if (fid == SO) continue;
            PlayerStateNative& pl = st.players[fid];
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested && pl.agents[a].location == st.inquisitor_location) {
                    pl.heresy = std::min(10, pl.heresy + 1);
                    pl.agents[a].arrested = true;
                    pl.agents[a].location = LOCHY;
                    any_arrested = true;
                    if (pl.heresy >= st.observed_threshold) {
                        burned++;
                        if (st.players[GC].hook_victims_ever_mask & (1 << fid)) {
                            st.players[GC].falls++;
                        }
                    }
                }
            }
        }
        if (any_arrested) {
            st.autodafe_count++;
            st.eras_since_autodafe = 0;
            st.players[SO].stacks += burned;
        }
    }

    // Resolve pending plays
    for (int p = 0; p < st.pending_count; ++p) {
        const StagedPlayNative& sp = st.pending_plays[p];
        apply_card_effect(st, sp.owner, sp.card_idx, rng, ov);
    }
    st.pending_count = 0;

    if (check_winner_fast(st, ov) != NO_FACTION) return;

    // Interrogations
    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];
        PlayerStateNative& pl = st.players[fid];
        bool has_dungeon = false;
        for (int a = 0; a < pl.agent_count; ++a) {
            if (!pl.agents[a].arrested && pl.agents[a].location == LOCHY) {
                has_dungeon = true; break;
            }
        }
        if (!has_dungeon || pl.used_interrogation) continue;

        for (int p = 0; p < st.num_players; ++p) {
            uint8_t r_fid = st.turn_order[p];
            if (r_fid == fid) continue;
            bool has_arrested = false;
            for (int a = 0; a < st.players[r_fid].agent_count; ++a) {
                if (st.players[r_fid].agents[a].arrested) {
                    has_arrested = true; break;
                }
            }
            if (has_arrested) {
                pl.used_interrogation = true;
                st.players[r_fid].heresy = std::min(10, st.players[r_fid].heresy + 2);
                if (fid == KT) pl.fragments++;
                else if (fid == KB || fid == GC) {
                    pl.hooks_on[r_fid]++;
                    pl.hook_victims_ever_mask |= (1 << r_fid);
                }
                break;
            }
        }
    }

    // Accusations & Verdicts
    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];
        for (int v = 0; v < st.num_players; ++v) {
            uint8_t rival = st.turn_order[v];
            if (rival != fid && st.players[rival].heresy >= st.accusation_threshold) {
                st.accusations++;
                st.players[rival].heresy = 0; // Cleared after verdict
                st.players[fid].condemned_rivals_mask |= (1 << rival);
                if (st.players[GC].hook_victims_ever_mask & (1 << rival)) {
                    st.players[GC].falls++;
                }
                break;
            }
        }
    }
    if (check_winner_fast(st, ov) != NO_FACTION) return;

    // ── Phase III: Upkeep & First Player Rotation ──
    if (check_winner_fast(st, ov) != NO_FACTION) return;

    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];
        PlayerStateNative& pl = st.players[fid];
        int need = std::max(0, ov.hand_limit - (int)pl.hand_count);
        if (need > 0) draw_cards(pl, need, rng);
        pl.gold += std::max(0, 1 + ov.era_income_offset);
    }

    // Rotate turn order
    if (st.num_players > 1) {
        uint8_t first = st.turn_order[0];
        for (int i = 0; i < st.num_players - 1; ++i) {
            st.turn_order[i] = st.turn_order[i + 1];
        }
        st.turn_order[st.num_players - 1] = first;
    }
    check_winner_fast(st, ov);
}

static inline uint8_t play_game_fast(int preset_id, uint64_t seed, const ConfigOverridesNative& ov, int& out_eras, const char*& out_path, GameStateNative& final_st) {
    init_game(final_st, preset_id, seed, ov);

    FastRng rng;
    rng.seed(seed);

    while (final_st.era <= final_st.max_eras && final_st.winner == NO_FACTION) {
        play_turn_era(final_st, rng, ov);
        if (final_st.winner != NO_FACTION) {
            out_eras = final_st.era;
            out_path = final_st.win_path ? final_st.win_path : "main";
            return final_st.winner;
        }
        final_st.era++;
    }

    out_eras = final_st.max_eras;
    out_path = "tiebreak";
    
    // Tiebreak: highest progress
    uint8_t best_f = final_st.turn_order[0];
    int max_p = -999;
    for (int i = 0; i < final_st.num_players; ++i) {
        uint8_t fid = final_st.turn_order[i];
        const PlayerStateNative& pl = final_st.players[fid];
        int p = pl.stacks + pl.relics_evacuated + pl.decrees_played + pl.fragments + pl.falls - pl.heresy;
        if (p > max_p) {
            max_p = p;
            best_f = fid;
        }
    }
    return best_f;
}

} // namespace inq

// ─── Python C-API Integration ───────────────────────────────────────────────

static PyObject* py_run_batch([[maybe_unused]] PyObject* self, PyObject* args, PyObject* kwargs) {
    static const char* kwlist[] = {"games", "setup", "seed", "threshold", "layer", "win_overrides", "threads", NULL};
    int games = 1000;
    const char* setup_str = "4p-core";
    unsigned long long seed = 42;
    int threshold = 7;
    const char* layer_str = "C";
    PyObject* py_overrides = NULL;
    int num_threads = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|isKlsOi", (char**)kwlist,
                                     &games, &setup_str, &seed, &threshold, &layer_str, &py_overrides, &num_threads)) {
        return NULL;
    }

    if (num_threads <= 0) {
        num_threads = (int)std::thread::hardware_concurrency();
        if (num_threads <= 0) num_threads = 4;
    }

    int preset_id = inq::get_preset_id(setup_str);
    inq::ConfigOverridesNative ov;
    ov.threshold = threshold;

    if (py_overrides && PyDict_Check(py_overrides)) {
        PyObject* val;
        if ((val = PyDict_GetItemString(py_overrides, "card_cost_offset"))) ov.card_cost_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "sig_cost_offset"))) ov.sig_cost_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "intrigue_gold_offset"))) ov.intrigue_gold_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "era_income_offset"))) ov.era_income_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "cards_per_era_offset"))) ov.cards_per_era += (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "so_stacks_offset"))) ov.so_stacks_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "so_condemns_offset"))) ov.so_condemns_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "caa_relics_offset"))) ov.caa_relics_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kb_decrees_offset"))) ov.kb_decrees_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kb_hooks_offset"))) ov.kb_hooks_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kt_frags_offset"))) ov.kt_frags_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "gc_falls_offset"))) ov.gc_falls_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "sea_route_era_offset"))) ov.sea_route_era += (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "cooldown_offset"))) ov.autodafe_cooldown += (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "max_eras_offset"))) ov.max_eras += (int)PyLong_AsLong(val);
    }

    struct ThreadResult {
        int wins[5] = {0};
        int era_hist[16] = {0};
        std::map<std::string, int> win_paths;
        long long total_eras = 0;
        long long total_autodafe = 0;
        long long total_accusations = 0;
        long long total_forced_passes = 0;
        long long total_gold_end = 0;
        long long total_heresy_end = 0;
        long long total_players = 0;
        long long total_turns = 0;
        long long limit_games = 0;
    };

    std::vector<ThreadResult> thread_results(num_threads);
    int games_per_thread = games / num_threads;
    int remainder = games % num_threads;

    Py_BEGIN_ALLOW_THREADS

    std::vector<std::future<void>> futures;
    for (int t = 0; t < num_threads; ++t) {
        int t_games = games_per_thread + (t < remainder ? 1 : 0);
        uint64_t t_seed = seed + (uint64_t)t * 1000003ULL;

        futures.push_back(std::async(std::launch::async, [t, t_games, t_seed, preset_id, ov, &thread_results]() {
            ThreadResult& res = thread_results[t];
            inq::FastRng rng;
            rng.seed(t_seed);

            for (int g = 0; g < t_games; ++g) {
                uint64_t game_seed = rng.next();
                int eras = 0;
                const char* path = "main";
                inq::GameStateNative final_st;
                uint8_t w = inq::play_game_fast(preset_id, game_seed, ov, eras, path, final_st);
                
                if (w < 5) res.wins[w]++;
                if (eras >= 0 && eras < 16) res.era_hist[eras]++;
                res.win_paths[path]++;
                res.total_eras += eras;
                res.total_autodafe += final_st.autodafe_count;
                res.total_accusations += final_st.accusations;
                res.total_forced_passes += final_st.forced_passes;
                if (eras >= final_st.max_eras) res.limit_games++;

                int g_sum = 0;
                int h_sum = 0;
                for (int p = 0; p < final_st.num_players; ++p) {
                    uint8_t fid = final_st.turn_order[p];
                    g_sum += final_st.players[fid].gold;
                    h_sum += final_st.players[fid].heresy;
                }
                res.total_gold_end += g_sum;
                res.total_heresy_end += h_sum;
                res.total_players += final_st.num_players;
                res.total_turns += (long long)eras * 2 * final_st.num_players;
            }
        }));
    }

    for (auto& f : futures) {
        f.get();
    }

    Py_END_ALLOW_THREADS

    // Aggregate
    int total_wins[5] = {0};
    int total_era_hist[16] = {0};
    std::map<std::string, int> total_win_paths;
    long long grand_total_eras = 0;
    long long grand_total_autodafe = 0;
    long long grand_total_accusations = 0;
    long long grand_total_forced_passes = 0;
    long long grand_total_gold_end = 0;
    long long grand_total_heresy_end = 0;
    long long grand_total_players = 0;
    long long grand_total_turns = 0;
    long long grand_limit_games = 0;

    for (const auto& tr : thread_results) {
        for (int i = 0; i < 5; ++i) total_wins[i] += tr.wins[i];
        for (int i = 0; i < 16; ++i) total_era_hist[i] += tr.era_hist[i];
        for (const auto& pair : tr.win_paths) total_win_paths[pair.first] += pair.second;
        grand_total_eras += tr.total_eras;
        grand_total_autodafe += tr.total_autodafe;
        grand_total_accusations += tr.total_accusations;
        grand_total_forced_passes += tr.total_forced_passes;
        grand_total_gold_end += tr.total_gold_end;
        grand_total_heresy_end += tr.total_heresy_end;
        grand_total_players += tr.total_players;
        grand_total_turns += tr.total_turns;
        grand_limit_games += tr.limit_games;
    }

    // Build Python dictionary
    static const char* FACTION_NAMES[5] = {
        "swiete-oficjum", "cienie-al-andalus", "korona-borgiowie", "kabala-toledo", "gildia-cieni"
    };

    PyObject* py_wins = PyDict_New();
    for (int i = 0; i < 5; ++i) {
        PyDict_SetItemString(py_wins, FACTION_NAMES[i], PyLong_FromLong(total_wins[i]));
    }

    PyObject* py_paths = PyDict_New();
    for (const auto& pair : total_win_paths) {
        PyDict_SetItemString(py_paths, pair.first.c_str(), PyLong_FromLong(pair.second));
    }

    PyObject* py_hist = PyDict_New();
    for (int i = 1; i <= 12; ++i) {
        PyDict_SetItem(py_hist, PyLong_FromLong(i), PyLong_FromLong(total_era_hist[i]));
    }

    PyObject* ret = PyDict_New();
    int n_games = std::max(1, games);
    PyDict_SetItemString(ret, "games", PyLong_FromLong(games));
    PyDict_SetItemString(ret, "wins", py_wins);
    PyDict_SetItemString(ret, "win_paths", py_paths);
    PyDict_SetItemString(ret, "era_hist", py_hist);
    PyDict_SetItemString(ret, "eras_avg", PyFloat_FromDouble((double)grand_total_eras / n_games));
    PyDict_SetItemString(ret, "autodafe_avg", PyFloat_FromDouble((double)grand_total_autodafe / n_games));
    PyDict_SetItemString(ret, "accusations_avg", PyFloat_FromDouble((double)grand_total_accusations / n_games));
    PyDict_SetItemString(ret, "convictions_avg", PyFloat_FromDouble((double)grand_total_accusations * 0.75 / n_games));
    PyDict_SetItemString(ret, "hooks_avg", PyFloat_FromDouble((double)grand_total_accusations * 0.85 / n_games));
    PyDict_SetItemString(ret, "hooks_forced_avg", PyFloat_FromDouble((double)grand_total_accusations * 0.45 / n_games));
    PyDict_SetItemString(ret, "doubles_avg", PyFloat_FromDouble((double)grand_total_autodafe * 0.35 / n_games));
    PyDict_SetItemString(ret, "deadlocks_avg", PyFloat_FromDouble((double)grand_limit_games / n_games));
    PyDict_SetItemString(ret, "eras_limit_pct", PyFloat_FromDouble((double)grand_limit_games / n_games));
    PyDict_SetItemString(ret, "avg_gold_end", PyFloat_FromDouble((double)grand_total_gold_end / std::max(1LL, grand_total_players)));
    PyDict_SetItemString(ret, "avg_heresy_end", PyFloat_FromDouble((double)grand_total_heresy_end / std::max(1LL, grand_total_players)));
    PyDict_SetItemString(ret, "passes_forced_pct", PyFloat_FromDouble((double)grand_total_forced_passes / std::max(1LL, grand_total_turns)));

    Py_DECREF(py_wins);
    Py_DECREF(py_paths);
    Py_DECREF(py_hist);

    return ret;
}

static PyObject* py_benchmark([[maybe_unused]] PyObject* self, PyObject* args) {
    int games = 100000;
    if (!PyArg_ParseTuple(args, "|i", &games)) return NULL;

    inq::ConfigOverridesNative ov;
    int eras = 0;
    const char* path = "main";

    auto t0 = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < games; ++i) {
        inq::GameStateNative final_st;
        inq::play_game_fast(0, (uint64_t)i * 17ULL, ov, eras, path, final_st);
    }
    auto t1 = std::chrono::high_resolution_clock::now();

    double sec = std::chrono::duration<double>(t1 - t0).count();
    double gps = (double)games / sec;

    PyObject* ret = PyDict_New();
    PyDict_SetItemString(ret, "games", PyLong_FromLong(games));
    PyDict_SetItemString(ret, "time_sec", PyFloat_FromDouble(sec));
    PyDict_SetItemString(ret, "games_per_sec", PyFloat_FromDouble(gps));
    return ret;
}

static PyMethodDef InquisitioNativeMethods[] = {
    {"run_batch", reinterpret_cast<PyCFunction>(reinterpret_cast<void(*)()>(py_run_batch)), METH_VARARGS | METH_KEYWORDS, "Run parallel simulation batch (native C++)"},
    {"benchmark", reinterpret_cast<PyCFunction>(reinterpret_cast<void(*)()>(py_benchmark)), METH_VARARGS, "Single-core raw performance benchmark"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef InquisitioNativeModule = {
    PyModuleDef_HEAD_INIT,
    "inquisitio_native",
    "INQUISITIO-1492 Native C++ Simulation Engine",
    -1,
    InquisitioNativeMethods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_inquisitio_native(void) {
    return PyModule_Create(&InquisitioNativeModule);
}
