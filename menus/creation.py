# menus/creation.py
# Fonctions de création de personnage

from datetime import datetime
from classes.base_combatant import Personnage
from classes.arme import Arme
from data.races_classes import DEFINITIONS_RACES_CLASSES
from data.armes import DEFINITIONS_ARMES
from .debug import appliquer_bonus_debug
from utils.affichage import COULEURS, afficher_titre_menu_avec_emoji, afficher_separateur, effacer_console

# --- Nouvelle fonction pour choisir l'arme de départ ---
def choisir_arme_depart(joueur):
    print()
    afficher_titre_menu_avec_emoji("Choisissez votre Arme de Départ", "personnage")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    armes_disponibles = list(DEFINITIONS_ARMES.keys())

    if not armes_disponibles:
        print(f"{COULEURS['ROUGE']}Aucune arme n'est définie. Le personnage ne sera pas équipé d'arme.{COULEURS['RESET']}")
        return

    for i, arme_id in enumerate(armes_disponibles):
        arme_data = DEFINITIONS_ARMES[arme_id]
        print(f"{COULEURS['BLEU']}{i+1}.{COULEURS['RESET']} {arme_data['nom']} (Dégâts: {arme_data['degats_base']})")

    choix_arme = -1
    while choix_arme < 1 or choix_arme > len(armes_disponibles):
        try:
            choix_input = input(f"\n{COULEURS['CYAN']}Votre choix d'arme (ou 'r' pour retour) : {COULEURS['RESET']}").strip().lower()
            if choix_input == 'r':
                return  # Retour sans équiper d'arme
            choix_arme = int(choix_input)
        except ValueError:
            print(f"{COULEURS['ROUGE']}Veuillez entrer un nombre valide.{COULEURS['RESET']}")

    arme_choisie_id = armes_disponibles[choix_arme - 1]
    arme_data = DEFINITIONS_ARMES[arme_choisie_id]
    arme = Arme(
        nom=arme_data["nom"],
        degats_base=arme_data["degats_base"],
        bonus_force=arme_data.get("bonus_force", 0),
        bonus_agilite=arme_data.get("bonus_agilite", 0),
        bonus_intelligence=arme_data.get("bonus_intelligence", 0),
        bonus_vitalite=arme_data.get("bonus_vitalite", 0),
        bonus_mana=arme_data.get("bonus_mana", 0),
        bonus_energie=arme_data.get("bonus_energie", 0),
        bonus_rage=arme_data.get("bonus_rage", 0),
        rarete=arme_data.get("rarete", None)  # Rareté si disponible dans les définitions
    )
    joueur.equiper_arme(arme)
    # Suppression du print : print(f"Vous avez équipé : {arme.nom}")


# --- Fonctions de Création de Personnage ---

def creer_personnage():
    from .sauvegarde import obtenir_sauvegardes_personnage, charger_jeu

    effacer_console()
    afficher_titre_menu_avec_emoji("CRÉATION DE PERSONNAGE", "personnage")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    while True:
        nom = input(f"\n{COULEURS['CYAN']}Entrez le nom de votre personnage (entre 3 et 12 caractères, ou 'r' pour retour) : {COULEURS['RESET']}").strip()

        # Permettre le retour
        if nom.lower() == 'r':
            return None

        if len(nom) < 3 or len(nom) > 12:
            print(f"{COULEURS['ROUGE']}Le nom doit faire entre 3 et 12 caractères.{COULEURS['RESET']}")
            continue

        # Vérifier si une sauvegarde existe déjà avec ce nom
        sauvegardes = obtenir_sauvegardes_personnage(nom)
        if sauvegardes:
            print(f"\n{COULEURS['JAUNE']}⚠️  Un personnage nommé '{nom}' existe déjà !{COULEURS['RESET']}")
            print(f"{COULEURS['CYAN']}Voulez-vous charger une sauvegarde existante ? (o/n){COULEURS['RESET']}")
            choix = input().strip().lower()
            if choix in ('o', 'oui', 'y', 'yes'):
                # Charger la première sauvegarde disponible (slot 1 par défaut)
                joueur = charger_jeu(nom, slot=1)
                if joueur:
                    return joueur
                # Si le slot 1 n'existe pas, proposer de choisir
                from .sauvegarde import menu_gestion_sauvegardes
                joueur = menu_gestion_sauvegardes(nom)
                if joueur:
                    return joueur
            else:
                print(f"{COULEURS['ROUGE']}Création annulée. Veuillez choisir un autre nom.{COULEURS['RESET']}")
                continue

        # Nom valide et unique, continuer la création
        break

    # Codes ANSI pour le gras
    GRAS = "\033[1m"
    RESET = COULEURS["RESET"]

    # Emojis pour chaque race
    EMOJIS_RACES = {
        "Elfe": "🌿",
        "Nain": "⛏️",
        "Humain": "👤",
        "Démon": "👹"
    }

    print(f"\n{COULEURS['CYAN']}Choisissez votre Race :{COULEURS['RESET']}")
    print()  # Espacement entre le titre et la première race
    races_disponibles = list(DEFINITIONS_RACES_CLASSES.keys())
    for i, race in enumerate(races_disponibles):
        emoji_race = EMOJIS_RACES.get(race, "👤")
        print(f"{COULEURS['BLEU']}{i+1}.{COULEURS['RESET']} {emoji_race}  {GRAS}{race}{RESET} : {DEFINITIONS_RACES_CLASSES[race]['description']}")
        print()  # Espace entre chaque race

    choix_race = -1
    while choix_race < 1 or choix_race > len(races_disponibles):
        try:
            choix_input = input(f"\n{COULEURS['CYAN']}Votre choix de race (ou 'r' pour retour) : {COULEURS['RESET']}").strip().lower()
            if choix_input == 'r':
                return None
            choix_race = int(choix_input)
        except ValueError:
            print(f"{COULEURS['ROUGE']}Veuillez entrer un nombre valide.{COULEURS['RESET']}")

    race_choisie = races_disponibles[choix_race - 1]
    # Suppression du print : print(f"Vous avez choisi la race : {race_choisie}")

    # Emojis pour chaque classe
    EMOJIS_CLASSES = {
        # Humain
        "Paladin": "🛡️",
        "Invocateur": "🔮",
        "Duelliste": "⚔️",
        # Démon
        "Dévoreur d'Âme": "💀",
        "Corrupteur": "☠️",
        "Cendrelame": "🔥",
        # Elfe
        "Archer Sylvestre": "🏹",
        "Sentinelle des Esprits": "✨",
        "Moissonneur d'Aube": "☀️",
        # Nain
        "Rageborn": "😡",
        "Marchepierre": "🗿",
        "Innovateur Gnomique": "⚙️"
    }

    print(f"\n{COULEURS['CYAN']}Choisissez votre Spécialisation ({race_choisie}) :{COULEURS['RESET']}")
    print()  # Espacement entre le titre et la première classe
    classes_disponibles = DEFINITIONS_RACES_CLASSES[race_choisie]["classes"]
    specialisations_noms = list(classes_disponibles.keys())

    for i, spec_nom in enumerate(specialisations_noms):
        spec_data = classes_disponibles[spec_nom]
        emoji_classe = EMOJIS_CLASSES.get(spec_nom, "⚔️")
        print(f"{COULEURS['BLEU']}{i+1}.{COULEURS['RESET']} {emoji_classe}  {GRAS}{spec_nom}{RESET} : {spec_data['description']}")
        print()  # Espace entre chaque classe

    choix_spec = -1
    while choix_spec < 1 or choix_spec > len(specialisations_noms):
        try:
            choix_input = input(f"\n{COULEURS['CYAN']}Votre choix de spécialisation (ou 'r' pour retour) : {COULEURS['RESET']}").strip().lower()
            if choix_input == 'r':
                return None
            choix_spec = int(choix_input)
        except ValueError:
            print(f"{COULEURS['ROUGE']}Veuillez entrer un nombre valide.{COULEURS['RESET']}")

    specialisation_choisie_nom = specialisations_noms[choix_spec - 1]
    # Suppression du print : print(f"Vous avez choisi la spécialisation : {specialisation_choisie_nom}")


    # Récupérer les stats de départ de la spécialisation choisie
    stats_depart = classes_disponibles[specialisation_choisie_nom]["stats_depart"]
    force = stats_depart["force"]
    agilite = stats_depart["agilite"]
    vitalite = stats_depart["vitalite"]
    intelligence = stats_depart["intelligence"]

    # Créer le personnage avec les stats de départ
    joueur = Personnage(nom, race_choisie, specialisation_choisie_nom, force, agilite, vitalite, intelligence)

    # Initialiser le temps de jeu
    joueur.temps_jeu_debut = datetime.now()

    # Appliquer les bonus de debug si nécessaire
    appliquer_bonus_debug(joueur, nom)

    # Initialiser le système de quêtes et déclencher les quêtes disponibles
    from world.declenchement_quetes import initialiser_quetes_joueur
    initialiser_quetes_joueur(joueur)

    print(f"\n{COULEURS['VERT']}✓ {joueur.nom}, un {joueur.race} {joueur.specialisation.nom}, a été créé !{COULEURS['RESET']}")
    joueur.afficher_stats()

    # Appel de la fonction de sélection d'arme après la création du personnage
    choisir_arme_depart(joueur)

    return joueur
