# combat/actions.py
# Fonctions pures pour les actions de combat (logique métier sans input/print)
# Ces fonctions peuvent être réutilisées côté serveur pour le multijoueur

import random
from typing import Dict, Optional, List, Any
from classes.base_combatant import Personnage, Ennemi
from classes.capacite import Capacite
from .calculs import calculer_degats_finaux, esquive


def executer_attaque(attaquant: Personnage, cible: Ennemi) -> Dict[str, Any]:
    """
    Exécute une attaque de base (logique pure, pas d'affichage).

    :param attaquant: Le personnage qui attaque
    :param cible: L'ennemi ciblé
    :return: Dictionnaire avec les résultats de l'attaque
        {
            "type": "esquive" | "degats",
            "cible": Ennemi,
            "degats"?: float,  # Si type == "degats"
            "critique"?: bool,  # Si type == "degats"
            "vie_avant"?: float,  # Si type == "degats"
            "vie_apres"?: float   # Si type == "degats"
        }
    """
    # Calculer les dégâts bruts
    degats_bruts = attaquant.attaquer(cible)

    # Vérifier l'esquive
    if esquive(attaquant.vitesse, cible.vitesse):
        return {
            "type": "esquive",
            "cible": cible,
            "attaquant": attaquant
        }

    # Vérifier le critique
    critique = False
    if random.randint(1, 100) <= attaquant.calculer_chance_critique_totale():
        degats_bruts *= 1.5
        critique = True

    # Calculer les dégâts finaux
    degats_finaux = calculer_degats_finaux(attaquant, cible, degats_bruts, est_capacite=False)

    # Appliquer les dégâts
    vie_avant = cible.vie
    cible.prendre_degats(degats_finaux)
    vie_apres = cible.vie

    return {
        "type": "degats",
        "cible": cible,
        "attaquant": attaquant,
        "degats": degats_finaux,
        "critique": critique,
        "vie_avant": vie_avant,
        "vie_apres": vie_apres
    }


def determiner_cibles_capacite(capacite: Capacite, joueur: Personnage, ennemis_vivants: List[Ennemi]) -> Optional[List[Any]]:
    """
    Détermine les cibles d'une capacité selon son type (logique pure).

    :param capacite: La capacité à utiliser
    :param joueur: Le joueur qui utilise la capacité
    :param ennemis_vivants: Liste des ennemis vivants
    :return: Liste des cibles ou None si impossible
    """
    if capacite.type_cible == "ennemi" or capacite.type_cible == "unique":
        # Nécessite une cible ennemie (sera choisie par l'UI)
        if not ennemis_vivants:
            return None
        # Retourne None car la cible doit être choisie par l'utilisateur
        return None
    elif capacite.type_cible == "aoe":
        return ennemis_vivants
    elif capacite.type_cible == "soi":
        return [joueur]
    elif capacite.type_cible == "aoe_amis":
        return [joueur]
    elif capacite.type_cible == "aoe_mixte":
        return [joueur] + ennemis_vivants
    else:
        return None


def executer_capacite(joueur: Personnage, capacite: Capacite, cibles: List[Any]) -> Dict[str, Any]:
    """
    Exécute une capacité (logique pure, pas d'affichage).

    :param joueur: Le joueur qui utilise la capacité
    :param capacite: La capacité à utiliser
    :param cibles: Liste des cibles (déterminée par determiner_cibles_capacite)
    :return: Dictionnaire avec les résultats
        {
            "success": bool,
            "joueur": Personnage,
            "capacite": Capacite,
            "cibles": List,
            "message"?: str  # Si success == False
        }
    """
    if cibles is None:
        return {
            "success": False,
            "joueur": joueur,
            "capacite": capacite,
            "cibles": None,
            "message": "Aucune cible disponible"
        }

    # Vérifier les ressources
    if joueur.specialisation.type_ressource == "Mana":
        if joueur.mana < capacite.cout_mana:
            return {
                "success": False,
                "joueur": joueur,
                "capacite": capacite,
                "cibles": cibles,
                "message": f"Pas assez de Mana ({joueur.mana:.1f}/{capacite.cout_mana})"
            }
    elif joueur.specialisation.type_ressource == "Energie":
        if joueur.energie < capacite.cout_energie:
            return {
                "success": False,
                "joueur": joueur,
                "capacite": capacite,
                "cibles": cibles,
                "message": f"Pas assez d'Énergie ({joueur.energie:.1f}/{capacite.cout_energie})"
            }
    elif joueur.specialisation.type_ressource == "Rage":
        if joueur.rage < capacite.cout_rage:
            return {
                "success": False,
                "joueur": joueur,
                "capacite": capacite,
                "cibles": cibles,
                "message": f"Pas assez de Rage ({joueur.rage:.1f}/{capacite.cout_rage})"
            }

    # Utiliser la capacité (la méthode utiliser() gère déjà les dégâts/soins)
    success = capacite.utiliser(joueur, cibles)

    return {
        "success": success,
        "joueur": joueur,
        "capacite": capacite,
        "cibles": cibles
    }


def obtenir_etat_combat(joueur: Personnage, ennemis: List[Ennemi]) -> Dict[str, Any]:
    """
    Obtient l'état actuel du combat (logique pure, pour affichage ou transmission réseau).

    :param joueur: Le joueur
    :param ennemis: Liste des ennemis
    :return: Dictionnaire avec l'état du combat
    """
    ennemis_vivants = [e for e in ennemis if e.est_vivant]

    resource_display = ""
    if joueur.specialisation.type_ressource == "Mana":
        resource_display = f"Mana: {joueur.mana:.1f}/{joueur.mana_max:.1f}"
    elif joueur.specialisation.type_ressource == "Energie":
        resource_display = f"Énergie: {joueur.energie:.1f}/{joueur.energie_max:.1f}"
    elif joueur.specialisation.type_ressource == "Rage":
        resource_display = f"Rage: {joueur.rage:.1f}/{joueur.rage_max:.1f}"

    return {
        "joueur": {
            "nom": joueur.nom,
            "vie": joueur.vie,
            "vie_max": joueur.vie_max,
            "ressource": resource_display,
            "est_vivant": joueur.est_vivant
        },
        "ennemis": [
            {
                "nom": e.nom,
                "vie": e.vie,
                "vie_max": e.vie_max,
                "est_vivant": e.est_vivant
            }
            for e in ennemis
        ],
        "ennemis_vivants": len(ennemis_vivants)
    }
