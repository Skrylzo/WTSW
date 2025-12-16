# menus/monnaie.py
# Système de gestion de l'or du joueur

def obtenir_or_joueur(joueur) -> int:
    """Retourne l'or du joueur (ajoute l'attribut si nécessaire)."""
    if not hasattr(joueur, 'or_'):
        joueur.or_ = 100  # Or de départ
    return joueur.or_


def ajouter_or(joueur, montant: int):
    """Ajoute de l'or au joueur."""
    obtenir_or_joueur(joueur)  # S'assurer que l'attribut existe
    joueur.or_ += montant


def retirer_or(joueur, montant: int) -> bool:
    """Retire de l'or du joueur. Retourne True si réussi."""
    or_actuel = obtenir_or_joueur(joueur)
    if or_actuel >= montant:
        joueur.or_ -= montant
        return True
    return False


def afficher_or(joueur):
    """Affiche l'or du joueur."""
    or_actuel = obtenir_or_joueur(joueur)
    print(f"{or_actuel} pièces")
