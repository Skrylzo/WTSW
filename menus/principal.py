# menus/principal.py
# Menus principaux du jeu

from .sauvegarde import sauvegarder_jeu, charger_jeu
from .creation import creer_personnage
from .inventaire import menu_inventaire


def menu_principal():
    joueur = None
    while True:
        print("\n--- Menu Principal ---")
        print("1. Nouvelle Partie")
        print("2. Charger Partie")
        print("3. Quitter le jeu") # Renommé
        choix = input("Votre choix : ")

        if choix == '1':
            joueur = creer_personnage()
            if joueur:
                return joueur
        elif choix == '2':
            nom_a_charger = input("Entrez le nom du personnage à charger : ")
            from .sauvegarde import menu_gestion_sauvegardes
            joueur = menu_gestion_sauvegardes(nom_a_charger)
            if joueur:
                return joueur
        elif choix == '3':
            print("Merci d'avoir joué ! Au revoir.")
            return None
        else:
            print("Choix invalide. Veuillez réessayer.")

def menu_personnage(joueur):
    while True:
        print(f"\n--- Menu de {joueur.nom} ---")
        print("1. Afficher Statistiques")
        print("2. Gérer Inventaire")
        print("3. Dépenser Points d'Attribut")
        print("4. Sauvegarder Partie")
        print("5. Afficher Capacités")
        print("6. Quitter la partie")

        choix = input("Votre choix : ")

        if choix == '1':
            joueur.afficher_stats()
        elif choix == '2':
            menu_inventaire(joueur)
        elif choix == '3':
            allouer_points_attributs(joueur)
        elif choix == '4':
            from .sauvegarde import menu_sauvegarde_manuelle
            menu_sauvegarde_manuelle(joueur)
        elif choix == '5':
            joueur.afficher_capacites()
        elif choix == '6':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def allouer_points_attributs(joueur):
    if joueur.points_attribut <= 0:
        print("Vous n'avez pas de points d'attribut à dépenser.")
        return

    while joueur.points_attribut > 0:
        joueur.afficher_stats()
        print(f"\nPoints d'attribut disponibles : {joueur.points_attribut}")
        print("Quel attribut souhaitez-vous augmenter ?")
        print("1. Force")
        print("2. Agilité")
        print("3. Vitalité")
        print("4. Intelligence")
        print("Ou '0' pour quitter.")

        choix_attr = input("Votre choix : ")

        if choix_attr == '0':
            break

        attributs_map = {
            '1': 'force',
            '2': 'agilite',
            '3': 'vitalite',
            '4': 'intelligence'
        }

        attribut_choisi = attributs_map.get(choix_attr)

        if attribut_choisi:
            try:
                montant = int(input(f"Combien de points voulez-vous allouer à {attribut_choisi.capitalize()} ? "))
                if montant > joueur.points_attribut:
                    print(f"Vous ne pouvez allouer que {joueur.points_attribut} points.")
                    continue
                joueur.depenser_points_attribut(attribut_choisi, montant)
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        else:
            print("Choix invalide. Veuillez réessayer.")
