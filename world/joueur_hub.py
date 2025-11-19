# world/joueur_hub.py
# Fonctions utilitaires pour lier les personnages aux hubs

from typing import Optional

from .hubs import HubCapital
from .royaumes import obtenir_hub_du_joueur, obtenir_royaume_du_joueur


def obtenir_capitale_joueur(joueur) -> Optional[HubCapital]:
    """
    Obtient la capitale (hub) du joueur selon sa race.
    Fonction principale à utiliser dans le code du jeu.

    :param joueur: Instance de Personnage (doit avoir l'attribut 'race')
    :return: HubCapital associé à la race du joueur, ou None si non trouvé
    """
    if not hasattr(joueur, 'race'):
        return None

    return obtenir_hub_du_joueur(joueur.race)


def teleporter_joueur_vers_capitale(joueur) -> bool:
    """
    Téléporte le joueur vers sa capitale (utilisé après défaite).
    Soigne le joueur et affiche le message de respawn.

    :param joueur: Instance de Personnage
    :return: True si téléportation réussie, False sinon
    """
    hub = obtenir_capitale_joueur(joueur)
    if not hub:
        return False

    # Soigner le joueur
    if hasattr(joueur, 'vie_max'):
        joueur.vie = joueur.vie_max
        joueur.est_vivant = True

    # Restaurer les ressources
    if hasattr(joueur, 'mana_max'):
        if joueur.specialisation.type_ressource == "Mana":
            joueur.mana = joueur.mana_max
        elif joueur.specialisation.type_ressource == "Energie":
            joueur.energie = joueur.energie_max
        elif joueur.specialisation.type_ressource == "Rage":
            joueur.rage = 0

    # Afficher le message de respawn
    print(f"\n{'='*60}")
    print(hub.respawn_message)
    print(f"{'='*60}\n")
    print(f"Vous êtes de retour à {hub.nom}, capitale de {hub.royaume_nom}.")
    print(f"Vos blessures ont été soignées et vos ressources restaurées.\n")

    return True


def afficher_services_capitale_joueur(joueur):
    """
    Affiche les services disponibles dans la capitale du joueur.

    :param joueur: Instance de Personnage
    """
    hub = obtenir_capitale_joueur(joueur)
    if not hub:
        print("Erreur : Impossible de trouver votre capitale.")
        return

    print(f"\n{'='*60}")
    print(f"SERVICES DE {hub.nom.upper()}")
    print(f"{'='*60}")

    services = hub.lister_services()
    for type_service, liste_features in services.items():
        if liste_features:
            print(f"\n{type_service.value.upper()} :")
            for feature in liste_features:
                print(f"  • {feature.nom}")
                if feature.description:
                    print(f"    {feature.description}")

    print(f"{'='*60}\n")
