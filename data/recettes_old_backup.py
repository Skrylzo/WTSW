# data/recettes.py
# Fichier principal qui importe et regroupe toutes les recettes
# Les recettes sont maintenant séparées en plusieurs fichiers pour une meilleure organisation

from typing import Dict, List, Optional

# Importer toutes les recettes depuis les fichiers séparés
from .recettes_potions import (
    RECETTES_POTIONS_SOIN,
    RECETTES_POTIONS_MANA,
    RECETTES_POTIONS_ENERGIE,
    RECETTES_POTIONS_BOOST_FORCE,
    RECETTES_POTIONS_BOOST_DEFENSE,
    RECETTES_POTIONS_BOOST_VITESSE,
    RECETTES_POTIONS_BOOST_CRITIQUE,
)

# TODO: Importer les autres fichiers une fois créés
# from .recettes_armes import (
#     RECETTES_ARMES_EPEES,
#     RECETTES_ARMES_HACHES,
#     RECETTES_ARMES_DAGUES,
#     RECETTES_ARMES_BATONS,
# )
# from .recettes_armures_torse import RECETTES_ARMURES_TORSE
# from .recettes_armures_casques import RECETTES_ARMURES_CASQUES
# from .recettes_armures_bottes import RECETTES_ARMURES_BOTTES

# Pour l'instant, utiliser les anciennes recettes (sera remplacé progressivement)
# Import temporaire depuis l'ancien fichier
import importlib.util
import os

# Charger temporairement les recettes d'armes et armures depuis l'ancien fichier
# Cela sera remplacé une fois que les nouveaux fichiers seront créés
_old_recettes_path = os.path.join(os.path.dirname(__file__), "recettes_old.py")
if os.path.exists(_old_recettes_path):
    spec = importlib.util.spec_from_file_location("recettes_old", _old_recettes_path)
    recettes_old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(recettes_old)
    
    RECETTES_ARMES_EPEES = getattr(recettes_old, "RECETTES_ARMES_EPEES", {})
    RECETTES_ARMES_HACHES = getattr(recettes_old, "RECETTES_ARMES_HACHES", {})
    RECETTES_ARMES_DAGUES = getattr(recettes_old, "RECETTES_ARMES_DAGUES", {})
    RECETTES_ARMES_BATONS = getattr(recettes_old, "RECETTES_ARMES_BATONS", {})
    RECETTES_ARMURES_TORSE = getattr(recettes_old, "RECETTES_ARMURES_TORSE", {})
    RECETTES_ARMURES_CASQUES = getattr(recettes_old, "RECETTES_ARMURES_CASQUES", {})
    RECETTES_ARMURES_BOTTES = getattr(recettes_old, "RECETTES_ARMURES_BOTTES", {})
else:
    # Si le fichier old n'existe pas, créer des dictionnaires vides temporaires
    RECETTES_ARMES_EPEES = {}
    RECETTES_ARMES_HACHES = {}
    RECETTES_ARMES_DAGUES = {}
    RECETTES_ARMES_BATONS = {}
    RECETTES_ARMURES_TORSE = {}
    RECETTES_ARMURES_CASQUES = {}
    RECETTES_ARMURES_BOTTES = {}

# ============================================================================
# REGROUPEMENT DE TOUTES LES RECETTES
# ============================================================================

TOUTES_LES_RECETTES: Dict[str, Dict] = {}

# Ajouter toutes les recettes de potions
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_SOIN)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_MANA)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_ENERGIE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_FORCE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_DEFENSE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_VITESSE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_CRITIQUE)

# Ajouter toutes les recettes d'armes (temporaire depuis l'ancien fichier)
TOUTES_LES_RECETTES.update(RECETTES_ARMES_EPEES)
TOUTES_LES_RECETTES.update(RECETTES_ARMES_HACHES)
TOUTES_LES_RECETTES.update(RECETTES_ARMES_DAGUES)
TOUTES_LES_RECETTES.update(RECETTES_ARMES_BATONS)

# Ajouter toutes les recettes d'armures (temporaire depuis l'ancien fichier)
TOUTES_LES_RECETTES.update(RECETTES_ARMURES_TORSE)
TOUTES_LES_RECETTES.update(RECETTES_ARMURES_CASQUES)
TOUTES_LES_RECETTES.update(RECETTES_ARMURES_BOTTES)

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def obtenir_recette(id_recette: str) -> Optional[Dict]:
    """
    Obtient une recette par son ID.

    :param id_recette: ID de la recette
    :return: Dictionnaire de la recette ou None si non trouvée
    """
    return TOUTES_LES_RECETTES.get(id_recette)


def obtenir_recettes_par_type(type_recette: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'un type donné.

    :param type_recette: Type de recette ("potion", "arme", "armure")
    :return: Liste des recettes du type demandé
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("type") == type_recette
    ]


def obtenir_recettes_par_sous_type(sous_type: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'un sous-type donné.

    :param sous_type: Sous-type de recette (ex: "soin", "mana", "epee", "torse")
    :return: Liste des recettes du sous-type demandé
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("sous_type") == sous_type
    ]


def obtenir_recettes_par_rarete(rarete: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'une rareté donnée.

    :param rarete: Rareté ("Commun", "Peu Commun", "Rare", "Épique", "Légendaire")
    :return: Liste des recettes de la rareté demandée
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("rarete") == rarete
    ]


def obtenir_recettes_disponibles(niveau_craft: int = 1) -> List[Dict]:
    """
    Obtient toutes les recettes disponibles pour un niveau de craft donné.

    :param niveau_craft: Niveau de craft du joueur
    :return: Liste des recettes accessibles
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("niveau_craft_requis", 1) <= niveau_craft
    ]
