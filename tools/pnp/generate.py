#!/usr/bin/env python3
"""Generate Print & Play HTML — UI-only layout (SVG/CSS).

No image assets in repo: tokens use temporary emoji on rounded-square chips.
Slots, board graph, and print sizes live entirely in code.

Usage (repo root, sim venv):
  python tools/pnp/generate.py
  # → assets/prototypes/ (warstwa C — jedyny commitowany PnP)
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SIM_ROOT = REPO_ROOT / "sim"
if str(SIM_ROOT) not in sys.path:
    sys.path.insert(0, str(SIM_ROOT))

from inquisitio.cards.loader import Card, cards_for_faction, load_all_cards  # noqa: E402

import yaml

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def load_game_config() -> dict:
    cfg_path = REPO_ROOT / "game_config.yaml"
    if cfg_path.is_file():
        with open(cfg_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    return {}


def get_factions_data(cfg: dict | None = None) -> list[tuple[str, str, str, str, str, int, str]]:
    """Returns list of (slug, name, goal_4p, note, progress_label, progress_n, progress_icon)."""
    if cfg is None:
        cfg = load_game_config()

    v = cfg.get("victory", {})

    # 1. Święte Oficjum
    so_v = v.get("swiete_oficjum", {})
    so_stacks = so_v.get("stacks", {})
    so_s4 = so_stacks.get("4p", 4) if isinstance(so_stacks, dict) else so_stacks
    so_s3 = so_stacks.get("3p", 3) if isinstance(so_stacks, dict) else so_stacks
    so_cond = so_v.get("condemns", 3)
    so_cond = so_cond.get("4p", 3) if isinstance(so_cond, dict) else so_cond
    so_goal = f"{so_s4} Stosy lub {so_cond} Skazania Werdyktem"
    so_note = f"*w 3p: {so_s3} Stosy" if so_s3 != so_s4 else ""

    # 2. Cienie Al-Andalus
    caa_v = v.get("cienie_al_andalus", {})
    caa_r = caa_v.get("relics", 2)
    caa_p = caa_v.get("path_era", 5)
    caa_p4 = caa_p.get("4p", 5) if isinstance(caa_p, dict) else caa_p
    caa_p3 = caa_p.get("3p", 5) if isinstance(caa_p, dict) else caa_p
    caa_goal = f"{caa_r} Relikwie + ścieżka (od Ery {caa_p4})"
    caa_note = f"*w 3p: od Ery {caa_p3}" if caa_p3 != caa_p4 else ""

    # 3. Korona & Borgiowie
    kb_v = v.get("korona_borgiowie", {})
    kb_d = kb_v.get("decrees", 2)
    kb_d4 = kb_d.get("4p", 2) if isinstance(kb_d, dict) else kb_d
    kb_e = kb_v.get("era")
    if kb_e is None:
        kb_goal = f"{kb_d4} Dekrety"
        kb_note = ""
    else:
        kb_e4 = kb_e.get("4p") if isinstance(kb_e, dict) else kb_e
        kb_e3 = kb_e.get("3p") if isinstance(kb_e, dict) else kb_e
        kb_goal = f"{kb_d4} Dekrety (od Ery {kb_e4})"
        kb_note = f"*w 3p: od Ery {kb_e3}" if kb_e3 != kb_e4 else ""

    # 4. Kabała z Toledo
    kt_v = v.get("kabala_toledo", {})
    kt_f = kt_v.get("fragments", 3)
    kt_f4 = kt_f.get("4p", 3) if isinstance(kt_f, dict) else kt_f
    kt_e = kt_v.get("era", 6)
    kt_e4 = kt_e.get("4p", 6) if isinstance(kt_e, dict) else kt_e
    kt_e3 = kt_e.get("3p", kt_e4) if isinstance(kt_e, dict) else kt_e4
    kt_hb = kt_v.get("heresy_band")
    if kt_hb:
        kt_goal = f"{kt_f4} Fragmenty + Herezja {kt_hb[0]}–{kt_hb[1]} (od Ery {kt_e4})"
    else:
        kt_goal = f"{kt_f4} Fragmenty (od Ery {kt_e4})"
    kt_note = f"*w 3p: od Ery {kt_e3}" if kt_e3 != kt_e4 else ""

    # 5. Gildia Cieni
    gc_v = v.get("gildia_cieni", {})
    gc_falls = gc_v.get("falls", {})
    gc_def = gc_falls.get("default", 4) if isinstance(gc_falls, dict) else gc_falls
    gc_no_so = gc_falls.get("no_oficjum", gc_def) if isinstance(gc_falls, dict) else gc_falls
    gc_goal = f"{gc_def} Upadki"
    gc_note = f"*{gc_no_so} gdy brak Oficjum w grze" if gc_no_so != gc_def else ""

    return [
        ("swiete-oficjum", "Święte Oficjum", so_goal, so_note, "Stosy", so_s4, "stack"),
        ("cienie-al-andalus", "Cienie Al-Andalus", caa_goal, caa_note, "Relikwie", caa_r, "relic"),
        ("korona-borgiowie", "Korona & Borgiowie", kb_goal, kb_note, "Dekrety", kb_d4, "decree"),
        ("kabala-toledo", "Kabała z Toledo", kt_goal, kt_note, "Fragmenty", kt_f4, "fragment"),
        ("gildia-cieni", "Gildia Cieni", gc_goal, gc_note, "Upadki", gc_def, "fall"),
    ]

FACTIONS = get_factions_data()

# Board graph: cycle + Lochy–Pałac chord. Phase III order = num only.
# Positions: % of board-play (center of node). Clear of top pools + top-right time deck.
LOCATIONS = [
    # num, short, full, hint, left%, top%, slug
    ("1", "Trybunał", "Trybunał Inkwizycji", "Czystość / procesy", 16, 48, "trybunal"),
    ("2", "Pałac", "Pałac Gubernatora", "Podatki / przekupstwo", 48, 16, "palac"),
    ("3", "Lochy", "Lochy & Podziemia", "Nadzór / areszt", 34, 82, "lochy"),
    ("4", "Rynek", "Rynek i Plac", "Handel / zamieszki", 84, 40, "rynek"),
    ("5", "Gildia", "Gildia / Dzielnica Garbarzy", "Informatorzy / Relikwie", 76, 70, "gildia"),
]

# Undirected edges as (slug_a, slug_b) — streets on PnP SVG
BOARD_EDGES = [
    ("trybunal", "palac"),
    ("palac", "rynek"),
    ("rynek", "gildia"),
    ("gildia", "lochy"),
    ("lochy", "trybunal"),
    ("lochy", "palac"),
]

# Robocze emotki (PnP / cut sheet) — docelowo pixel art per GDD
# (płomień Herezji, hak, marionetka, krzyż Inkwizytora, Relikwia…)
# Złoto = CSS moneta (jak na kartach), nie emoji.
ICON_SHORT = {
    "heresy": "🔥",
    "hook": "🪝",
    "double": "🎭",
    "stack": "🪵",
    "relic": "💎",
    "fragment": "📜",
    "inquisitor": "✝️",
    "decree": "🔏",
    "fall": "☠️",
    "spent": "✕",
    "patrol": "🛡",
    "autodafe_state": "🔥",
}


# PnP / 4p SSOT — żetony puli i cut sheet (playtesting/setups.md, game_config.yaml)
PNP_TOKEN_COUNTS: dict[str, int] = {
    "inquisitor": 1,
    "inquisitor_patrol": 1,
    "inquisitor_autodafe": 1,
    "heresy": 4,
    "gold": 40,
    "stack": 6,
    "relic": 6,
    "fragment": 6,
    "decree": 2,
    "fall": 8,
    "spent": 15,
    "hook": 12,
    "double": 8,
}
PNP_POOL_SLOTS = {"relic": 6, "stack": 6, "fragment": 6}


def _pool_slot_spans(n: int) -> str:
    return "".join('<span class="sq"></span>' for _ in range(n))


def _escape(s: str) -> str:
    return html.escape(s or "", quote=True)


# Słowa kluczowe efektów — tylko komendy / etykiety z game/mechanics/leksykon.md
# (Jeśli / Po / Podczas NIE są keywords; typ karty = badge, nie powtarzaj w effect)
_KEYWORD_LEAD_RE = re.compile(
    r"(?i)^(?:"
    r"limit:|"
    r"edykt(?:\s+ery)?\.?|"
    r"dekret\s+\d+|"
    r"łamie regułę|"
    r"odmowa:|"
    r"(?:przesuń|zyskaj|załóż|wskaż|aresztuj|uwolnij|przenieś|"
    r"wykonaj|ogłoś|wymuś|otwórz|umieść|ewakuuj|oznacz|zmień|ustaw)\b"
    r")"
)

# Komendy §1 — także po „Jeśli …,” / „…:” (szablony S4/S7), nie tylko na początku zdania
_COMMAND_INLINE_RE = re.compile(
    r"(?i)(?P<pre>^|,\s+|:\s+|—\s+|Autodafé\s+)"
    r"(?P<cmd>"
    r"przesuń|zyskaj|załóż|wskaż|aresztuj|uwolnij|przenieś|"
    r"wykonaj|ogłoś|wymuś|otwórz|umieść|ewakuuj|oznacz|zmień|ustaw"
    r")\b"
)

# Pojęcia mechaniczne → <em> (słownik); nie: Agent, Lokacja, złoto
_ITALIC_TERMS_RE = re.compile(
    r"(?<![A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])("
    r"Autodafé|"
    r"Przesłuchanie|"
    r"Werdykt(?:u|cie|em)?|"
    r"Hak(?:a|i|iem|owi)?|"
    r"Marionetk(?:a|ę|i|ą|ce|ek)?|"
    r"Relikwi(?:a|ę|i)|"
    r"Fragment(?:y|ów)?|"
    r"Stos(?:u|y|ów)?|"
    r"Inkwizytor(?:a|em|owi)?|"
    r"Szlak Morski|"
    r"Nasłanie|"
    r"Upadek|"
    r"Herezj(?:a|ę|i)"
    r")(?![A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])"
)


def _polish_nbsp(text: str) -> str:
    """Twarde spacje: nie dziel przyimków/zaimków (w lokacji, ze swoim, o 1 lokację)."""
    if not text:
        return text
    # Krótkie przyimki / spójniki + następne słowo
    text = re.sub(
        r"(?<![A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9])"
        r"(w|we|z|ze|na|do|od|po|za|u|o|i|a|oraz|vs|bez|dla|przy|nad|pod|przed|przez)\s+",
        lambda m: m.group(1) + "\u00a0",
        text,
        flags=re.IGNORECASE,
    )
    # Liczba + jednostka/rzeczownik (1 lokację, 2 Relikwii, ≥ 2 …)
    text = re.sub(r"(\d+)\s+", lambda m: m.group(1) + "\u00a0", text)
    # Zaimki dzierżawcze / wskazujące + rzeczownik
    text = re.sub(
        r"\b(swojego|swoją|swoje|swoim|swoich|tego|tej|tym|tych|"
        r"aresztowanego|pierwszy|najniższą)\s+",
        lambda m: m.group(1) + "\u00a0",
        text,
        flags=re.IGNORECASE,
    )
    return text


def _italicize_terms_html(text: str) -> str:
    """Escape + wrap mechanic nouns in <em>. Input = plain (unescaped) text."""
    if not text:
        return ""
    text = _polish_nbsp(text)
    out: list[str] = []
    pos = 0
    for mo in _ITALIC_TERMS_RE.finditer(text):
        out.append(_escape(text[pos : mo.start()]))
        out.append(f"<em>{_escape(mo.group(1))}</em>")
        pos = mo.end()
    out.append(_escape(text[pos:]))
    return "".join(out)


# S11: [Adresat]: [Komenda…] — komenda po dwukropku (nie lead linii)
_ADDRESS_COMMAND_RE = re.compile(
    r"(?i)^(?P<addr>.+?):\s+(?P<cmd>"
    r"przesuń|zyskaj|załóż|wskaż|aresztuj|uwolnij|przenieś|"
    r"wykonaj|ogłoś|wymuś|otwórz|umieść|ewakuuj|oznacz|zmień|ustaw"
    r")\b(?P<rest>.*)$"
)


def _format_effect_line(sent: str) -> str:
    plain = sent.strip()
    m = _KEYWORD_LEAD_RE.match(plain)
    if m:
        kw = m.group(0)
        rest = plain[len(kw) :]
        return f"<strong>{_escape(kw)}</strong>{_bold_commands_in_plain(_polish_nbsp(rest))}"

    # S11 — adresat i komenda w osobnych wierszach (jak S4), komenda pogrubiona
    m_addr = _ADDRESS_COMMAND_RE.match(plain)
    if m_addr:
        addr = plain[m_addr.start("addr") : m_addr.end("addr")]
        cmd = plain[m_addr.start("cmd") : m_addr.end("cmd")]
        rest = plain[m_addr.start("rest") : m_addr.end("rest")]
        return (
            f"{_italicize_terms_html(_polish_nbsp(addr + ':'))}<br>"
            f"<strong>{_escape(cmd)}</strong>"
            f"{_bold_commands_in_plain(_polish_nbsp(rest))}"
        )

    bolded = _bold_commands_in_plain(_polish_nbsp(plain))
    # Zachowaj inline <strong> (po „:” / „,”); nie nadpisuj samym italicize
    if "<strong>" in bolded:
        return bolded
    return _italicize_terms_html(_polish_nbsp(plain))


def _bold_commands_in_plain(text: str) -> str:
    """Pogrubia komendy §1; pozostały tekst → escape + kursywa pojęć."""
    out: list[str] = []
    pos = 0
    for mo in _COMMAND_INLINE_RE.finditer(text):
        out.append(_italicize_terms_html(text[pos : mo.start()]))
        out.append(_escape(mo.group("pre")))
        out.append(f"<strong>{_escape(mo.group('cmd'))}</strong>")
        pos = mo.end()
    out.append(_italicize_terms_html(text[pos:]))
    return "".join(out)


def _effect_auto_blocks(parts: list[str]) -> list[list[str]]:
    """Split lines into visual blocks: lead+actions | Jeśli… | Limit…"""
    if not parts:
        return []

    def is_cond(s: str) -> bool:
        return s.startswith("Jeśli") or s.startswith("Podczas")

    def is_meta(s: str) -> bool:
        return s.startswith("Limit:") or s.startswith("Odmowa:")

    blocks: list[list[str]] = []
    cur: list[str] = []
    i = 0
    while i < len(parts):
        line = parts[i]
        if (is_cond(line) or is_meta(line)) and cur:
            blocks.append(cur)
            cur = []
        cur.append(line)
        i += 1
        if is_cond(line) and i < len(parts):
            nxt = parts[i]
            if not is_cond(nxt) and not is_meta(nxt):
                cur.append(nxt)
                i += 1
    if cur:
        blocks.append(cur)
    return blocks


def _heresy_badge(heresy: int) -> str:
    """Pigułka Herezji — tylko gdy ≠ 0; ikona + liczba (bez słowa Herezja)."""
    if heresy == 0:
        return ""
    if heresy > 0:
        label = f"+{heresy}"
        cls = "badge badge-heresy badge-heresy-hot"
    else:
        label = str(heresy)
        cls = "badge badge-heresy badge-heresy-cool"
    return (
        f'<span class="{cls}" title="Herezja">'
        f'<span class="badge-ico" aria-hidden="true">🔥</span>'
        f" {_escape(label)}</span>"
    )


def _gold_badge(cost: int) -> str:
    if cost <= 0:
        return ""
    return (
        f'<span class="badge badge-gold" title="Koszt złota">'
        f'<span class="coin" aria-hidden="true"></span>'
        f" {cost}</span>"
    )


_TYPE_BADGE_CLASS = {
    "akcja": "type-akcja",
    "reakcja": "type-reakcja",
    "signature": "type-specjalna",
    "wydarzenie": "type-wydarzenie",
    "permanent": "type-akcja",
}

_OVERFLOW_WARNINGS: list[str] = []
# Po slocie art (~12 mm) długie signature wychodzą wcześniej niż przy samym tekście
_EFFECT_OVERFLOW_CHARS = 140
_EFFECT_OVERFLOW_LINES = 5


def _type_badge_class(card_type: str) -> str:
    return _TYPE_BADGE_CLASS.get((card_type or "").lower(), "type-akcja")


def _is_break_banner_line(line: str) -> bool:
    return bool(re.match(r"(?i)^(łamie\s+regułę|dekret\s+\d+\s*—\s*łamie)", line.strip()))


def _is_lead_banner_line(line: str) -> bool:
    s = line.strip()
    if _is_break_banner_line(s):
        return False
    return bool(re.match(r"(?i)^(edykt(\s+ery)?\.?|dekret\s+\d+)\b", s))


def _format_effect_group(group: list[str]) -> str:
    """Banery (Łamie / EDYKT / DEKRET) + pozostałe linie w fx-block."""
    lines = list(group)
    parts: list[str] = []
    while lines and (_is_break_banner_line(lines[0]) or _is_lead_banner_line(lines[0])):
        line = lines.pop(0)
        formatted = _format_effect_line(line)
        if _is_break_banner_line(line):
            parts.append(f'<div class="fx-break">{formatted}</div>')
        elif line.strip().upper().startswith("EDYKT"):
            parts.append(f'<div class="fx-banner fx-edykt">{formatted}</div>')
        else:
            parts.append(f'<div class="fx-banner fx-dekret">{formatted}</div>')
    if lines:
        inner = "<br>".join(_format_effect_line(ln) for ln in lines)
        parts.append(f'<div class="fx-block">{inner}</div>')
    return "".join(parts)


def _format_effect_html(effect: str) -> str:
    """Pogrubia słowa kluczowe; bloki logiczne + banery Łamie/EDYKT/DEKRET."""
    raw = effect.strip()
    if not raw:
        return ""

    if re.search(r"\n\s*\n", raw):
        chunks = [c.strip() for c in re.split(r"\n\s*\n", raw) if c.strip()]
        line_groups: list[list[str]] = [
            [ln.strip() for ln in c.splitlines() if ln.strip()] for c in chunks
        ]
    else:
        parts = (
            [p.strip() for p in raw.splitlines() if p.strip()]
            if "\n" in raw
            else [p.strip() for p in re.split(r"(?<=[.!?])\s+", raw) if p.strip()]
        )
        line_groups = _effect_auto_blocks(parts)

    if not line_groups:
        return ""

    blocks_html = [_format_effect_group(group) for group in line_groups]
    joined = "".join(blocks_html)
    # Single plain fx-block without banners — unwrap outer for short cards
    if (
        len(blocks_html) == 1
        and joined.startswith('<div class="fx-block">')
        and joined.endswith("</div>")
        and joined.count('<div class="fx-') == 1
    ):
        return joined[len('<div class="fx-block">') : -len("</div>")]
    return joined


def _note_effect_overflow(
    card_id: str,
    effect: str,
    *,
    lore: str = "",
    heresy_caption: str = "",
) -> None:
    n_lines = len([ln for ln in effect.splitlines() if ln.strip()]) or (
        1 if effect.strip() else 0
    )
    has_break = bool(re.search(r"(?i)^łamie\s+regułę|dekret\s+\d+\s*—", effect, re.M))
    pressure = len(effect) + len(lore) // 2 + len(heresy_caption) // 2
    if has_break:
        pressure += 40
    if (
        len(effect) > _EFFECT_OVERFLOW_CHARS
        or n_lines > _EFFECT_OVERFLOW_LINES
        or pressure > 220
    ):
        _OVERFLOW_WARNINGS.append(
            f"{card_id}: {len(effect)} chars, {n_lines} lines"
            f"{', Łamie/DEKRET' if has_break else ''}"
            f"{', lore' if lore else ''}{', HT' if heresy_caption else ''}"
            f" (pressure {pressure})"
        )


def _icon(key: str, alt: str = "") -> str:
    label = alt or key
    if key == "gold":
        return (
            f'<span class="coin" title="{_escape(label)}" aria-hidden="true"></span>'
        )
    short = ICON_SHORT.get(key, (label[:1] or "?").upper())
    return f'<span class="ico-fallback" title="{_escape(label)}">{_escape(short)}</span>'


# ---------------------------------------------------------------------------
# CSS — print dimensions
# ---------------------------------------------------------------------------

def _css() -> str:
    return """
:root {
  --ink: #1a120c;
  --parch: #f4ead7;
  --blood: #7a1f1f;
  --gold: #a67c2d;
  --line: #2a1c12;
  --ui: rgba(244, 234, 215, 0.92);
  --slot: #1a120c;
  /* locked print sizes */
  --card-w: 63mm;
  --card-h: 88mm;
  --card-trim-w: 63mm;
  --card-trim-h: 88mm;
  --card-bleed: 2.5mm;
  --card-gross-w: 68mm;
  --card-gross-h: 93mm;
  --card-safe-pad: 3mm;
  --board-w: 420mm;
  --board-h: 594mm;
  --page-a4-w: 210mm;
  --page-a4-h: 297mm;
  --player-w: 210mm; /* ½ A4 / A5 */
  --player-h: 148mm;
  --heresy-pip: 18mm;
  --agent-d: 20mm;
  --token-d: 20mm;
  --token-r: 2mm; /* lekko zaokrąglony kwadrat */
  --card-slot-w: 63mm;
  --card-slot-h: 88mm;
  --board-margin: 8mm;
}
* { box-sizing: border-box; }
body {
  font-family: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
  color: var(--ink); background: #ddd3c0; margin: 0; padding: 8mm;
}
h1 { color: var(--blood); font-size: 16pt; margin: 0 0 3mm; }
h2 { font-size: 13pt; margin: 3mm 0 2mm; border-bottom: 0.4mm solid var(--line); }
.meta { font-size: 9pt; color: #444; margin-bottom: 3mm; }
.nav a { margin-right: 4mm; }
.sheet { page-break-after: always; margin-bottom: 8mm; }
/* A4 page frame — same lock idea as board A2 */
.page-a4 {
  position: relative;
  width: var(--page-a4-w);
  height: var(--page-a4-h);
  min-width: var(--page-a4-w);
  max-width: var(--page-a4-w);
  min-height: var(--page-a4-h);
  max-height: var(--page-a4-h);
  background: var(--parch);
  border: 0.5mm solid var(--line);
  padding: 8mm;
  overflow: hidden;
  flex-shrink: 0;
  box-sizing: border-box;
  margin-bottom: 8mm;
}
.page-a4 > h1:first-child { margin-top: 0; }
/* Teach może zajmować >1 A4 wysokości — szerokość i min-wysokość zostają zablokowane */
.page-a4.teach-page {
  height: auto;
  max-height: none;
  min-height: var(--page-a4-h);
  overflow: visible;
}
.ico { width: 5mm; height: 5mm; object-fit: cover; vertical-align: middle; border-radius: 1mm; }
.ico-fallback {
  display: inline-flex; align-items: center; justify-content: center;
  width: auto; height: auto; min-width: 5mm; min-height: 5mm;
  font-size: 11pt; line-height: 1; font-weight: normal;
  border: none; background: transparent;
}
/* Board chrome icons — set with .board-chrome .ico below in BOARD section */

/* ===== BOARD: A2 portrait — token row + 3 cards side-by-side per node ===== */
.board-stack {
  position: relative;
  width: 420mm;
  height: 594mm;
  min-width: 420mm;
  min-height: 594mm;
  max-width: 420mm;
  max-height: 594mm;
  border: 0.6mm solid var(--line);
  overflow: hidden;
  background: var(--parch);
  flex-shrink: 0;
}
.board-a4-grid {
  position: absolute; inset: 0;
  pointer-events: none;
  z-index: 1;
}
/* Exact A2 midlines = A4 tile seams (210×297 mm portrait tiles) */
.a4-cut {
  position: absolute;
  pointer-events: none;
  margin: 0;
  padding: 0;
}
.a4-cut-v {
  left: 210mm; /* half of 420 */
  top: 0;
  bottom: 0;
  width: 0;
  border-left: 0.4mm dashed rgba(42, 28, 18, 0.45);
}
.a4-cut-h {
  top: 297mm; /* half of 594 */
  left: 0;
  right: 0;
  height: 0;
  border-top: 0.4mm dashed rgba(42, 28, 18, 0.45);
}
.board-ui {
  position: relative; z-index: 2;
  width: 100%; height: 100%;
  padding: 0;
  box-sizing: border-box;
}
.board-chrome {
  position: absolute;
  top: var(--board-margin); left: var(--board-margin); right: var(--board-margin);
  z-index: 3;
  display: block;
  background: transparent;
  border: none;
  padding: 0;
  font-size: initial;
  pointer-events: none;
}
.board-chrome .pool-box,
.board-chrome .time-deck {
  pointer-events: auto;
}
.pool-row {
  display: flex;
  flex-wrap: nowrap;
  align-items: stretch;
  gap: 3mm;
  /* leave room for time-deck on the right (2×63mm + gaps ≈ 140mm) */
  margin-right: 145mm;
}
.pool-box {
  flex: 0 0 auto;
  display: flex; flex-direction: column; align-items: center; gap: 2mm;
  background: rgba(244, 234, 215, 0.98);
  border: 0.45mm solid var(--line);
  padding: 2.5mm 3mm 3mm;
  width: max-content;
  max-width: none;
}
.pool-box .pool-title {
  font-size: 16pt; font-weight: bold; color: var(--blood);
  margin: 0; border: none; padding: 0;
  text-align: center; line-height: 1.15;
  width: 100%;
  border-bottom: 0.35mm solid var(--gold);
  padding-bottom: 1.5mm;
  white-space: nowrap;
}
.pool-box .pool-body {
  display: flex; flex-wrap: nowrap; align-items: center; justify-content: center;
  gap: 2mm;
}
.pool-slots { display: inline-flex; flex-wrap: nowrap; gap: 2mm; vertical-align: middle; }
.sq {
  width: var(--token-d); height: var(--token-d);
  border: 0.45mm solid var(--slot);
  background: #fff; display: inline-block;
  border-radius: var(--token-r);
  box-sizing: border-box;
}
/* Kronika Dziejów = karty — osobny blok top-right, nie rozciąga pul żetonów */
.time-deck {
  position: absolute;
  top: 0;
  right: 0;
  display: flex; flex-direction: column; align-items: center; gap: 2mm;
  background: rgba(244, 234, 215, 0.98);
  border: 0.45mm solid var(--line);
  padding: 2.5mm 3mm 3mm;
}
.time-deck .pool-title {
  font-size: 16pt; font-weight: bold; color: var(--blood);
  margin: 0; border: none; padding: 0;
  text-align: center; line-height: 1.15;
  width: 100%;
  border-bottom: 0.35mm solid var(--gold);
  padding-bottom: 1.5mm;
}
.time-deck .pool-body {
  display: flex; flex-wrap: nowrap;
  gap: 3mm;
  align-items: flex-end;
  justify-content: center;
}
.time-card {
  display: flex; flex-direction: column; align-items: center; gap: 1.5mm;
}
.time-card .card-slot {
  width: var(--card-slot-w);
  height: var(--card-slot-h);
}
.time-card .lbl {
  font-size: 12pt; font-weight: bold; color: var(--ink); line-height: 1.1;
}
.board-chrome .ico {
  width: 16mm; height: 16mm; border-radius: 2mm;
}
.board-chrome .ico-fallback {
  min-width: 16mm; min-height: 16mm; font-size: 18pt;
}
.board-play {
  position: absolute;
  left: var(--board-margin); right: var(--board-margin);
  /* clear short token pools; time-deck sits top-right outside node cluster */
  top: 48mm;
  bottom: var(--board-margin);
  z-index: 2;
}
.board-streets {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 0;
}
.board-streets line {
  stroke: rgba(122, 31, 31, 0.72);
  stroke-width: 0.55;
  stroke-linecap: round;
}
.loc-node {
  position: absolute;
  /* 1× karta 63mm (stos ≤3) + pad; żetony zawijają się w wierszu */
  width: 116mm;
  height: auto;
  transform: translate(-50%, -50%);
  background: rgba(244, 234, 215, 0.98);
  border: 0.55mm solid var(--line);
  display: flex; flex-direction: column; align-items: center;
  padding: 2.5mm;
  gap: 2mm;
  box-sizing: border-box;
  z-index: 1;
}
.loc-head {
  font-size: 18pt; font-weight: bold; color: var(--blood);
  letter-spacing: 0.02em;
  text-align: center;
  margin: 0; border: none; padding: 0 0 1.5mm;
  border-bottom: 0.45mm solid var(--gold);
  width: 100%;
  flex-shrink: 0;
  line-height: 1.15;
}
/* One row: all tokens for this location (wrap for Lochy arrests) */
.token-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 2mm;
  width: 100%;
  flex-shrink: 0;
}
.agent {
  width: var(--agent-d); height: var(--agent-d); border-radius: 50%;
  border: 0.5mm solid var(--slot); background: #fff;
  box-sizing: border-box; flex: 0 0 auto;
}
.relic-slot {
  width: var(--token-d); height: var(--token-d);
  border-radius: var(--token-r);
  border: 0.5mm solid var(--gold); background: #fff8e8;
  display: block; flex: 0 0 auto;
  box-sizing: border-box;
}
.arrest {
  width: var(--agent-d); height: var(--agent-d);
  border: 0.5mm solid var(--blood);
  background: #f5e4e4; border-radius: 50%;
  box-sizing: border-box; flex: 0 0 auto;
}
.inquisitor-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1mm;
  flex: 0 0 auto;
}
.inquisitor-fig {
  width: calc(var(--agent-d) * 1.12);
  height: calc(var(--agent-d) * 1.12);
  border-radius: 50%;
  border: 0.55mm solid var(--blood);
  background: #fff5f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13pt;
  box-sizing: border-box;
}
.inquisitor-states {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1mm;
  max-width: 22mm;
}
.inq-state {
  font-size: 6.5pt;
  font-weight: bold;
  letter-spacing: 0.02em;
  padding: 0.4mm 1mm;
  border: 0.35mm solid var(--line);
  border-radius: 1mm;
  background: #fff;
  color: var(--ink);
  line-height: 1.1;
}
.inq-state.is-active {
  background: var(--blood);
  color: #fff;
  border-color: var(--blood);
}
/* Jeden slot 63×88 = stos do 3 kart */
.card-row {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
  gap: 1.5mm;
  width: 100%;
  flex-shrink: 0;
}
.card-slot {
  width: var(--card-slot-w);
  height: var(--card-slot-h);
  border: 0.5mm dashed var(--line);
  background: rgba(255,255,255,0.97);
  box-sizing: border-box;
  flex: 0 0 var(--card-slot-h);
}

/* ===== CARDS: 63×88 mm — HDR / art / effect / lore ===== */
.cards {
  display: grid;
  grid-template-columns: repeat(3, var(--card-w));
  gap: 3mm;
  justify-content: start;
}
.card-proto {
  position: relative;
  width: var(--card-w); height: var(--card-h);
  min-width: var(--card-w); max-width: var(--card-w);
  min-height: var(--card-h); max-height: var(--card-h);
  border: 1.5mm solid var(--faction-edge, var(--blood));
  background: var(--parch);
  display: flex; flex-direction: column;
  overflow: visible;
  flex-shrink: 0;
  box-sizing: border-box;
}
/* Renaissance inner hairline frame on all 4 sides */
.card-proto::before {
  content: "";
  position: absolute;
  inset: 0.6mm;
  border: 0.25mm solid rgba(166, 124, 45, 0.5);
  pointer-events: none;
  z-index: 2;
}
.card-proto .hdr {
  padding: 1.6mm 2mm 1.2mm 2mm;
  border-bottom: 0.35mm solid var(--line);
  background: rgba(255,255,255,0.32);
  flex-shrink: 0;
  position: relative;
  z-index: 3;
}
.card-proto .hdr-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1.5mm;
}
.card-proto .name {
  font-size: 12pt;
  font-weight: bold;
  color: var(--blood);
  line-height: 1.15;
  flex: 1 1 auto;
  min-width: 0;
}
.card-footer-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 0.6mm;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-size: 5pt;
  color: #7a6e60;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  user-select: none;
  opacity: 0.75;
  line-height: 1;
}
.card-proto .name.name-long {
  font-size: 10.5pt;
}
.card-proto .type-badge {
  flex: 0 0 auto;
  font-size: 6.5pt;
  font-weight: bold;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  border-radius: 1mm;
  padding: 0.4mm 1.1mm;
  white-space: nowrap;
  line-height: 1.2;
  border: 0.25mm solid rgba(42,28,18,0.45);
  color: #3a3028;
  background: rgba(255,255,255,0.55);
}
.card-proto .type-badge.type-akcja {
  color: #2a1c12;
  background: rgba(255,255,255,0.7);
  border-color: rgba(42,28,18,0.55);
}
.card-proto .type-badge.type-reakcja {
  color: #1a3348;
  background: #d8e4ee;
  border-color: #3a5a72;
}
.card-proto .type-badge.type-specjalna {
  color: #5c4010;
  background: #f0dfa8;
  border-color: #a67c2d;
}
.card-proto .type-badge.type-wydarzenie {
  color: #f4ead7;
  background: #3a2e1c;
  border-color: #1e1810;
}
.card-proto .stat-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1mm;
  margin-top: 1.2mm;
}
.card-proto .stat-row:empty { display: none; }
.card-proto .badge {
  display: inline-flex;
  align-items: center;
  gap: 0.6mm;
  font-size: 7.5pt;
  font-weight: bold;
  line-height: 1.2;
  padding: 0.55mm 1.4mm;
  border-radius: 1.2mm;
  border: 0.25mm solid rgba(42,28,18,0.4);
  background: rgba(255,255,255,0.65);
  white-space: nowrap;
}
.card-proto .badge-ico { font-size: 8pt; line-height: 1; }
/* Moneta (CSS) — nie emoji „kamienia” */
.coin {
  display: inline-block;
  width: 3.4mm;
  height: 3.4mm;
  flex: 0 0 3.4mm;
  border-radius: 50%;
  box-sizing: border-box;
  vertical-align: middle;
  background:
    radial-gradient(circle at 32% 28%, #fff6c8 0%, #e8c84a 38%, #c9a227 72%, #8a6a14 100%);
  border: 0.35mm solid #6a5210;
  box-shadow: inset 0 0 0 0.35mm rgba(255, 236, 160, 0.55);
}
.card-proto .badge-gold {
  color: #5c4010;
  background: #f0dfa8;
  border-color: #a67c2d;
}
.card-proto .badge-heresy {
  color: #3a3028;
  background: rgba(255,255,255,0.7);
}
.card-proto .badge-heresy-hot {
  color: #fff8f4;
  background: #6e1818;
  border-color: #3a0c0c;
}
.card-proto .badge-heresy-cool {
  color: #1e3a2e;
  background: #cfe0d6;
  border-color: #2d5a45;
}
.card-proto .heresy-caption {
  margin-top: 0.8mm;
  font-size: 7.5pt;
  line-height: 1.25;
  color: #6e1818;
  font-weight: 600;
}
.card-art {
  flex: 0 0 12mm;
  height: 12mm;
  margin: 0;
  border-bottom: 0.35mm solid var(--line);
  border-top: none;
  background:
    repeating-linear-gradient(
      -45deg,
      transparent,
      transparent 2mm,
      rgba(42,28,18,0.04) 2mm,
      rgba(42,28,18,0.04) 4mm
    );
  box-shadow: inset 0 0 0 0.25mm dashed rgba(42,28,18,0.35);
  outline: 0.25mm dashed rgba(42,28,18,0.28);
  outline-offset: -1.2mm;
  box-sizing: border-box;
}
.card-main {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
  padding: 2mm 2.5mm 2.2mm 3.2mm;
  box-sizing: border-box;
}
.card-effect {
  flex: 1 1 auto;
  display: block;
  font-size: 11pt;
  line-height: 1.35;
  margin: 0;
  padding: 0;
  overflow: visible;
}
.card-effect strong { font-weight: bold; }
.card-effect em { font-style: italic; font-weight: inherit; }
.card-effect .fx-block + .fx-block {
  margin-top: 1.5mm;
  padding-top: 1.4mm;
  border-top: 0.3mm solid rgba(42, 28, 18, 0.28);
}
.card-effect .fx-break {
  margin: 0 0 1.2mm;
  padding: 1mm 1.4mm;
  background: rgba(122, 31, 31, 0.12);
  border: 0.3mm solid rgba(122, 31, 31, 0.45);
  border-radius: 1mm;
  font-size: 10pt;
  line-height: 1.3;
}
.card-effect .fx-banner {
  margin: 0 0 1.2mm;
  padding: 0.7mm 0 0.9mm;
  font-size: 9pt;
  font-weight: bold;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border-bottom: 0.35mm solid rgba(42, 28, 18, 0.4);
  line-height: 1.25;
}
.card-effect .fx-banner.fx-edykt {
  color: #3a2e1c;
  border-bottom-color: #3a2e1c;
}
.card-effect .fx-banner.fx-dekret {
  color: #8a6420;
  border-bottom-color: #a67c2d;
}
.card-effect .fx-break + .fx-block,
.card-effect .fx-banner + .fx-block {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
.card-lore {
  flex: 0 0 auto;
  margin-top: auto;
  padding-top: 1.8mm;
  border-top: 0.3mm solid rgba(42, 28, 18, 0.28);
  font-size: 9pt;
  font-style: italic;
  line-height: 1.35;
  color: #3a3028;
  opacity: 0.72;
}
/* Card tints + faction edge */
.card-proto.faction-swiete-oficjum { background: #f1ddd6; --faction-edge: #7a1f1f; }
.card-proto.faction-swiete-oficjum .name { color: #7a1f1f; }
.card-proto.faction-cienie-al-andalus { background: #dde8e2; --faction-edge: #1e4d3a; }
.card-proto.faction-cienie-al-andalus .name { color: #1e4d3a; }
.card-proto.faction-korona-borgiowie { background: #f2e6c8; --faction-edge: #8a6420; }
.card-proto.faction-korona-borgiowie .name { color: #8a6420; }
.card-proto.faction-kabala-toledo { background: #e6dde8; --faction-edge: #4a2d5c; }
.card-proto.faction-kabala-toledo .name { color: #4a2d5c; }
.card-proto.faction-gildia-cieni { background: #e5dfd2; --faction-edge: #4a3c28; }
.card-proto.faction-gildia-cieni .name { color: #4a3c28; }
.card-proto.faction-time { background: #e8e2d4; --faction-edge: #3a2e1c; }
.card-proto.faction-time .name { color: #3a2e1c; }
body.bw .card-proto {
  filter: grayscale(1);
  border-width: 0.7mm;
  border-color: #111;
}

/* ===== PLAYER BOARD: ½ A4 — fixed mm budget (see game/board/player-board.md) =====
   Outer 210×148 · pad 3 → 204×142
   Rows: header auto (treść) + heresy 28 + body 1fr (+ gaps 1.5×2)
*/
.player-stack {
  position: relative;
  width: var(--player-w);
  height: var(--player-h);
  min-width: var(--player-w); max-width: var(--player-w);
  min-height: var(--player-h); max-height: var(--player-h);
  border: 0.55mm solid var(--line);
  margin: 0 0 1mm;
  overflow: hidden;
  background: var(--parch);
  flex-shrink: 0;
  box-sizing: border-box;
  page-break-inside: avoid;
}
.player-stack.faction-swiete-oficjum { background: #f1ddd6; }
.player-stack.faction-swiete-oficjum .pb-head h2 { color: #7a1f1f; border-bottom-color: #7a1f1f; }
.player-stack.faction-cienie-al-andalus { background: #dde8e2; }
.player-stack.faction-cienie-al-andalus .pb-head h2 { color: #1e4d3a; border-bottom-color: #2f6b52; }
.player-stack.faction-korona-borgiowie { background: #f2e6c8; }
.player-stack.faction-korona-borgiowie .pb-head h2 { color: #8a6420; border-bottom-color: #a67c2d; }
.player-stack.faction-kabala-toledo { background: #e6dde8; }
.player-stack.faction-kabala-toledo .pb-head h2 { color: #4a2d5c; border-bottom-color: #6b4580; }
.player-stack.faction-gildia-cieni { background: #e5dfd2; }
.player-stack.faction-gildia-cieni .pb-head h2 { color: #4a3c28; border-bottom-color: #6b5a3e; }

.player-ui {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 3mm;
  display: grid;
  /* auto = zero dziury pod celem; wolne mm idą w korpus */
  grid-template-rows: auto 28mm minmax(0, 1fr);
  gap: 1.5mm;
  overflow: hidden;
  align-content: stretch;
}
.pb-head {
  grid-row: 1;
  overflow: hidden;
  min-height: 0;
  height: fit-content;
  display: flex;
  flex-direction: column;
  gap: 0.6mm;
}
.pb-head h2 {
  margin: 0;
  padding: 0 0 0.4mm;
  border: none;
  border-bottom: 0.35mm solid var(--gold);
  font-size: 18pt;
  line-height: 1.1;
  color: var(--blood);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 0 0 auto;
}
.pb-goal {
  margin: 0;
  font-size: 15pt;
  line-height: 1.15;
  font-weight: 600;
  color: #222;
  flex: 0 0 auto;
  overflow: hidden;
}
.pb-goal-note {
  font-size: 11pt;
  font-weight: normal;
  color: #4a3c28;
  margin-left: 2mm;
  display: inline-block;
}
.pb-heresy {
  grid-row: 2;
  overflow: hidden;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.8mm;
}
.pb-section-title {
  flex: 0 0 auto;
  font-size: 13pt;
  font-weight: bold;
  color: var(--blood);
  margin: 0;
  line-height: 1;
}
.pb-heresy-note {
  font-size: 9pt;
  font-weight: normal;
  color: #555;
  margin-left: 2mm;
  display: inline-block;
}
.heresy-track {
  display: flex;
  gap: 0.35mm;
  width: 100%;
  height: var(--heresy-pip);
  flex: 0 0 var(--heresy-pip);
}
.heresy-pip {
  flex: 1 1 0;
  min-width: 0;
  height: 100%;
  border: 0.35mm solid var(--line);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13pt;
  font-weight: bold;
  background: #fff;
  box-sizing: border-box;
}
.heresy-pip.z1 { background: #dcebc8; }
.heresy-pip.z2 { background: #f0d9a8; }
.heresy-pip.z2-3 { background: linear-gradient(135deg, #f0d9a8 50%, #e8b8b8 50%); }
.heresy-pip.z3 { background: #e8b8b8; }
.heresy-zones {
  display: grid;
  grid-template-columns: 4fr 3fr 4fr;
  margin: 0; /* tuż pod torem — nigdy margin-top: auto */
  flex: 0 0 auto;
  font-size: 11pt;
  font-weight: bold;
  text-align: center;
  line-height: 1.05;
}
.heresy-zones .hz-z1 { color: #3d5a20; }
.heresy-zones .hz-z2 { color: #7a5a18; }
.heresy-zones .hz-z3 { color: #7a1f1f; }

.pb-body {
  grid-row: 3;
  min-height: 0;
  height: 100%;
  display: grid;
  gap: 2mm;
  overflow: hidden;
}
.pb-body.layer-a {
  grid-template-columns: 70mm minmax(0, 1fr) 36mm auto;
  grid-template-rows: minmax(0, 1fr);
  grid-template-areas: "agents gold limits progress";
}
/* C: dwa niezależne rzędy — Haki ≠ Postęp (różne szerokości) */
.pb-body.layer-c {
  grid-template-columns: 1fr;
  grid-template-rows: minmax(0, 1.07fr) minmax(0, 1fr); /* ~45:42 */
}
.pb-row {
  display: grid;
  gap: 2mm;
  min-height: 0;
  min-width: 0;
}
.pb-row-top {
  grid-template-columns: 70mm minmax(0, 1fr) 48mm; /* Haki: 2×20 + pad */
}
.pb-row-bot {
  grid-template-columns: minmax(0, 1fr) auto; /* Postęp: auto width pod liczbę żetonów */
}
.pb-box {
  box-sizing: border-box;
  min-width: 0;
  min-height: 0;
  overflow: hidden;
  border: 0.4mm solid var(--line);
  background: rgba(255,255,255,0.55);
  padding: 1.5mm;
  display: grid;
  grid-template-rows: 7mm minmax(0, 1fr);
  gap: 1mm;
}
.pb-body.layer-a .pb-box.agents { grid-area: agents; }
.pb-body.layer-a .pb-box.gold { grid-area: gold; }
.pb-body.layer-a .pb-box.limits { grid-area: limits; }
.pb-body.layer-a .pb-box.progress { grid-area: progress; }
.pb-box-title {
  margin: 0;
  padding: 0 0 0.5mm;
  border-bottom: 0.25mm solid var(--gold);
  font-size: 13pt;
  font-weight: bold;
  color: var(--blood);
  line-height: 1.1;
  text-align: center;
  overflow: hidden;
  white-space: nowrap;
}
.pb-slots {
  display: flex;
  flex-wrap: nowrap;
  gap: 2mm;
  align-items: center;
  justify-content: center;
  min-height: 0;
  overflow: hidden;
}
.pb-tray {
  width: 100%;
  height: 100%;
  min-height: 0;
  border: 0.35mm dashed var(--gold);
  border-radius: var(--token-r);
  background: rgba(255, 248, 232, 0.65);
  box-sizing: border-box;
}
.agent-slot {
  width: var(--agent-d); height: var(--agent-d);
  flex: 0 0 var(--agent-d);
  border-radius: 50%;
  border: 0.5mm solid var(--slot);
  background: #fff;
  box-sizing: border-box;
}
.pb-token {
  width: var(--token-d); height: var(--token-d);
  flex: 0 0 var(--token-d);
  border: 0.5mm solid var(--slot);
  background: #fff;
  border-radius: var(--token-r);
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
}
.pb-token.hook-slot { border-color: var(--line); }
.pb-token.progress-slot {
  border-style: dashed;
  border-color: var(--gold);
  background: rgba(255,255,255,0.75);
}
.pb-token .ico-fallback {
  font-size: 16pt;
  line-height: 1;
  min-width: 0;
  min-height: 0;
  opacity: 0.32; /* ghost w odcisku — odróżnić od prawdziwego żetonu */
}
/* Limity C: tytuł u góry, 3 kolumny (✕ nad etykietą) — mieści się w ~130×41 mm */
.pb-body.layer-c .pb-box.limits {
  grid-template-columns: 1fr;
  grid-template-rows: 7mm minmax(0, 1fr);
  align-items: stretch;
  gap: 1mm;
  padding: 1.5mm;
  overflow: hidden;
}
.pb-body.layer-c .pb-box.limits .pb-box-title {
  border-bottom: 0.25mm solid var(--gold);
  padding: 0 0 0.5mm;
  text-align: center;
  white-space: nowrap;
  font-size: 13pt;
}
.pb-body.layer-c .pb-box.limits .pb-slots {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 2mm;
  align-items: center;
  justify-items: stretch;
  width: 100%;
  min-height: 0;
}
.pb-limit {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1mm;
  min-width: 0;
  width: 100%;
}
.pb-limit .pb-token {
  width: 12mm; height: 12mm;
  flex: 0 0 12mm;
  border-style: dashed;
}
.pb-limit .pb-token .ico-fallback { font-size: 11pt; }
.pb-limit-lbl {
  font-size: 12pt;
  font-weight: bold;
  color: var(--ink);
  line-height: 1.1;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}
.pb-body.layer-a .pb-box.limits {
  grid-template-rows: 7mm minmax(0, 1fr);
}
.pb-body.layer-a .pb-box.limits .pb-slots {
  display: flex;
  flex-direction: column;
  gap: 2mm;
}
.pb-body.layer-a .pb-limit-lbl { font-size: 11pt; }

.page-a4.player-page {
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 0;
  border: none;
}
.page-a4.player-page .player-stack {
  margin: 0;
  border-radius: 0;
}
.page-a4.player-page .player-stack + .player-stack {
  border-top: none;
}

/* tokens — 20×20 mm rounded squares packed onto one A4 */
.page-a4.token-page {
  padding: 6mm;
  display: flex;
  flex-direction: column;
  gap: 2.5mm;
}
.page-a4.token-page > h1 {
  margin: 0 0 1mm;
  font-size: 13pt;
  flex-shrink: 0;
}
.token-cut {
  display: flex;
  flex-direction: column;
  gap: 2mm;
  flex: 1 1 auto;
  min-height: 0;
}
.token-group {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 2mm;
  margin: 0;
  flex-shrink: 0;
}
.token-group h3 {
  flex: 0 0 28mm;
  width: 28mm;
  font-size: 8.5pt;
  margin: 0;
  padding-top: 3mm;
  color: var(--blood);
  line-height: 1.15;
  font-weight: bold;
}
.token-sheet {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5mm;
  flex: 1 1 auto;
  min-width: 0;
  justify-content: start;
}
.token-disc {
  width: var(--token-d); height: var(--token-d);
  min-width: var(--token-d); min-height: var(--token-d);
  border-radius: var(--token-r);
  border: 0.55mm solid var(--line);
  background: var(--parch);
  display: flex; align-items: center; justify-content: center;
  overflow: hidden;
  box-shadow: inset 0 0 0 0.35mm var(--gold);
  flex-shrink: 0;
}
.token-disc img {
  width: 14mm; height: 14mm; object-fit: cover; border-radius: 1mm;
}
.token-disc .ico-fallback {
  min-width: 0; min-height: 0;
  font-size: 22pt; line-height: 1;
}
.token-disc .coin {
  width: 12mm; height: 12mm; flex: 0 0 12mm;
  border-width: 0.55mm;
  box-shadow: inset 0 0 0 0.55mm rgba(255, 236, 160, 0.55);
}
.verdict { font-size: 11pt; }
.verdict ol { margin: 2mm 0 3mm 6mm; font-size: 11pt; line-height: 1.35; }
.verdict table {
  width: 100%;
  border-collapse: collapse;
  font-size: 10pt;
}
.verdict th, .verdict td {
  border: 0.35mm solid var(--line);
  padding: 3mm;
  height: 12mm;
}
.teach-page { font-size: 10pt; line-height: 1.35; }
.teach-page ul, .teach-page ol { margin: 2mm 0 2mm 5mm; }
.teach-page p { margin: 1.5mm 0; }
/* ===== CARDS MASTER PRINT SHEET (FULL BLEED & CROP MARKS) ===== */
.page-a4.cards-master-sheet {
  position: relative;
  width: 210mm;
  height: 297mm;
  min-width: 210mm; max-width: 210mm;
  min-height: 297mm; max-height: 297mm;
  padding: 0;
  margin: 0 auto 8mm auto;
  box-sizing: border-box;
  background: #ffffff;
  border: none;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.sheet-meta-header {
  font-size: 7pt;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin: 0 0 2mm 0;
  display: flex;
  justify-content: space-between;
  width: 204mm;
  flex-shrink: 0;
}
.cards-print-grid {
  display: grid;
  grid-template-columns: repeat(3, var(--card-gross-w));
  grid-template-rows: repeat(3, var(--card-gross-h));
  gap: 0;
  width: 204mm;
  height: 279mm;
  margin: 0 auto;
  box-sizing: border-box;
}

/* Card with full bleed: 68x93mm (Netto 63x88mm + 2.5mm Bleed all around) */
.card-proto.card-print-cell {
  position: relative;
  width: var(--card-gross-w);
  height: var(--card-gross-h);
  min-width: var(--card-gross-w); max-width: var(--card-gross-w);
  min-height: var(--card-gross-h); max-height: var(--card-gross-h);
  box-sizing: border-box;
  overflow: hidden;
  border: none;
  background: var(--faction-edge, var(--blood)); /* Full bleed of faction color to gross edge */
  display: flex;
  flex-direction: column;
  padding: calc(var(--card-bleed) + 1.5mm); /* 2.5mm bleed + 1.5mm border = 4.0mm inset */
  box-shadow: none;
}
.card-proto.card-print-cell::before {
  display: none !important; /* No side stripe */
}

/* Inner parchment canvas inside the faction frame */
.card-proto.card-print-cell .card-inner-flow,
.card-proto.card-print-cell .card-back-content {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  background: var(--parch, #f4ead7);
  position: relative;
  z-index: 3;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 0.25mm solid rgba(166, 124, 45, 0.55); /* Subtle inner gold hairline */
}

/* Header */
.card-proto.card-print-cell .hdr {
  position: relative;
  z-index: 5;
  width: 100%;
  box-sizing: border-box;
  padding: 1.6mm 2.2mm 1.2mm 2.2mm;
  background: rgba(255, 255, 255, 0.35);
  border-bottom: 0.35mm solid var(--line);
}

.card-proto.card-print-cell .card-art {
  margin: 1.5mm 2mm 1mm 2mm;
  position: relative;
  z-index: 5;
}

.card-proto.card-print-cell .card-main {
  padding: 1mm 2.2mm 1.8mm 2.2mm;
  position: relative;
  z-index: 5;
}

/* Corner Crop Marks (marking the 63x88mm trim line through the faction bleed) */
.crop-mark {
  position: absolute;
  pointer-events: none;
  z-index: 35;
  background: #ffffff; /* White hairlines clearly visible on faction color */
  box-shadow: 0 0 0.5px rgba(0, 0, 0, 0.8);
}
.crop-tl-h { top: var(--card-bleed); left: 0; width: var(--card-bleed); height: 0.25mm; }
.crop-tl-v { top: 0; left: var(--card-bleed); width: 0.25mm; height: var(--card-bleed); }

.crop-tr-h { top: var(--card-bleed); right: 0; width: var(--card-bleed); height: 0.25mm; }
.crop-tr-v { top: 0; right: var(--card-bleed); width: 0.25mm; height: var(--card-bleed); }

.crop-bl-h { bottom: var(--card-bleed); left: 0; width: var(--card-bleed); height: 0.25mm; }
.crop-bl-v { bottom: 0; left: var(--card-bleed); width: 0.25mm; height: var(--card-bleed); }

.crop-br-h { bottom: var(--card-bleed); right: 0; width: var(--card-bleed); height: 0.25mm; }
.crop-br-v { bottom: 0; right: var(--card-bleed); width: 0.25mm; height: var(--card-bleed); }

/* Safe Zone Guide (DTP inspection mode: 3mm inside trim line) */
.safe-zone-guide {
  display: none;
  position: absolute;
  top: calc(var(--card-bleed) + var(--card-safe-pad));
  left: calc(var(--card-bleed) + var(--card-safe-pad));
  width: calc(var(--card-trim-w) - 2 * var(--card-safe-pad));
  height: calc(var(--card-trim-h) - 2 * var(--card-safe-pad));
  border: 0.3mm dashed rgba(0, 120, 255, 0.9);
  pointer-events: none;
  z-index: 40;
  box-sizing: border-box;
}
body.mode-safe .safe-zone-guide {
  display: block;
}

/* Mode trim: preview without bleed (Netto 63x88mm with 1.5mm faction border) */
body.mode-trim .card-proto.card-print-cell {
  width: var(--card-trim-w);
  height: var(--card-trim-h);
  min-width: var(--card-trim-w); max-width: var(--card-trim-w);
  min-height: var(--card-trim-h); max-height: var(--card-trim-h);
  padding: 1.5mm;
  margin: 1.5mm;
}
body.mode-trim .cards-print-grid {
  grid-template-columns: repeat(3, var(--card-trim-w));
  grid-template-rows: repeat(3, var(--card-trim-h));
  gap: 3mm;
}
body.mode-trim .crop-mark { display: none; }

/* Light Ink-Saver Card Backs with Full Bleed Faction Border */
.card-proto.card-print-cell.card-back-cell {
  background: var(--back-accent, var(--faction-edge, var(--blood))) !important;
  color: var(--ink, #1a120c);
  border: none;
  position: relative;
  padding: calc(var(--card-bleed) + 1.5mm);
}
.card-proto.card-print-cell.card-back-cell .card-back-content {
  align-items: center;
  justify-content: space-around;
  padding: 4mm 3mm;
}

.card-back-title {
  font-family: "Palatino Linotype", Palatino, serif;
  font-size: 10pt;
  letter-spacing: 0.14em;
  color: var(--back-accent, #7a1f1f);
  text-transform: uppercase;
  text-align: center;
  font-weight: bold;
  position: relative;
  z-index: 5;
}
.card-back-crest {
  font-size: 32pt;
  line-height: 1;
  text-align: center;
  position: relative;
  z-index: 5;
}
.card-back-brand {
  font-family: "Palatino Linotype", Palatino, serif;
  font-size: 7.5pt;
  letter-spacing: 0.22em;
  color: #5c4c3e;
  font-weight: bold;
  text-align: center;
  position: relative;
  z-index: 5;
}

/* Print Toolbar UI */
.print-toolbar {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(244, 234, 215, 0.97);
  border-bottom: 1.5px solid #a67c2d;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
  padding: 8px 16px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-family: system-ui, -apple-system, sans-serif;
  margin: -8mm -8mm 6mm -8mm;
}
.tb-brand {
  font-size: 14px;
  font-weight: 700;
  color: #7a1f1f;
  display: flex;
  align-items: center;
  gap: 8px;
}
.tb-controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
}
.tb-group {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12.5px;
  color: #2a1c12;
}
.tb-select, .tb-btn {
  font-size: 12px;
  padding: 5px 10px;
  border-radius: 6px;
  border: 1px solid #a67c2d;
  background: #fff;
  color: #1a120c;
  cursor: pointer;
}
.tb-btn-primary {
  background: #7a1f1f;
  color: #fff;
  border-color: #521313;
  font-weight: 600;
}
.tb-btn-primary:hover {
  background: #922525;
}
.tb-checkbox-label {
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  user-select: none;
}

@page {
  size: A4 portrait;
  margin: 0;
}
@page board-a2 {
  size: 420mm 594mm;
  margin: 0;
}
@media print {
  body { background: white !important; padding: 0 !important; margin: 0 !important; }
  .nav, .print-toolbar { display: none !important; }
  .sheet { page-break-after: always; margin: 0; }
  .page-a4 {
    width: 210mm; height: 297mm;
    min-width: 210mm; max-width: 210mm;
    min-height: 297mm; max-height: 297mm;
    margin: 0;
    border: none;
    page-break-after: always;
    padding: 4mm;
    box-sizing: border-box;
  }
  .page-a4.cards-master-sheet {
    padding: 0 !important;
    margin: 0 !important;
  }
  .card-back-sheet.duplex-hidden {
    display: none !important;
  }
  .card-proto {
    overflow: hidden;
    box-shadow: none;
  }
  .card-effect { overflow: hidden; }
  .board-stack {
    width: 420mm; height: 594mm;
    min-width: 420mm; min-height: 594mm;
    max-width: 420mm; max-height: 594mm;
    page: board-a2;
  }
}
"""


def _page(
    title: str,
    body: str,
    index_href: str = "index.html",
    body_class: str = "",
) -> str:
    cls = f' class="{_escape(body_class)}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8"/>
<title>{_escape(title)}</title>
<style>{_css()}</style>
</head>
<body{cls}>
<nav class="nav"><a href="{index_href}">← Indeks PnP</a></nav>
{body}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Board — functional UI (code)
# ---------------------------------------------------------------------------

def render_board(layer: str) -> str:
    by_slug = {row[6]: row for row in LOCATIONS}
    street_lines = []
    for a, b in BOARD_EDGES:
        _, _, _, _, ax, ay, _ = by_slug[a]
        _, _, _, _, bx, by, _ = by_slug[b]
        street_lines.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" />')
    streets = f"""
<svg class="board-streets" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
  {"".join(street_lines)}
</svg>
"""
    # A2 portrait = 2×2 A4 portrait — cuts at 210mm (V) and 297mm (H)
    a4_grid = """
<div class="board-a4-grid" aria-hidden="true" title="Linie cięcia 2×2 A4">
  <div class="a4-cut a4-cut-v"></div>
  <div class="a4-cut a4-cut-h"></div>
</div>
"""

    chrome = f"""
<div class="board-chrome" aria-label="Pule wspólne">
  <div class="pool-row">
    <div class="pool-box">
      <div class="pool-title">Relikwie</div>
      <div class="pool-body pool-slots" title="Żetony Relikwii 20×20 mm">
        {_pool_slot_spans(PNP_POOL_SLOTS["relic"])}
      </div>
    </div>
    <div class="pool-box">
      <div class="pool-title">Stosy</div>
      <div class="pool-body pool-slots" title="Żetony Stosu 20×20 mm">
        {_pool_slot_spans(PNP_POOL_SLOTS["stack"])}
      </div>
    </div>
    <div class="pool-box">
      <div class="pool-title">Fragmenty</div>
      <div class="pool-body pool-slots" title="Żetony Fragmentu 20×20 mm">
        {_pool_slot_spans(PNP_POOL_SLOTS["fragment"])}
      </div>
    </div>
  </div>
  <div class="time-deck">
    <div class="pool-title">Kronika Dziejów</div>
    <div class="pool-body" title="Karty edyktów 63×88 mm">
      <div class="time-card">
        <div class="card-slot" title="Talia (zakryta)"></div>
        <span class="lbl">Talia</span>
      </div>
      <div class="time-card">
        <div class="card-slot" title="Aktywny edykt Ery"></div>
        <span class="lbl">Edykt Ery</span>
      </div>
    </div>
  </div>
</div>
"""

    nodes_html = []
    inq_icon = _escape(ICON_SHORT.get("inquisitor", "✝"))
    for num, short, full, _hint, left, top, slug in LOCATIONS:
        agents = "".join('<span class="agent" title="Agent Ø20 mm"></span>' for _ in range(4))
        arrest = ""
        if num == "3":
            arrest = "".join('<span class="arrest" title="Areszt Ø20 mm (Agent)"></span>' for _ in range(4))
        inquisitor = ""
        if slug == "trybunal":
            inquisitor = (
                '<div class="inquisitor-wrap" title="Wielki Inkwizytor — start: Trybunał, Patrol">'
                f'<span class="inquisitor-fig" aria-label="Inkwizytor">{inq_icon}</span>'
                '<div class="inquisitor-states">'
                '<span class="inq-state is-active" title="Patrol">Patrol</span>'
                '<span class="inq-state" title="Autodafé">Autodafé</span>'
                "</div></div>"
            )
        nodes_html.append(f"""
<section class="loc-node" data-loc="{_escape(num)}" data-slug="{_escape(slug)}"
  title="{_escape(full)}" style="left:{left}%;top:{top}%">
  <h2 class="loc-head">{_escape(num)} · {_escape(short)}</h2>
  <div class="token-row">
    {inquisitor}
    {agents}
    <span class="relic-slot" title="Relikwia 20×20 mm"></span>
    {arrest}
  </div>
  <div class="card-row" title="Stos kart akcji ≤3 (63×88 mm)">
    <div class="card-slot"></div>
  </div>
</section>
""")

    return f"""
<div class="sheet">
  <h1>Plansza</h1>
  <div class="board-stack" data-board-mm="420x594">
    {a4_grid}
    <div class="board-ui">
      {chrome}
      <div class="board-play">
        {streets}
        {"".join(nodes_html)}
      </div>
    </div>
  </div>
</div>
"""


# ---------------------------------------------------------------------------
# Cards — effect / heresy(+text) / lore  (no table_note on PnP)
# ---------------------------------------------------------------------------

def render_cards(cards: list[Card], faction_label: str, layer: str, faction_slug: str = "", version: str = "v0.35") -> str:
    fac = _escape(faction_slug or "time")
    items = []
    for c in cards:
        effect = (c.effect or "").strip()
        heresy_text = (getattr(c, "heresy_text", None) or "").strip()
        lore = (c.lore or "").strip()
        cost = int(getattr(c, "cost_gold", None) or c.cost or 0)
        heresy = c.heresy or 0
        badges = _gold_badge(cost) + _heresy_badge(heresy)
        type_label = getattr(c, "type_label", None) or c.type
        type_cls = _type_badge_class(c.type)
        name_cls = "name name-long" if len(c.name or "") > 28 else "name"
        caption_html = ""
        if heresy != 0 and heresy_text:
            caption_html = (
                f'<div class="heresy-caption">{_escape(heresy_text)}</div>'
            )
        _note_effect_overflow(
            c.id,
            effect,
            lore=lore,
            heresy_caption=heresy_text if heresy != 0 else "",
        )
        lore_html = (
            f'<div class="card-lore">{_escape(lore)}</div>' if lore else ""
        )
        stats_html = f'<div class="stat-row">{badges}</div>' if badges else ""
        items.append(f"""
<article class="card-proto faction-{fac}" data-faction="{fac}">
  <div class="hdr">
    <div class="hdr-top">
      <div class="{name_cls}">{_escape(c.name)}</div>
      <span class="type-badge {type_cls}">{_escape(type_label)}</span>
    </div>
    {stats_html}
    {caption_html}
  </div>
  <div class="card-art" aria-hidden="true" title="Slot ilustracji"></div>
  <div class="card-main">
    <div class="card-effect">{_format_effect_html(effect)}</div>
    {lore_html}
    <div class="card-footer-meta"><span>{_escape(c.id.upper())}</span><span>{_escape(version)}</span></div>
  </div>
</article>
""")

    pages = []
    per_page = 9
    for i in range(0, max(len(items), 1), per_page):
        chunk = items[i : i + per_page]
        title = _escape(faction_label) if i == 0 else f"{_escape(faction_label)} (cd.)"
        pages.append(
            f'<div class="page-a4" data-page-mm="210x297">'
            f"<h1>{title}</h1>"
            f'<div class="cards">{"".join(chunk)}</div>'
            f"</div>"
        )
    return "\n".join(pages)


# ---------------------------------------------------------------------------
# All Cards Master Print Deck — Bleed + Crop Marks + Duplex Backs
# ---------------------------------------------------------------------------

FACTION_BACK_INFO: dict[str, tuple[str, str, str]] = {
    "swiete-oficjum": ("Święte Oficjum", "✝️", "#7a1f1f"),
    "cienie-al-andalus": ("Cienie Al-Andalus", "💎", "#1e4d3a"),
    "korona-borgiowie": ("Korona & Borgia", "👑", "#8a6420"),
    "kabala-toledo": ("Kabała z Toledo", "📜", "#4a2d5c"),
    "gildia-cieni": ("Gildia Cieni", "🗡️", "#4a3c28"),
    "time": ("Kronika Dziejów", "⏳", "#3a2e1c"),
}


def render_card_print_cell(c: Card, faction_slug: str, version: str = "v0.35") -> str:
    fac = _escape(faction_slug or "time")
    effect = (c.effect or "").strip()
    heresy_text = (getattr(c, "heresy_text", None) or "").strip()
    lore = (c.lore or "").strip()
    cost = int(getattr(c, "cost_gold", None) or c.cost or 0)
    heresy = c.heresy or 0
    badges = _gold_badge(cost) + _heresy_badge(heresy)
    type_label = getattr(c, "type_label", None) or c.type
    type_cls = _type_badge_class(c.type)
    name_cls = "name name-long" if len(c.name or "") > 28 else "name"
    caption_html = ""
    if heresy != 0 and heresy_text:
        caption_html = f'<div class="heresy-caption">{_escape(heresy_text)}</div>'
    lore_html = f'<div class="card-lore">{_escape(lore)}</div>' if lore else ""
    stats_html = f'<div class="stat-row">{badges}</div>' if badges else ""

    return f"""
<article class="card-proto card-print-cell faction-{fac}" data-faction="{fac}">
  <div class="crop-mark crop-tl-h"></div><div class="crop-mark crop-tl-v"></div>
  <div class="crop-mark crop-tr-h"></div><div class="crop-mark crop-tr-v"></div>
  <div class="crop-mark crop-bl-h"></div><div class="crop-mark crop-bl-v"></div>
  <div class="crop-mark crop-br-h"></div><div class="crop-mark crop-br-v"></div>
  <div class="safe-zone-guide" title="Strefa Bezpieczna (3 mm od linii cięcia)"></div>
  <div class="card-inner-flow">
    <div class="hdr">
      <div class="hdr-top">
        <div class="{name_cls}">{_escape(c.name)}</div>
        <span class="type-badge {type_cls}">{_escape(type_label)}</span>
      </div>
      {stats_html}
      {caption_html}
    </div>
    <div class="card-art" aria-hidden="true" title="Slot ilustracji"></div>
    <div class="card-main">
      <div class="card-effect">{_format_effect_html(effect)}</div>
      {lore_html}
      <div class="card-footer-meta"><span>{_escape(c.id.upper())}</span><span>{_escape(version)}</span></div>
    </div>
  </div>
</article>
"""


def render_card_back_cell(faction_slug: str) -> str:
    fac = faction_slug or "time"
    title, crest, accent = FACTION_BACK_INFO.get(
        fac, ("INQUISITIO 1492", "⚔️", "#7a1f1f")
    )
    return f"""
<div class="card-proto card-print-cell card-back-cell faction-{fac}" data-faction="{fac}">
  <div class="crop-mark crop-tl-h"></div><div class="crop-mark crop-tl-v"></div>
  <div class="crop-mark crop-tr-h"></div><div class="crop-mark crop-tr-v"></div>
  <div class="crop-mark crop-bl-h"></div><div class="crop-mark crop-bl-v"></div>
  <div class="crop-mark crop-br-h"></div><div class="crop-mark crop-br-v"></div>
  <div class="safe-zone-guide" title="Strefa Bezpieczna (3 mm od linii cięcia)"></div>
  <div class="card-back-content" style="--back-accent: {accent};">
    <div class="card-back-title">{_escape(title)}</div>
    <div class="card-back-crest">{crest}</div>
    <div class="card-back-brand">INQUISITIO 1492</div>
  </div>
</div>
"""


def render_all_cards_print(layer: str) -> str:
    all_cards: list[tuple[Card, str, str]] = []
    for slug, label, *_ in FACTIONS:
        cs = cards_for_faction(slug, max_layer=layer)
        if layer == "A":
            cs = [c for c in cs if c.layer == "A"]
        for c in cs:
            all_cards.append((c, slug, label))

    if layer in ("B", "C"):
        time_cs = cards_for_faction("time", max_layer="C")
        for c in time_cs:
            all_cards.append((c, "time", "Kronika Dziejów"))

    per_page = 9
    total_cards = len(all_cards)
    total_sheets = (total_cards + per_page - 1) // per_page

    toolbar_html = """
<div class="print-toolbar" role="region" aria-label="Narzędzia druku PnP">
  <div class="tb-brand">
    <span>⚔️ <strong>INQUISITIO 1492</strong> — Arkusz Drukarski Kart (Bleed & Crop Marks)</span>
  </div>
  <div class="tb-controls">
    <button class="tb-btn tb-btn-primary" onclick="window.print()" title="Otwórz okno drukowania / Zapisz do PDF (Ctrl+P)">
      🖨️ Drukuj / PDF
    </button>
    <div class="tb-group">
      <label for="view-mode-sel">Widok:</label>
      <select id="view-mode-sel" class="tb-select" onchange="updateViewMode(this.value)">
        <option value="bleed">Spad + Znaczniki cięcia (Bleed 2.5 mm)</option>
        <option value="trim">Podgląd po docięciu (Netto 63×88 mm)</option>
        <option value="safe">Inspekcja DTP (Strefa Bezpieczna 3 mm)</option>
      </select>
    </div>
    <div class="tb-group">
      <label for="faction-filter-sel">Frakcja:</label>
      <select id="faction-filter-sel" class="tb-select" onchange="filterFaction(this.value)">
        <option value="all">Wszystkie talie (56 kart)</option>
        <option value="swiete-oficjum">Święte Oficjum (10)</option>
        <option value="cienie-al-andalus">Cienie Al-Andalus (10)</option>
        <option value="korona-borgiowie">Korona & Borgiowie (10)</option>
        <option value="kabala-toledo">Kabała z Toledo (10)</option>
        <option value="gildia-cieni">Gildia Cieni (10)</option>
        <option value="time">Kronika Dziejów (6)</option>
      </select>
    </div>
    <div class="tb-group">
      <label class="tb-checkbox-label">
        <input type="checkbox" id="duplex-toggle" onchange="toggleDuplex(this.checked)" checked>
        <span>Rewersy (Druk dwustronny)</span>
      </label>
    </div>
  </div>
</div>
"""

    cfg = load_game_config()
    version = cfg.get("version", "v0.35")

    pages_html: list[str] = [toolbar_html]

    for page_idx in range(total_sheets):
        start = page_idx * per_page
        chunk = all_cards[start : start + per_page]

        # Front cells
        front_cells: list[str] = []
        for c, fac, _label in chunk:
            front_cells.append(render_card_print_cell(c, fac, version=version))

        # Pad to 9 cells if last page is incomplete
        while len(front_cells) < 9:
            front_cells.append('<div class="card-proto card-print-cell empty-cell" style="background:transparent;border:none;"></div>')

        card_range = f"{start + 1}–{min(start + per_page, total_cards)}"
        front_sheet_html = f"""
<div class="page-a4 cards-master-sheet card-front-sheet" data-page-mm="210x297">
  <div class="sheet-meta-header">
    <span>INQUISITIO 1492 · Arkusz Kart {page_idx + 1}/{total_sheets} (Awersy {card_range})</span>
    <span>Wymiar: 63×88 mm · Spad: +2.5 mm (Brutto 68×93 mm) · Pasery narożne</span>
  </div>
  <div class="cards-print-grid">
    {"".join(front_cells)}
  </div>
</div>
"""
        pages_html.append(front_sheet_html)

        # Back cells with horizontally mirrored columns for accurate duplex alignment
        # Row 0: [2, 1, 0], Row 1: [5, 4, 3], Row 2: [8, 7, 6]
        back_chunk_facs = [fac for _c, fac, _label in chunk]
        while len(back_chunk_facs) < 9:
            back_chunk_facs.append("")

        mirrored_back_cells: list[str] = []
        for row in range(3):
            for col in range(2, -1, -1):
                idx = row * 3 + col
                f_slug = back_chunk_facs[idx]
                if f_slug:
                    mirrored_back_cells.append(render_card_back_cell(f_slug))
                else:
                    mirrored_back_cells.append('<div class="card-proto card-print-cell empty-cell" style="background:transparent;border:none;"></div>')

        back_sheet_html = f"""
<div class="page-a4 cards-master-sheet card-back-sheet" data-page-mm="210x297">
  <div class="sheet-meta-header">
    <span>INQUISITIO 1492 · Rewersy Kart {page_idx + 1}/{total_sheets} (Lustrzane pod dupleks)</span>
    <span>Druk obustronny: obrót wzdłuż długiej krawędzi (Flip on long edge)</span>
  </div>
  <div class="cards-print-grid">
    {"".join(mirrored_back_cells)}
  </div>
</div>
"""
        pages_html.append(back_sheet_html)

    script_html = """
<script>
function updateViewMode(mode) {
  document.body.classList.remove('mode-bleed', 'mode-trim', 'mode-safe');
  if (mode === 'trim') {
    document.body.classList.add('mode-trim');
  } else if (mode === 'safe') {
    document.body.classList.add('mode-safe');
  } else {
    document.body.classList.add('mode-bleed');
  }
}

function filterFaction(f) {
  document.querySelectorAll('.card-print-cell:not(.empty-cell)').forEach(el => {
    if (f === 'all' || el.dataset.faction === f) {
      el.style.opacity = '1';
      el.style.pointerEvents = 'auto';
    } else {
      el.style.opacity = '0.12';
      el.style.pointerEvents = 'none';
    }
  });
}

function toggleDuplex(show) {
  document.querySelectorAll('.card-back-sheet').forEach(el => {
    if (show) {
      el.classList.remove('duplex-hidden');
      el.style.display = 'flex';
    } else {
      el.classList.add('duplex-hidden');
      el.style.display = 'none';
    }
  });
}

// Initial setup on load
document.addEventListener('DOMContentLoaded', () => {
  updateViewMode(document.getElementById('view-mode-sel').value);
  toggleDuplex(document.getElementById('duplex-toggle').checked);
});
</script>
"""
    pages_html.append(script_html)
    return "\n".join(pages_html)



# ---------------------------------------------------------------------------
# Player boards — physical mat (½ A4), slots for components
# ---------------------------------------------------------------------------

def render_player_boards(layer: str) -> str:
    cfg = load_game_config()
    factions_data = get_factions_data(cfg)
    boards = []
    body_cls = "layer-a" if layer == "A" else "layer-c"
    spent = _icon("spent", "Piętno")

    def limit_well(label: str) -> str:
        return (
            f'<div class="pb-limit">'
            f'<span class="pb-token" title="Połóż żeton Piętna po akcji">{spent}</span>'
            f'<span class="pb-limit-lbl">{_escape(label)}</span>'
            f"</div>"
        )

    t_4p = cfg.get("system", {}).get("accusation_threshold", {}).get("4p", 7)
    t_3p = cfg.get("system", {}).get("accusation_threshold", {}).get("3p", 6)
    t_5p = cfg.get("system", {}).get("accusation_threshold", {}).get("5p", 8)

    for slug, name, goal, note, progress_label, progress_n, progress_icon in factions_data:
        pips = "".join(
            f'<span class="heresy-pip {"z1" if i <= 4 else "z2" if i < t_4p else "z3"}">{i}</span>'
            for i in range(11)
        )
        agents = "".join('<span class="agent-slot" title="Agent Ø20 mm"></span>' for _ in range(3))
        prog_face = _icon(progress_icon, progress_label)
        progress = "".join(
            f'<span class="pb-token progress-slot" title="{_escape(progress_label)}">{prog_face}</span>'
            for _ in range(progress_n)
        )
        hook_face = _icon("hook", "Hak")
        hooks = "".join(
            f'<span class="pb-token hook-slot" title="Hak">{hook_face}</span>' for _ in range(2)
        )

        if layer == "A":
            limits = limit_well("Nasłanie")
            body = f"""
  <div class="pb-body {body_cls}">
    <section class="pb-box agents">
      <div class="pb-box-title">Agenci</div>
      <div class="pb-slots">{agents}</div>
    </section>
    <section class="pb-box gold">
      <div class="pb-box-title">Złoto</div>
      <div class="pb-tray" title="Tacka na żetony złota (start 3)"></div>
    </section>
    <section class="pb-box limits">
      <div class="pb-box-title">Limit Ery</div>
      <div class="pb-slots">{limits}</div>
    </section>
    <section class="pb-box progress">
      <div class="pb-box-title">{_escape(progress_label)}</div>
      <div class="pb-slots">{progress}</div>
    </section>
  </div>
"""
        else:
            limits = (
                limit_well("Nasłanie")
                + limit_well("Hak")
                + limit_well("Przesłuchanie")
            )
            body = f"""
  <div class="pb-body {body_cls}">
    <div class="pb-row pb-row-top">
      <section class="pb-box agents">
        <div class="pb-box-title">Agenci</div>
        <div class="pb-slots">{agents}</div>
      </section>
      <section class="pb-box gold">
        <div class="pb-box-title">Złoto</div>
        <div class="pb-tray" title="Tacka na żetony złota (start 3)"></div>
      </section>
      <section class="pb-box hooks">
        <div class="pb-box-title">Haki</div>
        <div class="pb-slots">{hooks}</div>
      </section>
    </div>
    <div class="pb-row pb-row-bot">
      <section class="pb-box limits">
        <div class="pb-box-title">Limity Ery</div>
        <div class="pb-slots">{limits}</div>
      </section>
      <section class="pb-box progress">
        <div class="pb-box-title">{_escape(progress_label)}</div>
        <div class="pb-slots">{progress}</div>
      </section>
    </div>
  </div>
"""

        goal_html = f"<strong>Cel:</strong> {_escape(goal)}"
        if note:
            goal_html += f' <span class="pb-goal-note">({_escape(note)})</span>'

        boards.append(f"""
<div class="player-stack faction-{_escape(slug)}" data-player-mm="210x148" data-faction="{_escape(slug)}">
  <div class="player-ui">
    <header class="pb-head">
      <h2>{_escape(name)}</h2>
      <p class="pb-goal">{goal_html}</p>
    </header>
    <section class="pb-heresy">
      <div class="pb-section-title">Herezja <span class="pb-heresy-note">(*próg oskarżenia: 3p ≥{t_3p}, 4p ≥{t_4p}, 5p ≥{t_5p})</span></div>
      <div class="heresy-track">{pips}</div>
      <div class="heresy-zones">
        <span class="hz-z1">Czysta 0–4</span>
        <span class="hz-z2">Obserw. 5–{t_4p - 1}</span>
        <span class="hz-z3">Krytyczna ≥{t_4p}*</span>
      </div>
    </section>
    {body}
  </div>
</div>
""")

    pages = []
    per_page = 2
    for i in range(0, len(boards), per_page):
        chunk = boards[i : i + per_page]
        pages.append(
            f'<div class="page-a4 player-page" data-page-mm="210x297">'
            f'{"".join(chunk)}'
            f"</div>"
        )
    return "\n".join(pages)


def render_verdict() -> str:
    return f"""
<div class="page-a4 verdict" data-page-mm="210x297">
<h1>Arkusz Werdyktu {_icon("stack")}</h1>
<ol>
<li>Cel ma Herezję ≥ progu (domyślnie <strong>7</strong>).</li>
<li>Oskarżyciel ogłasza cel (1× przeciw temu graczowi / Erę).</li>
<li>Głosowanie <strong>jawne</strong>: każdy poza oskarżonym — Skazać / Uniewinnić.</li>
<li>Remis → Uniewinnienie.</li>
<li><strong>Skazanie:</strong> Agent → Stos <em>lub</em> Lochy +1 Herezja.</li>
<li><strong>Uniewinnienie:</strong> oskarżyciel +1 Herezja.</li>
</ol>
<table>
<tr><th>Oskarżyciel</th><th>Cel</th><th>Głosy S / U</th><th>Wynik</th></tr>
<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>
</table>
</div>
"""


def render_tokens(layer: str) -> str:
    """Cut sheet: 20×20 mm rounded-square chips with temporary emoji faces."""
    # (icon_key, Polish label, count to print)
    c = PNP_TOKEN_COUNTS
    specs: list[tuple[str, str, int]] = [
        ("inquisitor", "Inkwizytor (figurka)", c["inquisitor"]),
        ("patrol", "Patrol (stan Inkwizytora)", c["inquisitor_patrol"]),
        ("autodafe_state", "Autodafé (stan Inkwizytora)", c["inquisitor_autodafe"]),
        ("heresy", "Herezja (tor 0–10)", c["heresy"]),
        ("gold", "Złoto", c["gold"]),
        ("stack", "Stos / Autodafé", c["stack"]),
        ("relic", "Relikwia", c["relic"]),
        ("fragment", "Fragment Kodeksu", c["fragment"]),
        ("decree", "Dekret", c["decree"]),
        ("fall", "Upadek", c["fall"]),
        ("spent", "Piętno", c["spent"]),
    ]
    if layer in ("B", "C"):
        specs.extend([
            ("hook", "Hak", c["hook"]),
            ("double", "Marionetka", c["double"]),
        ])

    # Split across A4 pages when groups exceed one sheet
    groups_html: list[str] = []
    for key, label, count in specs:
        face = _icon(key, label)
        discs = "".join(f'<div class="token-disc" title="{_escape(label)}">{face}</div>' for _ in range(count))
        groups_html.append(
            f'<div class="token-group"><h3>{_escape(label)} ×{count}</h3>'
            f'<div class="token-sheet">{discs}</div></div>'
        )

    # Page 1: core; page 2 (C): hooks/double if needed — keep simple: pack all, allow 2 pages
    mid = len(groups_html)
    # Heuristic: first 7 groups on page 1, rest on page 2 when layer C
    if layer in ("B", "C") and len(groups_html) > 8:
        mid = 7
    pages = []
    chunks = [groups_html[:mid], groups_html[mid:]] if mid < len(groups_html) else [groups_html]
    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        title = "Żetony" if i == 0 else "Żetony (cd.)"
        pages.append(f"""
<div class="page-a4 token-page" data-page-mm="210x297">
  <h1>{title}</h1>
  <div class="token-cut">
  {"".join(chunk)}
  </div>
</div>
""")
    return "\n".join(pages)


def render_index(layer: str, files: list[tuple[str, str]]) -> str:
    links = "".join(f'<li><a href="{_escape(fn)}">{_escape(label)}</a></li>' for fn, label in files)
    return _page(
        f"PnP warstwa {layer}",
        f"""
<div class="page-a4" data-page-mm="210x297">
  <h1>INQUISITIO 1492 — PnP</h1>
  <ol>{links}</ol>
</div>
""",
        index_href="#",
    )


def render_teach_html(md: str, layer: str) -> str:
    lines = md.splitlines()
    parts: list[str] = ['<div class="page-a4 teach-page" data-page-mm="210x297">']
    in_ul = in_ol = False

    def close() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            parts.append("</ul>")
            in_ul = False
        if in_ol:
            parts.append("</ol>")
            in_ol = False

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close()
            continue
        if line.startswith("# "):
            close()
            parts.append(f"<h1>{_escape(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close()
            parts.append(f"<h2>{_escape(line[3:].strip())}</h2>")
        elif line.startswith("- "):
            if not in_ul:
                close()
                parts.append("<ul>")
                in_ul = True
            parts.append(f"<li>{_inline(line[2:].strip())}</li>")
        elif re.match(r"^\d+\.\s", line):
            if not in_ol:
                close()
                parts.append("<ol>")
                in_ol = True
            item = re.sub(r"^\d+\.\s", "", line)
            parts.append(f"<li>{_inline(item)}</li>")
        elif line.startswith("|"):
            close()
            parts.append(f"<pre style='font-size:9pt'>{_escape(line)}</pre>")
        else:
            close()
            parts.append(f"<p>{_inline(line)}</p>")
    close()
    parts.append("</div>")
    return _page("Teach sheet", "".join(parts))


def _inline(s: str) -> str:
    s = _escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def generate(out_dir: Path, layer: str, bw: bool = False) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    load_all_cards(force=True)
    _OVERFLOW_WARNINGS.clear()
    written: list[Path] = []
    index_entries: list[tuple[str, str]] = []
    body_cls = "bw" if bw else ""

    # Master all-cards printable deck (Bleed + Crop Marks + Duplex Backs)
    all_cards_fn = "cards-all-print.html"
    all_cards_path = out_dir / all_cards_fn
    all_cards_path.write_text(
        _page(
            "Wszystkie Karty — Druk PDF (Spady / Bleed & Crop Marks)",
            render_all_cards_print(layer),
            body_class=f"{body_cls} mode-bleed",
        ),
        encoding="utf-8",
    )
    written.append(all_cards_path)
    index_entries.append((all_cards_fn, "🖨️ Wszystkie Karty — Druk PDF (Spady / Bleed & Crop Marks)"))

    cfg = load_game_config()
    version = cfg.get("version", "v0.35")

    for slug, label, *_ in FACTIONS:
        cards = cards_for_faction(slug, max_layer=layer)
        if layer == "A":
            cards = [c for c in cards if c.layer == "A"]
        fn = f"cards-{slug}.html"
        path = out_dir / fn
        path.write_text(
            _page(
                f"Karty {label}",
                render_cards(cards, label, layer, faction_slug=slug, version=version),
                body_class=body_cls,
            ),
            encoding="utf-8",
        )
        written.append(path)
        index_entries.append((fn, f"Karty — {label} ({len(cards)})"))

    if layer == "C":
        time_cs = cards_for_faction("time", max_layer="C")
        fn = "cards-time-deck.html"
        path = out_dir / fn
        path.write_text(
            _page(
                "Kronika Dziejów",
                render_cards(time_cs, "Kronika Dziejów", layer, faction_slug="time", version=version),
                body_class=body_cls,
            ),
            encoding="utf-8",
        )
        written.append(path)
        index_entries.append((fn, f"Kronika Dziejów ({len(time_cs)})"))

    for fn, title, renderer in [
        ("board.html", "Plansza", lambda: render_board(layer)),
        ("player-boards.html", "Planszetki", lambda: render_player_boards(layer)),
        ("verdict.html", "Werdykt", render_verdict),
        ("tokens.html", "Żetony", lambda: render_tokens(layer)),
    ]:
        path = out_dir / fn
        path.write_text(_page(title, renderer(), body_class=body_cls), encoding="utf-8")
        written.append(path)
        index_entries.append((fn, title))

    if (out_dir / "ksiega-zasad.html").exists():
        index_entries.append(("ksiega-zasad.html", "📖 Księga Zasad 4P (Druk HTML / PDF)"))
    if (out_dir / "slownik.html").exists():
        index_entries.append(("slownik.html", "📚 Słownik Pojęć A–Z (Druk HTML / PDF)"))
    if (out_dir / "wariant-2p.html").exists():
        index_entries.append(("wariant-2p.html", "⚔️ Wariant 2-osobowy 2P (Druk HTML / PDF)"))
    if (out_dir / "ksiega-zasad.pdf").exists():
        index_entries.append(("ksiega-zasad.pdf", "📄 Księga Zasad 4P (Plik PDF)"))
    if (out_dir / "slownik.pdf").exists():
        index_entries.append(("slownik.pdf", "📄 Słownik Pojęć A–Z (Plik PDF)"))
    if (out_dir / "wariant-2p.pdf").exists():
        index_entries.append(("wariant-2p.pdf", "📄 Wariant 2-osobowy 2P (Plik PDF)"))

    if (out_dir / "card-editor.html").exists():
        index_entries.append(("card-editor.html", "🛠️ Interaktywny Generator & Podgląd Kart (Live Editor)"))

    index_path = out_dir / "index.html"
    index_path.write_text(render_index(layer, index_entries), encoding="utf-8")
    written.append(index_path)

    if _OVERFLOW_WARNINGS:
        import sys

        print(
            f"PnP overflow warning ({len(_OVERFLOW_WARNINGS)} cards; "
            f">{_EFFECT_OVERFLOW_CHARS}+ chars or {_EFFECT_OVERFLOW_LINES}+ lines):",
            file=sys.stderr,
        )
        for note in _OVERFLOW_WARNINGS:
            print(f"  {note}", file=sys.stderr)

    return written


def main(argv: list[str] | None = None) -> int:
    import shutil

    p = argparse.ArgumentParser(description="PnP HTML: UI-only print layout")
    p.add_argument(
        "--layer",
        default="C",
        choices=["A", "B", "C"],
        help="Filtrowanie kart (domyślnie C = produkt)",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "assets" / "prototypes",
        help="Katalog PnP (domyślnie assets/prototypes/ — bez layer-*)",
    )
    p.add_argument(
        "--bw",
        action="store_true",
        help="Desaturacja kart (grayscale) pod druk Xerox",
    )
    args = p.parse_args(argv)
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    # Jedna aktualna wersja w assets/prototypes/ — usuń legacy layer-A/B/C
    if out == (REPO_ROOT / "assets" / "prototypes").resolve():
        for legacy in sorted(out.glob("layer-*")):
            if legacy.is_dir():
                shutil.rmtree(legacy)
    paths = generate(out, args.layer, bw=args.bw)
    print(f"Wrote {len(paths)} files → {out}")
    for path in paths:
        print(f"  {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
