# menus/__init__.py
# Exporte toutes les fonctions de menus pour faciliter les imports

from .sauvegarde import sauvegarder_jeu, charger_jeu
from .creation import creer_personnage, choisir_arme_depart
from .principal import menu_principal, menu_personnage, allouer_points_attributs
from .inventaire import menu_inventaire, afficher_inventaire_complet, afficher_inventaire_par_type, consulter_objet, jeter_objet

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
    'jeter_objet'
]
