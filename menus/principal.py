# menus/principal.py
# Menus principaux du jeu

from .sauvegarde import sauvegarder_jeu, charger_jeu
from .creation import creer_personnage
from .inventaire import menu_inventaire
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS


def menu_principal():
    joueur = None
    while True:
        effacer_console()
        afficher_titre_menu_avec_emoji("MENU PRINCIPAL", "principal")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print("\nOptions disponibles :")
        print("1. 🎮 Nouvelle Partie")
        print("2. 📂 Charger Partie")
        print("3. 🚪 Quitter le jeu")
        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}")

        if choix == '1':
            joueur = creer_personnage()
            if joueur:
                # Afficher l'introduction complète (histoire + royaume + première quête)
                from .introduction import afficher_introduction_complete
                afficher_introduction_complete(joueur)
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
        effacer_console()
        afficher_titre_menu_avec_emoji(f"MENU DE {joueur.nom.upper()}", "personnage")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print("\nOptions disponibles :")
        print("1. 📊 Afficher Statistiques")
        print("2. 🎒 Gérer Inventaire")
        print("3. ⚡ Dépenser Points d'Attribut")
        print("4. 💾 Sauvegarder Partie")
        print("5. ✨ Afficher Capacités")
        print("6. ⬅️  Retour")

        choix = input(f"\n{COULEURS['BLEU']}Votre choix : {COULEURS['RESET']}")

        if choix == '1':
            joueur.afficher_stats()
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == '2':
            menu_inventaire(joueur)
        elif choix == '3':
            allouer_points_attributs(joueur)
        elif choix == '4':
            from .sauvegarde import menu_sauvegarde_manuelle
            menu_sauvegarde_manuelle(joueur)
        elif choix == '5':
            joueur.afficher_capacites()
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == '6':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

def allouer_points_attributs(joueur):
    if joueur.points_attribut <= 0:
        print("Vous n'avez pas de points d'attribut à dépenser.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    while joueur.points_attribut > 0:
        effacer_console()
        afficher_titre_menu_avec_emoji("ALLOCATION DES POINTS D'ATTRIBUT", "attributs")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        joueur.afficher_stats()
        print(f"\n{COULEURS['JAUNE']}⚡ Points d'attribut disponibles : {joueur.points_attribut}{COULEURS['RESET']}")
        print(f"\n{COULEURS['CYAN']}Quel attribut souhaitez-vous augmenter ?{COULEURS['RESET']}")
        print("1. 💪 Force")
        print("2. 🏃 Agilité")
        print("3. ❤️  Vitalité")
        print("4. 🧠 Intelligence")
        print(f"{COULEURS['GRIS']}Ou '0' pour quitter.{COULEURS['RESET']}")

        choix_attr = input(f"\n{COULEURS['JAUNE']}Votre choix : {COULEURS['RESET']}")

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
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue
                joueur.depenser_points_attribut(attribut_choisi, montant)
                print(f"\n✓ {montant} point(s) alloué(s) à {attribut_choisi.capitalize()}.")
                input("\nAppuyez sur Entrée pour continuer...")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                input("\nAppuyez sur Entrée pour continuer...")
        else:
            print("Choix invalide. Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")
