# menus/inventaire.py
# Fonctions de gestion de l'inventaire

from classes.objet import Objet

def menu_inventaire(joueur):
    """Menu de gestion de l'inventaire du joueur"""
    while True:
        print(f"\n--- Inventaire de {joueur.nom} ---")
        print("1. Afficher tout l'inventaire")
        print("2. Afficher l'inventaire par type")
        print("3. Consulter un objet spécifique")
        print("4. Jeter un objet")
        print("5. Retour au menu personnage")

        choix = input("Votre choix : ")

        if choix == '1':
            afficher_inventaire_complet(joueur)
        elif choix == '2':
            afficher_inventaire_par_type(joueur)
        elif choix == '3':
            consulter_objet(joueur)
        elif choix == '4':
            jeter_objet(joueur)
        elif choix == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def afficher_inventaire_complet(joueur):
    """Affiche tout l'inventaire du joueur"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    print("\n--- Inventaire Complet ---")
    total_objets = 0
    for nom_objet, objet in joueur.inventaire.items():
        print(f"  • {objet}")
        total_objets += objet.quantite

    print(f"\nTotal: {len(joueur.inventaire)} type(s) d'objets, {total_objets} objet(s) au total")

def afficher_inventaire_par_type(joueur):
    """Affiche l'inventaire organisé par type d'objet"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    # Organiser les objets par type
    objets_par_type = {}
    for nom_objet, objet in joueur.inventaire.items():
        type_objet = objet.type
        if type_objet not in objets_par_type:
            objets_par_type[type_objet] = []
        objets_par_type[type_objet].append(objet)

    print("\n--- Inventaire par Type ---")
    for type_objet in sorted(objets_par_type.keys()):
        print(f"\n[{type_objet.capitalize()}]")
        for objet in objets_par_type[type_objet]:
            print(f"  • {objet}")

def consulter_objet(joueur):
    """Permet de consulter les détails d'un objet spécifique"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    print("\n--- Consulter un Objet ---")
    # Afficher la liste des objets disponibles
    objets_liste = list(joueur.inventaire.keys())
    for i, nom_objet in enumerate(objets_liste, 1):
        objet = joueur.inventaire[nom_objet]
        print(f"{i}. {objet.nom} (x{objet.quantite})")

    try:
        choix = int(input("\nChoisissez un objet (numéro) : "))
        if 1 <= choix <= len(objets_liste):
            nom_objet = objets_liste[choix - 1]
            objet = joueur.inventaire[nom_objet]

            print(f"\n--- Détails de {objet.nom} ---")
            print(f"Type: {objet.type.capitalize()}")
            print(f"Quantité: {objet.quantite}")
            if objet.description:
                print(f"Description: {objet.description}")
            else:
                print("Description: Aucune description disponible")
            if objet.rarete:
                print(f"Rareté: {objet.rarete}")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except (IndexError, KeyError):
        print("Erreur lors de la consultation de l'objet.")

def jeter_objet(joueur):
    """Permet de jeter un objet de l'inventaire"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    print("\n--- Jeter un Objet ---")
    # Afficher la liste des objets disponibles
    objets_liste = list(joueur.inventaire.keys())
    for i, nom_objet in enumerate(objets_liste, 1):
        objet = joueur.inventaire[nom_objet]
        print(f"{i}. {objet.nom} (x{objet.quantite})")

    try:
        choix = int(input("\nChoisissez un objet à jeter (numéro) : "))
        if 1 <= choix <= len(objets_liste):
            nom_objet = objets_liste[choix - 1]
            objet = joueur.inventaire[nom_objet]

            if objet.quantite > 1:
                print(f"\nVous avez {objet.quantite} {objet.nom}.")
                quantite_a_jeter = input(f"Combien voulez-vous jeter ? (1-{objet.quantite}) : ")
                try:
                    quantite = int(quantite_a_jeter)
                    if 1 <= quantite <= objet.quantite:
                        joueur.retirer_objet(nom_objet, quantite)
                        print(f"Vous avez jeté {quantite} {objet.nom}.")
                        if joueur.avoir_objet(nom_objet):
                            print(f"Il vous reste {joueur.compter_objet(nom_objet)} {objet.nom}.")
                        else:
                            print(f"Vous n'avez plus de {objet.nom}.")
                    else:
                        print(f"Quantité invalide. Vous devez entrer un nombre entre 1 et {objet.quantite}.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            else:
                # Confirmation pour jeter le dernier objet
                confirmation = input(f"Êtes-vous sûr de vouloir jeter {objet.nom} ? (o/n) : ").lower()
                if confirmation == 'o' or confirmation == 'oui':
                    joueur.retirer_objet(nom_objet, 1)
                    print(f"Vous avez jeté {objet.nom}.")
                else:
                    print("Action annulée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except (IndexError, KeyError):
        print("Erreur lors du retrait de l'objet.")
