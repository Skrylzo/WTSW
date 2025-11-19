# menus/exploration.py
# Menu d'exploration de Valdoria avec système de chapitres

from world import (
    obtenir_royaume_du_joueur,
    obtenir_hub_du_joueur,
    SystemeChapitres,
    Chapitre,
    TypeChapitre,
)
from combat import deroulement_combat


def menu_exploration_valdoria(joueur):
    """
    Menu principal d'exploration de Valdoria.
    Permet d'explorer les zones débloquées selon les chapitres.
    """
    # Obtenir le royaume du joueur
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        print("Erreur : Impossible de trouver votre royaume.")
        return

    # Pour l'instant, on crée un système de chapitres de base
    # TODO: Charger les chapitres depuis un fichier de configuration
    systeme_chapitres = creer_systeme_chapitres_base(joueur)

    while True:
        chapitre_actuel = systeme_chapitres.obtenir_chapitre_actuel()

        if not chapitre_actuel:
            print("\nErreur : Aucun chapitre actuel disponible.")
            break

        print(f"\n{'='*60}")
        print("--- EXPLORATION DE VALDORIA ---")
        print(f"{'='*60}")

        # Afficher les informations du chapitre actuel
        chapitre_actuel.afficher_info()

        # Afficher l'or du joueur
        from .capitale import afficher_or
        afficher_or(joueur)

        # Afficher les options
        print("\nQue voulez-vous faire ?")
        print("1. Explorer une zone")
        print("2. Informations sur les royaumes")
        print("3. Retour au menu principal")

        choix = input("\nVotre choix : ")

        if choix == '1':
            menu_selection_zone(joueur, systeme_chapitres)
        elif choix == '2':
            afficher_infos_royaumes(joueur)
        elif choix == '3':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_selection_zone(joueur, systeme_chapitres: SystemeChapitres):
    """
    Menu de sélection de zone à explorer.
    """
    chapitre_actuel = systeme_chapitres.obtenir_chapitre_actuel()
    if not chapitre_actuel:
        print("\nAucune zone disponible pour l'instant.")
        return

    zones_accessibles = chapitre_actuel.zones_accessibles

    if not zones_accessibles:
        print("\nAucune zone disponible dans ce chapitre.")
        print("Complétez les objectifs pour débloquer de nouvelles zones.")
        return

    print(f"\n{'='*60}")
    print("--- SÉLECTION DE ZONE ---")
    print(f"{'='*60}")
    print(f"\nChapitre actuel : {chapitre_actuel.numero} - {chapitre_actuel.titre}")
    print(f"Zones disponibles ({len(zones_accessibles)}) :\n")

    # Afficher les zones
    zones_liste = []
    for i, zone_id in enumerate(zones_accessibles, 1):
        est_completee = zone_id in chapitre_actuel.zones_completees
        statut = "✓ Complétée" if est_completee else "○ Disponible"
        print(f"{i}. {zone_id} [{statut}]")
        zones_liste.append(zone_id)

    print(f"{len(zones_liste) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))

        if 1 <= choix <= len(zones_liste):
            zone_choisie = zones_liste[choix - 1]
            explorer_zone(joueur, zone_choisie, systeme_chapitres)
        elif choix == len(zones_liste) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def explorer_zone(joueur, zone_id: str, systeme_chapitres: SystemeChapitres):
    """
    Explore une zone : combat aléatoire ou accès au donjon.
    TODO: Intégrer les vrais biomes et leurs mobs une fois le parser Valdoria créé.
    """
    print(f"\n{'='*60}")
    print(f"--- {zone_id.upper()} ---")
    print(f"{'='*60}\n")

    print(f"Vous explorez {zone_id}...")
    print("(Système d'exploration en développement)")
    print("Pour l'instant, combat de test avec un gobelin basique.\n")

    # Pour l'instant, combat de test
    # TODO: Remplacer par les vrais mobs de la zone une fois le parser créé
    ennemis_a_combattre_ids = ["gobelin_basique"]

    # Lancer le combat
    deroulement_combat(joueur, ennemis_a_combattre_ids)

    # Après le combat, vérifier si le joueur a gagné
    if joueur.est_vivant:
        print(f"\nVous avez exploré {zone_id} avec succès.")
        # TODO: Marquer la zone comme complétée si nécessaire
        # systeme_chapitres.obtenir_chapitre_actuel().completer_zone(zone_id)
    else:
        # Le joueur est déjà téléporté à sa capitale par deroulement_combat
        pass

    input("\nAppuyez sur Entrée pour continuer...")


def afficher_infos_royaumes(joueur):
    """
    Affiche des informations sur les royaumes.
    """
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    hub_joueur = obtenir_hub_du_joueur(joueur.race)

    print(f"\n{'='*60}")
    print("--- INFORMATIONS SUR LES ROYAUMES ---")
    print(f"{'='*60}")

    if royaume_joueur:
        print(f"\nVotre royaume : {royaume_joueur.nom}")
        print(f"Race associée : {royaume_joueur.race_associee}")
        print(f"Capitale : {royaume_joueur.capitale}")
        if royaume_joueur.description:
            print(f"Description : {royaume_joueur.description}")

        if hub_joueur:
            print(f"\nCapitale actuelle : {hub_joueur.nom}")
            print(f"Description : {hub_joueur.description}")

    print(f"\n{'='*60}\n")
    input("Appuyez sur Entrée pour continuer...")


def creer_systeme_chapitres_base(joueur):
    """
    Crée un système de chapitres de base pour le démarrage.
    TODO: Remplacer par un chargement depuis fichier de configuration.
    """
    systeme = SystemeChapitres()

    # Chapitre 1 : Début de l'aventure (zones du royaume d'origine)
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)

    if royaume_joueur:
        # Pour l'instant, on crée des zones de test
        # TODO: Remplacer par les vrais biomes une fois le parser créé
        zones_royaume = [
            f"Biome 1 de {royaume_joueur.nom}",
            f"Biome 2 de {royaume_joueur.nom}",
        ]

        chapitre1 = Chapitre(
            numero=1,
            titre="Les Premiers Pas",
            type_chapitre=TypeChapitre.EXPLORATION_LIBRE,
            description=f"Vous commencez votre aventure dans {royaume_joueur.nom}. "
                       f"Explorez les zones de votre royaume pour progresser.",
            zones_accessibles=zones_royaume,
            objectifs=[],  # Pour l'instant, pas d'objectifs stricts
            chapitre_suivant=2,  # Prochain chapitre (à créer plus tard)
        )
        chapitre1.est_debloque = True
        systeme.ajouter_chapitre(chapitre1)
        systeme.chapitre_actuel_numero = 1

    return systeme
