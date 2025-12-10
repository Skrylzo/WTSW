# menus/commerce.py
# Système de commerce : achat et vente d'objets

from typing import List

from world import HubFeature, HubCapital
from classes.objet import Objet
from data.objets import DEFINITIONS_OBJETS
from data.categories_ingredients import INGREDIENTS_SPECIAUX
from .monnaie import obtenir_or_joueur, ajouter_or, retirer_or, afficher_or


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
