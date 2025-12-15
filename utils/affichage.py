import os
import sys

# ==================== SYSTÈME DE COULEURS CENTRALISÉ ====================
# Codes couleur ANSI standardisés pour tout le jeu

COULEURS = {
    "VERT": "\033[92m",      # Succès, complétion, gains, soins
    "ROUGE": "\033[91m",      # Erreurs, dégâts reçus, danger, mort
    "JAUNE": "\033[93m",     # Avertissements, coups critiques, objets rares
    "BLEU": "\033[94m",      # Informations, quêtes, dialogues importants
    "MAGENTA": "\033[95m",   # Épique, spécial, capacités puissantes
    "CYAN": "\033[96m",      # Actions, interactions, dégâts infligés
    "GRIS": "\033[90m",      # Texte secondaire, désactivé
    "RESET": "\033[0m"       # Réinitialisation de la couleur
}

# Couleurs pour les barres de vie selon le pourcentage
COULEUR_VIE_HAUTE = COULEURS["VERT"]      # > 60%
COULEUR_VIE_MOYENNE = COULEURS["JAUNE"]   # 30-60%
COULEUR_VIE_BASSE = COULEURS["ROUGE"]     # < 30%


def formater_nombre(nombre: int) -> str:
    """
    Formate un nombre avec des séparateurs de milliers pour améliorer la lisibilité.

    :param nombre: Le nombre à formater
    :return: String formatée avec séparateurs (ex: 1,250)
    """
    return f"{nombre:,}"


def remplacer_accents(texte: str) -> str:
    """
    Remplace les caractères accentués par leurs équivalents ASCII pour éviter les problèmes d'affichage.
    Utilise unicodedata pour une normalisation robuste, similaire à world/data_loader.py.

    :param texte: Texte avec accents
    :return: Texte sans accents
    """
    import unicodedata
    if not texte:
        return ""
    # Normaliser en NFKD (décompose les caractères accentués)
    texte_normalise = unicodedata.normalize('NFKD', texte)
    # Supprimer les caractères combinants (accents)
    texte_sans_accent = ''.join(c for c in texte_normalise if not unicodedata.combining(c))
    return texte_sans_accent


def print_sans_accent(*args, **kwargs):
    """
    Version de print qui remplace automatiquement les accents.
    Utilisez cette fonction au lieu de print() pour éviter les problèmes d'affichage.
    """
    if args:
        args_list = list(args)
        args_list[0] = remplacer_accents(str(args_list[0]))
        print(*args_list, **kwargs)
    else:
        print(**kwargs)


def effacer_console():
    """
    Efface la console pour garder l'écran lisible.
    Utilise les séquences ANSI quand c'est possible.
    """
    # Sous Windows, utiliser la commande système
    if os.name == "nt":
        os.system("cls")
    else:
        # Sur macOS/Linux, utiliser les séquences ANSI directement
        # \033[2J efface tout l'écran, \033[H remet le curseur en haut à gauche
        # \033[3J efface aussi le scrollback buffer sur certains terminaux
        try:
            sys.stdout.write("\033[2J\033[H\033[3J")
            sys.stdout.flush()
        except:
            # Fallback avec clear si les séquences ANSI ne fonctionnent pas
            os.system("clear")


def creer_separateur(longueur: int = 60, style: str = "double") -> str:
    """
    Crée un séparateur visuel pour améliorer la lisibilité.

    :param longueur: Longueur du séparateur (défaut: 60)
    :param style: Style du séparateur ("double", "simple", "epais")
    :return: String du séparateur
    """
    if style == "double":
        return "═" * longueur
    elif style == "simple":
        return "─" * longueur
    elif style == "epais":
        return "█" * longueur
    else:
        return "=" * longueur


def creer_bordure(titre: str, longueur: int = 60, couleur: str = None) -> str:
    """
    Crée une bordure avec un titre centré pour les menus importants.

    :param titre: Titre à afficher
    :param longueur: Longueur de la bordure (défaut: 60)
    :param couleur: Code couleur ANSI (optionnel)
    :return: String de la bordure avec titre
    """
    if couleur is None:
        couleur = COULEURS["BLEU"]
    reset = COULEURS["RESET"]

    # Calculer l'espacement pour centrer le titre
    espace_gauche = (longueur - len(titre) - 2) // 2
    espace_droite = longueur - len(titre) - 2 - espace_gauche

    ligne_haut = f"{couleur}╔{'═' * (longueur - 2)}╗{reset}"
    ligne_titre = f"{couleur}║{' ' * espace_gauche}{titre}{' ' * espace_droite}║{reset}"
    ligne_bas = f"{couleur}╚{'═' * (longueur - 2)}╝{reset}"

    return f"{ligne_haut}\n{ligne_titre}\n{ligne_bas}"


def afficher_titre_menu(titre: str, longueur: int = 60, couleur: str = None):
    """
    Affiche un titre de menu avec bordures améliorées.

    :param titre: Titre du menu
    :param longueur: Longueur de la bordure (défaut: 60)
    :param couleur: Code couleur ANSI (optionnel, défaut: BLEU)
    """
    print(creer_bordure(titre, longueur, couleur))


def afficher_separateur(longueur: int = 60, style: str = "double", couleur: str = None):
    """
    Affiche un séparateur visuel.

    :param longueur: Longueur du séparateur (défaut: 60)
    :param style: Style du séparateur ("double", "simple", "epais")
    :param couleur: Code couleur ANSI (optionnel)
    """
    sep = creer_separateur(longueur, style)
    if couleur:
        print(f"{couleur}{sep}{COULEURS['RESET']}")
    else:
        print(sep)


def afficher_message_confirmation(message: str, type_message: str = "succes"):
    """
    Affiche un message de confirmation avec couleur appropriée.

    :param message: Message à afficher
    :param type_message: Type de message ("succes", "erreur", "info", "avertissement")
    """
    couleurs_type = {
        "succes": COULEURS["VERT"],
        "erreur": COULEURS["ROUGE"],
        "info": COULEURS["BLEU"],
        "avertissement": COULEURS["JAUNE"]
    }

    emojis_type = {
        "succes": "✓",
        "erreur": "✗",
        "info": "ℹ",
        "avertissement": "⚠"
    }

    couleur = couleurs_type.get(type_message, COULEURS["RESET"])
    emoji = emojis_type.get(type_message, "")

    print(f"{couleur}{emoji} {message}{COULEURS['RESET']}")


# Emojis et couleurs pour les menus
EMOJIS_MENUS = {
    "principal": "🏠",
    "personnage": "👤",
    "capitale": "🏛️",
    "commerce": "💰",
    "inventaire": "🎒",
    "quetes": "📜",
    "exploration": "🗺️",
    "combat": "⚔️",
    "formation": "📚",
    "craft": "🔨",
    "pnj": "👥",
    "sauvegarde": "💾",
    "statistiques": "📊",
    "capacites": "✨",
    "attributs": "⚡",
    "achat": "🛒",
    "vente": "💵",
    "equipement": "🛡️",
    "potion": "🧪",
    "zone": "🌍",
    "donjon": "🏰"
}

COULEURS_MENUS = {
    "principal": COULEURS["CYAN"],
    "personnage": COULEURS["BLEU"],
    "capitale": COULEURS["MAGENTA"],
    "commerce": COULEURS["JAUNE"],
    "inventaire": COULEURS["CYAN"],
    "quetes": COULEURS["VERT"],
    "exploration": COULEURS["BLEU"],
    "combat": COULEURS["ROUGE"],
    "formation": COULEURS["MAGENTA"],
    "craft": COULEURS["JAUNE"],
    "pnj": COULEURS["CYAN"],
    "sauvegarde": COULEURS["GRIS"],
    "statistiques": COULEURS["BLEU"],
    "capacites": COULEURS["MAGENTA"],
    "attributs": COULEURS["JAUNE"],
    "achat": COULEURS["VERT"],
    "vente": COULEURS["JAUNE"],
    "equipement": COULEURS["CYAN"],
    "potion": COULEURS["VERT"],
    "zone": COULEURS["BLEU"],
    "donjon": COULEURS["ROUGE"]
}


def afficher_titre_menu_avec_emoji(titre: str, type_menu: str = None, longueur: int = 60):
    """
    Affiche un titre de menu avec emoji et couleur appropriés.

    :param titre: Titre du menu
    :param type_menu: Type de menu pour déterminer emoji et couleur (optionnel)
    :param longueur: Longueur de la bordure (défaut: 60)
    """
    emoji = EMOJIS_MENUS.get(type_menu, "📋") if type_menu else "📋"
    couleur = COULEURS_MENUS.get(type_menu, COULEURS["BLEU"]) if type_menu else COULEURS["BLEU"]

    titre_complet = f"{emoji} {titre}"
    afficher_titre_menu(titre_complet, longueur, couleur)
