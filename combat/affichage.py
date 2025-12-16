# combat/affichage.py
# Fonctions d'affichage pour le combat (séparation UI/logique)
# Ces fonctions peuvent être remplacées par des messages réseau pour le multijoueur

from typing import Dict, Any, List
from classes.base_combatant import Personnage, Ennemi
from classes.capacite import Capacite
from .calculs import creer_barre_vie
from utils.affichage import COULEURS, formater_nombre


def afficher_tour_joueur(joueur: Personnage, ennemis: List[Ennemi]) -> None:
    """
    Affiche les informations du tour du joueur.

    :param joueur: Le joueur
    :param ennemis: Liste des ennemis
    """
    from utils.affichage import effacer_console
    effacer_console()

    resource_display = ""
    couleur_ressource = COULEURS["CYAN"]
    if joueur.specialisation.type_ressource == "Mana":
        resource_display = f"Mana: {int(joueur.mana)}/{int(joueur.mana_max)}"
        couleur_ressource = COULEURS["BLEU"]
    elif joueur.specialisation.type_ressource == "Energie":
        resource_display = f"Energie: {int(joueur.energie)}/{int(joueur.energie_max)}"
        couleur_ressource = COULEURS["JAUNE"]
    elif joueur.specialisation.type_ressource == "Rage":
        resource_display = f"Rage: {int(joueur.rage)}/{int(joueur.rage_max)}"
        couleur_ressource = COULEURS["ROUGE"]

    barre_vie_joueur = creer_barre_vie(joueur.vie, joueur.vie_max)
    from utils.affichage import afficher_titre_menu_avec_emoji, afficher_separateur
    print()
    afficher_titre_menu_avec_emoji(f"TOUR DE {joueur.nom}", "combat")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print(f"Vie: {barre_vie_joueur} {int(joueur.vie)}/{int(joueur.vie_max)} | {couleur_ressource}{resource_display}{COULEURS['RESET']}")

    ennemis_vivants = [e for e in ennemis if e.est_vivant]
    if ennemis_vivants:
        print(f"\n{COULEURS['ROUGE']}Ennemis actuels :{COULEURS['RESET']}")
        for i, ennemi in enumerate(ennemis_vivants):
            barre_vie_ennemi = creer_barre_vie(ennemi.vie, ennemi.vie_max)
            print(f"{COULEURS['ROUGE']}{i+1}. {ennemi.nom}{COULEURS['RESET']} - Vie: {barre_vie_ennemi} {int(ennemi.vie)}/{int(ennemi.vie_max)}")


def afficher_menu_actions() -> None:
    """Affiche le menu des actions disponibles."""
    print("\nChoisissez votre action :")
    print()
    print(f"{COULEURS['CYAN']}1. ⚔️  Attaquer{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['MAGENTA']}2. ✨ Utiliser une Capacité{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['VERT']}3. 🧪 Utiliser un Objet{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['BLEU']}4. 📊 Afficher les Stats{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['MAGENTA']}5. ✨ Afficher les Capacités{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['JAUNE']}6. 📋 Voir les Quêtes{COULEURS['RESET']}")
    print()
    print(f"{COULEURS['GRIS']}7. ⬅️  Retour (r){COULEURS['RESET']}")
    print()


def afficher_resultat_attaque(resultat: Dict[str, Any]) -> None:
    """
    Affiche le résultat d'une attaque avec couleurs et emojis.

    :param resultat: Résultat retourné par executer_attaque()
    """
    if resultat["type"] == "esquive":
        print(f"  {COULEURS['CYAN']}✨ {resultat['cible'].nom} a esquivé votre attaque !{COULEURS['RESET']}")
        print()
    elif resultat["type"] == "degats":
        degats = int(resultat['degats'])  # Arrondir à l'entier
        if resultat.get("critique", False):
            print(f"  {COULEURS['JAUNE']}⚡ COUP CRITIQUE !{COULEURS['RESET']}")
            print()
        print(f"  {COULEURS['CYAN']}→ Vous infligez {formater_nombre(degats)} dégâts à {resultat['cible'].nom}.{COULEURS['RESET']}")
        print()


def afficher_resultat_capacite(resultat: Dict[str, Any]) -> None:
    """
    Affiche le résultat d'une capacité.

    :param resultat: Résultat retourné par executer_capacite()
    """
    if not resultat["success"]:
        if "message" in resultat:
            print(f"  {resultat['message']}")
        else:
            print(f"  Impossible d'utiliser {resultat['capacite'].nom}")
    # Note: L'affichage détaillé des capacités est géré par la méthode utiliser() de Capacite


def afficher_message_erreur(message: str) -> None:
    """
    Affiche un message d'erreur en rouge.

    :param message: Message à afficher
    """
    print(f"{COULEURS['ROUGE']}⚠️  {message}{COULEURS['RESET']}")


def afficher_tour_ennemis(joueur: Personnage, ennemi: Ennemi) -> None:
    """
    Affiche le début du tour d'un ennemi.

    :param joueur: Le joueur
    :param ennemi: L'ennemi qui attaque
    """
    print(f"{ennemi.nom} attaque {joueur.nom}!")


def afficher_attaque_ennemi(ennemi: Ennemi, joueur: Personnage, degats: float, critique: bool = False, esquive: bool = False) -> None:
    """
    Affiche le résultat d'une attaque d'ennemi avec couleurs et emojis.

    :param ennemi: L'ennemi qui attaque
    :param joueur: Le joueur qui reçoit
    :param degats: Dégâts infligés
    :param critique: Si c'est un coup critique
    :param esquive: Si le joueur a esquivé
    """
    if esquive:
        print(f"  {COULEURS['CYAN']}✨ Vous avez esquivé l'attaque de {ennemi.nom} !{COULEURS['RESET']}")
    else:
        degats_arrondis = int(degats)  # Arrondir à l'entier
        if critique:
            print(f"  {COULEURS['ROUGE']}⚡ COUP CRITIQUE !{COULEURS['RESET']}")
        print(f"  {COULEURS['ROUGE']}← {ennemi.nom} vous inflige {formater_nombre(degats_arrondis)} dégâts.{COULEURS['RESET']}")


def afficher_fin_combat(joueur: Personnage, victoire: bool) -> None:
    """
    Affiche la fin du combat avec couleurs.

    :param joueur: Le joueur
    :param victoire: True si le joueur a gagné
    """
    if victoire:
        from utils.affichage import afficher_titre_menu_avec_emoji, afficher_separateur
        print("-" * 30)
        print()
        afficher_titre_menu_avec_emoji("FIN DU COMBAT", "combat")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print(f"{COULEURS['VERT']}🎉 {joueur.nom} est victorieux !{COULEURS['RESET']}")
    else:
        print(f"\n{COULEURS['ROUGE']}💀 {joueur.nom} a été vaincu...{COULEURS['RESET']}")
