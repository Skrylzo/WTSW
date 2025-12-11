# menus/introduction.py
# Système d'introduction narrative du jeu

from data.histoire_principale import INTRODUCTION_HISTOIRE_PRINCIPALE
from world import obtenir_royaume_du_joueur


def afficher_introduction_globale():
    """Affiche l'introduction de l'histoire principale."""
    print("\n" + "="*70)
    print(" " * 20 + "VALDORIA")
    print(" " * 15 + "L'Éveil des Ombres")
    print("="*70)
    print()
    print(INTRODUCTION_HISTOIRE_PRINCIPALE)
    print("="*70)
    print()


def afficher_introduction_royaume(joueur):
    """Affiche l'introduction spécifique au royaume du joueur."""
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        return

    print("\n" + "="*70)
    print(f"Votre Royaume : {royaume_joueur.nom}")
    print("="*70)
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

    # Accepter automatiquement la première quête principale
    premiere_quete_id = "decouverte_ordre"
    premiere_quete = joueur.systeme_quetes.obtenir_quete(premiere_quete_id)

    if premiere_quete and premiere_quete.statut.value == "disponible":
        success, message = joueur.systeme_quetes.accepter_quete(premiere_quete_id, joueur)
        if success:
            print("\n" + "="*70)
            print("📖 VOTRE PREMIÈRE MISSION")
            print("="*70)
            print(f"\n{premiere_quete.nom}")
            print(f"\n{premiere_quete.description}")
            print("\n" + "="*70)

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
