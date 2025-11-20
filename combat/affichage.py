# combat/affichage.py
# Fonctions d'affichage pour le combat (séparation UI/logique)
# Ces fonctions peuvent être remplacées par des messages réseau pour le multijoueur

from typing import Dict, Any, List
from classes.base_combatant import Personnage, Ennemi
from classes.capacite import Capacite
from .calculs import creer_barre_vie


def afficher_tour_joueur(joueur: Personnage, ennemis: List[Ennemi]) -> None:
    """
    Affiche les informations du tour du joueur.

    :param joueur: Le joueur
    :param ennemis: Liste des ennemis
    """
    resource_display = ""
    if joueur.specialisation.type_ressource == "Mana":
        resource_display = f"Mana: {joueur.mana:.1f}/{joueur.mana_max:.1f}"
    elif joueur.specialisation.type_ressource == "Energie":
        resource_display = f"Énergie: {joueur.energie:.1f}/{joueur.energie_max:.1f}"
    elif joueur.specialisation.type_ressource == "Rage":
        resource_display = f"Rage: {joueur.rage:.1f}/{joueur.rage_max:.1f}"

    barre_vie_joueur = creer_barre_vie(joueur.vie, joueur.vie_max)
    print(f"\n--- TOUR DE {joueur.nom} ---")
    print(f"Vie: {barre_vie_joueur} {joueur.vie:.1f}/{joueur.vie_max:.1f} | {resource_display}")

    ennemis_vivants = [e for e in ennemis if e.est_vivant]
    if ennemis_vivants:
        print("\nEnnemis actuels :")
        for i, ennemi in enumerate(ennemis_vivants):
            barre_vie_ennemi = creer_barre_vie(ennemi.vie, ennemi.vie_max)
            print(f"{i+1}. {ennemi.nom} - Vie: {barre_vie_ennemi} {ennemi.vie:.1f}/{ennemi.vie_max:.1f}")


def afficher_menu_actions() -> None:
    """Affiche le menu des actions disponibles."""
    print("\nChoisissez votre action :")
    print("1. Attaquer")
    print("2. Utiliser une Capacité")
    print("3. Afficher les Stats")
    print("4. Afficher les Capacités")


def afficher_resultat_attaque(resultat: Dict[str, Any]) -> None:
    """
    Affiche le résultat d'une attaque.

    :param resultat: Résultat retourné par executer_attaque()
    """
    if resultat["type"] == "esquive":
        print(f"  {resultat['cible'].nom} a esquivé votre attaque !")
    elif resultat["type"] == "degats":
        if resultat.get("critique", False):
            print("  Coup critique !")
        print(f"  {resultat['attaquant'].nom} inflige {resultat['degats']:.1f} points de dégâts à {resultat['cible'].nom}.")


def afficher_resultat_capacite(resultat: Dict[str, Any]) -> None:
    """
    Affiche le résultat d'une capacité.

    :param resultat: Résultat retourné par executer_capacite()
    """
    if not resultat["success"]:
        if "message" in resultat:
            print(f"  {resultat['message']}")
        else:
            print(f"  Impossible d'utiliser {resultat['capacite'].nom}")
    # Note: L'affichage détaillé des capacités est géré par la méthode utiliser() de Capacite


def afficher_message_erreur(message: str) -> None:
    """
    Affiche un message d'erreur.

    :param message: Message à afficher
    """
    print(message)


def afficher_tour_ennemis(joueur: Personnage, ennemi: Ennemi) -> None:
    """
    Affiche le début du tour d'un ennemi.

    :param joueur: Le joueur
    :param ennemi: L'ennemi qui attaque
    """
    print(f"{ennemi.nom} attaque {joueur.nom}!")


def afficher_attaque_ennemi(ennemi: Ennemi, joueur: Personnage, degats: float, critique: bool = False, esquive: bool = False) -> None:
    """
    Affiche le résultat d'une attaque d'ennemi.

    :param ennemi: L'ennemi qui attaque
    :param joueur: Le joueur qui reçoit
    :param degats: Dégâts infligés
    :param critique: Si c'est un coup critique
    :param esquive: Si le joueur a esquivé
    """
    if esquive:
        print(f"  Vous avez esquivé l'attaque de {ennemi.nom} !")
    else:
        if critique:
            print("  Coup critique !")
        print(f"  {ennemi.nom} inflige {degats:.1f} points de dégâts à {joueur.nom}.")


def afficher_fin_combat(joueur: Personnage, victoire: bool) -> None:
    """
    Affiche la fin du combat.

    :param joueur: Le joueur
    :param victoire: True si le joueur a gagné
    """
    print("-" * 30)
    print("\n--- FIN DU COMBAT ---")
    if victoire:
        print(f"{joueur.nom} est victorieux !")
    else:
        print(f"{joueur.nom} a été vaincu...")
