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
import signal
import sys

if __name__ == "__main__":
    def signal_handler(sig, frame):
        """Gère les signaux d'interruption (CTRL+C, CTRL+D)"""
        print("\n\nInterruption détectée. Fermeture propre du jeu...")
        sys.exit(0)

    # Enregistrer les gestionnaires de signaux uniquement quand le script est exécuté directement
    signal.signal(signal.SIGINT, signal_handler)  # CTRL+C
    signal.signal(signal.SIGTERM, signal_handler)  # Terminaison

    joueur_principal = None
    try:
        joueur_principal = menu_principal() # menu_principal retourne le joueur créé/chargé ou None si on quitte

        if joueur_principal: # S'assurer qu'un joueur a bien été créé ou chargé
            effacer_console()
            from utils.affichage import afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS as COULEURS_DISPLAY
            print()
            afficher_titre_menu_avec_emoji("DÉBUT DE L'AVENTURE", "principal")
            afficher_separateur(style="simple", couleur=COULEURS_DISPLAY["GRIS"])

            while joueur_principal.est_vivant:
                try:
                    effacer_console()
                    from utils.affichage import afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS as COULEURS_DISPLAY
                    print()
                    afficher_titre_menu_avec_emoji("MENU PRINCIPAL", "principal")
                    afficher_separateur(style="simple", couleur=COULEURS_DISPLAY["GRIS"])
                    print(f"\n{COULEURS_DISPLAY['CYAN']}Que voulez-vous faire ?{COULEURS_DISPLAY['RESET']}")
                    print()
                    print(f"1. {COULEURS_DISPLAY['VERT']}🌍 Explorer Valdoria{COULEURS_DISPLAY['RESET']}")
                    print()
                    print(f"2. {COULEURS_DISPLAY['BLEU']}🏛️  Accéder à votre Capitale{COULEURS_DISPLAY['RESET']}")
                    print()
                    print(f"3. {COULEURS_DISPLAY['MAGENTA']}👤 Accéder au Menu Personnage{COULEURS_DISPLAY['RESET']}")
                    print()
                    print(f"4. {COULEURS_DISPLAY['JAUNE']}💾 Sauvegarder la partie{COULEURS_DISPLAY['RESET']}")
                    print()
                    print(f"5. {COULEURS_DISPLAY['ROUGE']}🚪 Quitter le jeu{COULEURS_DISPLAY['RESET']}")

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
                except KeyboardInterrupt:
                    # CTRL+C
                    print("\n\nInterruption détectée. Fermeture propre du jeu...")
                    break
                except EOFError:
                    # CTRL+D
                    print("\n\nFin de l'entrée détectée. Fermeture propre du jeu...")
                    break
    except KeyboardInterrupt:
        # CTRL+C au niveau principal
        print("\n\nInterruption détectée. Fermeture propre du jeu...")
    except EOFError:
        # CTRL+D au niveau principal
        print("\n\nFin de l'entrée détectée. Fermeture propre du jeu...")
    finally:
        print("\nFin du programme.")
