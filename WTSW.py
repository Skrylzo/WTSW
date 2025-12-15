# WTSW.py
# Point d'entrée principal du jeu

# Importation depuis la nouvelle structure modulaire
from menus import (
    menu_principal,
    menu_sauvegarde_manuelle,
    allouer_points_attributs,
    menu_personnage,
    menu_capitale,
    menu_exploration_valdoria,
)
from combat import deroulement_combat
from world import teleporter_joueur_vers_capitale
from utils.affichage import effacer_console

if __name__ == "__main__":
    joueur_principal = None
    joueur_principal = menu_principal() # menu_principal retourne le joueur créé/chargé ou None si on quitte

    if joueur_principal: # S'assurer qu'un joueur a bien été créé ou chargé
        effacer_console()
        print("\n--- DÉBUT DE L'AVENTURE ---")

        while joueur_principal.est_vivant:
            effacer_console()
            print("\n" + "="*60)
            print("--- MENU PRINCIPAL ---")
            print("="*60)
            print("\nQue voulez-vous faire ?")
            print("1. Explorer Valdoria")  # Nouveau : exploration avec chapitres
            print("2. Accéder à votre Capitale")  # Nouveau : menu de la capitale
            print("3. Accéder au Menu Personnage")
            print("4. Sauvegarder la partie")
            print("5. Quitter le jeu")

            choix_aventure = input("\nVotre choix : ")

            if choix_aventure == '1':
                # Nouveau système d'exploration avec chapitres
                menu_exploration_valdoria(joueur_principal)

                # Si le joueur est mort après l'exploration, la téléportation a déjà été gérée
                if not joueur_principal.est_vivant:
                    # S'assurer que la téléportation a bien eu lieu
                    if not teleporter_joueur_vers_capitale(joueur_principal):
                        print("Erreur : Impossible de vous téléporter vers votre capitale.")
                        print("Game Over. Votre aventure se termine ici.")
                        break
                    # Le joueur est maintenant soigné et peut continuer à jouer
                    continue

            elif choix_aventure == '2':
                # Nouveau menu de capitale (commerce, craft, quêtes, téléportation)
                menu_capitale(joueur_principal)

                # Si le joueur est mort (peu probable dans un menu, mais possible)
                if not joueur_principal.est_vivant:
                    if not teleporter_joueur_vers_capitale(joueur_principal):
                        print("Erreur : Impossible de vous téléporter vers votre capitale.")
                        print("Game Over. Votre aventure se termine ici.")
                        break
                    continue

            elif choix_aventure == '3':
                menu_personnage(joueur_principal)
                # Si le joueur est mort dans le menu personnage
                if not joueur_principal.est_vivant:
                    if not teleporter_joueur_vers_capitale(joueur_principal):
                        print("Erreur : Impossible de vous téléporter vers votre capitale.")
                        print("Game Over. Votre aventure se termine ici.")
                        break
                    continue

            elif choix_aventure == '4':
                menu_sauvegarde_manuelle(joueur_principal)

            elif choix_aventure == '5':
                print("Quitter l'aventure. Votre progression actuelle n'est pas sauvegardée si vous n'avez pas sauvegardé manuellement.")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    print("\nFin du programme.")
