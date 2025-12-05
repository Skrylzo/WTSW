# menus/capitale.py
# Menus des capitales (hubs) : commerce, craft, quêtes, téléportation

from typing import Optional, Dict, List

from world import obtenir_capitale_joueur, FeatureType, HubFeature, HubCapital
from classes.objet import Objet
from data.objets import DEFINITIONS_OBJETS
from data.categories_ingredients import INGREDIENTS_SPECIAUX
from .craft import menu_craft


def menu_capitale(joueur):
    """
    Menu principal de la capitale du joueur.
    Point d'entrée pour accéder aux services de la capitale.
    """
    hub = obtenir_capitale_joueur(joueur)
    if not hub:
        print("Erreur : Impossible de trouver votre capitale.")
        return

    while True:
        print(f"\n{'='*60}")
        print(f"--- {hub.nom.upper()} ---")
        print(f"Capitale de {hub.royaume_nom}")
        print(f"{'='*60}")
        print(f"{hub.description}\n")

        # Obtenir les services disponibles
        services = hub.lister_services()

        options = []
        options_display = []
        option_num = 1

        # Commerce
        # services est un dict avec des clés string, utiliser .value pour obtenir la clé
        if FeatureType.COMMERCE.value in services and services[FeatureType.COMMERCE.value]:
            options_display.append(f"{option_num}. Commerce")
            options.append(('commerce', FeatureType.COMMERCE))
            option_num += 1

        # Craft
        if FeatureType.CRAFT.value in services and services[FeatureType.CRAFT.value]:
            options_display.append(f"{option_num}. Atelier de Craft")
            options.append(('craft', FeatureType.CRAFT))
            option_num += 1

        # Quêtes
        if FeatureType.QUETE.value in services and services[FeatureType.QUETE.value]:
            options_display.append(f"{option_num}. Quêtes")
            options.append(('quetes', FeatureType.QUETE))
            option_num += 1

        # Téléportation
        if hub.teleportations:
            options_display.append(f"{option_num}. Téléportation")
            options.append(('teleportation', None))
            option_num += 1

        # Formation (si disponible)
        if FeatureType.FORMATION.value in services and services[FeatureType.FORMATION.value]:
            options_display.append(f"{option_num}. Formation")
            options.append(('formation', FeatureType.FORMATION))
            option_num += 1

        # Note : "Services disponibles" retiré car redondant avec les options ci-dessus
        # Tous les services sont déjà listés directement dans le menu

        options_display.append(f"{option_num}. Retour")
        options.append(('retour', None))

        # Afficher les options
        for option_text in options_display:
            print(option_text)

        choix = input("\nVotre choix : ")

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                option_type, feature_type = options[choix_int - 1]

                if option_type == 'commerce':
                    menu_commerce(joueur, hub, services[FeatureType.COMMERCE.value])
                elif option_type == 'craft':
                    menu_craft(joueur, hub, services[FeatureType.CRAFT.value])
                elif option_type == 'quetes':
                    menu_quetes(joueur, hub, services[FeatureType.QUETE.value])
                elif option_type == 'teleportation':
                    menu_teleportation(joueur, hub)
                elif option_type == 'formation':
                    menu_formation(joueur, hub, services[FeatureType.FORMATION.value])
                elif option_type == 'retour':
                    break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def afficher_services_capitale(hub: HubCapital):
    """Affiche tous les services disponibles dans la capitale."""
    print(f"\n{'='*60}")
    print(f"SERVICES DE {hub.nom.upper()}")
    print(f"{'='*60}")

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

    print(f"{'='*60}\n")


# ============================================================================
# SYSTÈME DE MONNAIE
# ============================================================================

def obtenir_or_joueur(joueur) -> int:
    """Retourne l'or du joueur (ajoute l'attribut si nécessaire)."""
    if not hasattr(joueur, 'or_'):
        joueur.or_ = 100  # Or de départ
    return joueur.or_


def ajouter_or(joueur, montant: int):
    """Ajoute de l'or au joueur."""
    obtenir_or_joueur(joueur)  # S'assurer que l'attribut existe
    joueur.or_ += montant


def retirer_or(joueur, montant: int) -> bool:
    """Retire de l'or du joueur. Retourne True si réussi."""
    or_actuel = obtenir_or_joueur(joueur)
    if or_actuel >= montant:
        joueur.or_ -= montant
        return True
    return False


def afficher_or(joueur):
    """Affiche l'or du joueur."""
    or_actuel = obtenir_or_joueur(joueur)
    print(f"Or : {or_actuel} pièces")


# ============================================================================
# MENU COMMERCE
# ============================================================================

def menu_commerce(joueur, hub: HubCapital, features_commerce: List[HubFeature]):
    """
    Menu de commerce : achat et vente d'objets.
    """
    while True:
        print(f"\n{'='*60}")
        print("--- COMMERCE ---")
        afficher_or(joueur)
        print(f"{'='*60}")
        print("1. Acheter des objets")
        print("2. Vendre des objets")
        print("3. Retour")

        choix = input("\nVotre choix : ")

        if choix == '1':
            menu_achat(joueur, hub, features_commerce)
        elif choix == '2':
            menu_vente(joueur)
        elif choix == '3':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_achat(joueur, hub: HubCapital, features_commerce: List[HubFeature]):
    """
    Menu d'achat d'objets.
    TODO: Intégrer les objets disponibles dans les features de commerce.
    """
    print(f"\n{'='*60}")
    print("--- ACHAT ---")
    afficher_or(joueur)
    print(f"{'='*60}")

    # Liste d'objets de base disponibles à l'achat
    objets_disponibles = {
        "Potion de Vie Mineure": {"prix": 50, "id": "potion_de_vie_mineure"},
        "Potion de Mana Mineure": {"prix": 50, "id": "potion_de_mana_mineure"},
    }

    # Ajouter les ingrédients spéciaux (achetables en boutique)
    for nom_ingredient, data_ingredient in INGREDIENTS_SPECIAUX.items():
        if data_ingredient.get("achetable", False):
            prix = data_ingredient.get("prix_base", 10)
            objets_disponibles[nom_ingredient] = {
                "prix": prix,
                "id": None,  # Pas d'ID dans DEFINITIONS_OBJETS, c'est un ingrédient spécial
                "type": "ingredient_special"
            }

    print("\nObjets disponibles :")
    for i, (nom, data) in enumerate(objets_disponibles.items(), 1):
        print(f"{i}. {nom} - {data['prix']} pièces")

    print(f"{len(objets_disponibles) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(objets_disponibles):
            nom_objet = list(objets_disponibles.keys())[choix - 1]
            objet_data = objets_disponibles[nom_objet]

            quantite = int(input(f"Combien de {nom_objet} voulez-vous acheter ? "))
            if quantite <= 0:
                print("Quantité invalide.")
                return

            prix_total = objet_data["prix"] * quantite
            or_actuel = obtenir_or_joueur(joueur)

            if or_actuel >= prix_total:
                # Créer l'objet
                obj_id = objet_data.get("id")
                type_objet = objet_data.get("type", "consommable")

                if type_objet == "ingredient_special":
                    # C'est un ingrédient spécial (comme "Eau Pure")
                    description = INGREDIENTS_SPECIAUX.get(nom_objet, {}).get("description", "")
                    nouvel_objet = Objet(
                        nom=nom_objet,
                        type_objet="matériau",
                        quantite=quantite,
                        description=description,
                        rarete=None  # Les ingrédients spéciaux n'ont pas de rareté
                    )
                    joueur.ajouter_objet(nouvel_objet)
                    retirer_or(joueur, prix_total)
                    print(f"\n✓ Vous avez acheté {quantite}x {nom_objet} pour {prix_total} pièces.")
                    print(f"Or restant : {obtenir_or_joueur(joueur)} pièces")
                elif obj_id and obj_id in DEFINITIONS_OBJETS:
                    obj_def = DEFINITIONS_OBJETS[obj_id]
                    nouvel_objet = Objet(
                        nom=obj_def["nom"],
                        type_objet=obj_def["type"],
                        quantite=quantite,
                        description=obj_def.get("description", ""),
                        rarete=obj_def.get("rarete")
                    )
                    joueur.ajouter_objet(nouvel_objet)
                    retirer_or(joueur, prix_total)
                    print(f"\n✓ Vous avez acheté {quantite}x {nom_objet} pour {prix_total} pièces.")
                    print(f"Or restant : {obtenir_or_joueur(joueur)} pièces")
                else:
                    print("Erreur : Objet introuvable dans les définitions.")
            else:
                print(f"\n✗ Vous n'avez pas assez d'or. Prix : {prix_total}, Or actuel : {or_actuel}")
        elif choix == len(objets_disponibles) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def menu_vente(joueur):
    """
    Menu de vente d'objets.
    """
    print(f"\n{'='*60}")
    print("--- VENTE ---")
    afficher_or(joueur)
    print(f"{'='*60}")

    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    print("\nObjets à vendre :")
    objets_liste = list(joueur.inventaire.items())
    for i, (nom, objet) in enumerate(objets_liste, 1):
        prix_vente = calculer_prix_vente(objet)
        print(f"{i}. {objet} - Prix de vente : {prix_vente} pièces")

    print(f"{len(objets_liste) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(objets_liste):
            nom_objet, objet = objets_liste[choix - 1]

            quantite_max = objet.quantite
            quantite = int(input(f"Combien de {nom_objet} voulez-vous vendre (max: {quantite_max}) ? "))

            if quantite <= 0 or quantite > quantite_max:
                print("Quantité invalide.")
                return

            prix_total = calculer_prix_vente(objet) * quantite

            # Retirer l'objet
            joueur.retirer_objet(nom_objet, quantite)

            # Ajouter l'or
            ajouter_or(joueur, prix_total)

            print(f"\n✓ Vous avez vendu {quantite}x {nom_objet} pour {prix_total} pièces.")
            print(f"Or actuel : {obtenir_or_joueur(joueur)} pièces")
        elif choix == len(objets_liste) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def calculer_prix_vente(objet: Objet) -> int:
    """
    Calcule le prix de vente d'un objet (30% de sa valeur d'achat approximative).
    TODO: Améliorer avec un système de prix basé sur la rareté et les stats.
    """
    # Prix de base selon la rareté
    prix_base = {
        "commun": 10,
        "rare": 50,
        "épique": 200,
        "légendaire": 1000,
        None: 5
    }

    base = prix_base.get(objet.rarete, 5)

    # Multiplicateur selon le type
    multiplicateur = {
        "matériau": 1.0,
        "potion": 1.5,
        "équipement": 2.0,
        "consommable": 1.2
    }

    multi = multiplicateur.get(objet.type, 1.0)

    return int(base * multi)


# ============================================================================
# MENU CRAFT
# ============================================================================
# Le menu de craft est maintenant dans menus/craft.py
# Cette fonction est conservée pour compatibilité mais redirige vers le nouveau système


# ============================================================================
# MENU QUÊTES
# ============================================================================

def menu_quetes(joueur, hub: HubCapital, features_quetes: List[HubFeature]):
    """
    Menu de quêtes : affichage et gestion des quêtes.
    TODO: Intégrer le système de quêtes une fois défini.
    """
    print(f"\n{'='*60}")
    print("--- QUÊTES ---")
    print(f"{'='*60}")
    print("\nLe système de quêtes est en cours de développement.")
    print("Les quêtes seront définies avec l'histoire du jeu.\n")

    print("Fonctionnalités prévues :")
    print("- Quêtes principales (histoire)")
    print("- Quêtes secondaires")
    print("- Quêtes journalières")
    print("- Suivi de progression\n")

    # TODO: Implémenter le système de quêtes
    # 1. Afficher les quêtes disponibles
    # 2. Afficher les quêtes en cours
    # 3. Afficher les quêtes complétées
    # 4. Accepter/Abandonner des quêtes


# ============================================================================
# MENU TÉLÉPORTATION
# ============================================================================

def menu_teleportation(joueur, hub: HubCapital):
    """
    Menu de téléportation vers d'autres royaumes.
    """
    # hub.teleportations est une List[str], pas un dict
    if not hub.teleportations:
        print("\nAucune téléportation disponible pour le moment.")
        return

    print(f"\n{'='*60}")
    print("--- TÉLÉPORTATION ---")
    print(f"{'='*60}")
    print(f"\nDepuis {hub.nom}, les options de téléportation disponibles :\n")

    # Afficher les options de téléportation (qui sont des strings descriptives)
    for i, teleportation_desc in enumerate(hub.teleportations, 1):
        print(f"{i}. {teleportation_desc}")

    print(f"{len(hub.teleportations) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(hub.teleportations):
            teleportation_choisie = hub.teleportations[choix - 1]

            # TODO: Vérifier si le royaume est débloqué
            # TODO: Implémenter la téléportation effective

            print(f"\n✓ {teleportation_choisie}")
            print("(Fonctionnalité à implémenter - nécessite système de zones débloquées)")
            print("La téléportation sera disponible une fois le système de progression implémenté.\n")
        elif choix == len(hub.teleportations) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


# ============================================================================
# MENU FORMATION
# ============================================================================

def menu_formation(joueur, hub: HubCapital, features_formation: List[HubFeature]):
    """
    Menu de formation : amélioration des compétences.
    TODO: Implémenter le système de formation.
    """
    print(f"\n{'='*60}")
    print("--- FORMATION ---")
    print(f"{'='*60}")
    print("\nLe système de formation est en cours de développement.\n")

    print("Fonctionnalités prévues :")
    print("- Apprentissage de nouvelles capacités")
    print("- Amélioration de capacités existantes")
    print("- Formation spécialisée selon la classe\n")
