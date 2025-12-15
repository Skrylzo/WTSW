# menus/teleportation.py
# Système de téléportation entre royaumes

from typing import List

from world import (
    obtenir_royaume_du_joueur, obtenir_royaume_par_nom,
    HubCapital
)
from .exploration import creer_systeme_chapitres_base


def parser_royaumes_depuis_teleportations(teleportations: List[str], royaume_actuel: str = None) -> List[str]:
    """
    Parse les strings de téléportation pour extraire les noms de royaumes disponibles.
    Si aucune description spécifique n'est trouvée, retourne tous les autres royaumes.

    :param teleportations: Liste de strings descriptives (ex: "Portails vers Khazak-Dûm, Luthesia")
    :param royaume_actuel: Nom du royaume actuel (sera exclu de la liste)
    :return: Liste des noms de royaumes disponibles
    """
    royaumes_disponibles = []
    tous_royaumes = ["Aerthos", "Khazak-Dûm", "Luthesia", "Vrak'thar"]

    for teleportation_desc in teleportations:
        # Chercher les noms de royaumes dans la description
        for royaume in tous_royaumes:
            # Vérifier si le nom du royaume apparaît dans la description
            if royaume.lower() in teleportation_desc.lower():
                if royaume not in royaumes_disponibles:
                    royaumes_disponibles.append(royaume)

    # Si aucune description spécifique n'a été trouvée mais qu'il y a des descriptions
    # qui mentionnent "capitales", "royaumes", "alliances", etc., inclure tous les autres royaumes
    if not royaumes_disponibles and teleportations:
        descriptions_lower = [desc.lower() for desc in teleportations]
        mots_cles = ["capitale", "royaume", "alliance", "ennemi", "fissure", "portail", "miroir"]

        # Si une description contient un mot-clé suggérant des téléportations vers d'autres royaumes
        if any(mot in " ".join(descriptions_lower) for mot in mots_cles):
            # Retourner tous les autres royaumes (sauf le royaume actuel)
            royaumes_disponibles = [r for r in tous_royaumes if r != royaume_actuel]

    return royaumes_disponibles


def teleporter_vers_royaume(joueur, nom_royaume: str) -> bool:
    """
    Téléporte le joueur vers un autre royaume.
    :param joueur: Instance du personnage joueur
    :param nom_royaume: Nom du royaume de destination
    :return: True si téléportation réussie, False sinon
    """
    # Obtenir le royaume de destination
    royaume_dest = obtenir_royaume_par_nom(nom_royaume)
    if not royaume_dest:
        print(f"❌ Impossible de trouver le royaume '{nom_royaume}'.")
        return False

    # Vérifier que le royaume a une capitale
    if not royaume_dest.hub_capital:
        print(f"❌ Le royaume '{nom_royaume}' n'a pas de capitale définie.")
        return False

    # Obtenir le royaume actuel du joueur
    # Si le joueur a un royaume_actuel (après téléportation), l'utiliser
    # Sinon, utiliser le royaume de sa race
    if hasattr(joueur, 'royaume_actuel') and joueur.royaume_actuel:
        nom_royaume_actuel = joueur.royaume_actuel
    else:
        royaume_actuel = obtenir_royaume_du_joueur(joueur.race)
        nom_royaume_actuel = royaume_actuel.nom if royaume_actuel else None

    # Vérifier si le joueur est déjà dans ce royaume
    if nom_royaume_actuel == nom_royaume:
        print(f"❌ Vous êtes déjà dans le royaume '{nom_royaume}'.")
        return False

    # Téléporter le joueur
    joueur.royaume_actuel = nom_royaume

    # Afficher le message de téléportation
    hub_dest = royaume_dest.hub_capital
    print(f"\n{'='*60}")
    print("✨ TÉLÉPORTATION ✨")
    print(f"{'='*60}")
    print(f"\nVous avez été téléporté vers {hub_dest.nom}, capitale de {nom_royaume}.")
    print(f"{hub_dest.description}\n")

    # Déclencher automatiquement les quêtes de royaume disponibles
    if hasattr(joueur, 'systeme_quetes'):
        from world.declenchement_quetes import verifier_et_declencher_quetes_royaume
        verifier_et_declencher_quetes_royaume(joueur, nom_royaume)

    return True


def menu_teleportation(joueur, hub: HubCapital):
    """
    Menu de téléportation vers d'autres royaumes.
    La téléportation n'est disponible qu'après avoir complété son propre royaume.
    """
    # Import différé pour éviter les dépendances circulaires
    from .capitale import royaume_est_complete

    if not hub.teleportations:
        print("\nAucune téléportation disponible pour le moment.")
        return

    # Obtenir le royaume actuel du joueur
    # Si le joueur a un royaume_actuel (après téléportation), l'utiliser
    # Sinon, utiliser le royaume de sa race
    if hasattr(joueur, 'royaume_actuel') and joueur.royaume_actuel:
        nom_royaume_actuel = joueur.royaume_actuel
    else:
        royaume_actuel = obtenir_royaume_du_joueur(joueur.race)
        nom_royaume_actuel = royaume_actuel.nom if royaume_actuel else None

    # Parser les royaumes disponibles depuis les descriptions
    royaumes_disponibles = parser_royaumes_depuis_teleportations(hub.teleportations, nom_royaume_actuel)

    if not royaumes_disponibles:
        print("\nAucun royaume disponible pour la téléportation.")
        return

    print(f"\n{'='*60}")
    print("--- TÉLÉPORTATION ---")
    print(f"{'='*60}")
    print(f"\nDepuis {hub.nom}, vous pouvez vous téléporter vers :\n")

    # Afficher les royaumes disponibles
    royaumes_affiches = []
    for i, royaume_nom in enumerate(royaumes_disponibles, 1):
        # Ne pas afficher le royaume actuel
        if royaume_nom == nom_royaume_actuel:
            continue

        royaume = obtenir_royaume_par_nom(royaume_nom)
        if royaume and royaume.hub_capital:
            hub_dest = royaume.hub_capital
            print(f"{len(royaumes_affiches) + 1}. {hub_dest.nom} ({royaume_nom})")
            royaumes_affiches.append(royaume_nom)

    if not royaumes_affiches:
        print("Aucun autre royaume disponible pour la téléportation.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"{len(royaumes_affiches) + 1}. ⬅️  Retour (r)")

    try:
        choix_input = input(f"\nVotre choix : ").strip().lower()
        if choix_input == 'r':
            return
        choix = int(choix_input)
        if 1 <= choix <= len(royaumes_affiches):
            royaume_choisi = royaumes_affiches[choix - 1]

            # Demander confirmation
            print(f"\nTéléporter vers {royaume_choisi} ?")
            confirmation = input("Confirmer (o/n) : ").strip().lower()

            if confirmation == 'o':
                if teleporter_vers_royaume(joueur, royaume_choisi):
                    input("\nAppuyez sur Entrée pour continuer...")
                    # Retourner au menu de capitale du nouveau royaume
                    # Import différé pour éviter les dépendances circulaires
                    from .capitale import menu_capitale
                    menu_capitale(joueur)
                    return
                else:
                    input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("Téléportation annulée.")
        elif choix == len(royaumes_affiches) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except KeyboardInterrupt:
        print("\n\nRetour au menu précédent...")
        return
