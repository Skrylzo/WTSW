# menus/exploration.py
# Menu d'exploration de Valdoria avec système de chapitres

from world import (
    obtenir_royaume_du_joueur,
    obtenir_hub_du_joueur,
    SystemeChapitres,
    Chapitre,
    TypeChapitre,
)
from world.data_loader import attacher_biomes_depuis_valdoria
from combat import deroulement_combat


def menu_exploration_valdoria(joueur):
    """
    Menu principal d'exploration de Valdoria.
    Permet d'explorer les zones débloquées selon les chapitres.
    """
    attacher_biomes_depuis_valdoria()
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        print("Erreur : Impossible de trouver votre royaume.")
        return

    # Pour l'instant, on crée un système de chapitres de base
    # TODO: Charger les chapitres depuis un fichier de configuration
    systeme_chapitres = creer_systeme_chapitres_base(joueur, royaume_joueur)

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
        from .monnaie import afficher_or
        afficher_or(joueur)

        # Afficher les options
        print("\nQue voulez-vous faire ?")
        print("1. Explorer une zone")
        print("2. Informations sur les royaumes")
        print("3. Retour au menu principal")

        choix = input("\nVotre choix : ")

        if choix == '1':
            menu_selection_zone(joueur, royaume_joueur, systeme_chapitres)
        elif choix == '2':
            afficher_infos_royaumes(joueur)
        elif choix == '3':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_selection_zone(joueur, royaume, systeme_chapitres: SystemeChapitres):
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

    # Afficher les zones avec leurs niveaux recommandés
    zones_liste = []
    for i, zone_id in enumerate(zones_accessibles, 1):
        est_completee = zone_id in chapitre_actuel.zones_completees
        statut = "✓ Complétée" if est_completee else "○ Disponible"

        # Trouver le biome pour afficher le niveau recommandé
        biome_zone = trouver_biome_par_nom(royaume, zone_id)
        niveau_info = ""
        if biome_zone:
            niveau_info = f" ({biome_zone.afficher_niveau_recommande()})"

        print(f"{i}. {zone_id}{niveau_info} [{statut}]")
        zones_liste.append(zone_id)

    print(f"{len(zones_liste) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))

        if 1 <= choix <= len(zones_liste):
            zone_choisie = zones_liste[choix - 1]
            explorer_zone(joueur, royaume, zone_choisie, systeme_chapitres)
        elif choix == len(zones_liste) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def explorer_zone(joueur, royaume, zone_id: str, systeme_chapitres: SystemeChapitres):
    """
    Explore une zone : combat aléatoire ou accès au donjon.
    TODO: Intégrer les vrais biomes et leurs mobs une fois le parser Valdoria créé.
    """
    print(f"\n{'='*60}")
    print(f"--- {zone_id.upper()} ---")
    print(f"{'='*60}\n")

    biome_cible = trouver_biome_par_nom(royaume, zone_id)

    # Afficher les informations du biome
    if biome_cible:
        if biome_cible.description:
            print(f"Description: {biome_cible.description[:200]}...")  # Afficher les 200 premiers caractères
        print(f"Niveau recommandé: {biome_cible.afficher_niveau_recommande()}")
        print(f"Votre niveau actuel: {joueur.niveau}")

        # Afficher un avertissement et demander confirmation si le niveau est trop faible
        if joueur.niveau < biome_cible.niveau_min:
            print(f"⚠️  Attention: Cette zone est recommandée pour les niveaux {biome_cible.niveau_min}-{biome_cible.niveau_max}. "
                  f"Votre niveau ({joueur.niveau}) est inférieur au minimum recommandé.")
            print()

            while True:
                reponse = input("Voulez-vous continuer malgré tout ? (o/n): ").strip().lower()
                if reponse in ('o', 'oui', 'y', 'yes'):
                    print("Vous décidez de continuer malgré les risques...")
                    print()
                    break
                elif reponse in ('n', 'non', 'no'):
                    print("Vous rebroussez chemin. Il est peut-être sage d'attendre d'être plus fort...")
                    print()
                    return
                else:
                    print("Réponse invalide. Veuillez répondre par 'o' (oui) ou 'n' (non).")
        else:
            print()

    if biome_cible and biome_cible.mobs_ids:
        ennemis_a_combattre_ids = biome_cible.obtenir_mobs_aleatoires(nombre=1)
    else:
        print("(Aucun biome trouvé ou pas de mobs définis, combat de secours)")
        ennemis_a_combattre_ids = ["gobelin_basique"]

    # Lancer le combat
    # Passer le niveau du biome pour le système de bonus de craft
    niveau_biome = biome_cible.niveau_min if biome_cible else None
    deroulement_combat(joueur, ennemis_a_combattre_ids, niveau_biome=niveau_biome)

    # Après le combat, vérifier si le joueur a gagné
    if joueur.est_vivant:
        print(f"\nVous avez exploré {zone_id} avec succès.")
        chapitre = systeme_chapitres.obtenir_chapitre_actuel()
        if chapitre:
            chapitre.completer_zone(zone_id)
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


def creer_systeme_chapitres_base(joueur, royaume_joueur):
    """
    Crée un système de chapitres de base pour le démarrage.
    TODO: Remplacer par un chargement depuis fichier de configuration.
    """
    systeme = SystemeChapitres()

    if royaume_joueur and royaume_joueur.biomes:
        zones_royaume = [biome.nom for biome in royaume_joueur.biomes]
    else:
        nom_royaume = royaume_joueur.nom if royaume_joueur else "votre royaume"
        zones_royaume = [
            f"Biome 1 de {nom_royaume}",
            f"Biome 2 de {nom_royaume}",
        ]

    chapitre1 = Chapitre(
        numero=1,
        titre="Les Premiers Pas",
        type_chapitre=TypeChapitre.EXPLORATION_LIBRE,
        description=f"Vous commencez votre aventure dans {royaume_joueur.nom if royaume_joueur else 'Valdoria'}. "
                   f"Explorez les zones de votre royaume pour progresser.",
        zones_accessibles=zones_royaume,
        objectifs=[],
        chapitre_suivant=2,
    )
    chapitre1.est_debloque = True
    systeme.ajouter_chapitre(chapitre1)
    systeme.chapitre_actuel_numero = 1

    return systeme


def trouver_biome_par_nom(royaume, nom_biome):
    if not royaume:
        return None
    for biome in royaume.biomes:
        if biome.nom == nom_biome:
            return biome
    return None
