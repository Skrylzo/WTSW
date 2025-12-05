# data/craft_bonus.py
# Système de bonus de niveau pour le craft

from typing import Dict, Optional, List
from classes.objet import Objet
from data.recettes import TOUTES_LES_RECETTES


def calculer_bonus_niveau(niveau_biome: int) -> float:
    """
    Calcule le multiplicateur de bonus basé sur le niveau du biome.

    Formule : 1 + (niveau_biome / 20)
    - Niveau 1-5 → ×1.0 à ×1.25
    - Niveau 20-25 → ×2.0 à ×2.25
    - Niveau 40-45 → ×3.0 à ×3.25

    :param niveau_biome: Niveau minimum du biome d'origine
    :return: Multiplicateur de bonus
    """
    if niveau_biome is None or niveau_biome <= 0:
        return 1.0

    return 1.0 + (niveau_biome / 20.0)


def calculer_niveau_moyen_ingredients(ingredients: List[Objet]) -> Optional[int]:
    """
    Calcule le niveau moyen des ingrédients utilisés pour une recette.

    :param ingredients: Liste des objets ingrédients
    :return: Niveau moyen ou None si aucun ingrédient n'a de niveau
    """
    niveaux = [ing.niveau_biome for ing in ingredients if ing.niveau_biome is not None]

    if not niveaux:
        return None

    return int(sum(niveaux) / len(niveaux))


def calculer_effet_avec_bonus(effet_base: float, niveau_biome: Optional[int]) -> float:
    """
    Calcule l'effet final d'un objet crafté avec bonus de niveau.

    :param effet_base: Effet de base de la recette
    :param niveau_biome: Niveau moyen du biome d'origine des ingrédients
    :return: Effet final avec bonus
    """
    if niveau_biome is None or niveau_biome <= 0:
        return effet_base

    bonus = calculer_bonus_niveau(niveau_biome)
    return effet_base * bonus


def calculer_stats_avec_bonus(stats_base: Dict, niveau_biome: Optional[int]) -> Dict:
    """
    Calcule les stats finales d'une arme/armure craftée avec bonus de niveau.

    :param stats_base: Dictionnaire des stats de base de la recette
    :param niveau_biome: Niveau moyen du biome d'origine des ingrédients
    :return: Dictionnaire des stats avec bonus
    """
    if niveau_biome is None or niveau_biome <= 0:
        return stats_base.copy()

    bonus = calculer_bonus_niveau(niveau_biome)
    stats_finales = {}

    for key, value in stats_base.items():
        if value is not None and isinstance(value, (int, float)):
            stats_finales[key] = value * bonus
        else:
            stats_finales[key] = value

    return stats_finales


def obtenir_ingredients_par_categorie_avec_niveau(joueur, categorie: str, royaume: str) -> List[Objet]:
    """
    Retourne tous les ingrédients du joueur correspondant à une catégorie générique,
    avec leur niveau de biome.

    :param joueur: Le personnage joueur
    :param categorie: Catégorie générique (ex: "Ingrédient Potion Niveau 1-5")
    :param royaume: Nom du royaume
    :return: Liste des objets ingrédients correspondants
    """
    from data.categories_ingredients import obtenir_ingredients_par_categorie
    from data.ingredients import extraire_nom_base_ingredient

    # Obtenir les noms d'ingrédients réels pour cette catégorie
    noms_ingredients = obtenir_ingredients_par_categorie(categorie, royaume)

    # Chercher dans l'inventaire du joueur
    ingredients_trouves = []

    for nom_objet, objet in joueur.inventaire.items():
        nom_base = extraire_nom_base_ingredient(nom_objet)
        if nom_base in noms_ingredients:
            ingredients_trouves.append(objet)

    return ingredients_trouves
