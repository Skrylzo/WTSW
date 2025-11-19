# WTSW.py
# Point d'entrée principal du jeu

# Importation depuis la nouvelle structure modulaire
from menus import menu_principal, sauvegarder_jeu, charger_jeu, allouer_points_attributs, menu_personnage
from combat import deroulement_combat

if __name__ == "__main__":
    joueur_principal = None
    joueur_principal = menu_principal() # menu_principal retourne le joueur créé/chargé ou None si on quitte

    if joueur_principal: # S'assurer qu'un joueur a bien été créé ou chargé
        print("\n--- DÉBUT DE L'AVENTURE ---")

        while joueur_principal.est_vivant:
            print("\nQue voulez-vous faire ?")
            print("1. Explorer la Grotte (Combattre des monstres)") # Renommé et mis en 1
            print("2. Accéder au Menu Personnage") # Nouvelle option pour le menu détaillé du joueur
            print("3. Sauvegarder la partie") # Décalé
            print("4. Quitter le jeu") # Décalé

            choix_aventure = input("Votre choix : ")

            if choix_aventure == '1':
                # --- MODIFICATION ICI ---
                # On passe maintenant une liste d'IDs d'ennemis, pas des instances
                ennemis_a_combattre_ids = ["gobelin_basique"] # Liste des IDs d'ennemis
                # ennemis_a_combattre_ids = ["gobelin_basique", "orc_furieux"] # Exemple avec plusieurs ennemis

                # deroulement_combat va maintenant créer de nouvelles instances d'ennemis
                # à partir de ces IDs avec leur vie pleine.
                deroulement_combat(joueur_principal, ennemis_a_combattre_ids)

                if not joueur_principal.est_vivant:
                    print("Game Over. Votre aventure se termine ici.")
                    break

            elif choix_aventure == '2':
                menu_personnage(joueur_principal)
                if not joueur_principal.est_vivant:
                    print("Game Over. Votre aventure se termine ici.")
                    break

            elif choix_aventure == '3':
                sauvegarder_jeu(joueur_principal)
            elif choix_aventure == '4':
                print("Quitter l'aventure. Votre progression actuelle n'est pas sauvegardée si vous n'avez pas sauvegardé manuellement.")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    print("\nFin du programme.")
