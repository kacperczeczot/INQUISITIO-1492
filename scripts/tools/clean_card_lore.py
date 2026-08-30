#!/usr/bin/env python3
"""Przepisanie pól LORE na 100% klimatyczny, mroczny, historyczny tekst fabularny (rok 1492)."""

import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CARDS_DIR = REPO_ROOT / "docs" / "game" / "cards" / "factions"

LORE_TEXTS = {
    # === ŚWIĘTE OFICJUM ===
    "so-01": "Cisi bracia zakonni krążą po bruku Toledo, nasłuchując każdego szeptu niezgodnego z dogmatem.",
    "so-02": "Złoto skonfiskowane heretykom zasila machinerię trybunału i opłaca setki donosicieli.",
    "so-03": "Jeden donos wrzucony do puszki w katedrze wystarczy, by cień podejrzeń padł na całą rodzinę.",
    "so-04": "Dzwon zwiastujący procesję pokutną zmusza grzeszników do natychmiastowego opuszczenia miasta.",
    "so-05": "Gdy zbrojni strażnicy pukają nocą do wrót, w Toledo nie ma człowieka, który czułby się bezpieczny.",
    "so-06": "Kute żelazem bramy trybunalskich kazamatów zamykają się za każdym, kogo dosięgnie oskarżenie.",
    "so-07": "W kamiennych podziemiach trybunału milczenie jest tylko chwilową iluzją przed nieuchronnym wyznaniem.",
    "so-08": "Widok czarnego habitu i płonącej pochodni Inkwizytora paraliżuje całe dzielnice Toledo.",
    "so-09": "Świadek, który otrzymał rozgrzeszenie w zamian za zeznania, jest najgroźniejszą bronią oskarżyciela.",
    "so-10": "Dym z placu Zocodover unosi się ku niebiosom, oczyszczając miasto z grzechu i buntu.",
    "so-11": "Kto odmawia posłuszeństwa dekretom wiary, sam wydaje na siebie wyrok wiecznego potępienia.",
    "so-12": "Zbrojna straż w żelaznych pancerzach pilnuje, by żaden heretyk nie zbiegł przed oblicze sprawiedliwości.",

    # === CIENIE AL-ANDALUS ===
    "caa-01": "Podziemne akwedukty Maurów wciąż łączą pałace z ruinami dawnych meczetów.",
    "caa-02": "Skarby ukryte w murach przed upadkiem Grenady finansują walkę o ocalenie dziedzictwa.",
    "caa-03": "W gwarze targowiska najłatwiej przekazać zakazany zwój lub ostrzec braci przed obławą.",
    "caa-04": "Porzucony burnus i ślad w zaułku kierują inkwizytorów w ślepą uliczkę, z dala od prawdziwych uciekinierów.",
    "caa-05": "Zaufany posłaniec przemyka nocą przez bramy miejskie, niosąc relikwię ku bezpiecznym górom.",
    "caa-06": "Podrobiony klucz i przekupiony strażnik otwierają kraty lochów nim nadejdzie świt.",
    "caa-07": "Wiemy, jakie tajemnice skrywasz w alkowie — jeden nasz krok i trybunał pozna całą prawdę.",
    "caa-08": "Złamany szantażem urzędnik wykonuje nasze polecenia, nie mając pojęcia, komu naprawdę służy.",
    "caa-09": "Ocalone manuskrypty i relikwie przodków są warte więcej niż całe złoto kastylijskiej korony.",
    "caa-10": "Echo dawnej chwały Andaluzji rozbrzmiewa w sercach tych, którzy nigdy nie złożyli broni.",
    "caa-11": "Zmienić latarnika, zgasić pochodnię w zaułku — i oto inkwizytor błądzi w labiryncie nocy.",
    "caa-12": "Stare mauretańskie złoto ukryte w murach pałacowych czekało na ten decydujący dzień.",

    # === KORONA & BORGIOWIE ===
    "kb-01": "Królewski rozkaz z pieczęcią z laku łamie każdy opór i otwiera najpilniej strzeżone wrota.",
    "kb-02": "Skarbiec korony musi być pełny, by opłacić lojalność wielmożów i milczenie kardynałów.",
    "kb-03": "Zatruty szept w królewskiej alkowie potrafi zniszczyć ród potężniejszy niż armia zbrojnych.",
    "kb-04": "Faworyt dworu cieszy się łaską królowej, dopóki jego użyteczność przewyższa jego ambicję.",
    "kb-05": "Królewski list żelazny chroni przed szubienicą, lecz czyni jego posiadacza wiecznym dłużnikiem tronu.",
    "kb-06": "Królewscy halabardnicy nie pytają o winę — wykonują wolę suwerena z bezwzględną precyzją.",
    "kb-07": "Papieska bulla i królewska pieczęć dają władzę, przed którą uginają się najtwardsze karki.",
    "kb-08": "Każdy wyrok ma swoją cenę, a waga sprawiedliwości przechyla się tam, gdzie padnie cięższe złoto.",
    "kb-09": "Królewski edykt nie podlega dyskusji — opór wobec korony jest tożsamy ze zdradą stanu.",
    "kb-10": "Gdy obie pieczęcie spoczną na pergaminie, żaden wielmoża w Kastylii nie zdoła podnieść głowy.",
    "kb-11": "Złote pierścienie i listy polecające otwierają przed naszymi ludźmi każde drzwi w Toledo.",
    "kb-12": "Jedno niedyskretne słowo przy królewskim stole staje się wieczystą smyczą w naszych rękach.",

    # === KABAŁA Z TOLEDO ===
    "kt-01": "Dyskretne kroki adepta po bruku Toledo nie przyciągają wzroku czujnych inkwizytorów.",
    "kt-02": "Alchemia i wiedza przodków pozwalają pomnażać kruszec z dala od chciwych oczu poborców.",
    "kt-03": "Karty tajemnego Kodeksu świecą blaskiem widocznym tylko dla oczu wtajemniczonych.",
    "kt-04": "Mistyczne zwierciadło odbija złą wolę prześladowców, kierując ich gniew na inne imię.",
    "kt-05": "Układ gwiazd nad Toledo wskazuje godzinę, w której pieczęć wiedzy może zostać otwarta.",
    "kt-06": "Imię wyryte na pergaminie zawiera w sobie moc wiązania woli i odsłaniania tajemnic.",
    "kt-07": "W podziemiach synagogi spoczywają archiwa, o których istnieniu biskupi nie śmią nawet marzyć.",
    "kt-08": "Strażnicy wiedzy wiedzą, jak zamknąć w lochu każdego, kto zbezcześci święte manuskrypty.",
    "kt-09": "Odnaleziony fragment starożytnego Kodeksu przybliża nas do poznania ostatecznej tajemnicy stworzenia.",
    "kt-10": "Gdy Pieczęć Salomona zostanie domknięta, pradawna mądrość zatriumfuje nad mrokiem prześladowań.",
    "kt-11": "Waga losu wymaga idealnej równowagi — ani zbyt czysty, ani zbyt splamiony w oczach świata.",
    "kt-12": "Kto zagląda w pergaminy Salomona, ten nieświadomie zostawia swój ślad na kartach przeznaczenia.",

    # === GILDIA CIENI ===
    "gc-01": "Dźwięk złotych dukatów w sakiewce strażnika potrafi uczynić go ślepym i głuchym na całą noc.",
    "gc-02": "Handel spod lady i przemyt w zaułkach portowych — w piwnicach Toledo kupisz wszystko: od noża po fałszywe rozgrzeszenie.",
    "gc-03": "Zakazana księga podłożona do komnaty rywala sprowadzi na niego inkwizycję jeszcze przed południem.",
    "gc-04": "Donosiciel z zaułka nie żąda wiele, lecz pamięta każdą twarz i każdy brudny sekret miasta.",
    "gc-05": "Za odpowiednią sumę fałszywy świadek przysięgnie przed trybunałem na wszystkie świętości.",
    "gc-06": "List z dowodem zdrady leży na stole — albo zapłacisz naszą cenę, albo jutro zawiśniesz.",
    "gc-07": "Ciało w mrocznym kanale Toledo mówi więcej niż sto kazań o kruchości ludzkiego żywota.",
    "gc-08": "Pieniądze pachnące trucizną parzą dłonie tego, kto przyjmie je w godzinie chciwości.",
    "gc-09": "Dług zaciągnięty w podziemiach Gildii spłaca się majątkiem, wolnością albo krwią.",
    "gc-10": "Gdy upada potężny ród, w ruinach jego pałacu ucztują ci, którzy pociągali za sznurki z cienia.",
    "gc-11": "Podrobiony podpis na wekslu to najtańszy i najszybszy sposób na zrujnowanie wielkiego rodu.",
    "gc-12": "Dla zwinnego kieszonkowca nocny spacer wąskimi uliczkami Toledo zawsze przynosi pełną sakiewkę.",
}

updated_count = 0

for p in CARDS_DIR.rglob("*.md"):
    if p.name.upper() in ("README.MD", "SCHEMA.MD", "KATALOG.MD"):
        continue
    text = p.read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 3:
        continue
    try:
        meta = yaml.safe_load(parts[1])
    except Exception:
        continue
    if not isinstance(meta, dict) or "id" not in meta:
        continue
    cid = meta["id"]
    if cid in LORE_TEXTS:
        meta["lore"] = LORE_TEXTS[cid]
        new_yaml = yaml.dump(meta, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_yaml}---\n" + "---".join(parts[2:])
        p.write_text(new_content, encoding="utf-8")
        updated_count += 1

print(f"Zaktualizowano LORE w {updated_count} plikach kart na 100% klimatyczne opisy fabularne!")
