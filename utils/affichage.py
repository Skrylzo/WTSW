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

# Couleurs pour les raretés d'objets (centralisé)
COULEURS_RARETE = {
    "commun": "\033[0m",           # Blanc/par défaut
    "peu commun": "\033[92m",      # Vert clair
    "rare": "\033[94m",             # Bleu
    "épique": "\033[95m",           # Magenta/Violet
    "légendaire": "\033[93m"        # Jaune/Doré
}

# Couleur ocre/dorée pour les prix (jaune foncé)
COULEUR_OR = "\033[33m"  # Jaune foncé/ocre

# Couleurs standardisées pour les stats
COULEURS_STATS = {
    "force": COULEURS["ROUGE"],
    "agilite": COULEURS["CYAN"],
    "vitalite": COULEURS["VERT"],
    "intelligence": COULEURS["MAGENTA"],
    "defense": COULEURS["BLEU"],
    "degats": COULEURS["ROUGE"],
    "vie": COULEURS["VERT"],
    "mana": COULEURS["BLEU"],
    "energie": COULEURS["JAUNE"],
    "rage": COULEURS["ROUGE"]
}


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


def _longueur_sans_codes_ansi(texte: str) -> int:
    """
    Calcule la longueur réelle d'un texte sans les codes ANSI.
    Prend en compte que les emojis prennent généralement 2 caractères de largeur.
    Ignore les caractères combinants (variation selectors, etc.) qui ne prennent pas de largeur.

    Utilise une méthode robuste qui compte TOUS les emojis comme 2 caractères,
    indépendamment de leur east_asian_width, car dans les terminaux modernes,
    tous les emojis prennent 2 colonnes de largeur.

    :param texte: Texte avec potentiellement des codes ANSI
    :return: Longueur réelle du texte visible (en tenant compte de la largeur des emojis)
    """
    import re
    import unicodedata

    # Supprimer tous les codes ANSI (séquences commençant par \033[ ou \x1b[)
    texte_sans_ansi = re.sub(r'\033\[[0-9;]*m|\x1b\[[0-9;]*m', '', texte)

    # Calculer la largeur réelle en tenant compte des emojis
    longueur = 0
    i = 0
    while i < len(texte_sans_ansi):
        char = texte_sans_ansi[i]
        code_point = ord(char)
        category = unicodedata.category(char)

        # Vérifier si le caractère suivant est un variation selector
        # Les emojis avec variation selector peuvent prendre plus de place dans certains terminaux
        has_variation_selector = False
        if i + 1 < len(texte_sans_ansi):
            next_char = texte_sans_ansi[i + 1]
            if unicodedata.category(next_char) == 'Mn' and ord(next_char) == 0xFE0F:
                has_variation_selector = True

        # Ignorer les caractères combinants (variation selectors, etc.)
        # Ces caractères ne prennent pas de largeur visuelle
        if category == 'Mn':  # Mark, nonspacing (comme VARIATION SELECTOR-16)
            i += 1
            continue

        # Détecter les emojis de manière exhaustive
        # TOUS les emojis prennent 2 caractères de largeur dans les terminaux
        # Méthode robuste : utiliser à la fois les plages Unicode ET la catégorie 'So'
        is_emoji = False

        # Vérifier d'abord si c'est dans une plage emoji connue
        dans_plage_emoji = (
            # Emojis de base (Miscellaneous Symbols and Pictographs) - 0x1F300-0x1F9FF
            0x1F300 <= code_point <= 0x1F9FF or
            # Symboles et pictogrammes supplémentaires - 0x1FA00-0x1FAFF
            0x1FA00 <= code_point <= 0x1FAFF or
            # Symboles divers (Miscellaneous Symbols) - 0x2600-0x26FF
            0x2600 <= code_point <= 0x26FF or
            # Symboles supplémentaires (Dingbats) - 0x2700-0x27BF
            0x2700 <= code_point <= 0x27BF or
            # Symboles et pictogrammes (Emoticons) - 0x1F600-0x1F64F
            0x1F600 <= code_point <= 0x1F64F or
            # Symboles de transport et cartes (Transport and Map Symbols) - 0x1F680-0x1F6FF
            0x1F680 <= code_point <= 0x1F6FF or
            # Symboles et pictogrammes étendus A - 0x1FA70-0x1FAFF
            0x1FA70 <= code_point <= 0x1FAFF
        )

        # Si c'est dans une plage emoji ET que c'est un symbole (So), c'est définitivement un emoji
        if dans_plage_emoji and category == 'So':
            is_emoji = True
        # Sinon, si c'est dans une plage emoji, c'est probablement un emoji aussi
        elif dans_plage_emoji:
            is_emoji = True

        # Vérifier si c'est un caractère large (CJK, etc.)
        east_asian = unicodedata.east_asian_width(char)
        is_wide = east_asian in ('F', 'W')

        # TOUS les emojis prennent 2 caractères de largeur, même si east_asian_width = 'N'
        # C'est important car dans les terminaux, les emojis prennent toujours 2 colonnes
        if is_emoji:
            longueur += 2  # Emojis prennent 2 caractères
        elif is_wide:
            longueur += 2  # Caractères CJK pleine largeur
        else:
            longueur += 1  # Caractères normaux

        i += 1

    return longueur


def centrer_texte(texte: str, longueur: int = 60) -> str:
    """
    Centre un texte en tenant compte de la largeur réelle des emojis.
    Utile pour les cadres simples avec séparateurs.

    :param texte: Texte à centrer
    :param longueur: Longueur totale de la ligne
    :return: Texte centré avec espaces appropriés
    """
    longueur_texte_reelle = _longueur_sans_codes_ansi(texte)
    espace_total = longueur - longueur_texte_reelle
    espace_gauche = espace_total // 2
    espace_droite = espace_total - espace_gauche
    return ' ' * espace_gauche + texte + ' ' * espace_droite


def creer_cadre_simple(titre: str, longueur: int = 60, couleur: str = None, style: str = "simple") -> str:
    """
    Crée un cadre simple avec séparateurs (--- TITRE --- ou ==== TITRE ====).
    Prend en compte la largeur réelle des emojis pour un centrage correct.

    :param titre: Titre à afficher
    :param longueur: Longueur totale du cadre
    :param couleur: Code couleur ANSI (optionnel)
    :param style: Style du séparateur ("simple" pour ---, "double" pour ===)
    :return: String du cadre avec titre centré
    """
    if couleur is None:
        couleur = COULEURS["BLEU"]
    reset = COULEURS["RESET"]

    # Calculer la longueur réelle du titre (sans codes ANSI)
    longueur_titre_reelle = _longueur_sans_codes_ansi(titre)

    # Déterminer le séparateur selon le style
    if style == "double":
        separateur = "="
    else:
        separateur = "-"

    # Calculer l'espacement pour centrer le titre
    # Format: "--- TITRE ---" ou "==== TITRE ===="
    # On veut 3 ou 4 caractères de chaque côté
    prefixe = separateur * 3 if style == "simple" else separateur * 4
    suffixe = separateur * 3 if style == "simple" else separateur * 4

    # Longueur totale du titre avec séparateurs et espaces
    longueur_titre_complet = len(prefixe) + 1 + longueur_titre_reelle + 1 + len(suffixe)

    # Calculer l'espacement pour centrer le tout
    espace_total = longueur - longueur_titre_complet
    espace_gauche = espace_total // 2
    espace_droite = espace_total - espace_gauche

    ligne_separateur = f"{couleur}{separateur * longueur}{reset}"
    ligne_titre = f"{couleur}{' ' * espace_gauche}{prefixe} {titre} {suffixe}{' ' * espace_droite}{reset}"

    return f"{ligne_separateur}\n{ligne_titre}\n{ligne_separateur}"


def creer_bordure(titre: str, longueur: int = 60, couleur: str = None) -> str:
    """
    Crée une bordure avec un titre centré pour les menus importants.
    Ajuste automatiquement la largeur si le titre est trop long.

    :param titre: Titre à afficher
    :param longueur: Longueur de la bordure (défaut: 60)
    :param couleur: Code couleur ANSI (optionnel)
    :return: String de la bordure avec titre
    """
    if couleur is None:
        couleur = COULEURS["BLEU"]
    reset = COULEURS["RESET"]

    # Calculer la longueur réelle du titre (sans codes ANSI)
    longueur_titre_reelle = _longueur_sans_codes_ansi(titre)

    # Ajuster la longueur du cadre si le titre est trop long
    # Minimum 60, mais s'adapter si nécessaire (avec marge de 4 caractères pour les bordures)
    longueur_necessaire = longueur_titre_reelle + 4  # 2 pour les bordures + 2 de marge
    longueur_finale = max(longueur, longueur_necessaire)

    # Calculer l'espacement pour centrer le titre
    # longueur - 2 pour les caractères de bordure (║)
    espace_total = longueur_finale - 2 - longueur_titre_reelle
    espace_gauche = espace_total // 2
    espace_droite = espace_total - espace_gauche

    ligne_haut = f"{couleur}╔{'═' * (longueur_finale - 2)}╗{reset}"
    ligne_titre = f"{couleur}║{' ' * espace_gauche}{titre}{' ' * espace_droite}║{reset}"
    ligne_bas = f"{couleur}╚{'═' * (longueur_finale - 2)}╝{reset}"

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
    Affiche un titre de menu avec couleur appropriée.
    Note: Les emojis sont retirés des bordures pour éviter les problèmes d'alignement.

    :param titre: Titre du menu
    :param type_menu: Type de menu pour déterminer couleur (optionnel)
    :param longueur: Longueur de la bordure (défaut: 60)
    """
    couleur = COULEURS_MENUS.get(type_menu, COULEURS["BLEU"]) if type_menu else COULEURS["BLEU"]

    # Afficher uniquement le titre dans la bordure, sans emoji
    afficher_titre_menu(titre, longueur, couleur)
