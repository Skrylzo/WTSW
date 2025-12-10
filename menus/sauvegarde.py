# menus/sauvegarde.py
# Fonctions de sauvegarde et chargement avec système de slots multiples

import json
import os
from datetime import datetime
from typing import Optional, List, Dict
from pathlib import Path

from classes.base_combatant import Personnage
from classes.arme import Arme
from data.armes import DEFINITIONS_ARMES
from world import obtenir_royaume_du_joueur, obtenir_capitale_joueur


# Nombre de slots de sauvegarde par personnage
NOMBRE_SLOTS = 3

# Dossier des sauvegardes
SAVES_DIR = Path("saves")


def _assurer_dossier_saves():
    """Crée le dossier saves s'il n'existe pas."""
    SAVES_DIR.mkdir(exist_ok=True)


def _obtenir_nom_fichier_sauvegarde(nom_personnage: str, slot: int) -> str:
    """Retourne le nom du fichier de sauvegarde pour un personnage et un slot."""
    return f"{nom_personnage}_slot{slot}.json"


def _obtenir_chemin_sauvegarde(nom_personnage: str, slot: int) -> Path:
    """Retourne le chemin complet du fichier de sauvegarde."""
    _assurer_dossier_saves()
    return SAVES_DIR / _obtenir_nom_fichier_sauvegarde(nom_personnage, slot)


def _obtenir_metadonnees_sauvegarde(joueur) -> Dict:
    """
    Crée les métadonnées d'une sauvegarde.

    :param joueur: Instance du personnage joueur
    :return: Dictionnaire avec les métadonnées
    """
    # Obtenir le royaume actuel
    royaume_actuel = None
    if hasattr(joueur, 'royaume_actuel') and joueur.royaume_actuel:
        royaume_actuel = joueur.royaume_actuel
    else:
        royaume = obtenir_royaume_du_joueur(joueur.race)
        if royaume:
            royaume_actuel = royaume.nom

    # Obtenir la capitale actuelle
    capitale_actuelle = None
    hub = obtenir_capitale_joueur(joueur)
    if hub:
        capitale_actuelle = hub.nom

    # Calculer le temps de jeu approximatif (si disponible)
    temps_jeu = None
    if hasattr(joueur, 'temps_jeu_debut'):
        temps_jeu = (datetime.now() - joueur.temps_jeu_debut).total_seconds()

    return {
        "date_sauvegarde": datetime.now().isoformat(),
        "niveau": joueur.niveau,
        "race": joueur.race,
        "specialisation": joueur.specialisation.nom,
        "royaume_actuel": royaume_actuel,
        "capitale_actuelle": capitale_actuelle,
        "temps_jeu_secondes": temps_jeu,
        "or": getattr(joueur, 'or_', 0),
        "xp": joueur.xp,
        "xp_requise": joueur.xp_requise
    }


def sauvegarder_jeu(joueur, slot: int = 1, silencieux: bool = False) -> bool:
    """
    Sauvegarde le jeu dans un slot spécifique.

    :param joueur: Instance du personnage joueur
    :param slot: Numéro du slot (1-3)
    :param silencieux: Si True, n'affiche pas de message de confirmation
    :return: True si la sauvegarde a réussi, False sinon
    """
    if slot < 1 or slot > NOMBRE_SLOTS:
        if not silencieux:
            print(f"Erreur : Le slot doit être entre 1 et {NOMBRE_SLOTS}.")
        return False

    try:
        # Obtenir les données du joueur
        data = joueur.sauvegarder_donnees()

        # Ajouter les métadonnées
        data["metadonnees"] = _obtenir_metadonnees_sauvegarde(joueur)

        # Sauvegarder dans le fichier
        chemin = _obtenir_chemin_sauvegarde(joueur.nom, slot)
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        if not silencieux:
            print(f"✓ Partie sauvegardée dans le slot {slot} pour {joueur.nom}.")
        return True
    except Exception as e:
        if not silencieux:
            print(f"Erreur lors de la sauvegarde : {e}")
        return False


def charger_jeu(nom_personnage: str, slot: int = 1) -> Optional[Personnage]:
    """
    Charge une partie depuis un slot spécifique.

    :param nom_personnage: Nom du personnage
    :param slot: Numéro du slot (1-3)
    :return: Instance de Personnage chargée, ou None en cas d'erreur
    """
    if slot < 1 or slot > NOMBRE_SLOTS:
        print(f"Erreur : Le slot doit être entre 1 et {NOMBRE_SLOTS}.")
        return None

    try:
        chemin = _obtenir_chemin_sauvegarde(nom_personnage, slot)

        if not chemin.exists():
            print(f"Aucune sauvegarde trouvée pour {nom_personnage} dans le slot {slot}.")
            return None

        with open(chemin, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Charger l'arme si disponible
        arme = None
        arme_nom_ou_id = data.get("arme")

        if arme_nom_ou_id:
            # Essayer d'abord avec l'ID (ancien format)
            if arme_nom_ou_id in DEFINITIONS_ARMES:
                arme_data = DEFINITIONS_ARMES[arme_nom_ou_id]
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
            else:
                # Si pas trouvé par ID, chercher par nom (nouveau format)
                arme_trouvee = None
                for arme_id, arme_data in DEFINITIONS_ARMES.items():
                    if arme_data.get("nom") == arme_nom_ou_id:
                        arme_trouvee = arme_data
                        break

                if arme_trouvee:
                    arme = Arme(
                        nom=arme_trouvee["nom"],
                        degats_base=arme_trouvee["degats_base"],
                        bonus_force=arme_trouvee.get("bonus_force", 0),
                        bonus_agilite=arme_trouvee.get("bonus_agilite", 0),
                        bonus_intelligence=arme_trouvee.get("bonus_intelligence", 0),
                        bonus_vitalite=arme_trouvee.get("bonus_vitalite", 0),
                        bonus_mana=arme_trouvee.get("bonus_mana", 0),
                        bonus_energie=arme_trouvee.get("bonus_energie", 0),
                        bonus_rage=arme_trouvee.get("bonus_rage", 0),
                        rarete=arme_trouvee.get("rarete", None)  # Rareté si disponible dans les définitions
                    )
                else:
                    # Arme non trouvée : créer une arme par défaut pour éviter les erreurs
                    print(f"Avertissement: Arme '{arme_nom_ou_id}' introuvable dans DEFINITIONS_ARMES lors du chargement.")
                    print(f"  → Création d'une arme par défaut. Vous pouvez rééquiper une arme depuis votre inventaire.")
                    arme = Arme(nom=arme_nom_ou_id, degats_base=0)

        # Charger le personnage
        joueur = Personnage.from_dict(data)
        if arme:
            joueur.equiper_arme(arme)

        print(f"✓ Partie chargée depuis le slot {slot} pour {joueur.nom}.")
        return joueur
    except FileNotFoundError:
        print(f"Aucune sauvegarde trouvée pour {nom_personnage} dans le slot {slot}.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None


def obtenir_sauvegardes_personnage(nom_personnage: str) -> List[Dict]:
    """
    Retourne la liste des sauvegardes disponibles pour un personnage.

    :param nom_personnage: Nom du personnage
    :return: Liste de dictionnaires avec les informations des sauvegardes
    """
    sauvegardes = []

    for slot in range(1, NOMBRE_SLOTS + 1):
        chemin = _obtenir_chemin_sauvegarde(nom_personnage, slot)

        if chemin.exists():
            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    data = json.load(f)

                metadonnees = data.get("metadonnees", {})

                sauvegardes.append({
                    "slot": slot,
                    "nom_personnage": nom_personnage,
                    "date_sauvegarde": metadonnees.get("date_sauvegarde", "Inconnue"),
                    "niveau": metadonnees.get("niveau", 1),
                    "race": metadonnees.get("race", "Inconnue"),
                    "specialisation": metadonnees.get("specialisation", "Inconnue"),
                    "royaume_actuel": metadonnees.get("royaume_actuel", "Inconnu"),
                    "capitale_actuelle": metadonnees.get("capitale_actuelle", "Inconnue"),
                    "or": metadonnees.get("or", 0),
                    "temps_jeu_secondes": metadonnees.get("temps_jeu_secondes"),
                    "chemin": str(chemin)
                })
            except Exception as e:
                print(f"Erreur lors de la lecture de la sauvegarde slot {slot} : {e}")

    return sauvegardes


def supprimer_sauvegarde(nom_personnage: str, slot: int) -> bool:
    """
    Supprime une sauvegarde spécifique.

    :param nom_personnage: Nom du personnage
    :param slot: Numéro du slot (1-3)
    :return: True si la suppression a réussi, False sinon
    """
    if slot < 1 or slot > NOMBRE_SLOTS:
        print(f"Erreur : Le slot doit être entre 1 et {NOMBRE_SLOTS}.")
        return False

    chemin = _obtenir_chemin_sauvegarde(nom_personnage, slot)

    if not chemin.exists():
        print(f"Aucune sauvegarde trouvée pour {nom_personnage} dans le slot {slot}.")
        return False

    try:
        chemin.unlink()
        print(f"✓ Sauvegarde du slot {slot} supprimée avec succès.")
        return True
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return False


def formater_temps_jeu(secondes: Optional[float]) -> str:
    """
    Formate le temps de jeu en heures, minutes et secondes.

    :param secondes: Nombre de secondes de jeu
    :return: Chaîne formatée (ex: "2h 30m 15s")
    """
    if secondes is None:
        return "Inconnu"

    heures = int(secondes // 3600)
    minutes = int((secondes % 3600) // 60)
    secs = int(secondes % 60)

    if heures > 0:
        return f"{heures}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"


def menu_gestion_sauvegardes(nom_personnage: str) -> Optional[Personnage]:
    """
    Menu de gestion des sauvegardes pour un personnage.

    :param nom_personnage: Nom du personnage
    :return: Instance de Personnage chargée, ou None si aucune action de chargement
    """
    while True:
        print(f"\n{'='*60}")
        print(f"--- GESTION DES SAUVEGARDES - {nom_personnage.upper()} ---")
        print(f"{'='*60}\n")

        # Obtenir les sauvegardes disponibles
        sauvegardes = obtenir_sauvegardes_personnage(nom_personnage)

        # Afficher les slots
        print("Slots de sauvegarde :\n")
        for slot in range(1, NOMBRE_SLOTS + 1):
            sauvegarde = next((s for s in sauvegardes if s["slot"] == slot), None)

            if sauvegarde:
                # Formater la date
                try:
                    date_obj = datetime.fromisoformat(sauvegarde["date_sauvegarde"])
                    date_formatee = date_obj.strftime("%d/%m/%Y %H:%M")
                except:
                    date_formatee = sauvegarde["date_sauvegarde"]

                # Formater le temps de jeu
                temps_jeu = formater_temps_jeu(sauvegarde["temps_jeu_secondes"])

                print(f"Slot {slot} : ✓ OCCUPÉ")
                print(f"  • Date : {date_formatee}")
                print(f"  • Niveau : {sauvegarde['niveau']}")
                print(f"  • Race : {sauvegarde['race']} - {sauvegarde['specialisation']}")
                print(f"  • Royaume : {sauvegarde['royaume_actuel']}")
                print(f"  • Capitale : {sauvegarde['capitale_actuelle']}")
                print(f"  • Or : {sauvegarde['or']:,} pièces")
                print(f"  • Temps de jeu : {temps_jeu}")
            else:
                print(f"Slot {slot} : ✗ VIDE")
            print()

        # Options du menu
        print("Options :")
        print("1-3. Charger depuis le slot 1, 2 ou 3")
        print("4-6. Supprimer le slot 1, 2 ou 3")
        print("7. Retour")

        choix = input("\nVotre choix : ").strip()

        if choix in ['1', '2', '3']:
            slot = int(choix)
            joueur = charger_jeu(nom_personnage, slot)
            if joueur:
                return joueur
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix in ['4', '5', '6']:
            slot = int(choix) - 3  # 4->1, 5->2, 6->3
            sauvegarde = next((s for s in sauvegardes if s["slot"] == slot), None)

            if sauvegarde:
                confirmation = input(f"Êtes-vous sûr de vouloir supprimer la sauvegarde du slot {slot} ? (o/n) : ").strip().lower()
                if confirmation in ('o', 'oui', 'y', 'yes'):
                    supprimer_sauvegarde(nom_personnage, slot)
                else:
                    print("Suppression annulée.")
            else:
                print(f"Aucune sauvegarde dans le slot {slot}.")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == '7':
            return None

        else:
            print("Choix invalide. Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")


def sauvegarder_automatique(joueur) -> bool:
    """
    Effectue une sauvegarde automatique silencieuse dans le slot 1.
    Utilisée lors de l'entrée dans une capitale.

    :param joueur: Instance du personnage joueur
    :return: True si la sauvegarde a réussi, False sinon
    """
    return sauvegarder_jeu(joueur, slot=1, silencieux=True)


def menu_sauvegarde_manuelle(joueur):
    """
    Menu pour sauvegarder manuellement dans un slot spécifique.

    :param joueur: Instance du personnage joueur
    """
    print(f"\n{'='*60}")
    print("--- SAUVEGARDE MANUELLE ---")
    print(f"{'='*60}\n")

    # Afficher les slots existants
    sauvegardes = obtenir_sauvegardes_personnage(joueur.nom)

    print("Slots disponibles :\n")
    for slot in range(1, NOMBRE_SLOTS + 1):
        sauvegarde = next((s for s in sauvegardes if s["slot"] == slot), None)
        if sauvegarde:
            try:
                date_obj = datetime.fromisoformat(sauvegarde["date_sauvegarde"])
                date_formatee = date_obj.strftime("%d/%m/%Y %H:%M")
            except:
                date_formatee = sauvegarde["date_sauvegarde"]
            print(f"Slot {slot} : ✓ Occupé (dernière sauvegarde : {date_formatee})")
        else:
            print(f"Slot {slot} : ✗ Vide")

    print("\nDans quel slot voulez-vous sauvegarder ? (1-3, ou 0 pour annuler)")
    choix = input("Votre choix : ").strip()

    if choix == '0':
        print("Sauvegarde annulée.")
        return

    if choix in ['1', '2', '3']:
        slot = int(choix)
        sauvegarde_existante = next((s for s in sauvegardes if s["slot"] == slot), None)

        if sauvegarde_existante:
            confirmation = input(f"Le slot {slot} contient déjà une sauvegarde. Écraser ? (o/n) : ").strip().lower()
            if confirmation not in ('o', 'oui', 'y', 'yes'):
                print("Sauvegarde annulée.")
                return

        sauvegarder_jeu(joueur, slot=slot)
        input("\nAppuyez sur Entrée pour continuer...")
    else:
        print("Choix invalide.")
        input("\nAppuyez sur Entrée pour continuer...")
