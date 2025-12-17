# menus/capitale.py
# Menu principal de la capitale et navigation entre les services

from typing import List

from world import (
    obtenir_capitale_joueur, obtenir_royaume_du_joueur,
    FeatureType, HubFeature, HubCapital
)
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS, COULEUR_OR
from .craft import menu_craft
from .exploration import creer_systeme_chapitres_base
from .monnaie import afficher_or, retirer_or
from .commerce import menu_commerce
from .quetes import menu_quetes
from .teleportation import menu_teleportation
from .formation import menu_formation
from .pnj import menu_pnj_capitale


def royaume_est_complete(joueur) -> bool:
    """
    Vérifie si le royaume du joueur est complété.
    Un royaume est complété si tous ses chapitres sont complétés.

    Pour l'instant, utilise un attribut du joueur pour suivre la complétion.
    Cet attribut peut être défini manuellement ou via le système de chapitres.

    :param joueur: Instance du personnage joueur
    :return: True si le royaume est complété, False sinon
    """
    # Vérifier si le joueur a un attribut indiquant que le royaume est complété
    if hasattr(joueur, 'royaume_complete'):
        return joueur.royaume_complete

    # Sinon, créer le système de chapitres pour vérifier l'état
    # Note: Pour un système complet, le système de chapitres devrait être stocké dans le joueur
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        return False

    # Créer le système de chapitres pour vérifier l'état
    systeme_chapitres = creer_systeme_chapitres_base(joueur, royaume_joueur)

    # Vérifier si le royaume est complété
    est_complete = systeme_chapitres.royaume_est_complete()

    # Stocker le résultat dans le joueur pour éviter de recalculer à chaque fois
    joueur.royaume_complete = est_complete

    return est_complete


def menu_capitale(joueur):
    """
    Menu principal de la capitale du joueur.
    Point d'entrée pour accéder aux services de la capitale.
    """
    hub = obtenir_capitale_joueur(joueur)
    if not hub:
        print("Erreur : Impossible de trouver votre capitale.")
        return

    # Sauvegarde automatique lors de l'entrée dans la capitale
    from .sauvegarde import sauvegarder_automatique
    sauvegarder_automatique(joueur)

    # Ne plus déclencher automatiquement les quêtes de royaume
    # Elles seront données par les mentors quand le joueur leur parle

    while True:
        effacer_console()
        afficher_titre_menu_avec_emoji(f"{hub.nom.upper()}", "capitale")
        print(f"{COULEURS['CYAN']}Capitale de {hub.royaume_nom}{COULEURS['RESET']}")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print(f"\n{hub.description}\n")

        # Obtenir les services disponibles
        services = hub.lister_services()

        options = []
        options_display = []
        option_num = 1

        # Commerce
        # services est un dict avec des clés string, utiliser .value pour obtenir la clé
        if FeatureType.COMMERCE.value in services and services[FeatureType.COMMERCE.value]:
            options_display.append(f"{option_num}. 💰 Commerce")
            options.append(('commerce', FeatureType.COMMERCE))
            option_num += 1

        # Craft
        if FeatureType.CRAFT.value in services and services[FeatureType.CRAFT.value]:
            options_display.append(f"{option_num}. 🔨 Atelier de Craft")
            options.append(('craft', FeatureType.CRAFT))
            option_num += 1

        # Quêtes
        if FeatureType.QUETE.value in services and services[FeatureType.QUETE.value]:
            options_display.append(f"{option_num}. 📜 Quêtes")
            options.append(('quetes', FeatureType.QUETE))
            option_num += 1

        # Téléportation (uniquement si le royaume est complété)
        if hub.teleportations and royaume_est_complete(joueur):
            options_display.append(f"{option_num}. 🌀 Téléportation")
            options.append(('teleportation', None))
            option_num += 1

        # Formation (toujours disponible dans toutes les capitales)
        options_display.append(f"{option_num}. 📚 Formation")
        options.append(('formation', FeatureType.FORMATION))
        option_num += 1

        # Parler aux PNJ (toujours disponible dans la capitale)
        options_display.append(f"{option_num}. 👥 Parler aux habitants")
        options.append(('pnj', None))
        option_num += 1

        # Soin pour 100 or (toujours disponible)
        options_display.append(f"{option_num}. 💊 Se soigner (100 or)")
        options.append(('soin', None))
        option_num += 1

        # Note : "Services disponibles" retiré car redondant avec les options ci-dessus
        # Tous les services sont déjà listés directement dans le menu

        options_display.append(f"{option_num}. ⬅️  Retour (r)")
        options.append(('retour', None))

        # Afficher les options
        for option_text in options_display:
            print(option_text)
            print()

        choix = input(f"\n{COULEURS['MAGENTA']}Votre choix : {COULEURS['RESET']}").strip().lower()

        try:
            if choix == 'r':
                break
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                option_type, feature_type = options[choix_int - 1]

                if option_type == 'commerce':
                    menu_commerce(joueur, hub, services[FeatureType.COMMERCE.value])
                elif option_type == 'craft':
                    menu_craft(joueur, hub, services[FeatureType.CRAFT.value])
                elif option_type == 'quetes':
                    # Initialiser le systeme de quetes si necessaire
                    if not hasattr(joueur, 'systeme_quetes'):
                        from .quetes import initialiser_systeme_quetes
                        joueur.systeme_quetes = initialiser_systeme_quetes()
                    menu_quetes(joueur, hub, services[FeatureType.QUETE.value], joueur.systeme_quetes)
                elif option_type == 'teleportation':
                    menu_teleportation(joueur, hub)
                elif option_type == 'formation':
                    # Formation toujours disponible, utiliser une liste vide si pas dans les services
                    features_formation = services.get(FeatureType.FORMATION.value, [])
                    menu_formation(joueur, hub, features_formation)
                elif option_type == 'pnj':
                    menu_pnj_capitale(joueur)
                elif option_type == 'soin':
                    cout = 100
                    if getattr(joueur, "or_", 0) < cout:
                        print(f"\n{COULEURS['ROUGE']}❌ Vous n'avez pas assez d'or. Il vous manque {COULEUR_OR}{cout - joueur.or_} pièces{COULEURS['RESET']}.")
                    else:
                        retirer_or(joueur, cout)
                        joueur.vie = joueur.vie_max
                        # Si le joueur a du mana/energie/rage, on peut aussi les reinitialiser
                        if hasattr(joueur, 'mana_max'):
                            joueur.mana = getattr(joueur, 'mana_max', joueur.mana)
                        if hasattr(joueur, 'energie_max'):
                            joueur.energie = getattr(joueur, 'energie_max', joueur.energie)
                        if hasattr(joueur, 'rage_max'):
                            joueur.rage = 0
                        print(f"\n{COULEURS['VERT']}💚 Vous êtes entièrement soigné pour {COULEUR_OR}{cout} or{COULEURS['RESET']}.")
                    input("\nAppuyez sur Entrée pour continuer...")
                elif option_type == 'retour':
                    break
            else:
                print("Choix invalide. Veuillez reessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def afficher_services_capitale(hub: HubCapital):
    """Affiche tous les services disponibles dans la capitale."""
    print()
    afficher_titre_menu_avec_emoji(f"SERVICES DE {hub.nom.upper()}", "capitale")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    services = hub.lister_services()
    for type_service, liste_features in services.items():
        if liste_features:
            # type_service est déjà une string (la valeur de l'enum), pas besoin de .value
            print(f"\n{type_service.upper()} :")
            for nom_feature in liste_features:
                # liste_features contient des noms de features (strings), pas des objets HubFeature
                print(f"  • {nom_feature}")
                # Pour obtenir la description, chercher la feature correspondante
                feature = None
                for f in hub.features:
                    if f.nom == nom_feature:
                        feature = f
                        break
                if feature and feature.description:
                    print(f"    {feature.description}")

    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()
