# menus/pnj.py
# Menu pour interagir avec les PNJ

from typing import List, Optional
from world.pnj import PNJS, obtenir_pnj, parler_a_pnj
from data.pnjs_quetes import initialiser_pnjs

# S'assurer que les PNJ sont initialisés
initialiser_pnjs()


def obtenir_pnjs_capitale(joueur) -> List[str]:
    """
    Retourne la liste des IDs de PNJ disponibles dans la capitale du joueur.

    :param joueur: Le personnage joueur
    :return: Liste des IDs de PNJ disponibles
    """
    # Obtenir le royaume actuel du joueur
    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        from world.royaumes import obtenir_royaume_du_joueur
        royaume_actuel = obtenir_royaume_du_joueur(joueur.race)
        if royaume_actuel:
            royaume_actuel = royaume_actuel.nom

    pnjs_disponibles = []

    # Parcourir tous les PNJ et trouver ceux du royaume actuel
    for pnj_id, pnj in PNJS.items():
        # Inclure les PNJ du royaume actuel ou les PNJ génériques (sans royaume spécifique)
        if pnj.royaume == royaume_actuel or pnj.royaume is None:
            pnjs_disponibles.append(pnj_id)

    return pnjs_disponibles


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
        print(f"\n{'='*60}")
        print("--- PARLER À UN PNJ ---")
        print(f"{'='*60}\n")

        # Afficher les PNJ disponibles
        options = []
        option_num = 1

        for pnj_id in pnjs_disponibles:
            pnj = obtenir_pnj(pnj_id)
            if pnj:
                print(f"{option_num}. {pnj.nom}")
                if pnj.description:
                    print(f"   {pnj.description}")
                options.append(pnj_id)
                option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ")

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                pnj_id = options[choix_int - 1]
                parler_a_pnj(joueur, pnj_id)
                input("\nAppuyez sur Entrée pour continuer...")
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
