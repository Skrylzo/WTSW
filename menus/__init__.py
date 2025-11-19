# menus/__init__.py
# Exporte toutes les fonctions de menus pour faciliter les imports

from .sauvegarde import sauvegarder_jeu, charger_jeu
from .creation import creer_personnage, choisir_arme_depart
from .principal import menu_principal, menu_personnage, allouer_points_attributs
from .inventaire import menu_inventaire, afficher_inventaire_complet, afficher_inventaire_par_type, consulter_objet, jeter_objet
from .capitale import (
    menu_capitale,
    obtenir_or_joueur,
    ajouter_or,
    retirer_or,
    afficher_or,
)
from .exploration import menu_exploration_valdoria

__all__ = [
    'sauvegarder_jeu',
    'charger_jeu',
    'creer_personnage',
    'choisir_arme_depart',
    'menu_principal',
    'menu_personnage',
    'allouer_points_attributs',
    'menu_inventaire',
    'afficher_inventaire_complet',
    'afficher_inventaire_par_type',
    'consulter_objet',
    'jeter_objet',
    'menu_capitale',
    'obtenir_or_joueur',
    'ajouter_or',
    'retirer_or',
    'afficher_or',
    'menu_exploration_valdoria',
]
