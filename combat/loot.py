# combat/loot.py
# Système de loot des ingrédients après combat

import random
from typing import List, Dict, Optional
from classes.objet import Objet
from data.ingredients import (
    obtenir_ingredients_par_mob,
    obtenir_nom_complet_avec_qualite,
    DISTRIBUTION_RARETE,
    RARETES
)


def determiner_qualite_ingredient() -> str:
    """
    Détermine la qualité d'un ingrédient selon la distribution de rareté.

    :return: Qualité de l'ingrédient (Commun, Peu Commun, Rare, Épique, Légendaire)
    """
    roll = random.random()  # Nombre entre 0.0 et 1.0

    cumul = 0.0
    for qualite in RARETES:
        cumul += DISTRIBUTION_RARETE[qualite]
        if roll <= cumul:
            return qualite

    # Fallback (ne devrait jamais arriver)
    return RARETES[0]


def generer_loot_ingredients(nom_mob: str) -> List[Objet]:
    """
    Génère le loot d'ingrédients pour un mob spécifique.
    Chaque mob drop exactement 1 ingrédient choisi aléatoirement parmi les 3 possibles
    (1 Potion, 1 Arme, 1 Armure), avec une qualité déterminée aléatoirement selon la distribution.

    :param nom_mob: Nom du mob qui drop les ingrédients
    :return: Liste contenant 1 objet Objet représentant l'ingrédient obtenu (ou liste vide)
    """
    # Récupérer les ingrédients associés à ce mob
    ingredients_data = obtenir_ingredients_par_mob(nom_mob)

    if not ingredients_data:
        # Si le mob n'a pas d'ingrédients définis, retourner une liste vide
        return []

    # Choisir aléatoirement 1 ingrédient parmi les 3 possibles
    ing_data = random.choice(ingredients_data)

    nom_base = ing_data['nom']
    usage = ing_data['usage']

    # Déterminer la qualité de cet ingrédient
    qualite = determiner_qualite_ingredient()

    # Créer le nom complet avec qualité
    nom_complet = obtenir_nom_complet_avec_qualite(nom_base, qualite)

    # Créer l'objet ingrédient
    objet_ingredient = Objet(
        nom=nom_complet,
        type_objet="matériau",
        quantite=1,
        description=f"Ingrédient pour {usage.lower()} ({qualite})",
        rarete=qualite.lower()
    )

    return [objet_ingredient]


def ajouter_ingredients_a_inventaire(joueur, nom_mob: str) -> List[Objet]:
    """
    Génère et ajoute les ingrédients d'un mob à l'inventaire du joueur.

    :param joueur: Le personnage joueur
    :param nom_mob: Nom du mob qui drop les ingrédients
    :return: Liste des objets ingrédients ajoutés
    """
    ingredients = generer_loot_ingredients(nom_mob)

    for ingredient in ingredients:
        joueur.ajouter_objet(ingredient)

    return ingredients
