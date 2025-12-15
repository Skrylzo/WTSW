# menus/quetes.py
# Menu des quêtes

from typing import List, Optional

from world import HubFeature, HubCapital
from world.quetes import SystemeQuetes, TypeQuete, StatutQuete
from data.histoire_principale import QUETES_PRINCIPALES, INTRODUCTION_HISTOIRE_PRINCIPALE
from data.quetes_royaume import TOUTES_LES_QUETES_ROYAUME
from data.quetes_secondaires import TOUTES_LES_QUETES_SECONDAIRES
from data.pnjs_quetes import initialiser_pnjs
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS

# Initialiser les PNJ au chargement du module
initialiser_pnjs()


def initialiser_systeme_quetes() -> SystemeQuetes:
    """
    Initialise le système de quêtes avec toutes les quêtes disponibles.
    """
    systeme = SystemeQuetes()

    # Ajouter les quêtes principales
    for quete in QUETES_PRINCIPALES.values():
        systeme.ajouter_quete(quete)

    # Ajouter les quêtes de royaume
    for royaume, quetes in TOUTES_LES_QUETES_ROYAUME.items():
        for quete in quetes:
            systeme.ajouter_quete(quete)

    # Ajouter les quêtes secondaires
    for royaume, quetes in TOUTES_LES_QUETES_SECONDAIRES.items():
        for quete in quetes:
            systeme.ajouter_quete(quete)

    return systeme


def menu_quetes(joueur, hub: HubCapital, features_quetes: List[HubFeature], systeme_quetes: Optional[SystemeQuetes] = None):
    """
    Menu de quêtes : affichage et gestion des quêtes.

    :param joueur: Le personnage joueur
    :param hub: Le hub de la capitale
    :param features_quetes: Liste des features de quêtes (pour futur)
    :param systeme_quetes: Le système de quêtes (sera initialisé si None)
    """
    if systeme_quetes is None:
        systeme_quetes = initialiser_systeme_quetes()

    while True:
        effacer_console()
        afficher_titre_menu_avec_emoji("JOURNAL DE QUÊTES", "quetes")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

        # Menu d'actions
        print(f"\n{COULEURS['VERT']}Options disponibles :{COULEURS['RESET']}")
        print("1. 📋 Voir les quêtes en cours")
        print("2. ✅ Voir les quêtes complétées")
        print("3. 📖 Voir l'histoire principale")
        print("4. ⬅️  Retour (r)")

        choix = input(f"\n{COULEURS['VERT']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            afficher_quetes_en_cours_details(systeme_quetes, joueur)
        elif choix == '2':
            afficher_quetes_completees(systeme_quetes, joueur)
        elif choix == '3':
            afficher_histoire_principale()
        elif choix == '4' or choix == 'r':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def afficher_quetes_disponibles(joueur, systeme_quetes: SystemeQuetes):
    """Affiche les quêtes disponibles pour le joueur."""
    disponibles = systeme_quetes.obtenir_quetes_disponibles(joueur)

    if not disponibles:
        print("\nAucune quête disponible pour le moment.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{'='*60}")
    print("QUÊTES DISPONIBLES")
    print(f"{'='*60}")

    # Séparer par type
    principales = [q for q in disponibles if q.type_quete == TypeQuete.PRINCIPALE]
    royaume = [q for q in disponibles if q.type_quete == TypeQuete.ROYAUME]
    secondaires = [q for q in disponibles if q.type_quete == TypeQuete.SECONDAIRE]

    if principales:
        print("\n📖 QUÊTES PRINCIPALES :")
        for i, quete in enumerate(principales, 1):
            print(f"  {i}. {quete.nom} (Niveau requis : {quete.niveau_requis})")

    if royaume:
        royaume_actuel = getattr(joueur, 'royaume_actuel', None)
        if not royaume_actuel:
            from world import obtenir_royaume_du_joueur
            royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
            royaume_actuel = royaume_joueur.nom if royaume_joueur else "Inconnu"
        print(f"\n🏰 QUÊTES DE ROYAUME ({royaume_actuel}) :")
        for i, quete in enumerate(royaume, 1):
            print(f"  {i+len(principales)}. {quete.nom} (Niveau requis : {quete.niveau_requis})")

    if secondaires:
        royaume_actuel = getattr(joueur, 'royaume_actuel', None)
        if not royaume_actuel:
            from world import obtenir_royaume_du_joueur
            royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
            royaume_actuel = royaume_joueur.nom if royaume_joueur else "Inconnu"
        print(f"\n📜 QUÊTES SECONDAIRES ({royaume_actuel}) :")
        for i, quete in enumerate(secondaires, 1):
            print(f"  {i+len(principales)+len(royaume)}. {quete.nom} (Niveau requis : {quete.niveau_requis})")

    input("\nAppuyez sur Entrée pour continuer...")


def afficher_quetes_en_cours_details(systeme_quetes: SystemeQuetes, joueur):
    """Affiche les détails des quêtes en cours."""
    quetes_en_cours = systeme_quetes.obtenir_quetes_en_cours()

    if not quetes_en_cours:
        print("\nAucune quête en cours.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{'='*60}")
    print("QUÊTES EN COURS")
    print(f"{'='*60}")

    # Afficher la quête principale en cours
    quete_principale = systeme_quetes.obtenir_quete_principale_actuelle()
    if quete_principale:
        print(f"\n📖 QUÊTE PRINCIPALE EN COURS :")
        quete_principale.afficher()

    # Afficher les quêtes de royaume en cours
    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        from world import obtenir_royaume_du_joueur
        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        royaume_actuel = royaume_joueur.nom if royaume_joueur else None

    quetes_royaume_en_cours = [q for q in quetes_en_cours
                               if q.type_quete == TypeQuete.ROYAUME and q.royaume == royaume_actuel]
    if quetes_royaume_en_cours:
        print(f"\n🏰 QUÊTES DE ROYAUME EN COURS ({royaume_actuel}) :")
        for quete in quetes_royaume_en_cours:
            quete.afficher()

    # Afficher les quêtes secondaires en cours
    quetes_secondaires_en_cours = [q for q in quetes_en_cours
                                   if q.type_quete == TypeQuete.SECONDAIRE]
    if quetes_secondaires_en_cours:
        print(f"\n📜 QUÊTES SECONDAIRES EN COURS :")
        for quete in quetes_secondaires_en_cours:
            quete.afficher()

    input("\nAppuyez sur Entrée pour continuer...")


def accepter_quete_menu(joueur, systeme_quetes: SystemeQuetes):
    """Menu pour accepter une quête."""
    disponibles = systeme_quetes.obtenir_quetes_disponibles(joueur)

    if not disponibles:
        print("\nAucune quête disponible pour le moment.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{'='*60}")
    print("ACCEPTER UNE QUÊTE")
    print(f"{'='*60}")

    for i, quete in enumerate(disponibles, 1):
        print(f"{i}. {quete.nom} ({quete.type_quete.value})")

    try:
        choix = int(input("\nChoisissez une quête (numéro) : ").strip())
        if 1 <= choix <= len(disponibles):
            quete = disponibles[choix - 1]
            succes, message = systeme_quetes.accepter_quete(quete.id_quete, joueur)
            print(f"\n{message}")
            if succes:
                print(f"Quête '{quete.nom}' ajoutée à votre journal !")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

    input("\nAppuyez sur Entrée pour continuer...")


def abandonner_quete_menu(systeme_quetes: SystemeQuetes):
    """Menu pour abandonner une quête."""
    quetes_en_cours = systeme_quetes.obtenir_quetes_en_cours()

    if not quetes_en_cours:
        print("\nAucune quête en cours à abandonner.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{'='*60}")
    print("ABANDONNER UNE QUÊTE")
    print(f"{'='*60}")

    for i, quete in enumerate(quetes_en_cours, 1):
        print(f"{i}. {quete.nom}")

    try:
        choix = int(input("\nChoisissez une quête à abandonner (numéro) : ").strip())
        if 1 <= choix <= len(quetes_en_cours):
            quete = quetes_en_cours[choix - 1]
            if systeme_quetes.abandonner_quete(quete.id_quete):
                print(f"\nQuête '{quete.nom}' abandonnée.")
            else:
                print("\nImpossible d'abandonner cette quête.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

    input("\nAppuyez sur Entrée pour continuer...")


def afficher_quetes_completees(systeme_quetes: SystemeQuetes, joueur):
    """Affiche les quêtes complétées."""
    quetes_completees = systeme_quetes.obtenir_quetes_completees()

    if not quetes_completees:
        print("\nAucune quête complétée pour le moment.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{'='*60}")
    print("QUÊTES COMPLÉTÉES")
    print(f"{'='*60}")

    # Afficher les quêtes principales complétées
    principales_completees = [q for q in quetes_completees if q.type_quete == TypeQuete.PRINCIPALE]
    if principales_completees:
        print(f"\n📖 QUÊTES PRINCIPALES COMPLÉTÉES :")
        for quete in principales_completees:
            print(f"\n  ✓ {quete.nom}")
            if quete.recompenses:
                print("    Récompenses obtenues :")
                if "xp" in quete.recompenses:
                    print(f"      - {quete.recompenses['xp']} XP")
                if "or" in quete.recompenses:
                    print(f"      - {quete.recompenses['or']} pièces d'or")
                if "objets" in quete.recompenses:
                    from data.objets import DEFINITIONS_OBJETS
                    for objet_id in quete.recompenses["objets"]:
                        objet_data = DEFINITIONS_OBJETS.get(objet_id)
                        nom_objet = objet_data.get("nom", objet_id) if objet_data else objet_id
                        print(f"      - {nom_objet}")

    # Afficher les quêtes de royaume complétées
    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        from world import obtenir_royaume_du_joueur
        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        royaume_actuel = royaume_joueur.nom if royaume_joueur else None

    quetes_royaume_completees = [q for q in quetes_completees
                                if q.type_quete == TypeQuete.ROYAUME and q.royaume == royaume_actuel]
    if quetes_royaume_completees:
        print(f"\n🏰 QUÊTES DE ROYAUME COMPLÉTÉES ({royaume_actuel}) :")
        for quete in quetes_royaume_completees:
            print(f"\n  ✓ {quete.nom}")
            if quete.recompenses:
                print("    Récompenses obtenues :")
                if "xp" in quete.recompenses:
                    print(f"      - {quete.recompenses['xp']} XP")
                if "or" in quete.recompenses:
                    print(f"      - {quete.recompenses['or']} pièces d'or")
                if "objets" in quete.recompenses:
                    from data.objets import DEFINITIONS_OBJETS
                    for objet_id in quete.recompenses["objets"]:
                        objet_data = DEFINITIONS_OBJETS.get(objet_id)
                        nom_objet = objet_data.get("nom", objet_id) if objet_data else objet_id
                        print(f"      - {nom_objet}")

    # Afficher les quêtes secondaires complétées
    quetes_secondaires_completees = [q for q in quetes_completees
                                    if q.type_quete == TypeQuete.SECONDAIRE]
    if quetes_secondaires_completees:
        print(f"\n📜 QUÊTES SECONDAIRES COMPLÉTÉES :")
        for quete in quetes_secondaires_completees:
            print(f"\n  ✓ {quete.nom}")
            if quete.recompenses:
                print("    Récompenses obtenues :")
                if "xp" in quete.recompenses:
                    print(f"      - {quete.recompenses['xp']} XP")
                if "or" in quete.recompenses:
                    print(f"      - {quete.recompenses['or']} pièces d'or")
                if "objets" in quete.recompenses:
                    from data.objets import DEFINITIONS_OBJETS
                    for objet_id in quete.recompenses["objets"]:
                        objet_data = DEFINITIONS_OBJETS.get(objet_id)
                        nom_objet = objet_data.get("nom", objet_id) if objet_data else objet_id
                        print(f"      - {nom_objet}")

    input("\nAppuyez sur Entrée pour continuer...")


def afficher_histoire_principale():
    """Affiche l'introduction de l'histoire principale."""
    print(f"\n{'='*60}")
    print("HISTOIRE PRINCIPALE")
    print(f"{'='*60}")
    print(INTRODUCTION_HISTOIRE_PRINCIPALE)
    input("\nAppuyez sur Entrée pour continuer...")
