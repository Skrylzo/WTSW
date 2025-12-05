# data/mapping_recettes.py
# Mapping des ingrédients génériques vers les catégories génériques

# Mapping des ingrédients génériques (utilisés dans les recettes) vers les catégories
MAPPING_INGREDIENTS_VERS_CATEGORIES = {
    # Potions - Base
    "Herbe Médicinale": "Ingrédient Potion Niveau 1-5",
    "Herbe Rare": "Ingrédient Potion Niveau 5-10",
    "Cristal Magique": "Ingrédient Potion Niveau 10-15",
    "Essence Démoniaque": "Ingrédient Potion Niveau 15-20",

    # Armes - Base
    "Minerai de Fer": "Ingrédient Arme Niveau 1-5",
    "Minerai d'Argent": "Ingrédient Arme Niveau 5-10",
    "Minerai de Mithril": "Ingrédient Arme Niveau 10-15",
    "Minerai d'Adamantium": "Ingrédient Arme Niveau 15-20",
    "Minerai Divin": "Ingrédient Arme Niveau 15-20",  # Légendaire, même niveau que Adamantium

    # Armures - Base
    "Peau de Gobelin": "Ingrédient Armure Niveau 1-5",
    "Cuir Renforcé": "Ingrédient Armure Niveau 5-10",
    # Note: Les recettes utilisent aussi "Cristal Magique" pour les armures rares
    # On peut utiliser le même mapping

    # Ingrédients spéciaux (restent inchangés)
    "Eau Pure": "Eau Pure",  # Ingrédient spécial, pas une catégorie
    "Fragment d'Âme": "Ingrédient Potion Niveau 15-20",  # Légendaire
}

def convertir_ingredient_vers_categorie(ingredient: str) -> str:
    """
    Convertit un ingrédient générique vers sa catégorie correspondante.
    Si l'ingrédient n'est pas dans le mapping, retourne l'ingrédient tel quel.

    :param ingredient: Nom de l'ingrédient générique
    :return: Catégorie générique ou nom d'ingrédient spécial
    """
    return MAPPING_INGREDIENTS_VERS_CATEGORIES.get(ingredient, ingredient)
