# menus/__init__.py
# Exporte toutes les fonctions de menus pour faciliter les imports

from .sauvegarde import (
    sauvegarder_jeu, charger_jeu, menu_gestion_sauvegardes,
    menu_sauvegarde_manuelle, sauvegarder_automatique
)
from .creation import creer_personnage, choisir_arme_depart
from .principal import menu_principal, menu_personnage, allouer_points_attributs
from .inventaire import menu_inventaire, afficher_inventaire_complet, afficher_inventaire_par_type, consulter_objet, jeter_objet
from .capitale import menu_capitale, afficher_services_capitale, royaume_est_complete
from .monnaie import obtenir_or_joueur, ajouter_or, retirer_or, afficher_or
from .commerce import menu_commerce, calculer_prix_vente
from .quetes import menu_quetes
from .teleportation import menu_teleportation, teleporter_vers_royaume
from .formation import (
    menu_formation,
    obtenir_bonus_formation_classe,
    menu_formation_specialisee,
    calculer_prix_apprentissage_capacite,
    apprendre_capacite,
    ameliorer_capacite
)
from .exploration import menu_exploration_valdoria

__all__ = [
    'sauvegarder_jeu',
    'charger_jeu',
    'menu_gestion_sauvegardes',
    'menu_sauvegarde_manuelle',
    'sauvegarder_automatique',
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
    'afficher_services_capitale',
    'royaume_est_complete',
    'obtenir_or_joueur',
    'ajouter_or',
    'retirer_or',
    'afficher_or',
    'menu_commerce',
    'calculer_prix_vente',
    'menu_quetes',
    'menu_teleportation',
    'teleporter_vers_royaume',
    'menu_formation',
    'obtenir_bonus_formation_classe',
    'menu_formation_specialisee',
    'calculer_prix_apprentissage_capacite',
    'apprendre_capacite',
    'ameliorer_capacite',
    'menu_exploration_valdoria',
]
