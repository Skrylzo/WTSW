import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Tuple

from .biomes import Biome
from .royaumes import (
    TOUS_LES_ROYAUMES,
    initialiser_royaumes_avec_hubs,
)
from data.ennemis import DEFINITIONS_ENNEMIS


VALDORIA_DIR = Path(__file__).resolve().parents[1] / "Valdoria"
BIOMES_PRE_GENERES_FILE = Path(__file__).parent / "biomes_valdoria.py"
ROYAUME_NAME_MAP = {
    "aerthos": "Aerthos",
    "khazak-dum": "Khazak-Dûm",
    "khazak-dûm": "Khazak-Dûm",
    "khazak düm": "Khazak-Dûm",
    "luthesia": "Luthesia",
    "vrak'thar": "Vrak'thar",
    "vrak’thar": "Vrak'thar",
    "vrakthar": "Vrak'thar",
}

DEFAULT_MOB_STATS = {
    "vie_max": 120,
    "vitesse": 12,
    "attaque": 22,
    "defense": 8,
    "chance_critique": 5,
    "xp_a_donner": 120,
    "loot_table": [],
}

DEFAULT_BOSS_STATS = {
    "vie_max": 320,
    "vitesse": 15,
    "attaque": 38,
    "defense": 15,
    "chance_critique": 10,
    "xp_a_donner": 500,
    "loot_table": [],
}

_BIOMES_CHARGES = False


def normaliser_texte(nom: str) -> str:
    if not nom:
        return ""
    nom = nom.replace("’", "'")
    nom = unicodedata.normalize("NFKD", nom)
    return "".join(c for c in nom if not unicodedata.combining(c)).strip()


def slugify(nom: str) -> str:
    texte = normaliser_texte(nom).lower()
    texte = re.sub(r"[^a-z0-9]+", "_", texte)
    return texte.strip("_") or "inconnu"


def parse_basic_file(path: Path) -> List[Dict]:
    biomes: List[Dict] = []
    current = None
    collecting_mobs = False
    mobs_buffer: List[str] = []
    in_biomes_section = False

    def finalize_mobs():
        nonlocal mobs_buffer
        if current is not None and mobs_buffer:
            current["mobs"].extend(mobs_buffer)
            mobs_buffer = []

    with path.open(encoding="utf-8", errors="replace") as fichier:
        for raw_line in fichier:
            line = raw_line.strip()
            if not line:
                continue
            lower = line.lower()

            if in_biomes_section and any(lower.startswith(prefix) for prefix in ("habitant", "roi", "les 4")):
                break

            if not in_biomes_section:
                if "biomes" in lower:
                    in_biomes_section = True
                continue

            if "mob" in lower:
                collecting_mobs = True
                mobs_buffer = []
                mobs_buffer.extend(extraire_mobs(line))
                continue

            if collecting_mobs:
                lower_line = line.lower()
                if line.startswith("-") or (line and not any(keyword in lower_line for keyword in ("donjon", "boss"))):
                    # Traiter comme entrée de mob (même sans tiret, ex: "Roches Vivantes")
                    mobs_buffer.extend(extraire_mobs(f"- {line}"))
                    continue
                else:
                    finalize_mobs()
                    collecting_mobs = False
                    # poursuivre pour analyser (peut être Donjon/Boss/nouveau biome)

            if "donjon" in lower:
                if current:
                    current["donjon"] = line.split(":", 1)[1].strip()
                continue

            if "boss" in lower:
                if current:
                    boss_value = line.split(":", 1)[1].strip()
                    current["boss"] = boss_value
                continue

            # New biome name
            ignored_prefixes = ("habitant", "roi", "les 4", "le boss", "le donjon", "boss", "donjon", "mob", "mobs")
            if any(lower.startswith(prefix) for prefix in ignored_prefixes):
                continue
            biome_nom = nettoyer_nom_biome(line)
            if not biome_nom:
                continue
            current = {
                "nom": biome_nom,
                "slug": slugify(biome_nom),
                "mobs": [],
                "donjon": "",
                "boss": "",
            }
            biomes.append(current)

    if collecting_mobs:
        finalize_mobs()

    return biomes


def extraire_mobs(ligne: str) -> List[str]:
    if ":" in ligne:
        ligne = ligne.split(":", 1)[1]
    segments = re.split(r"-\s+", ligne)
    elements = []
    for part in segments:
        nom = part.strip(" :–—\t")
        if nom:
            elements.append(nom)
    return elements


def nettoyer_nom_biome(texte: str) -> str:
    texte = texte.strip()
    texte = re.sub(r"^\d+[\).\s]+", "", texte)
    return texte.strip(" -")


def parser_detail_file(path: Path) -> Dict[str, str]:
    descriptions: Dict[str, str] = {}
    if not path.exists():
        return descriptions

    current_slug = None
    buffer: List[str] = []

    header_regex = re.compile(r"^\s*\d+[\).]\s*(.+)")

    with path.open(encoding="utf-8", errors="replace") as fichier:
        for raw_line in fichier:
            line = raw_line.rstrip()
            if not line.strip():
                continue
            match = header_regex.match(line)
            if match:
                if current_slug and buffer:
                    descriptions[current_slug] = " ".join(buffer).strip()
                biome_nom = nettoyer_nom_biome(match.group(1))
                current_slug = slugify(biome_nom)
                buffer = []
            else:
                if current_slug:
                    buffer.append(line.strip())

    if current_slug and buffer:
        descriptions[current_slug] = " ".join(buffer).strip()

    return descriptions


def creer_ennemi_si_absent(nom: str, slug: str, is_boss: bool = False) -> str:
    if not nom:
        return slug

    if slug in DEFINITIONS_ENNEMIS:
        return slug

    stats = DEFAULT_BOSS_STATS if is_boss else DEFAULT_MOB_STATS
    loot_table = list(stats.get("loot_table", []))

    DEFINITIONS_ENNEMIS[slug] = {
        "nom": nom,
        "vie_max": stats["vie_max"],
        "vitesse": stats["vitesse"],
        "attaque": stats["attaque"],
        "defense": stats["defense"],
        "chance_critique": stats["chance_critique"],
        "xp_a_donner": stats["xp_a_donner"],
        "loot_table": loot_table,
    }
    return slug


def charger_biomes_valdoria() -> Dict[str, List[Biome]]:
    biomes_par_royaume: Dict[str, List[Biome]] = {}

    basic_files = set(VALDORIA_DIR.glob("*Basic*World*.txt"))
    basic_files.update(VALDORIA_DIR.glob("*Basic*world*.txt"))

    for basic_file in sorted(basic_files):
        royaume_raw = basic_file.stem.replace("(Basic World)", "").replace("(Basic world)", "").strip()
        royaume_nom = normaliser_nom_royaume(royaume_raw)
        if not royaume_nom:
            continue

        detail_file = trouver_fichier_detail(basic_file.stem)
        descriptions = parser_detail_file(detail_file) if detail_file else {}
        biomes_data = parse_basic_file(basic_file)

        biomes_instances: List[Biome] = []
        for idx, data in enumerate(biomes_data, start=1):
            mobs_ids = []
            for mob_nom in data["mobs"]:
                mob_slug = slugify(mob_nom)
                creer_ennemi_si_absent(mob_nom, mob_slug, is_boss=False)
                mobs_ids.append(mob_slug)

            boss_slug = ""
            if data["boss"]:
                boss_slug = slugify(data["boss"])
                creer_ennemi_si_absent(data["boss"], boss_slug, is_boss=True)

            biome = Biome(
                nom=data["nom"],
                description=descriptions.get(data["slug"], ""),
                mobs_ids=mobs_ids,
                donjon_nom=data["donjon"],
                boss_id=boss_slug,
                difficulte=idx,
            )
            biomes_instances.append(biome)

        biomes_par_royaume.setdefault(royaume_nom, []).extend(biomes_instances)

    return biomes_par_royaume


def normaliser_nom_royaume(nom: str) -> str:
    nom = normaliser_texte(nom).lower()
    nom = nom.replace("(detail world)", "").strip()
    return ROYAUME_NAME_MAP.get(nom, nom.title())


def trouver_fichier_detail(basic_stem: str) -> Path | None:
    base_nom = basic_stem.replace("(Basic World)", "").replace("(Basic world)", "").strip()
    patterns = [
        f"{base_nom} (Détail World).txt",
        f"{base_nom} (Détail world).txt",
        f"{base_nom} (Details World).txt",
        f"{base_nom} (Details world).txt",
        f"{base_nom} (Détail World) copie.txt",
        f"{base_nom} (Details world) copie.txt",
    ]
    for pattern in patterns:
        candidate = VALDORIA_DIR / pattern
        if candidate.exists():
            return candidate
    # Dernier recours : prendre le premier fichier contenant le nom et "Détail"
    for candidate in VALDORIA_DIR.glob(f"{base_nom}*Détail*.txt"):
        return candidate
    for candidate in VALDORIA_DIR.glob(f"{base_nom}*Detail*.txt"):
        return candidate
    return None


def serialiser_biomes_en_python(biomes_par_royaume: Dict[str, List[Biome]]) -> str:
    """Génère le code Python pour le fichier biomes_valdoria.py"""
    lines = [
        '# world/biomes_valdoria.py',
        '# Fichier AUTO-GÉNÉRÉ par world/data_loader.py',
        '# NE PAS MODIFIER MANUELLEMENT - Régénéré depuis Valdoria/*.txt',
        '',
        'from .biomes import Biome',
        '',
        'BIOMES_DATA = {'
    ]

    for royaume_nom, biomes in sorted(biomes_par_royaume.items()):
        lines.append(f"    {repr(royaume_nom)}: [")
        for biome in biomes:
            lines.append("        Biome(")
            lines.append(f"            nom={repr(biome.nom)},")
            # Utiliser des triples guillemets pour les descriptions longues
            if biome.description:
                desc_escaped = biome.description.replace('"""', '\\"\\"\\"')
                lines.append(f'            description="""{desc_escaped}""",')
            else:
                lines.append("            description='',")
            lines.append(f"            mobs_ids={repr(biome.mobs_ids)},")
            lines.append(f"            donjon_nom={repr(biome.donjon_nom)},")
            lines.append(f"            boss_id={repr(biome.boss_id)},")
            lines.append(f"            difficulte={biome.difficulte},")
            lines.append("        ),")
        lines.append("    ],")

    lines.append("}")
    return "\n".join(lines)


def charger_biomes_pre_generes() -> Dict[str, List[Biome]]:
    """Charge les biomes depuis le fichier pré-généré si les .txt n'existent pas"""
    if not BIOMES_PRE_GENERES_FILE.exists():
        return {}

    try:
        # Importer le module dynamiquement
        import importlib.util
        spec = importlib.util.spec_from_file_location("world.biomes_valdoria", BIOMES_PRE_GENERES_FILE)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return getattr(module, 'BIOMES_DATA', {})
        return {}
    except Exception as e:
        print(f"⚠️  Erreur lors du chargement de biomes_valdoria.py : {e}")
        return {}


def generer_fichier_biomes(biomes_par_royaume: Dict[str, List[Biome]]) -> None:
    """Génère le fichier biomes_valdoria.py avec les biomes parsés"""
    if not biomes_par_royaume:
        return

    contenu = serialiser_biomes_en_python(biomes_par_royaume)
    BIOMES_PRE_GENERES_FILE.write_text(contenu, encoding='utf-8')


def attacher_biomes_depuis_valdoria(force: bool = False) -> Dict[str, List[Biome]]:
    global _BIOMES_CHARGES
    if _BIOMES_CHARGES and not force:
        return {}

    if force:
        _BIOMES_CHARGES = False

    initialiser_royaumes_avec_hubs()

    if force:
        for royaume in TOUS_LES_ROYAUMES.values():
            royaume.biomes = []

    # Essayer de charger depuis les .txt si disponibles
    if VALDORIA_DIR.exists():
        biomes_par_royaume = charger_biomes_valdoria()
        # Générer le fichier pré-généré pour les joueurs sans .txt
        generer_fichier_biomes(biomes_par_royaume)
    else:
        # Charger depuis le fichier pré-généré
        biomes_par_royaume = charger_biomes_pre_generes()

    for royaume_nom, biomes in biomes_par_royaume.items():
        royaume = TOUS_LES_ROYAUMES.get(royaume_nom)
        if not royaume:
            continue
        existing_names = {biome.nom for biome in royaume.biomes}
        for biome in biomes:
            if biome.nom not in existing_names:
                royaume.ajouter_biome(biome)

    _BIOMES_CHARGES = True
    return biomes_par_royaume
