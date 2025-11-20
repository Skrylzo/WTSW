# combat/__init__.py
# Exporte toutes les fonctions de combat pour faciliter les imports

from .calculs import calculer_degats_finaux, esquive, creer_barre_vie
from .selection import choisir_cible, choisir_capacite
from .deroulement import debut_combat, tour_joueur, tour_ennemis, resoudre_effets_fin_tour, deroulement_combat
from .actions import executer_attaque, executer_capacite, determiner_cibles_capacite, obtenir_etat_combat
from .affichage import (
    afficher_tour_joueur, afficher_menu_actions, afficher_resultat_attaque,
    afficher_resultat_capacite, afficher_message_erreur,
    afficher_tour_ennemis, afficher_attaque_ennemi, afficher_fin_combat
)

__all__ = [
    # Calculs
    'calculer_degats_finaux',
    'esquive',
    'creer_barre_vie',
    # Sélection (UI solo)
    'choisir_cible',
    'choisir_capacite',
    # Déroulement
    'debut_combat',
    'tour_joueur',
    'tour_ennemis',
    'resoudre_effets_fin_tour',
    'deroulement_combat',
    # Actions pures (pour multijoueur)
    'executer_attaque',
    'executer_capacite',
    'determiner_cibles_capacite',
    'obtenir_etat_combat',
    # Affichage (séparé de la logique)
    'afficher_tour_joueur',
    'afficher_menu_actions',
    'afficher_resultat_attaque',
    'afficher_resultat_capacite',
    'afficher_message_erreur',
    'afficher_tour_ennemis',
    'afficher_attaque_ennemi',
    'afficher_fin_combat',
]
