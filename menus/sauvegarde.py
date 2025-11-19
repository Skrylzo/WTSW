# menus/sauvegarde.py
# Fonctions de sauvegarde et chargement

import json
from classes.base_combatant import Personnage
from classes.arme import Arme
from data.armes import DEFINITIONS_ARMES

def sauvegarder_jeu(joueur):
    try:
        data = joueur.sauvegarder_donnees()
        with open(f"saves/{joueur.nom}_save.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"Partie sauvegardée pour {joueur.nom}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def charger_jeu(nom_personnage):
    try:
        with open(f"saves/{nom_personnage}_save.json", "r") as f:
            data = json.load(f)

        arme = None
        if data.get("arme") and data["arme"] in DEFINITIONS_ARMES:
            arme_data = DEFINITIONS_ARMES[data["arme"]]
            arme = Arme(
                nom=arme_data["nom"],
                degats_base=arme_data["degats_base"],
                bonus_force=arme_data.get("bonus_force", 0),
                bonus_agilite=arme_data.get("bonus_agilite", 0),
                bonus_intelligence=arme_data.get("bonus_intelligence", 0),
                bonus_vitalite=arme_data.get("bonus_vitalite", 0),
                bonus_mana=arme_data.get("bonus_mana", 0),
                bonus_energie=arme_data.get("bonus_energie", 0),
                bonus_rage=arme_data.get("bonus_rage", 0)
            )

        joueur = Personnage.from_dict(data)
        if arme:
            joueur.equiper_arme(arme)

        print(f"Partie chargée pour {joueur.nom}.")
        return joueur
    except FileNotFoundError:
        print(f"Aucune sauvegarde trouvée pour {nom_personnage}.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None
