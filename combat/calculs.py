# combat/calculs.py
# Fonctions de calcul pour le combat

import random
from classes.base_combatant import Personnage, Ennemi

def calculer_degats_finaux(attaquant, cible, degats_bruts, est_capacite=False):
    """
    Calcule les dégâts finaux après application de la défense et des réductions.

    Ordre d'application :
    1. Les critiques sont appliqués AVANT cet appel (dans le code appelant)
    2. La défense réduit les dégâts selon le type d'attaque

    :param attaquant: L'entité qui inflige les dégâts.
    :param cible: L'entité qui reçoit les dégâts.
    :param degats_bruts: Les dégâts après application des critiques (mais avant défense).
    :param est_capacite: True si les dégâts proviennent d'une capacité, False sinon (attaque de base).
    :return: Les dégâts finaux à appliquer (minimum 1 pour les attaques normales, 0 pour les capacités).
    """
    degats_finaux = degats_bruts

    # Obtenir la défense totale de la cible (avec effets)
    defense_cible = cible.calculer_defense_totale()

    if est_capacite:
        # Les capacités ont une réduction de défense réduite (50% de l'efficacité)
        # Cela les rend plus puissantes que les attaques normales mais pas complètement ignorées
        if isinstance(cible, Personnage):
            # Pour les personnages : réduction par pourcentage, mais à 50% de l'efficacité
            reduction_pourcentage = cible.calculer_reduction_degats_pourcentage()
            reduction_capacite = reduction_pourcentage * 0.5  # 50% de la réduction normale
            degats_finaux = degats_bruts * (1 - reduction_capacite)
        elif isinstance(cible, Ennemi):
            # Pour les ennemis : soustraction réduite (50% de la défense)
            degats_finaux = max(0, degats_bruts - (defense_cible * 0.5))
    else:
        # Attaques normales : réduction complète de la défense
        if isinstance(cible, Personnage):
            # Pour les personnages : réduction par pourcentage
            reduction_pourcentage = cible.calculer_reduction_degats_pourcentage()
            degats_finaux = degats_bruts * (1 - reduction_pourcentage)
        elif isinstance(cible, Ennemi):
            # Pour les ennemis : soustraction de la défense totale
            degats_finaux = max(1, degats_bruts - defense_cible)  # Dégâts minimum de 1

    # Arrondir et s'assurer que les dégâts ne sont pas négatifs
    # Pour les attaques normales, minimum 1. Pour les capacités, minimum 0.
    if est_capacite:
        return max(0, round(degats_finaux))
    else:
        return max(1, round(degats_finaux))


def esquive(vitesse_attaquant, vitesse_defenseur):
    """
    Calcule si une attaque est esquivée basée sur la différence de vitesse.
    :param vitesse_attaquant: Vitesse de l'attaquant
    :param vitesse_defenseur: Vitesse du défenseur
    :return: True si l'attaque est esquivée, False sinon
    """
    if vitesse_defenseur <= vitesse_attaquant:
        return False
    chance = min(50, (vitesse_defenseur - vitesse_attaquant) * 5)
    return random.randint(1, 100) <= chance


def creer_barre_vie(vie_actuelle, vie_max, longueur=20):
    """
    Crée une barre de vie visuelle avec couleurs selon le pourcentage.
    :param vie_actuelle: Vie actuelle
    :param vie_max: Vie maximale
    :param longueur: Longueur de la barre en caractères
    :return: String représentant la barre de vie avec codes couleur
    """
    from utils.affichage import COULEUR_VIE_HAUTE, COULEUR_VIE_MOYENNE, COULEUR_VIE_BASSE, COULEURS

    if vie_max <= 0:
        return "[" + "-" * longueur + "]"

    # Calculer le pourcentage de vie
    pourcentage_vie = (vie_actuelle / vie_max) * 100

    # Choisir la couleur selon le pourcentage
    if pourcentage_vie > 60:
        couleur = COULEUR_VIE_HAUTE
    elif pourcentage_vie > 30:
        couleur = COULEUR_VIE_MOYENNE
    else:
        couleur = COULEUR_VIE_BASSE

    vie_pct = int((vie_actuelle / vie_max) * longueur)
    barre_pleine = "█" * vie_pct
    barre_vide = "░" * (longueur - vie_pct)
    barre = f"{couleur}[{barre_pleine}{barre_vide}]{COULEURS['RESET']}"

    return barre
