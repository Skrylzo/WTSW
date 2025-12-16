# menus/pnj.py
# Menu pour interagir avec les PNJ

from typing import List, Optional
from world.pnj import PNJS, obtenir_pnj, parler_a_pnj
from data.pnjs_quetes import initialiser_pnjs
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS

# S'assurer que les PNJ sont initialisés
initialiser_pnjs()


def obtenir_pnjs_capitale(joueur) -> List[str]:
    """
    Retourne la liste des IDs de PNJ disponibles dans la capitale du joueur.
    Ne retourne que les PNJ visibles (débloqués selon les quêtes complétées).

    :param joueur: Le personnage joueur
    :return: Liste des IDs de PNJ disponibles et visibles
    """
    from data.pnjs_deblocage import obtenir_pnjs_visibles_capitale
    # Utiliser directement la fonction qui gère la visibilité
    return obtenir_pnjs_visibles_capitale(joueur)


def menu_parler_pnj(joueur):
    """
    Menu pour parler aux PNJ disponibles dans la capitale.

    :param joueur: Le personnage joueur
    """
    pnjs_disponibles = obtenir_pnjs_capitale(joueur)

    if not pnjs_disponibles:
        print("\nAucun PNJ disponible dans cette capitale pour le moment.")
        return

    while True:
        effacer_console()
        print()
        afficher_titre_menu_avec_emoji("PARLER À UN HABITANT", "pnj")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()

        # Afficher les PNJ disponibles
        options = []
        option_num = 1

        for pnj_id in pnjs_disponibles:
            pnj = obtenir_pnj(pnj_id)
            if pnj:
                print(f"{option_num}. {pnj.nom}")
                print()
                if pnj.description:
                    print(f"   {pnj.description}")
                    print()
                options.append(pnj_id)
                option_num += 1

        print(f"{option_num}. ⬅️  Retour (r)")
        print()

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        try:
            if choix == 'r':
                return
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                pnj_id = options[choix_int - 1]
                parler_a_pnj(joueur, pnj_id)
                input("\nAppuyez sur Entree pour continuer...")
            elif choix_int == len(options) + 1:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def menu_pnj_capitale(joueur):
    """
    Menu principal pour les PNJ dans la capitale.
    Point d'entrée depuis le menu de la capitale.

    :param joueur: Le personnage joueur
    """
    menu_parler_pnj(joueur)
