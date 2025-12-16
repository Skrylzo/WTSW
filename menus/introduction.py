# menus/introduction.py
# Système d'introduction narrative du jeu

from data.histoire_principale import INTRODUCTION_HISTOIRE_PRINCIPALE
from world import obtenir_royaume_du_joueur
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS


def afficher_introduction_globale():
    """Affiche l'introduction de l'histoire principale."""
    effacer_console()
    print()

    # Créer un cadre combiné pour VALDORIA et L'ÉVEIL DES OMBRES
    couleur = COULEURS["BLEU"]
    reset = COULEURS["RESET"]
    longueur = 60

    # Calculer les longueurs réelles des titres
    from utils.affichage import _longueur_sans_codes_ansi
    longueur_valdoria = _longueur_sans_codes_ansi("VALDORIA")
    longueur_eveil = _longueur_sans_codes_ansi("L'ÉVEIL DES OMBRES")
    longueur_max = max(longueur_valdoria, longueur_eveil)
    longueur_necessaire = longueur_max + 4
    longueur_finale = max(longueur, longueur_necessaire)

    # Centrer chaque ligne
    espace_valdoria = longueur_finale - 2 - longueur_valdoria
    espace_gauche_valdoria = espace_valdoria // 2
    espace_droite_valdoria = espace_valdoria - espace_gauche_valdoria

    espace_eveil = longueur_finale - 2 - longueur_eveil
    espace_gauche_eveil = espace_eveil // 2
    espace_droite_eveil = espace_eveil - espace_gauche_eveil

    # Afficher le cadre combiné
    ligne_haut = f"{couleur}╔{'═' * (longueur_finale - 2)}╗{reset}"
    ligne_valdoria = f"{couleur}║{' ' * espace_gauche_valdoria}VALDORIA{' ' * espace_droite_valdoria}║{reset}"
    ligne_eveil = f"{couleur}║{' ' * espace_gauche_eveil}L'ÉVEIL DES OMBRES{' ' * espace_droite_eveil}║{reset}"
    ligne_bas = f"{couleur}╚{'═' * (longueur_finale - 2)}╝{reset}"

    print(ligne_haut)
    print(ligne_valdoria)
    print(ligne_eveil)
    print(ligne_bas)

    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()
    print(INTRODUCTION_HISTOIRE_PRINCIPALE)
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()


def afficher_introduction_royaume(joueur):
    """Affiche l'introduction spécifique au royaume du joueur."""
    effacer_console()
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        return

    print()
    afficher_titre_menu_avec_emoji(f"VOTRE ROYAUME : {royaume_joueur.nom.upper()}", "principal")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    # Introduction spécifique selon le royaume
    introductions_royaumes = {
        "Aerthos": """
Vous êtes né dans le royaume des Elfes, Aerthos, une terre de forêts anciennes et de magie sylvestre.
Votre peuple vit en harmonie avec la nature, mais récemment, des événements troublants ont commencé
à perturber cette paix millénaire. Des disparitions mystérieuses, des symboles étranges gravés
sur les arbres... Quelque chose de sombre se trame dans les profondeurs de la forêt.

Votre mentor, Faelar Éternelbranche, un Gardien de la Forêt respecté, vous a convoqué pour vous
confier une mission urgente. Il semble que vous soyez la personne idéale pour découvrir la vérité
derrière ces événements inquiétants.
""",
        "Khazak-Dûm": """
Vous êtes né dans le royaume des Nains, Khazak-Dûm, une citadelle souterraine creusée dans la
montagne. Votre peuple est réputé pour sa maîtrise de la forge et de l'ingénierie, mais ces
derniers temps, des rumeurs inquiétantes circulent dans les galeries profondes. Des créatures
inconnues rôdent dans les mines abandonnées, et certains artisans parlent de symboles étranges
gravés dans la roche.

Votre mentor, Borina Yer, une maître-forgeronne respectée, vous a appelé dans son atelier.
Elle pense que vous avez les compétences nécessaires pour enquêter sur ces mystères qui menacent
la sécurité du royaume.
""",
        "Luthesia": """
Vous êtes né dans le royaume des Humains, Luthesia, une terre de plaines fertiles et de châteaux
majestueux. Votre peuple est connu pour sa diplomatie et sa capacité à unir les différentes races,
mais récemment, des tensions inexpliquées ont émergé. Des documents secrets ont été volés,
des chevaliers ont disparu, et des rumeurs de trahison circulent dans les couloirs du palais.

Votre mentor, un conseiller de confiance du Roi Magnus, vous a convoqué. Il croit que vous êtes
la personne idéale pour découvrir la vérité et protéger le royaume de ceux qui cherchent à le
détruire de l'intérieur.
""",
        "Vrak'thar": """
Vous êtes né dans le royaume des Démons, Vrak'thar, une terre de cendres et de flammes éternelles.
Votre peuple est puissant et redouté, mais même parmi les démons, certains événements suscitent
l'inquiétude. Des serviteurs ont été corrompus par une force inconnue, des rituels interdits ont
été découverts, et une ombre grandissante menace l'équilibre même du royaume.

Votre mentor, un érudit démoniaque respecté, vous a appelé. Il pense que vous avez la force et
la détermination nécessaires pour affronter cette menace qui dépasse même la compréhension des
démons les plus anciens.
"""
    }

    introduction = introductions_royaumes.get(royaume_joueur.nom, "")
    if introduction:
        print(introduction.strip())
        print()
        print("="*70)
        print()


def donner_premiere_quete(joueur):
    """
    Donne la première quête principale au joueur après l'introduction.
    La première quête de royaume sera donnée par le mentor lors de la première visite à la capitale.
    """
    if not hasattr(joueur, 'systeme_quetes'):
        from menus.quetes import initialiser_systeme_quetes
        joueur.systeme_quetes = initialiser_systeme_quetes()

    # Accepter automatiquement la première quête principale (ou afficher son briefing si déjà acceptée)
    premiere_quete_id = "decouverte_ordre"
    premiere_quete = joueur.systeme_quetes.obtenir_quete(premiere_quete_id)

    quete_a_presenter = None
    if premiere_quete:
        if premiere_quete.statut.value == "disponible":
            success, message = joueur.systeme_quetes.accepter_quete(premiere_quete_id, joueur)
            if success:
                quete_a_presenter = joueur.systeme_quetes.obtenir_quete(premiere_quete_id)
        elif premiere_quete.statut.value == "en_cours":
            quete_a_presenter = premiere_quete

    if quete_a_presenter:
        effacer_console()
        print()
        afficher_titre_menu_avec_emoji("VOTRE PREMIÈRE MISSION", "principal")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        # Remplacer "Les Ombres qui Grandissent" par "📖 Les Ombres qui Grandissent"
        nom_quete = quete_a_presenter.nom
        if "Ombres qui Grandissent" in nom_quete or "ombres qui grandissent" in nom_quete.lower():
            nom_quete = nom_quete.replace("Les Ombres qui Grandissent", "📖  Les Ombres qui Grandissent")
            nom_quete = nom_quete.replace("les Ombres qui Grandissent", "📖  Les Ombres qui Grandissent")
        print(f"\n{nom_quete}")
        print(f"\n{quete_a_presenter.description}")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

        # Informer le joueur qu'il doit aller voir son mentor pour la première quête de royaume
        from world import obtenir_royaume_du_joueur
        from data.mentors_quetes import obtenir_premiere_quete_royaume
        from world.pnj import obtenir_pnj

        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        if royaume_joueur:
            mentor_id, premiere_quete_royaume_id = obtenir_premiere_quete_royaume(royaume_joueur.nom)
            if mentor_id:
                mentor = obtenir_pnj(mentor_id)
                if mentor:
                    print(f"\n💡 Pour commencer votre aventure dans {royaume_joueur.nom}, allez voir")
                    print(f"   {mentor.nom} dans la capitale. Il vous confiera votre première mission.")

        print("\nAppuyez sur Entrée pour continuer...")
        input()


def afficher_introduction_complete(joueur):
    """
    Affiche l'introduction complète du jeu (globale + royaume + première quête).
    """
    # Introduction globale
    afficher_introduction_globale()

    print("\nAppuyez sur Entrée pour continuer...")
    input()

    # Introduction du royaume
    afficher_introduction_royaume(joueur)

    print("\nAppuyez sur Entrée pour commencer votre aventure...")
    input()

    # Donner la première quête
    donner_premiere_quete(joueur)
