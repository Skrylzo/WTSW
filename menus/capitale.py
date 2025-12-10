# menus/capitale.py
# Menus des capitales (hubs) : commerce, craft, quêtes, téléportation

from typing import Optional, Dict, List
import re

from world import (
    obtenir_capitale_joueur, obtenir_royaume_du_joueur, obtenir_royaume_par_nom,
    obtenir_tous_royaumes, FeatureType, HubFeature, HubCapital, TOUS_LES_ROYAUMES
)
from classes.objet import Objet
from data.objets import DEFINITIONS_OBJETS
from data.categories_ingredients import INGREDIENTS_SPECIAUX
from .craft import menu_craft
from .exploration import creer_systeme_chapitres_base


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

        # Téléportation (uniquement si le royaume est complété)
        if hub.teleportations and royaume_est_complete(joueur):
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

    return True


def menu_teleportation(joueur, hub: HubCapital):
    """
    Menu de téléportation vers d'autres royaumes.
    La téléportation n'est disponible qu'après avoir complété son propre royaume.
    """
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

    print(f"{len(royaumes_affiches) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(royaumes_affiches):
            royaume_choisi = royaumes_affiches[choix - 1]

            # Demander confirmation
            print(f"\nTéléporter vers {royaume_choisi} ?")
            confirmation = input("Confirmer (o/n) : ").strip().lower()

            if confirmation == 'o':
                if teleporter_vers_royaume(joueur, royaume_choisi):
                    input("\nAppuyez sur Entrée pour continuer...")
                    # Retourner au menu de capitale du nouveau royaume
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


# ============================================================================
# MENU FORMATION
# ============================================================================

def calculer_prix_apprentissage_capacite(niveau_requis: int) -> int:
    """
    Calcule le prix d'apprentissage d'une capacité en fonction de son niveau requis.
    Le prix augmente de manière exponentielle pour refléter le parcours fait.

    Prix par niveau :
    - Niveau 1 : 100 or
    - Niveau 5 : 1250 or
    - Niveau 10 : 5000 or
    - Niveau 15 : 7500 or (avant-dernière capacité, prix réduit)
    - Niveau 20 : 15000 or (dernière capacité, prix augmenté)

    :param niveau_requis: Niveau requis pour apprendre la capacité
    :return: Prix en or pour apprendre la capacité
    """
    prix_base = 100

    # Prix spéciaux pour les dernières capacités
    if niveau_requis == 20:
        # Dernière capacité : prix élevé
        return 15000
    elif niveau_requis == 15:
        # Avant-dernière capacité : prix réduit
        return 7500

    # Formule standard pour les autres niveaux : prix_base * niveau^2 * 0.5
    prix = int(prix_base * (niveau_requis ** 2) * 0.5)
    # Minimum 100 or
    return max(100, prix)


def obtenir_capacites_disponibles(joueur):
    """
    Retourne les capacités disponibles pour le joueur selon sa classe et son niveau.
    :param joueur: Instance du personnage joueur
    :return: Liste des capacités disponibles (non apprises) avec leurs données
    """
    from data.capacites import TOUTES_LES_CAPACITES_DATA
    from data.races_classes import DEFINITIONS_RACES_CLASSES

    # Obtenir les capacités de la classe du joueur
    race_data = DEFINITIONS_RACES_CLASSES.get(joueur.race, {})
    classe_data = race_data.get('classes', {}).get(joueur.specialisation.nom, {})
    capacites_classe = classe_data.get('capacites_ids', [])

    # Obtenir les IDs des capacités déjà apprises
    capacites_apprises_ids = [cap.id for cap in joueur.capacites_apprises]

    # Filtrer les capacités disponibles
    capacites_disponibles = []
    for cap_id in capacites_classe:
        # Vérifier que la capacité n'est pas déjà apprise
        if cap_id in capacites_apprises_ids:
            continue

        # Vérifier que la capacité existe dans les données
        if cap_id not in TOUTES_LES_CAPACITES_DATA:
            continue

        cap_data = TOUTES_LES_CAPACITES_DATA[cap_id]
        niveau_requis = cap_data.get('niveau_requis', 1)

        # Vérifier que le joueur a le niveau requis
        if joueur.niveau < niveau_requis:
            continue

        # Ajouter la capacité avec son prix
        prix = calculer_prix_apprentissage_capacite(niveau_requis)
        capacites_disponibles.append({
            'id': cap_id,
            'nom': cap_data.get('nom', 'Capacité Inconnue'),
            'description': cap_data.get('description', ''),
            'niveau_requis': niveau_requis,
            'prix': prix
        })

    # Trier par niveau requis puis par nom
    capacites_disponibles.sort(key=lambda x: (x['niveau_requis'], x['nom']))

    return capacites_disponibles


def apprendre_capacite(joueur, cap_id: str) -> bool:
    """
    Apprend une capacité au joueur si les conditions sont remplies.
    :param joueur: Instance du personnage joueur
    :param cap_id: ID de la capacité à apprendre
    :return: True si la capacité a été apprise, False sinon
    """
    from data.capacites import TOUTES_LES_CAPACITES_DATA
    from classes.capacite import Capacite

    # Vérifier que la capacité existe
    if cap_id not in TOUTES_LES_CAPACITES_DATA:
        print(f"❌ Capacité '{cap_id}' introuvable.")
        return False

    # Vérifier que la capacité n'est pas déjà apprise
    capacites_apprises_ids = [cap.id for cap in joueur.capacites_apprises]
    if cap_id in capacites_apprises_ids:
        print(f"❌ Vous connaissez déjà cette capacité.")
        return False

    cap_data = TOUTES_LES_CAPACITES_DATA[cap_id]
    niveau_requis = cap_data.get('niveau_requis', 1)

    # Vérifier le niveau requis
    if joueur.niveau < niveau_requis:
        print(f"❌ Vous devez être niveau {niveau_requis} pour apprendre cette capacité.")
        return False

    # Calculer le prix
    prix = calculer_prix_apprentissage_capacite(niveau_requis)

    # Vérifier que le joueur a assez d'or
    or_actuel = obtenir_or_joueur(joueur)
    if or_actuel < prix:
        print(f"❌ Vous n'avez pas assez d'or. Prix : {prix} or, Vous avez : {or_actuel} or.")
        return False

    # Retirer l'or
    retirer_or(joueur, prix)

    # Créer et ajouter la capacité
    capacite = Capacite(
        id_cap=cap_id,
        nom=cap_data["nom"],
        description=cap_data["description"],
        cout_mana=cap_data.get("cout_mana", 0),
        cout_energie=cap_data.get("cout_energie", 0),
        cout_rage=cap_data.get("cout_rage", 0),
        degats_fixes=cap_data.get("degats_fixes", 0),
        soin_fixe=cap_data.get("soin_fixe", 0),
        effet_data=cap_data.get("effet_data"),
        type_cible=cap_data.get("type_cible", "unique"),
        niveau_requis=cap_data.get("niveau_requis", 1),
        peut_critiquer=cap_data.get("peut_critiquer", False)
    )

    joueur.capacites_apprises.append(capacite)
    print(f"✅ Vous avez appris '{capacite.nom}' pour {prix} or !")
    print(f"   {capacite.description}")
    return True


def menu_formation(joueur, hub: HubCapital, features_formation: List[HubFeature]):
    """
    Menu de formation : amélioration des compétences.
    Permet d'apprendre de nouvelles capacités selon la classe et le niveau.
    """
    while True:
        print(f"\n{'='*60}")
        print("--- FORMATION ---")
        print(f"{'='*60}")
        afficher_or(joueur)
        print(f"Niveau : {joueur.niveau}")
        print(f"Classe : {joueur.specialisation.nom}")

        # Obtenir les capacités disponibles
        capacites_disponibles = obtenir_capacites_disponibles(joueur)

        if not capacites_disponibles:
            print("\n❌ Aucune capacité disponible pour le moment.")
            print("   Vous avez déjà appris toutes les capacités accessibles à votre niveau.")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        print(f"\n📚 Capacités disponibles ({len(capacites_disponibles)}) :\n")

        for i, cap in enumerate(capacites_disponibles, 1):
            niveau_info = f"Niveau {cap['niveau_requis']}"
            prix_info = f"{cap['prix']} or"
            print(f"{i}. {cap['nom']} ({niveau_info}) - {prix_info}")
            if cap['description']:
                print(f"   {cap['description']}")

        print(f"{len(capacites_disponibles) + 1}. Retour")

        try:
            choix = int(input("\nVotre choix : "))
            if 1 <= choix <= len(capacites_disponibles):
                cap_choisie = capacites_disponibles[choix - 1]

                # Demander confirmation
                print(f"\nApprendre '{cap_choisie['nom']}' pour {cap_choisie['prix']} or ?")
                confirmation = input("Confirmer (o/n) : ").strip().lower()

                if confirmation == 'o':
                    if apprendre_capacite(joueur, cap_choisie['id']):
                        input("\nAppuyez sur Entrée pour continuer...")
                        # Continuer la boucle pour voir les nouvelles capacités disponibles
                        continue
                    else:
                        input("\nAppuyez sur Entrée pour continuer...")
                else:
                    print("Apprentissage annulé.")
            elif choix == len(capacites_disponibles) + 1:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\n\nRetour au menu précédent...")
            return
