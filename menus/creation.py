# menus/creation.py
# Fonctions de création de personnage

from datetime import datetime
from classes.base_combatant import Personnage
from classes.arme import Arme
from data.races_classes import DEFINITIONS_RACES_CLASSES
from data.armes import DEFINITIONS_ARMES
from .debug import appliquer_bonus_debug
# choisir_arme_depart est défini dans ce fichier

# --- Nouvelle fonction pour choisir l'arme de départ ---
def choisir_arme_depart(joueur):
    print("\n--- Choisissez votre Arme de Départ ---")
    armes_disponibles = list(DEFINITIONS_ARMES.keys())

    if not armes_disponibles:
        print("Aucune arme n'est définie. Le personnage ne sera pas équipé d'arme.")
        return

    for i, arme_id in enumerate(armes_disponibles):
        arme_data = DEFINITIONS_ARMES[arme_id]
        print(f"{i+1}. {arme_data['nom']} (Dégâts: {arme_data['degats_base']})")

    choix_arme = -1
    while choix_arme < 1 or choix_arme > len(armes_disponibles):
        try:
            choix_arme = int(input("Votre choix d'arme : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

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
    print("\n--- Création de Personnage ---")
    while True:
        nom = input("Entrez le nom de votre personnage (entre 3 et 12 caractères) : ").strip()
        if 3 <= len(nom) <= 12:
            break
        print("Le nom doit faire entre 3 et 12 caractères.")

    print("\nChoisissez votre Race :")
    races_disponibles = list(DEFINITIONS_RACES_CLASSES.keys())
    for i, race in enumerate(races_disponibles):
        print(f"{i+1}. {race} : {DEFINITIONS_RACES_CLASSES[race]['description']}")

    choix_race = -1
    while choix_race < 1 or choix_race > len(races_disponibles):
        try:
            choix_race = int(input("Votre choix de race : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    race_choisie = races_disponibles[choix_race - 1]
    # Suppression du print : print(f"Vous avez choisi la race : {race_choisie}")

    print(f"\nChoisissez votre Spécialisation ({race_choisie}) :")
    classes_disponibles = DEFINITIONS_RACES_CLASSES[race_choisie]["classes"]
    specialisations_noms = list(classes_disponibles.keys())

    for i, spec_nom in enumerate(specialisations_noms):
        spec_data = classes_disponibles[spec_nom]
        print(f"{i+1}. {spec_nom} : {spec_data['description']}")

    choix_spec = -1
    while choix_spec < 1 or choix_spec > len(specialisations_noms):
        try:
            choix_spec = int(input("Votre choix de spécialisation : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

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

    print(f"\n{joueur.nom}, un {joueur.race} {joueur.specialisation.nom}, a été créé !")
    joueur.afficher_stats()

    # Appel de la fonction de sélection d'arme après la création du personnage
    choisir_arme_depart(joueur)

    return joueur
