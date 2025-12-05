# data/categories_ingredients.py
# Système de catégories génériques pour les recettes
# Permet d'utiliser des catégories au lieu de noms d'ingrédients spécifiques

from typing import Dict, List, Optional
from data.ingredients import DEFINITIONS_INGREDIENTS, obtenir_ingredients_par_usage

# Mapping des niveaux de biome aux catégories
# Les biomes sont organisés : 1-5, 5-10, 10-15, 15-20
NIVEAUX_BIOMES = {
    "1-5": {"niveau_min": 1, "niveau_max": 5, "difficulte": 1},
    "5-10": {"niveau_min": 5, "niveau_max": 10, "difficulte": 2},
    "10-15": {"niveau_min": 10, "niveau_max": 15, "difficulte": 3},
    "15-20": {"niveau_min": 15, "niveau_max": 20, "difficulte": 4},
}

# Catégories génériques d'ingrédients
CATEGORIES_GENERIQUES = {
    # Potions
    "Ingrédient Potion Niveau 1-5": {
        "usage": "Potions",
        "niveau": "1-5",
        "description": "Ingrédient de potion du premier biome (Niveau 1-5)"
    },
    "Ingrédient Potion Niveau 5-10": {
        "usage": "Potions",
        "niveau": "5-10",
        "description": "Ingrédient de potion du deuxième biome (Niveau 5-10)"
    },
    "Ingrédient Potion Niveau 10-15": {
        "usage": "Potions",
        "niveau": "10-15",
        "description": "Ingrédient de potion du troisième biome (Niveau 10-15)"
    },
    "Ingrédient Potion Niveau 15-20": {
        "usage": "Potions",
        "niveau": "15-20",
        "description": "Ingrédient de potion du quatrième biome (Niveau 15-20)"
    },

    # Armes
    "Ingrédient Arme Niveau 1-5": {
        "usage": "Armes",
        "niveau": "1-5",
        "description": "Ingrédient d'arme du premier biome (Niveau 1-5)"
    },
    "Ingrédient Arme Niveau 5-10": {
        "usage": "Armes",
        "niveau": "5-10",
        "description": "Ingrédient d'arme du deuxième biome (Niveau 5-10)"
    },
    "Ingrédient Arme Niveau 10-15": {
        "usage": "Armes",
        "niveau": "10-15",
        "description": "Ingrédient d'arme du troisième biome (Niveau 10-15)"
    },
    "Ingrédient Arme Niveau 15-20": {
        "usage": "Armes",
        "niveau": "15-20",
        "description": "Ingrédient d'arme du quatrième biome (Niveau 15-20)"
    },

    # Armures
    "Ingrédient Armure Niveau 1-5": {
        "usage": "Armures",
        "niveau": "1-5",
        "description": "Ingrédient d'armure du premier biome (Niveau 1-5)"
    },
    "Ingrédient Armure Niveau 5-10": {
        "usage": "Armures",
        "niveau": "5-10",
        "description": "Ingrédient d'armure du deuxième biome (Niveau 5-10)"
    },
    "Ingrédient Armure Niveau 10-15": {
        "usage": "Armures",
        "niveau": "10-15",
        "description": "Ingrédient d'armure du troisième biome (Niveau 10-15)"
    },
    "Ingrédient Armure Niveau 15-20": {
        "usage": "Armures",
        "niveau": "15-20",
        "description": "Ingrédient d'armure du quatrième biome (Niveau 15-20)"
    },
}

# Ingrédients spéciaux (achetables en boutique, universels)
INGREDIENTS_SPECIAUX = {
    "Eau Pure": {
        "description": "Eau pure achetée en boutique. Nécessaire pour toutes les potions.",
        "achetable": True,
        "prix_base": 10
    }
}

# Cache pour le mapping catégorie → ingrédients réels par royaume
_MAPPING_CACHE: Optional[Dict] = None


def _construire_mapping_ingredients_par_biome():
    """
    Construit un mapping des ingrédients par royaume, usage et niveau de biome.
    Retourne un dictionnaire : {royaume: {usage: {niveau: [liste_ingredients]}}}
    """
    mapping = {}

    for ing_id, ing_data in DEFINITIONS_INGREDIENTS.items():
        nom = ing_data.get('nom', '')
        usage = ing_data.get('usage', '')
        sources = ing_data.get('sources', [])

        for source in sources:
            royaume = source.get('royaume', '')
            biome_nom = source.get('biome', '')

            # Déterminer le niveau du biome basé sur son ordre dans le royaume
            # On va utiliser une approche basée sur le mapping des biomes
            niveau_biome = _determiner_niveau_biome(royaume, biome_nom)

            if not niveau_biome:
                continue

            if royaume not in mapping:
                mapping[royaume] = {}
            if usage not in mapping[royaume]:
                mapping[royaume][usage] = {}
            if niveau_biome not in mapping[royaume][usage]:
                mapping[royaume][usage][niveau_biome] = []

            if nom not in mapping[royaume][usage][niveau_biome]:
                mapping[royaume][usage][niveau_biome].append(nom)

    return mapping


def _determiner_niveau_biome(royaume: str, biome_nom: str) -> Optional[str]:
    """
    Détermine la catégorie d'un biome basé sur sa POSITION dans le royaume.

    IMPORTANT : Le mapping se fait par POSITION (1er, 2ème, 3ème, 4ème biome),
    pas par niveau absolu. Cela garantit que les recettes restent craftables
    même quand le joueur change de royaume (ex: biomes 20-25, 25-30, etc.).

    Retourne "1-5", "5-10", "10-15", ou "15-20" selon la position du biome.
    Ces valeurs correspondent aux catégories génériques des recettes.
    """
    try:
        from world.biomes_valdoria import BIOMES_DATA

        if royaume not in BIOMES_DATA:
            return None

        biomes = BIOMES_DATA[royaume]

        # Trouver le biome correspondant par sa POSITION dans le royaume
        for idx, biome in enumerate(biomes, start=1):
            if biome.nom == biome_nom or biome_nom in biome.nom or biome.nom in biome_nom:
                # Mapping par POSITION (pas par niveau absolu) :
                # - 1er biome → "1-5" (même si le biome réel est 20-25)
                # - 2ème biome → "5-10" (même si le biome réel est 25-30)
                # - 3ème biome → "10-15" (même si le biome réel est 30-35)
                # - 4ème biome → "15-20" (même si le biome réel est 35-40)
                # Cela garantit que les recettes restent craftables dans tous les royaumes !
                if idx == 1:
                    return "1-5"
                elif idx == 2:
                    return "5-10"
                elif idx == 3:
                    return "10-15"
                elif idx == 4:
                    return "15-20"

        # Si pas trouvé, utiliser les niveaux du biome directement
        for biome in biomes:
            if biome.nom == biome_nom or biome_nom in biome.nom or biome.nom in biome_nom:
                niveau_min = biome.niveau_min
                niveau_max = biome.niveau_max
                return f"{niveau_min}-{niveau_max}"

        return None
    except ImportError:
        # Fallback : utiliser une approche basée sur les mots-clés
        biome_lower = biome_nom.lower()
        if any(mot in biome_lower for mot in ["premier", "1", "début", "forêt", "plaine", "tunnel"]):
            return "1-5"
        elif any(mot in biome_lower for mot in ["deuxième", "2", "montagne", "crête", "caverne"]):
            return "5-10"
        elif any(mot in biome_lower for mot in ["troisième", "3", "lac", "jardin", "lave"]):
            return "10-15"
        elif any(mot in biome_lower for mot in ["quatrième", "4", "galerie", "ruine", "plaine céleste"]):
            return "15-20"
        return None


def obtenir_ingredients_par_categorie(categorie: str, royaume: str) -> List[str]:
    """
    Retourne tous les ingrédients réels correspondant à une catégorie générique pour un royaume donné.

    IMPORTANT : Le mapping se fait par POSITION du biome dans le royaume, pas par niveau absolu.
    Cela garantit que les recettes restent craftables même quand le joueur change de royaume.

    Exemple :
    - Catégorie "Ingrédient Potion Niveau 1-5" → 1er biome du royaume
    - Dans Vrak'thar : Biome 1-5 → "Cendre Maudite"
    - Dans Aerthos débloqué : Biome 20-25 → "Herbe Lumineuse"
    - Les deux correspondent à la même catégorie, donc les recettes fonctionnent !

    :param categorie: Catégorie générique (ex: "Ingrédient Potion Niveau 1-5")
    :param royaume: Nom du royaume (ex: "Vrak'thar")
    :return: Liste des noms d'ingrédients réels
    """
    global _MAPPING_CACHE

    if _MAPPING_CACHE is None:
        _MAPPING_CACHE = _construire_mapping_ingredients_par_biome()

    if categorie not in CATEGORIES_GENERIQUES:
        return []

    categorie_data = CATEGORIES_GENERIQUES[categorie]
    usage = categorie_data["usage"]
    niveau = categorie_data["niveau"]  # "1-5", "5-10", etc. (position du biome)

    if royaume not in _MAPPING_CACHE:
        return []
    if usage not in _MAPPING_CACHE[royaume]:
        return []
    if niveau not in _MAPPING_CACHE[royaume][usage]:
        return []

    return _MAPPING_CACHE[royaume][usage][niveau]


def est_categorie_generique(nom: str) -> bool:
    """
    Vérifie si un nom d'ingrédient est une catégorie générique.

    :param nom: Nom à vérifier
    :return: True si c'est une catégorie générique
    """
    return nom in CATEGORIES_GENERIQUES


def est_ingredient_special(nom: str) -> bool:
    """
    Vérifie si un nom d'ingrédient est un ingrédient spécial (achetable).

    :param nom: Nom à vérifier
    :return: True si c'est un ingrédient spécial
    """
    return nom in INGREDIENTS_SPECIAUX


def obtenir_toutes_categories() -> List[str]:
    """
    Retourne la liste de toutes les catégories génériques disponibles.

    :return: Liste des noms de catégories
    """
    return list(CATEGORIES_GENERIQUES.keys())


def obtenir_ingredients_speciaux() -> List[str]:
    """
    Retourne la liste de tous les ingrédients spéciaux disponibles.

    :return: Liste des noms d'ingrédients spéciaux
    """
    return list(INGREDIENTS_SPECIAUX.keys())
