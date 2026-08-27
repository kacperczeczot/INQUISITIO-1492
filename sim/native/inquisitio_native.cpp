#include <Python.h>
#include <cstdint>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <thread>
#include <future>
#include <map>

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

static const uint8_t STEP_TOWARD_TABLE[5][5] = {
    {TRYBUNAL, PALAC, LOCHY, PALAC, LOCHY}, // TRYBUNAL (0)
    {TRYBUNAL, PALAC, LOCHY, RYNEK, RYNEK}, // PALAC (1)
    {TRYBUNAL, PALAC, LOCHY, PALAC, GILDIA},// LOCHY (2)
    {PALAC, PALAC, PALAC, RYNEK, GILDIA},   // RYNEK (3)
    {LOCHY, RYNEK, LOCHY, RYNEK, GILDIA}    // GILDIA (4)
};

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

    void seed(uint64_t seed_val) {
        uint64_t z = (seed_val + 0x9e3779b97f4a7c15ULL);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        s[0] = z ^ (z >> 31);
        z = (seed_val + 0x9e3779b97f4a7c15ULL * 2);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        s[1] = z ^ (z >> 31);
        if (s[0] == 0 && s[1] == 0) s[0] = 1;
    }

    inline uint64_t next_u64() {
        const uint64_t s0 = s[0];
        uint64_t s1 = s[1];
        const uint64_t result = rotl(s0 + s1, 17) + s0;
        s1 ^= s0;
        s[0] = rotl(s0, 49) ^ s1 ^ (s1 << 21);
        s[1] = rotl(s1, 28);
        return result;
    }

    inline uint32_t next_u32(uint32_t bound) {
        if (bound <= 1) return 0;
        return (uint32_t)((next_u64() & 0xFFFFFFFFULL) % bound);
    }

    inline double next_double() {
        return (next_u64() >> 11) * (1.0 / 9007199254740992.0);
    }

    void shuffle(uint8_t* arr, int n) {
        for (int i = n - 1; i > 0; --i) {
            int j = (int)next_u32(i + 1);
            std::swap(arr[i], arr[j]);
        }
    }
};

// ─── Card Database ──────────────────────────────────────────────────────────
#define TAG_NONE       0
#define TAG_GOLD       (1 << 0)
#define TAG_HERESY     (1 << 1)
#define TAG_MOVE       (1 << 2)
#define TAG_HOOK       (1 << 3)
#define TAG_ARREST     (1 << 4)
#define TAG_AUTODAFE   (1 << 5)
#define TAG_DECREE     (1 << 6)
#define TAG_RELIC      (1 << 7)
#define TAG_FRAGMENT   (1 << 8)
#define TAG_FALL       (1 << 9)
#define TAG_INQUISITOR (1 << 10)
#define TAG_SIGNATURE  (1 << 11)

struct CardDef {
    const char* id;
    uint8_t faction;
    int cost_gold;
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
    // SWIETE-OFICJUM (SO)
    {"so-01", SO, 1, 2, 0, 2, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE},
    {"so-02", SO, 1, 2, 1, 2, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD},
    {"so-03", SO, 2, 3, 3, 1, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"so-04", SO, 1, 0, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_INQUISITOR},
    {"so-05", SO, 0, 0, 1, 0, 0, false, false, false, 1, NO_LOCATION, TAG_NONE},
    {"so-06", SO, 2, 0, 1, 0, 0, true, false, false, 0, NO_LOCATION, TAG_ARREST},
    {"so-07", SO, 1, 0, 0, 2, 0, false, false, false, 0, NO_LOCATION, TAG_NONE},
    {"so-08", SO, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_INQUISITOR | TAG_HERESY},
    {"so-09", SO, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    {"so-10", SO, 5, 1, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_AUTODAFE | TAG_HERESY},
    {"so-11", SO, 1, 1, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY | TAG_GOLD},
    {"so-12", SO, 1, 0, 1, 1, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_GOLD},
    // CIENIE-AL-ANDALUS (CAA)
    {"caa-01", CAA, 1, 1, 1, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE},
    {"caa-02", CAA, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD},
    {"caa-03", CAA, 0, 1, 0, 2, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_RELIC | TAG_HERESY},
    {"caa-04", CAA, 0, 0, 1, 3, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"caa-05", CAA, 1, 0, 3, 3, 0, false, false, false, 0, NO_LOCATION, TAG_RELIC},
    {"caa-06", CAA, 0, 0, 2, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_ARREST},
    {"caa-07", CAA, 0, 0, 0, 3, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    {"caa-08", CAA, 3, 0, 2, 3, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"caa-09", CAA, 0, 0, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_RELIC | TAG_MOVE},
    {"caa-10", CAA, 3, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_RELIC | TAG_HERESY},
    {"caa-11", CAA, 1, 0, 2, 3, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_INQUISITOR},
    {"caa-12", CAA, 0, 0, 0, 4, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD | TAG_HERESY},
    // KORONA-BORGIOWIE (KB)
    {"kb-01", KB, 1, 1, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE},
    {"kb-02", KB, 1, 0, 1, 2, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD},
    {"kb-03", KB, 1, 1, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"kb-04", KB, 2, 0, 0, 0, 1, false, true, false, 0, NO_LOCATION, TAG_HOOK | TAG_MOVE | TAG_HERESY},
    {"kb-05", KB, 2, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_DECREE | TAG_HOOK},
    {"kb-06", KB, 2, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_ARREST},
    {"kb-07", KB, 2, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    {"kb-08", KB, 3, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_NONE},
    {"kb-09", KB, 2, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_DECREE | TAG_HERESY},
    {"kb-10", KB, 4, 1, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_DECREE | TAG_HERESY},
    {"kb-11", KB, 1, 0, 1, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_GOLD},
    {"kb-12", KB, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    // KABALA-TOLEDO (KT)
    {"kt-01", KT, 1, 0, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE},
    {"kt-02", KT, 0, 0, 0, 3, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD},
    {"kt-03", KT, 0, 2, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT | TAG_HERESY},
    {"kt-04", KT, 1, 0, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"kt-05", KT, 1, 1, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-06", KT, 2, 0, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT},
    {"kt-07", KT, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    {"kt-08", KT, 1, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_ARREST},
    {"kt-09", KT, 1, 1, 0, 0, 0, false, false, false, 0, NO_LOCATION, TAG_FRAGMENT | TAG_HERESY},
    {"kt-10", KT, 4, 0, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_FRAGMENT},
    {"kt-11", KT, 2, 0, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD | TAG_HERESY},
    {"kt-12", KT, 0, 1, 0, 0, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_HERESY},
    // GILDIA-CIENI (GC)
    {"gc-01", GC, 1, 1, 0, 1, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE},
    {"gc-02", GC, 0, 0, 0, 2, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD | TAG_HERESY},
    {"gc-03", GC, 1, 2, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY},
    {"gc-04", GC, 1, 1, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK | TAG_HERESY},
    {"gc-05", GC, 0, 0, 0, 0, 0, false, false, false, 1, NO_LOCATION, TAG_NONE},
    {"gc-06", GC, 3, 1, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK},
    {"gc-07", GC, 0, 0, 0, 0, 0, true, false, false, 0, NO_LOCATION, TAG_ARREST | TAG_HERESY},
    {"gc-08", GC, 1, 2, 1, 1, 0, false, false, false, 0, NO_LOCATION, TAG_GOLD | TAG_HERESY},
    {"gc-09", GC, 1, 0, 0, 0, 0, false, true, false, 0, NO_LOCATION, TAG_HOOK | TAG_FALL},
    {"gc-10", GC, 4, 2, 0, 0, 0, false, false, true, 2, NO_LOCATION, TAG_SIGNATURE | TAG_FALL | TAG_HERESY},
    {"gc-11", GC, 0, 2, 1, 0, 0, false, false, false, 0, NO_LOCATION, TAG_HERESY | TAG_HOOK},
    {"gc-12", GC, 0, 2, 0, 1, 1, false, false, false, 0, NO_LOCATION, TAG_MOVE | TAG_GOLD | TAG_HERESY}
};

// ─── Native Structures ──────────────────────────────────────────────────────
struct AgentNative {
    uint8_t owner;
    uint8_t location;
    bool arrested;
    bool double_agent;
    uint8_t controller;
};

struct PlayerStateNative {
    uint8_t faction;
    int heresy;
    int gold;
    AgentNative agents[4];
    uint8_t agent_count;

    // Deck management (indices into CARD_DB 0..59)
    uint8_t hand[12];
    uint8_t hand_count;
    uint8_t deck[12];
    uint8_t deck_count;
    uint8_t discard[12];
    uint8_t discard_count;

    // Faction specific tracks
    int stacks;
    uint8_t condemned_rivals_mask;
    int relics_evacuated;
    int decrees_played;
    int fragments;
    bool kt10_played;
    int falls;
    int hooks_on[5];
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

    inline bool hand_has(uint8_t cid) const {
        for (int h = 0; h < hand_count; ++h) if (hand[h] == cid) return true;
        return false;
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
    int cards_per_era = 2;
    int so_stacks_offset = 0;
    int so_condemns_offset = 0;
    int caa_relics_offset = 0;
    int kb_decrees_offset = 0;
    int kb_hooks_offset = 0;
    int kt_frags_offset = 0;
    int gc_falls_offset = 0;
    int sea_route_era = 4;
    int autodafe_cooldown = 4;
    int threshold = 7;
    int observed_threshold = 5;
    int hand_limit = 5;
    int max_eras = 12;

    int card_cost_overrides[60];
    bool has_card_cost_override[60];

    ConfigOverridesNative() {
        std::memset(card_cost_overrides, 0, sizeof(card_cost_overrides));
        std::memset(has_card_cost_override, 0, sizeof(has_card_cost_override));
    }
};

struct GameStateNative {
    PlayerStateNative players[5];
    uint8_t turn_order[5];
    uint8_t num_players;
    int era;
    uint8_t inquisitor_location;
    int eras_since_autodafe;
    bool sea_route_open;
    uint8_t relics_on_board[5];
    uint8_t accused_this_era_mask;
    uint8_t active_time_edict;

    StagedPlayNative pending_plays[10];
    int pending_count;

    uint8_t winner;
    const char* win_path;

    // Metrics counters
    int autodafe_count;
    int accusations;
    int convictions;
    int cards_played[60];
    int forced_passes;
    int legal_moves_sampled;
    int deadlocks;
    int hooks_created;
    int hooks_forced;
    int doubles_created;
};

// ─── Setup Presets ──────────────────────────────────────────────────────────
static void init_game(GameStateNative& st, int preset_id, uint64_t seed, const ConfigOverridesNative& ov) {
    FastRng rng;
    rng.seed(seed);

    st.era = 0;
    st.eras_since_autodafe = 0;
    st.sea_route_open = false;
    st.inquisitor_location = TRYBUNAL;
    st.pending_count = 0;
    st.winner = NO_FACTION;
    st.win_path = "";
    std::memset(st.cards_played, 0, sizeof(st.cards_played));

    if (preset_id == 0) { // 4p-core: SO, CAA, KB, KT
        st.num_players = 4;
        st.turn_order[0] = SO; st.turn_order[1] = CAA; st.turn_order[2] = KB; st.turn_order[3] = KT;
    } else if (preset_id == 1) { // 4p-no-cienie: SO, GC, KB, KT
        st.num_players = 4;
        st.turn_order[0] = SO; st.turn_order[1] = GC; st.turn_order[2] = KB; st.turn_order[3] = KT;
    } else if (preset_id == 2) { // 4p-no-kabala: SO, CAA, KB, GC
        st.num_players = 4;
        st.turn_order[0] = SO; st.turn_order[1] = CAA; st.turn_order[2] = KB; st.turn_order[3] = GC;
    } else if (preset_id == 3) { // 4p-no-korona: SO, CAA, KT, GC
        st.num_players = 4;
        st.turn_order[0] = SO; st.turn_order[1] = CAA; st.turn_order[2] = KT; st.turn_order[3] = GC;
    } else if (preset_id == 4) { // 4p-no-oficjum: CAA, KB, KT, GC
        st.num_players = 4;
        st.turn_order[0] = CAA; st.turn_order[1] = KB; st.turn_order[2] = KT; st.turn_order[3] = GC;
    } else { // default: 4p-core
        st.num_players = 4;
        st.turn_order[0] = SO; st.turn_order[1] = CAA; st.turn_order[2] = KB; st.turn_order[3] = KT;
    }

    rng.shuffle(st.turn_order, st.num_players);

    st.accused_this_era_mask = 0;
    st.active_time_edict = 255;
    st.autodafe_count = 0;
    st.accusations = 0;
    st.convictions = 0;
    st.forced_passes = 0;
    st.legal_moves_sampled = 0;
    st.deadlocks = 0;
    st.hooks_created = 0;
    st.hooks_forced = 0;
    st.doubles_created = 0;

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

        // Initialize deck (12 faction cards)
        uint8_t deck_cards[12];
        for (int c = 0; c < 12; ++c) {
            deck_cards[c] = fid * 12 + c;
        }
        rng.shuffle(deck_cards, 12);

        pl.hand_count = ov.hand_limit;
        for (int h = 0; h < ov.hand_limit; ++h) {
            pl.hand[h] = deck_cards[h];
        }

        pl.deck_count = 12 - ov.hand_limit;
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
            if (pl.decrees_played >= decrees_need && pl.distinct_hooks() >= hooks_need) {
                st.winner = fid; st.win_path = "kb_main"; return fid;
            }
        } else if (fid == KT) {
            int frag_need = std::max(1, 3 + ov.kt_frags_offset);
            bool heresy_ok = (pl.heresy >= 4 && pl.heresy <= 6);
            if (pl.kt10_played && pl.fragments >= frag_need && heresy_ok) {
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
                pl.deck[d] = pl.discard[pl.discard_count - 1 - d];
            }
            pl.deck_count = pl.discard_count;
            pl.discard_count = 0;
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
        if (cnt == 0) continue;

        // Smart agent movement:
        // 1. Flee from Inquisitor location if here
        if (loc == st.inquisitor_location) {
            uint8_t safe_dests[4];
            int safe_cnt = 0;
            for (uint8_t i = 0; i < cnt; ++i) {
                uint8_t dest = NEIGHBORS[loc][i];
                if (dest != st.inquisitor_location) safe_dests[safe_cnt++] = dest;
            }
            if (safe_cnt > 0) {
                pl.agents[a].location = safe_dests[rng.next_u32(safe_cnt)];
                return;
            }
        }

        // 2. CAA relic movement
        if (fid == CAA) {
            if (st.relics_on_board[loc] > 0) {
                for (uint8_t i = 0; i < cnt; ++i) {
                    uint8_t dest = NEIGHBORS[loc][i];
                    if (dest == RYNEK || dest == GILDIA) {
                        pl.agents[a].location = dest;
                        return;
                    }
                }
            }
            for (uint8_t i = 0; i < cnt; ++i) {
                uint8_t dest = NEIGHBORS[loc][i];
                if (st.relics_on_board[dest] > 0 || dest == RYNEK || dest == GILDIA) {
                    pl.agents[a].location = dest;
                    return;
                }
            }
        }

        // 3. SO agent movement toward rival concentrations
        if (fid == SO) {
            int cur_c = 0;
            for (int p = 0; p < st.num_players; ++p) {
                uint8_t other = st.turn_order[p];
                if (other == SO) continue;
                for (int oa = 0; oa < st.players[other].agent_count; ++oa) {
                    if (!st.players[other].agents[oa].arrested && st.players[other].agents[oa].location == loc) cur_c++;
                }
            }
            uint8_t best_nb = loc;
            int best_c = cur_c;
            for (uint8_t i = 0; i < cnt; ++i) {
                uint8_t dest = NEIGHBORS[loc][i];
                int dest_c = 0;
                for (int p = 0; p < st.num_players; ++p) {
                    uint8_t other = st.turn_order[p];
                    if (other == SO) continue;
                    for (int oa = 0; oa < st.players[other].agent_count; ++oa) {
                        if (!st.players[other].agents[oa].arrested && st.players[other].agents[oa].location == dest) dest_c++;
                    }
                }
                if (dest_c > best_c) {
                    best_c = dest_c;
                    best_nb = dest;
                }
            }
            if (best_nb != loc) {
                pl.agents[a].location = best_nb;
                return;
            }
        }
        // Otherwise, do not move (None in Python SSOT)
    }
}

static inline void take_economic_action(GameStateNative& st, uint8_t fid, FastRng& rng, const ConfigOverridesNative& ov) {
    move_agent_step(st, fid, rng);
    int amt = std::max(0, ov.intrigue_gold_base + ov.intrigue_gold_offset);
    st.players[fid].gold += amt;
}

static inline bool card_condition_met_native(const GameStateNative& st, uint8_t fid, uint8_t card_idx);

// Canonical heuristic card choice matching Python PoliticsAgent
static inline int choose_card_heuristic(const GameStateNative& st, uint8_t fid, const uint8_t* legal, int legal_count, FastRng& rng, const ConfigOverridesNative& ov) {
    if (legal_count == 0) return -1;
    const PlayerStateNative& pl = st.players[fid];

    float best_u = -999.0f;
    int best_idx = -1;

    // Threat calculation
    float max_threat = 0.0f;
    for (int p = 0; p < st.num_players; ++p) {
        uint8_t r_fid = st.turn_order[p];
        if (r_fid == fid) continue;
        const PlayerStateNative& r_pl = st.players[r_fid];
        float th = 0.0f;
        if (r_fid == SO) {
            int so_c = 0;
            for (int k = 0; k < 5; ++k) if (r_pl.condemned_rivals_mask & (1 << k)) so_c++;
            if (so_c >= 2) th += 0.85f;
            else if (so_c == 1) th += 0.40f;
            if (r_pl.stacks >= 6) th += 0.85f;
            else if (r_pl.stacks >= 4) th += 0.45f;
        } else if (r_fid == CAA) {
            if (r_pl.relics_evacuated >= 1) th += 0.70f;
            if (st.sea_route_open) th += 0.20f;
        } else if (r_fid == KB) {
            int r_hooks = 0;
            for (int k = 0; k < 5; ++k) if (r_pl.hooks_on[k] > 0) r_hooks++;
            if (r_hooks >= 2) th += 0.75f;
            else if (r_hooks == 1) th += 0.35f;
            if (r_pl.decrees_played >= 1) th += 0.3f;
        } else if (r_fid == KT) {
            if (r_pl.fragments >= 2) th += 0.75f;
            else if (r_pl.fragments == 1 && st.era >= 4) th += 0.30f;
        } else if (r_fid == GC) {
            if (r_pl.falls >= 18) th += 0.85f;
            else if (r_pl.falls >= 12) th += 0.45f;
        }
        if (th > max_threat) max_threat = th;
    }

    bool has_so = false;
    for (int p = 0; p < st.num_players; ++p) if (st.turn_order[p] == SO && fid != SO) has_so = true;
    bool autodafe_near = has_so && (st.eras_since_autodafe >= (ov.autodafe_cooldown - 1));

    for (int i = 0; i < legal_count; ++i) {
        uint8_t c_idx = legal[i];
        const CardDef& c = CARD_DB[c_idx];
        int eff_cost = effective_card_cost(c_idx, st, ov);

        float u = 1.8f;

        // A. Net Gold
        int net_gold = (int)c.gold_gain - eff_cost;
        if (net_gold > 0) u += (float)net_gold * 1.5f;
        else if (net_gold < 0) {
            u += (float)net_gold * 0.8f;
            if (pl.gold - eff_cost == 0 && eff_cost > 0) u -= 0.4f;
        }

        // B. Heresy cleanse
        if (c_idx == 28 && pl.heresy > 0) u += (float)std::min(pl.heresy, 1) * 2.2f;
        if (c_idx == 46 || c_idx == 47) u += (float)std::min(pl.heresy, 2) * 2.2f;

        // C. Heresy self-gain risk
        if (c.heresy > 0) {
            int post_h = pl.heresy + c.heresy;
            if (post_h >= ov.threshold) {
                u -= (float)c.heresy * 4.5f;
            } else if (post_h >= ov.threshold - 1) {
                u -= (float)c.heresy * 2.5f;
            } else if (has_so && post_h >= ov.observed_threshold) {
                if (autodafe_near) {
                    u -= (float)c.heresy * 3.0f;
                } else {
                    u -= (float)c.heresy * 1.2f;
                }
            } else {
                u -= (float)c.heresy * 0.3f;
            }
        }

        // D. Target Heresy / Framing
        if (c.target_heresy > 0) {
            u += (float)c.target_heresy * 1.8f;
            if (max_threat >= 0.7f) u += 1.5f;
            if (fid == SO && autodafe_near) u += 1.5f;
        }

        // E. Hooks
        if (c.creates_hook) {
            if (fid == GC) u += 3.6f;
            else if (fid == KB) u += 3.2f;
            else u += 2.2f;
        }

        // F. Arrests
        if (c.is_arrest) {
            u += 2.5f;
            if (max_threat >= 0.7f) u += 1.5f;
        }

        // G. Agent mobility
        if (c.agents_move > 0) {
            if (fid == CAA) u += 2.8f;
            else if (fid == KB) u += 1.8f;
            else u += 1.0f;
        }

        // H. Faction specific political synergies
        if (fid == CAA) {
            int relics_left = std::max(0, 2 - pl.relics_evacuated);
            if (c.tags & TAG_RELIC) {
                u += 3.5f;
                if (pl.relics_evacuated >= 1) u += 2.5f;
                if (st.sea_route_open && pl.relics_evacuated < 2) u += 1.8f;
            }
            if (c_idx == 12) u += 3.2f; // caa-01
            if (c_idx == 13) u += (pl.gold < 3 ? 3.6f : 1.8f); // caa-02
            if (c_idx == 14) { // caa-03
                bool on_relic = false;
                for (int a = 0; a < pl.agent_count; ++a) if (!pl.agents[a].arrested && st.relics_on_board[pl.agents[a].location] > 0) on_relic = true;
                if (on_relic) u += 3.5f;
            }
            if (c_idx == 15) u += 1.6f; // caa-04
            if (c_idx == 16) { // caa-05
                if (!pl.used_hook && pl.relics_evacuated < 2) {
                    bool on_relic = false;
                    for (int a = 0; a < pl.agent_count; ++a) if (!pl.agents[a].arrested && st.relics_on_board[pl.agents[a].location] > 0) on_relic = true;
                    u += (on_relic ? 5.5f : 3.5f);
                }
            }
            if (c_idx == 17) { // caa-06
                int arr = 0;
                for (int a = 0; a < pl.agent_count; ++a) if (pl.agents[a].arrested) arr++;
                if (arr >= 2) u += 5.5f;
                else if (arr == 1) u += 3.8f;
                else u += 1.2f;
            }
            if (c_idx == 19) u += 2.0f; // caa-08
            if (c_idx == 20) u += (pl.relics_evacuated < 2 ? 3.0f : 1.0f); // caa-09
            if (c_idx == 21) { // caa-10
                if (card_condition_met_native(st, fid, c_idx) || st.sea_route_open) {
                    u += (pl.relics_evacuated >= 1 ? 7.0f : 4.0f);
                } else {
                    u -= 18.0f;
                }
            }
            if (c_idx == 22) u += 2.2f; // caa-11
            if (c_idx == 23) u += 3.5f; // caa-12
        } else if (fid == KB) {
            int active_hooks = pl.distinct_hooks();
            int decrees_left = std::max(0, 2 - pl.decrees_played);
            if (c.tags & TAG_DECREE) {
                u += 3.8f;
                if (decrees_left == 1 && active_hooks >= 2) u += 4.5f;
                else if (decrees_left == 1) u += 2.5f;
            }
            if (c_idx == 33) { // kb-10
                if (active_hooks >= 2) u += (pl.decrees_played >= 1 ? 7.5f : 4.5f);
                else u -= 20.0f;
            }
            if (c_idx == 32 && pl.decrees_played < 2) u += 3.5f; // kb-09
            if (c_idx == 24 || c_idx == 26 || c_idx == 34) u += 1.6f; // kb-01, kb-03, kb-11
            if (c.creates_hook) {
                if (active_hooks < 2) u += (active_hooks == 0 ? 3.5f : 2.5f);
                else if (pl.distinct_hooks_ever() < 2) u += 2.0f;
            }
        } else if (fid == KT) {
            int frags_left = std::max(0, 3 - pl.fragments);
            if (c.tags & TAG_FRAGMENT) {
                u += 4.5f;
                if (frags_left <= 1) u += 3.0f;
            }
            if (c_idx == 38) u += 5.5f; // kt-03
            if (c_idx == 40) u += 5.0f; // kt-05
            if (c_idx == 41) u += 5.0f; // kt-06
            if (c_idx == 44) u += 5.0f; // kt-09
            if (c_idx == 45) { // kt-10
                if (pl.fragments >= 3) u += 12.0f;
                else u -= 20.0f;
            }
            if (c_idx == 36 || c_idx == 37 || c_idx == 39 || c_idx == 42 || c_idx == 43 || c_idx == 46 || c_idx == 47) {
                u += 2.0f;
            }
        } else if (fid == GC) {
            int falls_left = std::max(0, 8 - pl.falls);
            if (c_idx == 57) { // gc-10
                if (card_condition_met_native(st, fid, c_idx)) {
                    u += (falls_left <= 2 ? 9.5f : 6.5f);
                } else {
                    u -= 15.0f;
                }
            } else if (c.tags & TAG_FALL) {
                u += 4.8f;
                if (falls_left <= 2) u += 4.0f;
                else if (falls_left <= 4) u += 2.0f;
            }
            if (c_idx == 48 || c_idx == 50 || c_idx == 51 || c_idx == 53 || c_idx == 54 || c_idx == 55 || c_idx == 56 || c_idx == 58 || c_idx == 59) {
                u += 2.2f;
            }
        } else if (fid == SO) {
            if (c.tags & TAG_AUTODAFE) {
                if (st.eras_since_autodafe >= ov.autodafe_cooldown) {
                    int condemnable = 0;
                    for (int p = 0; p < st.num_players; ++p) {
                        uint8_t r = st.turn_order[p];
                        if (r != SO && st.players[r].heresy >= ov.observed_threshold) condemnable++;
                    }
                    if (condemnable >= 1) u += (pl.gold >= eff_cost ? 5.0f : 2.0f);
                    else u += 2.5f;
                } else {
                    u += 0.8f;
                }
            }
            if (c.tags & TAG_INQUISITOR && !pl.used_inquisitor_send) u += 2.5f;
            if (c_idx == 2) u += 3.5f; // so-03
            if (c_idx == 9) { // so-10
                int condemnable = 0;
                for (int p = 0; p < st.num_players; ++p) {
                    uint8_t r = st.turn_order[p];
                    if (r != SO && st.players[r].heresy >= ov.observed_threshold) condemnable++;
                }
                u += (condemnable >= 1 ? 6.5f : 3.0f);
            }
            if (c_idx == 0 || c_idx == 3 || c_idx == 5 || c_idx == 6 || c_idx == 7 || c_idx == 8 || c_idx == 10 || c_idx == 11) {
                u += 1.8f;
            }
        }

        if (c.card_type == 2) { // signature
            u += 2.0f;
        }

        // Small entropy tie-breaker
        u += (float)rng.next_double() * 0.2f;

        if (u > best_u) {
            best_u = u;
            best_idx = c_idx;
        }
    }

    // Dynamic economic action comparison (v_econ)
    int econ_gold = std::max(0, ov.intrigue_gold_base + ov.intrigue_gold_offset);
    float v_econ = (float)econ_gold * 0.9f + 0.3f;

    for (int h = 0; h < pl.hand_count; ++h) {
        uint8_t cid = pl.hand[h];
        const CardDef& fc = CARD_DB[cid];
        if (fc.card_type == 2 || (fc.tags & (TAG_AUTODAFE | TAG_RELIC | TAG_DECREE | TAG_FRAGMENT | TAG_FALL))) {
            int fc_cost = effective_card_cost(cid, st, ov);
            if (fc_cost > pl.gold && (pl.gold + econ_gold >= fc_cost)) {
                v_econ = std::max(v_econ, 2.8f);
                break;
            }
        }
    }

    if (pl.gold == 0) v_econ = std::max(v_econ, 1.8f);

    if (best_u < v_econ) {
        return -1; // Economic action is better
    }
    return best_idx;
}

static inline uint8_t pick_rival_native(const GameStateNative& st, uint8_t fid, FastRng& rng) {
    uint8_t max_r = 255;
    int max_h = -1;
    uint8_t rivals[4];
    int r_cnt = 0;
    for (int p = 0; p < st.num_players; ++p) {
        uint8_t r = st.turn_order[p];
        if (r != fid) {
            rivals[r_cnt++] = r;
            if (st.players[r].heresy > max_h) {
                max_h = st.players[r].heresy;
                max_r = r;
            }
        }
    }
    if (r_cnt == 0) return fid;
    if (max_r != 255 && rng.next_double() < 0.70) return max_r;
    return rivals[rng.next_u32(r_cnt)];
}

static inline void apply_card_effect(GameStateNative& st, uint8_t fid, uint8_t card_idx, FastRng& rng, const ConfigOverridesNative& ov) {
    const CardDef& c = CARD_DB[card_idx];
    PlayerStateNative& pl = st.players[fid];

    st.cards_played[card_idx]++;

    if (c.gold_gain > 0) {
        pl.gold += c.gold_gain;
    }

    if (c.heresy > 0) {
        pl.heresy = std::min(10, pl.heresy + c.heresy);
    }

    if (c.target_heresy > 0) {
        uint8_t victim = pick_rival_native(st, fid, rng);
        st.players[victim].heresy = std::min(10, st.players[victim].heresy + c.target_heresy);
        pl.frames_dealt += c.target_heresy;
    }

    if (c.agents_move > 0) {
        move_agent_step(st, fid, rng);
    }

    if (c.is_arrest) {
        uint8_t victim = pick_rival_native(st, fid, rng);
        PlayerStateNative& vpl = st.players[victim];
        for (int a = 0; a < vpl.agent_count; ++a) {
            if (!vpl.agents[a].arrested) {
                vpl.agents[a].arrested = true;
                vpl.agents[a].location = LOCHY;
                break;
            }
        }
    }

    if (card_idx == 9) { // so-10 (Oczyść Miasto - Force Autodafe)
        int burned = 0;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t r_fid = st.turn_order[p];
            if (r_fid == SO) continue;
            PlayerStateNative& r_pl = st.players[r_fid];
            if (r_pl.avoided_autodafe) continue;
            for (int a = 0; a < r_pl.agent_count; ++a) {
                if (!r_pl.agents[a].arrested && r_pl.agents[a].location == st.inquisitor_location) {
                    r_pl.heresy = std::min(10, r_pl.heresy + 1);
                    r_pl.agents[a].arrested = true;
                    r_pl.agents[a].location = LOCHY;
                    if (r_pl.heresy >= ov.observed_threshold) {
                        burned++;
                        if (r_fid != GC && (st.players[GC].hook_victims_ever_mask & (1 << r_fid))) {
                            st.players[GC].falls++;
                        }
                    }
                }
            }
        }
        st.autodafe_count++;
        st.eras_since_autodafe = 0;
        if (burned > 0) {
            st.players[SO].stacks += burned;
        }
    }

    if (c.creates_hook) {
        st.hooks_created++;
        uint8_t victim = pick_rival_native(st, fid, rng);
        int total_hooks = 0;
        for (int k = 0; k < 5; ++k) total_hooks += pl.hooks_on[k];
        if (total_hooks < 2) {
            pl.hooks_on[victim]++;
        }
        pl.hook_victims_ever_mask |= (1 << victim);
    }

    if (card_idx == 28) { // kb-05 (List Żelazny)
        if (pl.heresy > 0) pl.heresy -= 1;
    }

    if (card_idx == 32 || card_idx == 33) { // kb-09, kb-10
        if (card_idx == 33) { // kb-10
            if (pl.distinct_hooks() >= 2) {
                pl.decrees_played++;
            }
        } else { // kb-09
            pl.decrees_played++;
            int active_h = pl.distinct_hooks();
            if (active_h == 0 && pl.distinct_hooks_ever() >= 1) {
                uint8_t rival = pick_rival_native(st, fid, rng);
                int total_hooks = 0;
                for (int k = 0; k < 5; ++k) total_hooks += pl.hooks_on[k];
                if (total_hooks < 2) {
                    pl.hooks_on[rival]++;
                    pl.hook_victims_ever_mask |= (1 << rival);
                }
            }
        }
    }

    if (c.tags & TAG_FRAGMENT) {
        if (card_idx == 38) { // kt-03 (Zakazana Wiedza)
            pl.fragments++;
        } else if (card_idx == 40) { // kt-05 (Wskazówka Cyklu)
            bool in_place = false;
            for (int a = 0; a < pl.agent_count; ++a) {
                if (pl.agents[a].location == LOCHY || pl.agents[a].location == TRYBUNAL) in_place = true;
            }
            if (in_place) pl.fragments++;
            else pl.gold++;
        } else if (card_idx == 41) { // kt-06 (Przesłuchanie Mistyczne)
            uint8_t rival = pick_rival_native(st, fid, rng);
            if (rival != fid) {
                st.players[rival].heresy = std::min(10, st.players[rival].heresy + 2);
                pl.fragments++;
            }
        } else if (card_idx == 44) { // kt-09 (Ostatnia Glosa)
            bool in_place = false;
            for (int a = 0; a < pl.agent_count; ++a) {
                if (pl.agents[a].location == LOCHY || pl.agents[a].location == TRYBUNAL) in_place = true;
            }
            if (pl.fragments >= 1 && in_place) pl.fragments++;
        } else if (card_idx == 45) { // kt-10 (Pieczęć Salomona)
            if (pl.fragments >= 3) {
                pl.kt10_played = true;
            }
        }
    }

    if (card_idx == 46) { // kt-11 (Głos z Ukrycia)
        pl.heresy = std::max(0, pl.heresy - 1);
    }
    if (card_idx == 47) { // kt-12 (Tajemna Ścieżka)
        pl.heresy = std::max(0, pl.heresy - 1);
    }

    if (card_idx == 57) { // gc-10 (Upadek Domu)
        pl.falls += 1;
    }

    if (c.tags & TAG_RELIC) {
        if (card_idx == 16) { // caa-05 (Odnalezienie Relikwii)
            uint8_t loc = RYNEK;
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested) {
                    loc = pl.agents[a].location;
                    break;
                }
            }
            if (st.relics_on_board[loc] > 0) {
                st.relics_on_board[loc]--;
                pl.relics_evacuated++;
            } else {
                st.relics_on_board[loc]++;
            }
        } else if (card_idx == 21) { // caa-10 (Echo Alhambry)
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested) {
                    uint8_t loc = pl.agents[a].location;
                    if (st.relics_on_board[loc] > 0) {
                        bool in_port = (loc == RYNEK || loc == GILDIA);
                        bool quiet = in_port && (st.inquisitor_location != loc);
                        if (pl.path_via_double || (st.sea_route_open && in_port) || quiet) {
                            st.relics_on_board[loc]--;
                            pl.relics_evacuated++;
                            if (quiet) pl.shadow_exit = true;
                            else pl.avoided_autodafe = true;
                            break;
                        }
                    }
                }
            }
        } else { // caa-03, caa-09
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested) {
                    uint8_t loc = pl.agents[a].location;
                    if (st.relics_on_board[loc] > 0) {
                        uint8_t cnt = NEIGHBOR_COUNTS[loc];
                        if (cnt > 0) {
                            uint8_t dest = NEIGHBORS[loc][rng.next_u32(cnt)];
                            st.relics_on_board[loc]--;
                            st.relics_on_board[dest]++;
                            break;
                        }
                    }
                }
            }
        }
    }

    // Add to discard
    if (pl.discard_count < 12) {
        pl.discard[pl.discard_count++] = card_idx;
    }
}

static inline bool card_condition_met_native(const GameStateNative& st, uint8_t fid, uint8_t card_idx) {
    const PlayerStateNative& pl = st.players[fid];

    // caa-10 (21)
    if (card_idx == 21) {
        if (st.sea_route_open || pl.path_via_double) return true;
        for (int a = 0; a < pl.agent_count; ++a) {
            if (!pl.agents[a].arrested && pl.agents[a].location != st.inquisitor_location) {
                return true;
            }
        }
        return false;
    }
    // kb-10 (33)
    if (card_idx == 33) {
        return pl.distinct_hooks() >= 2;
    }
    // kt-09 (44)
    if (card_idx == 44) {
        if (pl.fragments < 1) return false;
        for (int a = 0; a < pl.agent_count; ++a) {
            if (!pl.agents[a].arrested && (pl.agents[a].location == LOCHY || pl.agents[a].location == TRYBUNAL)) return true;
        }
        return false;
    }
    // kt-10 (45)
    if (card_idx == 45) {
        return pl.fragments >= 3;
    }
    // gc-10 (57)
    if (card_idx == 57) {
        if (pl.distinct_hooks() > 0 || pl.distinct_hooks_ever() > 0) return true;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t r = st.turn_order[p];
            if (r != fid && r != SO) {
                for (int a = 0; a < st.players[r].agent_count; ++a) {
                    if (!st.players[r].agents[a].arrested && st.players[r].agents[a].location == st.inquisitor_location) return true;
                }
            }
        }
        return false;
    }

    return true;
}

static inline void play_turn_era(GameStateNative& st, FastRng& rng, const ConfigOverridesNative& ov) {
    st.eras_since_autodafe++;
    if (st.era >= ov.sea_route_era) {
        st.sea_route_open = true;
    }
    st.accused_this_era_mask = 0;
    st.pending_count = 0;

    for (int p = 0; p < st.num_players; ++p) {
        PlayerStateNative& pl = st.players[st.turn_order[p]];
        pl.used_hook = false;
        pl.used_interrogation = false;
        pl.used_inquisitor_send = false;
        pl.frames_dealt = 0;
    }

    // ── Phase I: Intryga ──
    for (int round = 0; round < ov.cards_per_era; ++round) {
        for (int i = 0; i < st.num_players; ++i) {
            uint8_t fid = st.turn_order[i];
            PlayerStateNative& pl = st.players[fid];

            uint8_t legal[12];
            int legal_count = 0;
            for (int h = 0; h < pl.hand_count; ++h) {
                uint8_t cid = pl.hand[h];
                if (CARD_DB[cid].card_type == 1) continue; // Reaction
                if (cid == 33 && !card_condition_met_native(st, fid, cid)) continue; // kb-10
                if (cid == 21 && !card_condition_met_native(st, fid, cid)) continue; // caa-10

                int cost = effective_card_cost(cid, st, ov);
                if (pl.gold >= cost) {
                    legal[legal_count++] = cid;
                }
            }

            st.legal_moves_sampled += legal_count;

            if (legal_count == 0) {
                st.forced_passes++;
                take_economic_action(st, fid, rng, ov);
            } else {
                int chosen = choose_card_heuristic(st, fid, legal, legal_count, rng, ov);
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

                // Hook forcing (1 per player per era)
                if (!pl.used_hook) {
                    bool protect_hooks = (fid == KB && pl.hand_has(33) && pl.distinct_hooks() >= 2);
                    if (!protect_hooks) {
                        for (int k = 0; k < 5; ++k) {
                            if (pl.hooks_on[k] > 0) {
                                pl.used_hook = true;
                                st.hooks_forced++;
                                pl.hooks_on[k]--;
                                bool comply = (st.players[k].heresy + 2 >= ov.threshold);
                                if (comply && st.players[k].gold > 0) {
                                    st.players[k].gold--;
                                    pl.gold++;
                                } else {
                                    st.players[k].heresy = std::min(10, st.players[k].heresy + 2);
                                    if (fid == GC) pl.falls++;
                                }
                                break;
                            }
                        }
                    }
                }
            }
            if (check_winner_fast(st, ov) != NO_FACTION) return;
        }
    }

    // ── Phase II: Sąd (Inquisitor, Autodafe, Pending, Interrogations, Verdicts) ──
    // 1. Inquisitor movement (Nasłanie / Patrol)
    uint8_t naslanie_target[5] = {255, 255, 255, 255, 255};
    for (int p = 0; p < st.num_players; ++p) {
        uint8_t fid = st.turn_order[p];
        const PlayerStateNative& pl = st.players[fid];
        if (pl.used_inquisitor_send) continue;

        int r_counts_local[5] = {0, 0, 0, 0, 0};
        for (int op = 0; op < st.num_players; ++op) {
            uint8_t ofid = st.turn_order[op];
            if (ofid == fid) continue;
            const PlayerStateNative& opl = st.players[ofid];
            for (int a = 0; a < opl.agent_count; ++a) {
                if (!opl.agents[a].arrested && opl.agents[a].location < 5) {
                    r_counts_local[opl.agents[a].location]++;
                }
            }
        }

        if (fid == CAA) {
            bool has_relic_agent[5] = {false, false, false, false, false};
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested && pl.agents[a].location < 5 && st.relics_on_board[pl.agents[a].location] > 0) {
                    has_relic_agent[pl.agents[a].location] = true;
                }
            }
            int max_c = 0;
            uint8_t best_loc = 255;
            for (int l = 0; l < 5; ++l) {
                if (!has_relic_agent[l] && r_counts_local[l] > max_c) {
                    max_c = r_counts_local[l];
                    best_loc = l;
                }
            }
            if (best_loc != 255) naslanie_target[fid] = best_loc;
        } else {
            int max_c = 0;
            uint8_t best_loc = 255;
            for (int l = 0; l < 5; ++l) {
                if (r_counts_local[l] > max_c) {
                    max_c = r_counts_local[l];
                    best_loc = l;
                }
            }
            if (best_loc != 255) naslanie_target[fid] = best_loc;
        }
    }

    uint8_t naslanie_winner = 255;
    if (naslanie_target[SO] != 255) {
        naslanie_winner = SO;
    } else if (naslanie_target[st.turn_order[0]] != 255) {
        naslanie_winner = st.turn_order[0];
    } else {
        int min_h = 999;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t fid = st.turn_order[p];
            if (naslanie_target[fid] != 255 && st.players[fid].heresy < min_h) {
                min_h = st.players[fid].heresy;
                naslanie_winner = fid;
            }
        }
    }

    if (naslanie_winner != 255) {
        uint8_t tgt = naslanie_target[naslanie_winner];
        st.inquisitor_location = STEP_TOWARD_TABLE[st.inquisitor_location][tgt];
    } else {
        uint8_t chooser = st.turn_order[0];
        int min_h = 999;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t f = st.turn_order[p];
            if (st.players[f].heresy < min_h) {
                min_h = st.players[f].heresy;
                chooser = f;
            }
        }

        int r_counts[5] = {0};
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t f = st.turn_order[p];
            if (f == chooser) continue;
            const PlayerStateNative& pl = st.players[f];
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested && pl.agents[a].location < 5) {
                    r_counts[pl.agents[a].location]++;
                }
            }
        }

        uint8_t cur_inq = st.inquisitor_location;
        uint8_t n_cnt = NEIGHBOR_COUNTS[cur_inq];
        uint8_t best_dest = cur_inq;
        int best_score = r_counts[cur_inq];

        for (int i = 0; i < n_cnt; ++i) {
            uint8_t nb = NEIGHBORS[cur_inq][i];
            int nb_score = r_counts[nb];
            if (nb_score > best_score) {
                best_score = nb_score;
                best_dest = nb;
            }
        }
        st.inquisitor_location = best_dest;
    }

    // 2. Autodafe check (only if rival agent present at inquisitor location and cooldown elapsed)
    bool has_rival_agent = false;
    for (int p = 0; p < st.num_players; ++p) {
        uint8_t fid = st.turn_order[p];
        if (fid == SO) continue;
        const PlayerStateNative& pl = st.players[fid];
        for (int a = 0; a < pl.agent_count; ++a) {
            if (!pl.agents[a].arrested && pl.agents[a].location == st.inquisitor_location) {
                has_rival_agent = true;
                break;
            }
        }
        if (has_rival_agent) break;
    }

    if (has_rival_agent && st.eras_since_autodafe >= ov.autodafe_cooldown) {
        int burned = 0;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t fid = st.turn_order[p];
            if (fid == SO) continue;
            PlayerStateNative& pl = st.players[fid];
            if (pl.avoided_autodafe) continue; // Escaped
            for (int a = 0; a < pl.agent_count; ++a) {
                if (!pl.agents[a].arrested && pl.agents[a].location == st.inquisitor_location) {
                    pl.heresy = std::min(10, pl.heresy + 1);
                    pl.agents[a].arrested = true;
                    pl.agents[a].location = LOCHY;
                    if (pl.heresy >= ov.observed_threshold) {
                        burned++;
                        if (fid != GC && (st.players[GC].hook_victims_ever_mask & (1 << fid))) {
                            st.players[GC].falls++;
                        }
                    }
                }
            }
        }
        st.autodafe_count++;
        st.eras_since_autodafe = 0;
        if (burned > 0) {
            st.players[SO].stacks += burned;
        }
    }

    if (check_winner_fast(st, ov) != NO_FACTION) return;

    // 3. Resolve pending plays
    for (int p = 0; p < st.pending_count; ++p) {
        apply_card_effect(st, st.pending_plays[p].owner, st.pending_plays[p].card_idx, rng, ov);
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
                if (fid == CAA) {
                    pl.path_via_double = true;
                } else if (fid == SO) {
                    st.players[r_fid].heresy = std::min(10, st.players[r_fid].heresy + 2);
                } else {
                    // KB, GC, KT prefer hook (no +2 heresy)
                    pl.hooks_on[r_fid]++;
                    pl.hook_victims_ever_mask |= (1 << r_fid);
                }
                break;
            }
        }
    }

    // Accusations & Verdicts (1 accusation per player in turn order)
    for (int i = 0; i < st.num_players; ++i) {
        uint8_t fid = st.turn_order[i];

        uint8_t accused_list[5];
        int accused_cnt = 0;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t r = st.turn_order[p];
            if (r != fid && !(st.accused_this_era_mask & (1 << r)) && st.players[r].heresy >= ov.threshold) {
                accused_list[accused_cnt++] = r;
            }
        }
        if (accused_cnt == 0) continue;

        bool so_near_win = false;
        int so_cond_need = std::max(1, (st.num_players <= 3 ? 2 : 3) + ov.so_condemns_offset);
        int so_stack_need = std::max(1, 7 + ov.so_stacks_offset);
        int so_conds = 0;
        for (int k = 0; k < 5; ++k) if (st.players[SO].condemned_rivals_mask & (1 << k)) so_conds++;
        if (st.players[SO].stacks >= std::max(1, so_stack_need - 1) || so_conds >= std::max(1, so_cond_need - 1)) {
            so_near_win = true;
        }

        uint8_t fresh[5];
        int fresh_cnt = 0;
        for (int a = 0; a < accused_cnt; ++a) {
            uint8_t r = accused_list[a];
            if (!(st.players[SO].condemned_rivals_mask & (1 << r))) {
                fresh[fresh_cnt++] = r;
            }
        }

        uint8_t target = NO_FACTION;
        if (so_near_win) {
            for (int a = 0; a < accused_cnt; ++a) {
                if (accused_list[a] == SO) { target = SO; break; }
            }
        }
        if (target == NO_FACTION) {
            if (fid == SO && fresh_cnt > 0) {
                target = fresh[0];
            } else if (fresh_cnt > 0) {
                target = fresh[0];
            } else {
                target = accused_list[0];
            }
        }

        if (target == NO_FACTION || target == fid) continue;
        if (st.accused_this_era_mask & (1 << target)) continue;

        st.accused_this_era_mask |= (1 << target);
        st.accusations++;

        // Table vote:
        int votes_burn = 0;
        int votes_spare = 0;
        for (int p = 0; p < st.num_players; ++p) {
            uint8_t voter = st.turn_order[p];
            if (voter == target) continue;
            bool prefer_burn = false;
            if (target == SO && so_near_win) {
                prefer_burn = (st.players[target].heresy >= 7 || rng.next_double() < 0.65);
            } else if (so_near_win && target != SO) {
                prefer_burn = (st.players[target].heresy >= 9 || rng.next_double() < 0.22);
            } else {
                prefer_burn = (st.players[target].heresy >= 8 || rng.next_double() < 0.45);
            }
            if (prefer_burn) votes_burn++;
            else votes_spare++;
        }

        if (votes_burn > votes_spare) {
            // Convicted
            st.convictions++;
            st.players[target].heresy = std::min(10, st.players[target].heresy + 1);
            for (int a = 0; a < st.players[target].agent_count; ++a) {
                if (!st.players[target].agents[a].arrested) {
                    st.players[target].agents[a].arrested = true;
                    st.players[target].agents[a].location = LOCHY;
                    break;
                }
            }
            if (target != SO) {
                st.players[SO].condemned_rivals_mask |= (1 << target);
            }
            if (fid == SO && target != SO) {
                st.players[SO].stacks++;
            }
            if (target != GC && (st.players[GC].hook_victims_ever_mask & (1 << target))) {
                st.players[GC].falls++;
            }
        }
        if (check_winner_fast(st, ov) != NO_FACTION) return;
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

    for (int era = 1; era <= ov.max_eras; ++era) {
        final_st.era = era;
        play_turn_era(final_st, rng, ov);
        if (final_st.winner != NO_FACTION) {
            out_eras = era;
            out_path = final_st.win_path;
            return final_st.winner;
        }
    }

    // Tie-break after max eras
    out_eras = ov.max_eras;
    out_path = "tiebreak";
    final_st.deadlocks++;

    uint8_t best_f = final_st.turn_order[0];
    int max_prog = -999;
    for (int i = 0; i < final_st.num_players; ++i) {
        uint8_t fid = final_st.turn_order[i];
        const PlayerStateNative& pl = final_st.players[fid];
        int p = pl.stacks + pl.relics_evacuated + pl.decrees_played + pl.fragments + pl.falls - pl.heresy;
        if (p > max_prog) {
            max_prog = p;
            best_f = fid;
        }
    }
    final_st.winner = best_f;
    return best_f;
}

} // namespace inq

// ─── Python C-API Extension Wrapper ─────────────────────────────────────────
static PyObject* py_run_batch_fast(PyObject* self, PyObject* args, PyObject* kwargs) {
    int num_games = 500;
    const char* setup_str = "4p-core";
    uint64_t seed = 42;
    int threshold = 8;
    const char* layer = "C";
    PyObject* py_win_overrides = NULL;
    PyObject* py_overrides = NULL;

    static const char* kwlist[] = {"games", "setup", "seed", "threshold", "layer", "win_overrides", "overrides", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|isKizOO", (char**)kwlist,
                                     &num_games, &setup_str, &seed, &threshold, &layer, &py_win_overrides, &py_overrides)) {
        return NULL;
    }

    if (!py_overrides && py_win_overrides) {
        py_overrides = py_win_overrides;
    }

    int preset_id = 0;
    if (std::strcmp(setup_str, "4p-no-cienie") == 0) preset_id = 1;
    else if (std::strcmp(setup_str, "4p-no-kabala") == 0) preset_id = 2;
    else if (std::strcmp(setup_str, "4p-no-korona") == 0) preset_id = 3;
    else if (std::strcmp(setup_str, "4p-no-oficjum") == 0) preset_id = 4;

    inq::ConfigOverridesNative ov;
    if (py_overrides && PyDict_Check(py_overrides)) {
        PyObject* val;
        if ((val = PyDict_GetItemString(py_overrides, "card_cost_offset"))) ov.card_cost_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "sig_cost_offset"))) ov.sig_cost_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "intrigue_gold_offset"))) ov.intrigue_gold_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "era_income_offset"))) ov.era_income_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "cards_per_era"))) ov.cards_per_era = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "cards_per_era_offset"))) ov.cards_per_era += (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "so_stacks_offset"))) ov.so_stacks_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "so_condemns_offset"))) ov.so_condemns_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "caa_relics_offset"))) ov.caa_relics_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kb_decrees_offset"))) ov.kb_decrees_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kb_hooks_offset"))) ov.kb_hooks_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "kt_frags_offset"))) ov.kt_frags_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "gc_falls_offset"))) ov.gc_falls_offset = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "sea_route_era"))) ov.sea_route_era = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "autodafe_cooldown"))) ov.autodafe_cooldown = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "threshold"))) ov.threshold = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "observed_threshold"))) ov.observed_threshold = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "hand_limit"))) ov.hand_limit = (int)PyLong_AsLong(val);
        if ((val = PyDict_GetItemString(py_overrides, "max_eras"))) ov.max_eras = (int)PyLong_AsLong(val);

        PyObject* card_ov = PyDict_GetItemString(py_overrides, "card_cost_overrides");
        if (card_ov && PyDict_Check(card_ov)) {
            PyObject *key, *val_cost;
            Py_ssize_t pos = 0;
            while (PyDict_Next(card_ov, &pos, &key, &val_cost)) {
                if (PyUnicode_Check(key) && PyLong_Check(val_cost)) {
                    const char* cid_str = PyUnicode_AsUTF8(key);
                    for (int c = 0; c < 60; ++c) {
                        if (std::strcmp(inq::CARD_DB[c].id, cid_str) == 0) {
                            ov.card_cost_overrides[c] = (int)PyLong_AsLong(val_cost);
                            ov.has_card_cost_override[c] = true;
                            break;
                        }
                    }
                }
            }
        }
    }

    int win_counts[5] = {0, 0, 0, 0, 0};
    int total_eras = 0;
    int era_dist[13] = {0};
    int deadlocks = 0;
    int forced_passes = 0;
    int legal_moves_sampled = 0;
    int accusations = 0;
    int convictions = 0;
    int autodafe_count = 0;
    int hooks_created = 0;
    int hooks_forced = 0;
    int doubles_created = 0;
    long long total_end_gold = 0;
    long long total_end_heresy = 0;
    long long total_poor_turns = 0;
    std::map<std::string, int> win_paths;
    int card_plays[60] = {0};

    unsigned int n_threads = std::thread::hardware_concurrency();
    if (n_threads == 0) n_threads = 4;
    int games_per_thread = num_games / n_threads;

    struct ThreadResult {
        int wins[5] = {0};
        int eras = 0;
        int dist[13] = {0};
        int deadlocks = 0;
        int passes = 0;
        int sampled = 0;
        int accusations = 0;
        int convictions = 0;
        int autodafe = 0;
        int hooks_created = 0;
        int hooks_forced = 0;
        int doubles_created = 0;
        long long end_gold = 0;
        long long end_heresy = 0;
        long long poor_turns = 0;
        std::map<std::string, int> paths;
        int cards[60] = {0};
    };

    std::vector<std::future<ThreadResult>> futures;

    for (unsigned int t = 0; t < n_threads; ++t) {
        int count = (t == n_threads - 1) ? (num_games - t * games_per_thread) : games_per_thread;
        uint64_t thread_seed = seed + t * 1000003ULL;

        futures.push_back(std::async(std::launch::async, [preset_id, thread_seed, ov, count]() {
            ThreadResult res;
            inq::GameStateNative st;
            for (int g = 0; g < count; ++g) {
                int eras = 0;
                const char* path = "";
                uint8_t w = inq::play_game_fast(preset_id, thread_seed + g, ov, eras, path, st);
                if (w < 5) res.wins[w]++;
                res.eras += eras;
                if (eras >= 0 && eras <= 12) res.dist[eras]++;
                res.deadlocks += st.deadlocks;
                res.passes += st.forced_passes;
                res.sampled += st.legal_moves_sampled;
                res.accusations += st.accusations;
                res.convictions += st.convictions;
                res.autodafe += st.autodafe_count;
                res.hooks_created += st.hooks_created;
                res.hooks_forced += st.hooks_forced;
                res.doubles_created += st.doubles_created;
                res.paths[path]++;

                for (int i = 0; i < st.num_players; ++i) {
                    uint8_t fid = st.turn_order[i];
                    res.end_gold += st.players[fid].gold;
                    res.end_heresy += st.players[fid].heresy;
                    if (st.players[fid].gold <= 1) res.poor_turns++;
                }

                for (int c = 0; c < 60; ++c) {
                    res.cards[c] += st.cards_played[c];
                }
            }
            return res;
        }));
    }

    for (auto& f : futures) {
        ThreadResult r = f.get();
        for (int i = 0; i < 5; ++i) win_counts[i] += r.wins[i];
        total_eras += r.eras;
        for (int e = 0; e <= 12; ++e) era_dist[e] += r.dist[e];
        deadlocks += r.deadlocks;
        forced_passes += r.passes;
        legal_moves_sampled += r.sampled;
        accusations += r.accusations;
        convictions += r.convictions;
        autodafe_count += r.autodafe;
        hooks_created += r.hooks_created;
        hooks_forced += r.hooks_forced;
        doubles_created += r.doubles_created;
        total_end_gold += r.end_gold;
        total_end_heresy += r.end_heresy;
        total_poor_turns += r.poor_turns;
        for (auto const& [k, v] : r.paths) {
            win_paths[k] += v;
        }
        for (int c = 0; c < 60; ++c) {
            card_plays[c] += r.cards[c];
        }
    }

    // Build return Python dictionary
    PyObject* py_res = PyDict_New();

    // 1. wins dict
    static const char* FACTION_NAMES[5] = {
        "swiete-oficjum", "cienie-al-andalus", "korona-borgiowie", "kabala-toledo", "gildia-cieni"
    };
    PyObject* py_wins = PyDict_New();
    for (int i = 0; i < 5; ++i) {
        PyDict_SetItemString(py_wins, FACTION_NAMES[i], PyLong_FromLong(win_counts[i]));
    }
    PyDict_SetItemString(py_res, "wins", py_wins);
    Py_DECREF(py_wins);

    // 2. win_paths dict
    PyObject* py_paths = PyDict_New();
    for (auto const& [k, v] : win_paths) {
        PyDict_SetItemString(py_paths, k.c_str(), PyLong_FromLong(v));
    }
    PyDict_SetItemString(py_res, "win_paths", py_paths);
    Py_DECREF(py_paths);

    // 3. era_dist dict
    PyObject* py_dist = PyDict_New();
    for (int e = 1; e <= 12; ++e) {
        PyObject* k = PyLong_FromLong(e);
        PyObject* v = PyLong_FromLong(era_dist[e]);
        PyDict_SetItem(py_dist, k, v);
        Py_DECREF(k);
        Py_DECREF(v);
    }
    PyDict_SetItemString(py_res, "era_dist", py_dist);
    PyDict_SetItemString(py_res, "era_hist", py_dist);
    Py_DECREF(py_dist);

    // 4. card_plays dict
    PyObject* py_cards = PyDict_New();
    for (int c = 0; c < 60; ++c) {
        PyDict_SetItemString(py_cards, inq::CARD_DB[c].id, PyLong_FromLong(card_plays[c]));
    }
    PyDict_SetItemString(py_res, "card_plays", py_cards);
    Py_DECREF(py_cards);

    // 5. Scalars
    double avg_eras = (num_games > 0) ? (double)total_eras / num_games : 0.0;
    PyDict_SetItemString(py_res, "eras_avg", PyFloat_FromDouble(avg_eras));
    PyDict_SetItemString(py_res, "deadlocks", PyLong_FromLong(deadlocks));
    PyDict_SetItemString(py_res, "forced_passes", PyLong_FromLong(forced_passes));
    PyDict_SetItemString(py_res, "legal_moves_sampled", PyLong_FromLong(legal_moves_sampled));
    PyDict_SetItemString(py_res, "accusations", PyLong_FromLong(accusations));
    PyDict_SetItemString(py_res, "convictions", PyLong_FromLong(convictions));
    PyDict_SetItemString(py_res, "autodafe_count", PyLong_FromLong(autodafe_count));

    double autodafe_avg = (num_games > 0) ? (double)autodafe_count / num_games : 0.0;
    double accusations_avg = (num_games > 0) ? (double)accusations / num_games : 0.0;
    double convictions_avg = (num_games > 0) ? (double)convictions / num_games : 0.0;
    double deadlocks_avg = (num_games > 0) ? (double)deadlocks / num_games : 0.0;
    int total_turns = total_eras * 4 * ov.cards_per_era;
    double passes_forced_pct = (total_turns > 0) ? (double)forced_passes / total_turns : 0.0;
    double hooks_avg = (num_games > 0) ? (double)hooks_created / num_games : 0.0;
    double hooks_forced_avg = (num_games > 0) ? (double)hooks_forced / num_games : 0.0;
    double doubles_avg = (num_games > 0) ? (double)doubles_created / num_games : 0.0;
    double legal_moves_avg = (num_games > 0) ? (double)legal_moves_sampled / num_games : 0.0;

    PyDict_SetItemString(py_res, "autodafe_avg", PyFloat_FromDouble(autodafe_avg));
    PyDict_SetItemString(py_res, "accusations_avg", PyFloat_FromDouble(accusations_avg));
    PyDict_SetItemString(py_res, "convictions_avg", PyFloat_FromDouble(convictions_avg));
    PyDict_SetItemString(py_res, "deadlocks_avg", PyFloat_FromDouble(deadlocks_avg));
    PyDict_SetItemString(py_res, "eras_limit_pct", PyFloat_FromDouble(deadlocks_avg));
    PyDict_SetItemString(py_res, "passes_forced_pct", PyFloat_FromDouble(passes_forced_pct));
    PyDict_SetItemString(py_res, "hooks_avg", PyFloat_FromDouble(hooks_avg));
    PyDict_SetItemString(py_res, "hooks_forced_avg", PyFloat_FromDouble(hooks_forced_avg));
    PyDict_SetItemString(py_res, "doubles_avg", PyFloat_FromDouble(doubles_avg));
    PyDict_SetItemString(py_res, "legal_moves_avg", PyFloat_FromDouble(legal_moves_avg));

    int total_player_games = num_games * 4;
    double avg_gold = (total_player_games > 0) ? (double)total_end_gold / total_player_games : 0.0;
    double avg_heresy = (total_player_games > 0) ? (double)total_end_heresy / total_player_games : 0.0;
    double poverty_rate = (total_player_games > 0) ? (double)total_poor_turns / total_player_games : 0.0;

    PyDict_SetItemString(py_res, "avg_gold_end", PyFloat_FromDouble(avg_gold));
    PyDict_SetItemString(py_res, "avg_heresy_end", PyFloat_FromDouble(avg_heresy));
    PyDict_SetItemString(py_res, "avg_end_gold", PyFloat_FromDouble(avg_gold));
    PyDict_SetItemString(py_res, "avg_end_heresy", PyFloat_FromDouble(avg_heresy));
    PyDict_SetItemString(py_res, "poverty_rate", PyFloat_FromDouble(poverty_rate));

    return py_res;
}

static PyMethodDef InquisitioNativeMethods[] = {
    {"run_batch", (PyCFunction)py_run_batch_fast, METH_VARARGS | METH_KEYWORDS, "Run high performance simulation batch in native C++20"},
    {"run_batch_fast", (PyCFunction)py_run_batch_fast, METH_VARARGS | METH_KEYWORDS, "Run high performance simulation batch in native C++20"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef inquisitio_native_module = {
    PyModuleDef_HEAD_INIT,
    "inquisitio_native",
    "High performance native simulation engine for INQUISITIO-1492",
    -1,
    InquisitioNativeMethods
};

PyMODINIT_FUNC PyInit_inquisitio_native(void) {
    return PyModule_Create(&inquisitio_native_module);
}
