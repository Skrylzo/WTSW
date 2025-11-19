# combat/__init__.py
# Exporte toutes les fonctions de combat pour faciliter les imports

from .calculs import calculer_degats_finaux, esquive, creer_barre_vie
from .selection import choisir_cible, choisir_capacite
from .deroulement import debut_combat, tour_joueur, tour_ennemis, resoudre_effets_fin_tour, deroulement_combat

__all__ = [
    'calculer_degats_finaux',
    'esquive',
    'creer_barre_vie',
    'choisir_cible',
    'choisir_capacite',
    'debut_combat',
    'tour_joueur',
    'tour_ennemis',
    'resoudre_effets_fin_tour',
    'deroulement_combat'
]
