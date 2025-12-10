# menus/formation.py
# Système de formation : apprentissage et amélioration des capacités, formation spécialisée

from typing import List

from world import HubFeature, HubCapital
from .monnaie import obtenir_or_joueur, retirer_or, afficher_or


def calculer_prix_apprentissage_capacite(niveau_requis: int) -> int:
    """
    Calcule le prix d'apprentissage d'une capacité en fonction de son niveau requis.
    Le prix augmente de manière exponentielle pour refléter le parcours fait.

    Prix par niveau :
    - Niveau 1 : 100 or
    - Niveau 5 : 1250 or
    - Niveau 10 : 5000 or
    - Niveau 15 : 7500 or (avant-dernière capacité, prix réduit)
    - Niveau 20 : 15000 or (dernière capacité, prix augmenté)

    :param niveau_requis: Niveau requis pour apprendre la capacité
    :return: Prix en or pour apprendre la capacité
    """
    prix_base = 100

    # Prix spéciaux pour les dernières capacités
    if niveau_requis == 20:
        # Dernière capacité : prix élevé
        return 15000
    elif niveau_requis == 15:
        # Avant-dernière capacité : prix réduit
        return 7500

    # Formule standard pour les autres niveaux : prix_base * niveau^2 * 0.5
    prix = int(prix_base * (niveau_requis ** 2) * 0.5)
    # Minimum 100 or
    return max(100, prix)


def obtenir_capacites_disponibles(joueur):
    """
    Retourne les capacités disponibles pour le joueur selon sa classe et son niveau.
    :param joueur: Instance du personnage joueur
    :return: Liste des capacités disponibles (non apprises) avec leurs données
    """
    from data.capacites import TOUTES_LES_CAPACITES_DATA
    from data.races_classes import DEFINITIONS_RACES_CLASSES

    # Obtenir les capacités de la classe du joueur
    race_data = DEFINITIONS_RACES_CLASSES.get(joueur.race, {})
    classe_data = race_data.get('classes', {}).get(joueur.specialisation.nom, {})
    capacites_classe = classe_data.get('capacites_ids', [])

    # Obtenir les IDs des capacités déjà apprises
    capacites_apprises_ids = [cap.id for cap in joueur.capacites_apprises]

    # Filtrer les capacités disponibles
    capacites_disponibles = []
    for cap_id in capacites_classe:
        # Vérifier que la capacité n'est pas déjà apprise
        if cap_id in capacites_apprises_ids:
            continue

        # Vérifier que la capacité existe dans les données
        if cap_id not in TOUTES_LES_CAPACITES_DATA:
            continue

        cap_data = TOUTES_LES_CAPACITES_DATA[cap_id]
        niveau_requis = cap_data.get('niveau_requis', 1)

        # Vérifier que le joueur a le niveau requis
        if joueur.niveau < niveau_requis:
            continue

        # Ajouter la capacité avec son prix
        prix = calculer_prix_apprentissage_capacite(niveau_requis)
        capacites_disponibles.append({
            'id': cap_id,
            'nom': cap_data.get('nom', 'Capacité Inconnue'),
            'description': cap_data.get('description', ''),
            'niveau_requis': niveau_requis,
            'prix': prix
        })

    # Trier par niveau requis puis par nom
    capacites_disponibles.sort(key=lambda x: (x['niveau_requis'], x['nom']))

    return capacites_disponibles


def apprendre_capacite(joueur, cap_id: str) -> bool:
    """
    Apprend une capacité au joueur si les conditions sont remplies.
    :param joueur: Instance du personnage joueur
    :param cap_id: ID de la capacité à apprendre
    :return: True si la capacité a été apprise, False sinon
    """
    from data.capacites import TOUTES_LES_CAPACITES_DATA
    from classes.capacite import Capacite

    # Vérifier que la capacité existe
    if cap_id not in TOUTES_LES_CAPACITES_DATA:
        print(f"❌ Capacité '{cap_id}' introuvable.")
        return False

    # Vérifier que la capacité n'est pas déjà apprise
    capacites_apprises_ids = [cap.id for cap in joueur.capacites_apprises]
    if cap_id in capacites_apprises_ids:
        print(f"❌ Vous connaissez déjà cette capacité.")
        return False

    cap_data = TOUTES_LES_CAPACITES_DATA[cap_id]
    niveau_requis = cap_data.get('niveau_requis', 1)

    # Vérifier le niveau requis
    if joueur.niveau < niveau_requis:
        print(f"❌ Vous devez être niveau {niveau_requis} pour apprendre cette capacité.")
        return False

    # Calculer le prix
    prix = calculer_prix_apprentissage_capacite(niveau_requis)

    # Vérifier que le joueur a assez d'or
    or_actuel = obtenir_or_joueur(joueur)
    if or_actuel < prix:
        print(f"❌ Vous n'avez pas assez d'or. Prix : {prix} or, Vous avez : {or_actuel} or.")
        return False

    # Retirer l'or
    retirer_or(joueur, prix)

    # Créer et ajouter la capacité
    capacite = Capacite(
        id_cap=cap_id,
        nom=cap_data["nom"],
        description=cap_data["description"],
        cout_mana=cap_data.get("cout_mana", 0),
        cout_energie=cap_data.get("cout_energie", 0),
        cout_rage=cap_data.get("cout_rage", 0),
        degats_fixes=cap_data.get("degats_fixes", 0),
        soin_fixe=cap_data.get("soin_fixe", 0),
        effet_data=cap_data.get("effet_data"),
        type_cible=cap_data.get("type_cible", "unique"),
        niveau_requis=cap_data.get("niveau_requis", 1),
        peut_critiquer=cap_data.get("peut_critiquer", False)
    )

    joueur.capacites_apprises.append(capacite)
    print(f"✅ Vous avez appris '{capacite.nom}' pour {prix} or !")
    print(f"   {capacite.description}")
    return True


def calculer_prix_amelioration_capacite(niveau_amelioration: int, niveau_requis_capacite: int) -> int:
    """
    Calcule le prix d'amélioration d'une capacité.
    Le prix augmente avec le niveau d'amélioration et le niveau requis de la capacité.

    :param niveau_amelioration: Niveau actuel d'amélioration (1 = première amélioration)
    :param niveau_requis_capacite: Niveau requis pour apprendre la capacité
    :return: Prix en or pour améliorer la capacité
    """
    # Prix de base : 500 or par niveau d'amélioration
    prix_base = 500 * niveau_amelioration

    # Multiplicateur selon le niveau requis de la capacité
    multiplicateur_niveau = 1 + (niveau_requis_capacite / 20)

    prix = int(prix_base * multiplicateur_niveau)
    return prix


def obtenir_capacites_ameliorables(joueur):
    """
    Retourne les capacités apprises par le joueur qui peuvent être améliorées.
    :param joueur: Instance du personnage joueur
    :return: Liste des capacités améliorables avec leurs informations
    """
    capacites_ameliorables = []

    for cap in joueur.capacites_apprises:
        # Calculer le prix de la prochaine amélioration
        prix_amelioration = calculer_prix_amelioration_capacite(
            cap.niveau_amelioration,
            cap.niveau_requis
        )

        # Calculer les stats améliorées pour l'affichage
        bonus_degats = 0
        bonus_soin = 0

        if cap._degats_base > 0:
            bonus_degats = int(cap._degats_base * 0.20 * cap.niveau_amelioration)

        if cap._soin_base > 0:
            bonus_soin = int(cap._soin_base * 0.20 * cap.niveau_amelioration)

        capacites_ameliorables.append({
            'capacite': cap,
            'prix': prix_amelioration,
            'bonus_degats': bonus_degats,
            'bonus_soin': bonus_soin,
            'niveau_actuel': cap.niveau_amelioration
        })

    # Trier par niveau d'amélioration puis par nom
    capacites_ameliorables.sort(key=lambda x: (x['niveau_actuel'], x['capacite'].nom))

    return capacites_ameliorables


def ameliorer_capacite(joueur, capacite) -> bool:
    """
    Améliore une capacité du joueur.
    :param joueur: Instance du personnage joueur
    :param capacite: Instance de Capacite à améliorer
    :return: True si l'amélioration a réussi, False sinon
    """
    # Calculer le prix
    prix = calculer_prix_amelioration_capacite(
        capacite.niveau_amelioration,
        capacite.niveau_requis
    )

    # Vérifier que le joueur a assez d'or
    or_actuel = obtenir_or_joueur(joueur)
    if or_actuel < prix:
        print(f"❌ Vous n'avez pas assez d'or. Prix : {prix} or, Vous avez : {or_actuel} or.")
        return False

    # Retirer l'or
    retirer_or(joueur, prix)

    # Améliorer la capacité
    capacite.ameliorer()

    print(f"✅ '{capacite.obtenir_nom_avec_niveau()}' a été améliorée pour {prix} or !")

    # Afficher les nouvelles stats
    if capacite.degats_fixes > 0:
        print(f"   Dégâts : {capacite.degats_fixes} (+{int(capacite._degats_base * 0.20 * (capacite.niveau_amelioration - 1))})")
    if capacite.soin_fixe > 0:
        print(f"   Soin : {capacite.soin_fixe} (+{int(capacite._soin_base * 0.20 * (capacite.niveau_amelioration - 1))})")

    return True


def obtenir_bonus_formation_classe(classe_nom: str):
    """
    Retourne les bonus de formation spécialisée disponibles pour une classe.
    :param classe_nom: Nom de la classe
    :return: Liste des bonus disponibles avec leurs prix et descriptions
    """
    bonus_disponibles = {
        "Paladin": [
            {
                "nom": "Maîtrise du Bouclier",
                "description": "Augmente la défense de +5",
                "prix": 2000,
                "bonus": {"defense": 5},
                "id": "maitrise_bouclier"
            },
            {
                "nom": "Ferveur Divine",
                "description": "Augmente la force de +3 et l'intelligence de +2",
                "prix": 3000,
                "bonus": {"force": 3, "intelligence": 2},
                "id": "ferveur_divine"
            },
            {
                "nom": "Protection Céleste",
                "description": "Augmente la vitalité de +5 et la défense de +3",
                "prix": 4000,
                "bonus": {"vitalite": 5, "defense": 3},
                "id": "protection_celeste"
            }
        ],
        "Invocateur": [
            {
                "nom": "Maîtrise Arcanique",
                "description": "Augmente l'intelligence de +5",
                "prix": 2000,
                "bonus": {"intelligence": 5},
                "id": "maitrise_arcanique"
            },
            {
                "nom": "Lien Éthéré Renforcé",
                "description": "Augmente l'agilité de +3 et l'intelligence de +2",
                "prix": 3000,
                "bonus": {"agilite": 3, "intelligence": 2},
                "id": "lien_ethere_renforce"
            },
            {
                "nom": "Domination des Essences",
                "description": "Augmente l'intelligence de +5 et la vitalité de +3",
                "prix": 4000,
                "bonus": {"intelligence": 5, "vitalite": 3},
                "id": "domination_essences"
            }
        ],
        "Duelliste": [
            {
                "nom": "Précision Létale",
                "description": "Augmente l'agilité de +5",
                "prix": 2000,
                "bonus": {"agilite": 5},
                "id": "precision_letale"
            },
            {
                "nom": "Rapidité Fulgurante",
                "description": "Augmente la force de +3 et l'agilité de +2",
                "prix": 3000,
                "bonus": {"force": 3, "agilite": 2},
                "id": "rapidite_fulgurante"
            },
            {
                "nom": "Maître de l'Épée",
                "description": "Augmente la force de +5 et l'agilité de +3",
                "prix": 4000,
                "bonus": {"force": 5, "agilite": 3},
                "id": "maitre_epee"
            }
        ],
        "Dévoreur d'Âme": [
            {
                "nom": "Appétit Vorace",
                "description": "Augmente la force de +5",
                "prix": 2000,
                "bonus": {"force": 5},
                "id": "appetit_vorace"
            },
            {
                "nom": "Drain de Vie Amélioré",
                "description": "Augmente la vitalité de +3 et la force de +2",
                "prix": 3000,
                "bonus": {"vitalite": 3, "force": 2},
                "id": "drain_vie_ameliore"
            },
            {
                "nom": "Consommation Totale",
                "description": "Augmente la force de +5 et la vitalité de +3",
                "prix": 4000,
                "bonus": {"force": 5, "vitalite": 3},
                "id": "consommation_totale"
            }
        ],
        "Corrupteur": [
            {
                "nom": "Corruption Profonde",
                "description": "Augmente l'intelligence de +5",
                "prix": 2000,
                "bonus": {"intelligence": 5},
                "id": "corruption_profonde"
            },
            {
                "nom": "Malédiction Renforcée",
                "description": "Augmente l'agilité de +3 et l'intelligence de +2",
                "prix": 3000,
                "bonus": {"agilite": 3, "intelligence": 2},
                "id": "malediction_renforcee"
            },
            {
                "nom": "Domination Démoniaque",
                "description": "Augmente l'intelligence de +5 et l'agilité de +3",
                "prix": 4000,
                "bonus": {"intelligence": 5, "agilite": 3},
                "id": "domination_demoniaque"
            }
        ],
        "Cendrelame": [
            {
                "nom": "Flamme Intérieure",
                "description": "Augmente la force de +5",
                "prix": 2000,
                "bonus": {"force": 5},
                "id": "flamme_interieure"
            },
            {
                "nom": "Rage Incandescente",
                "description": "Augmente l'agilité de +3 et la force de +2",
                "prix": 3000,
                "bonus": {"agilite": 3, "force": 2},
                "id": "rage_incandescente"
            },
            {
                "nom": "Cendres Éternelles",
                "description": "Augmente la force de +5 et l'agilité de +3",
                "prix": 4000,
                "bonus": {"force": 5, "agilite": 3},
                "id": "cendres_eternelles"
            }
        ],
        "Garde-Ancien": [
            {
                "nom": "Protection Ancestrale",
                "description": "Augmente la défense de +5",
                "prix": 2000,
                "bonus": {"defense": 5},
                "id": "protection_ancestrale"
            },
            {
                "nom": "Force des Anciens",
                "description": "Augmente la vitalité de +3 et la défense de +2",
                "prix": 3000,
                "bonus": {"vitalite": 3, "defense": 2},
                "id": "force_anciens"
            },
            {
                "nom": "Résilience Légendaire",
                "description": "Augmente la vitalité de +5 et la défense de +3",
                "prix": 4000,
                "bonus": {"vitalite": 5, "defense": 3},
                "id": "resilience_legendaire"
            }
        ],
        "Archimage": [
            {
                "nom": "Maîtrise Élémentaire",
                "description": "Augmente l'intelligence de +5",
                "prix": 2000,
                "bonus": {"intelligence": 5},
                "id": "maitrise_elementaire"
            },
            {
                "nom": "Sagesse des Arcanes",
                "description": "Augmente l'intelligence de +3 et la vitalité de +2",
                "prix": 3000,
                "bonus": {"intelligence": 3, "vitalite": 2},
                "id": "sagesse_arcanes"
            },
            {
                "nom": "Puissance Arcanique",
                "description": "Augmente l'intelligence de +5 et la vitalité de +3",
                "prix": 4000,
                "bonus": {"intelligence": 5, "vitalite": 3},
                "id": "puissance_arcanique"
            }
        ],
        "Rôdeur": [
            {
                "nom": "Instinct Sauvage",
                "description": "Augmente l'agilité de +5",
                "prix": 2000,
                "bonus": {"agilite": 5},
                "id": "instinct_sauvage"
            },
            {
                "nom": "Précision de Chasseur",
                "description": "Augmente l'agilité de +3 et la force de +2",
                "prix": 3000,
                "bonus": {"agilite": 3, "force": 2},
                "id": "precision_chasseur"
            },
            {
                "nom": "Maîtrise de la Nature",
                "description": "Augmente l'agilité de +5 et la force de +3",
                "prix": 4000,
                "bonus": {"agilite": 5, "force": 3},
                "id": "maitrise_nature"
            }
        ],
        "Forgeron Runique": [
            {
                "nom": "Maîtrise de la Forge",
                "description": "Augmente la force de +5",
                "prix": 2000,
                "bonus": {"force": 5},
                "id": "maitrise_forge"
            },
            {
                "nom": "Runes Ancestrales",
                "description": "Augmente la force de +3 et l'intelligence de +2",
                "prix": 3000,
                "bonus": {"force": 3, "intelligence": 2},
                "id": "runes_ancestrales"
            },
            {
                "nom": "Artisanat Légendaire",
                "description": "Augmente la force de +5 et l'intelligence de +3",
                "prix": 4000,
                "bonus": {"force": 5, "intelligence": 3},
                "id": "artisanat_legendaire"
            }
        ],
        "Ingénieur": [
            {
                "nom": "Innovation Technique",
                "description": "Augmente l'intelligence de +5",
                "prix": 2000,
                "bonus": {"intelligence": 5},
                "id": "innovation_technique"
            },
            {
                "nom": "Précision Mécanique",
                "description": "Augmente l'intelligence de +3 et l'agilité de +2",
                "prix": 3000,
                "bonus": {"intelligence": 3, "agilite": 2},
                "id": "precision_mecanique"
            },
            {
                "nom": "Génie Inventif",
                "description": "Augmente l'intelligence de +5 et l'agilité de +3",
                "prix": 4000,
                "bonus": {"intelligence": 5, "agilite": 3},
                "id": "genie_inventif"
            }
        ],
        "Berserker": [
            {
                "nom": "Rage Incontrôlable",
                "description": "Augmente la force de +5",
                "prix": 2000,
                "bonus": {"force": 5},
                "id": "rage_incontrolee"
            },
            {
                "nom": "Fureur Sauvage",
                "description": "Augmente la force de +3 et la vitalité de +2",
                "prix": 3000,
                "bonus": {"force": 3, "vitalite": 2},
                "id": "fureur_sauvage"
            },
            {
                "nom": "Berserker Légendaire",
                "description": "Augmente la force de +5 et la vitalité de +3",
                "prix": 4000,
                "bonus": {"force": 5, "vitalite": 3},
                "id": "berserker_legendaire"
            }
        ]
    }

    return bonus_disponibles.get(classe_nom, [])


def menu_formation_specialisee(joueur):
    """
    Menu de formation spécialisée par classe.
    Permet d'acheter des bonus permanents spécifiques à la classe du joueur.
    """
    classe_nom = joueur.specialisation.nom
    bonus_disponibles = obtenir_bonus_formation_classe(classe_nom)

    if not bonus_disponibles:
        print(f"\n❌ Aucune formation spécialisée disponible pour la classe '{classe_nom}'.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Initialiser la liste des bonus achetés si elle n'existe pas
    if not hasattr(joueur, 'bonus_formation_achetes'):
        joueur.bonus_formation_achetes = []

    while True:
        print(f"\n{'='*60}")
        print(f"--- FORMATION SPÉCIALISÉE : {classe_nom.upper()} ---")
        print(f"{'='*60}")
        afficher_or(joueur)

        print(f"\n📖 Bonus disponibles pour votre classe :\n")

        bonus_a_afficher = []
        for i, bonus in enumerate(bonus_disponibles, 1):
            deja_achete = bonus['id'] in joueur.bonus_formation_achetes

            if deja_achete:
                print(f"{i}. ✅ {bonus['nom']} (DÉJÀ ACHETÉ)")
            else:
                print(f"{i}. {bonus['nom']} - {bonus['prix']} or")
                bonus_a_afficher.append((i, bonus))

            print(f"   {bonus['description']}")

            # Afficher les bonus détaillés
            bonus_details = []
            if "force" in bonus['bonus']:
                bonus_details.append(f"Force +{bonus['bonus']['force']}")
            if "agilite" in bonus['bonus']:
                bonus_details.append(f"Agilité +{bonus['bonus']['agilite']}")
            if "vitalite" in bonus['bonus']:
                bonus_details.append(f"Vitalité +{bonus['bonus']['vitalite']}")
            if "intelligence" in bonus['bonus']:
                bonus_details.append(f"Intelligence +{bonus['bonus']['intelligence']}")
            if "defense" in bonus['bonus']:
                bonus_details.append(f"Défense +{bonus['bonus']['defense']}")

            if bonus_details:
                print(f"   Bonus : {', '.join(bonus_details)}")

        print(f"{len(bonus_disponibles) + 1}. Retour")

        try:
            choix = int(input("\nVotre choix : "))

            if 1 <= choix <= len(bonus_disponibles):
                bonus_choisi = bonus_disponibles[choix - 1]

                # Vérifier si déjà acheté
                if bonus_choisi['id'] in joueur.bonus_formation_achetes:
                    print(f"\n❌ Vous avez déjà acheté '{bonus_choisi['nom']}'.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                # Demander confirmation
                print(f"\nAcheter '{bonus_choisi['nom']}' pour {bonus_choisi['prix']} or ?")
                confirmation = input("Confirmer (o/n) : ").strip().lower()

                if confirmation == 'o':
                    # Vérifier l'or
                    or_actuel = obtenir_or_joueur(joueur)
                    if or_actuel < bonus_choisi['prix']:
                        print(f"❌ Vous n'avez pas assez d'or. Prix : {bonus_choisi['prix']} or, Vous avez : {or_actuel} or.")
                        input("\nAppuyez sur Entrée pour continuer...")
                        continue

                    # Retirer l'or
                    retirer_or(joueur, bonus_choisi['prix'])

                    # Ajouter le bonus à la liste des bonus achetés
                    joueur.bonus_formation_achetes.append(bonus_choisi['id'])

                    # Appliquer les bonus aux attributs du joueur
                    if "force" in bonus_choisi['bonus']:
                        joueur.force += bonus_choisi['bonus']['force']
                    if "agilite" in bonus_choisi['bonus']:
                        joueur.agilite += bonus_choisi['bonus']['agilite']
                    if "vitalite" in bonus_choisi['bonus']:
                        joueur.vitalite += bonus_choisi['bonus']['vitalite']
                    if "intelligence" in bonus_choisi['bonus']:
                        joueur.intelligence += bonus_choisi['bonus']['intelligence']

                    # Appliquer les bonus de défense (si applicable)
                    # Note: La défense sera recalculée automatiquement via mettre_a_jour_stats_apres_attributs

                    # Recalculer les stats
                    joueur.mettre_a_jour_stats_apres_attributs()

                    print(f"✅ Vous avez acheté '{bonus_choisi['nom']}' pour {bonus_choisi['prix']} or !")
                    print(f"   Les bonus ont été appliqués à vos attributs.")
                    input("\nAppuyez sur Entrée pour continuer...")
                else:
                    print("Achat annulé.")
            elif choix == len(bonus_disponibles) + 1:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\n\nRetour au menu précédent...")
            return


def menu_formation(joueur, hub: HubCapital, features_formation: List[HubFeature]):
    """
    Menu de formation : amélioration des compétences.
    Permet d'apprendre de nouvelles capacités, améliorer les existantes, et accéder à la formation spécialisée.
    """
    while True:
        print(f"\n{'='*60}")
        print("--- FORMATION ---")
        print(f"{'='*60}")
        afficher_or(joueur)
        print(f"Niveau : {joueur.niveau}")
        print(f"Classe : {joueur.specialisation.nom}")

        print("\nQue souhaitez-vous faire ?")
        print("1. Apprendre une nouvelle capacité")
        print("2. Améliorer une capacité existante")
        print("3. Formation spécialisée par classe")
        print("4. Retour")

        try:
            choix_menu = input("\nVotre choix : ").strip()

            if choix_menu == '1':
                # Menu d'apprentissage de nouvelles capacités
                capacites_disponibles = obtenir_capacites_disponibles(joueur)

                if not capacites_disponibles:
                    print("\n❌ Aucune capacité disponible pour le moment.")
                    print("   Vous avez déjà appris toutes les capacités accessibles à votre niveau.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                print(f"\n📚 Capacités disponibles ({len(capacites_disponibles)}) :\n")

                for i, cap in enumerate(capacites_disponibles, 1):
                    niveau_info = f"Niveau {cap['niveau_requis']}"
                    prix_info = f"{cap['prix']} or"
                    print(f"{i}. {cap['nom']} ({niveau_info}) - {prix_info}")
                    if cap['description']:
                        print(f"   {cap['description']}")

                print(f"{len(capacites_disponibles) + 1}. Retour")

                try:
                    choix = int(input("\nVotre choix : "))
                    if 1 <= choix <= len(capacites_disponibles):
                        cap_choisie = capacites_disponibles[choix - 1]

                        print(f"\nApprendre '{cap_choisie['nom']}' pour {cap_choisie['prix']} or ?")
                        confirmation = input("Confirmer (o/n) : ").strip().lower()

                        if confirmation == 'o':
                            if apprendre_capacite(joueur, cap_choisie['id']):
                                input("\nAppuyez sur Entrée pour continuer...")
                                continue
                            else:
                                input("\nAppuyez sur Entrée pour continuer...")
                        else:
                            print("Apprentissage annulé.")
                    elif choix == len(capacites_disponibles) + 1:
                        continue
                    else:
                        print("Choix invalide.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            elif choix_menu == '2':
                # Menu d'amélioration des capacités
                capacites_ameliorables = obtenir_capacites_ameliorables(joueur)

                if not capacites_ameliorables:
                    print("\n❌ Aucune capacité à améliorer.")
                    print("   Vous devez d'abord apprendre des capacités.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                print(f"\n⚡ Capacités améliorables ({len(capacites_ameliorables)}) :\n")

                for i, cap_info in enumerate(capacites_ameliorables, 1):
                    cap = cap_info['capacite']
                    niveau_info = f"Niveau {cap_info['niveau_actuel']}"
                    prix_info = f"{cap_info['prix']} or"

                    print(f"{i}. {cap.obtenir_nom_avec_niveau()} - {prix_info}")
                    print(f"   {cap.description}")

                    # Afficher les améliorations
                    if cap_info['bonus_degats'] > 0:
                        print(f"   Dégâts actuels : {cap.degats_fixes} (prochaine amélioration : +{int(cap._degats_base * 0.20)})")
                    if cap_info['bonus_soin'] > 0:
                        print(f"   Soin actuel : {cap.soin_fixe} (prochaine amélioration : +{int(cap._soin_base * 0.20)})")

                print(f"{len(capacites_ameliorables) + 1}. Retour")

                try:
                    choix = int(input("\nVotre choix : "))
                    if 1 <= choix <= len(capacites_ameliorables):
                        cap_info = capacites_ameliorables[choix - 1]
                        cap = cap_info['capacite']

                        print(f"\nAméliorer '{cap.obtenir_nom_avec_niveau()}' pour {cap_info['prix']} or ?")
                        confirmation = input("Confirmer (o/n) : ").strip().lower()

                        if confirmation == 'o':
                            if ameliorer_capacite(joueur, cap):
                                input("\nAppuyez sur Entrée pour continuer...")
                                continue
                            else:
                                input("\nAppuyez sur Entrée pour continuer...")
                        else:
                            print("Amélioration annulée.")
                    elif choix == len(capacites_ameliorables) + 1:
                        continue
                    else:
                        print("Choix invalide.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")

            elif choix_menu == '3':
                # Menu de formation spécialisée par classe
                menu_formation_specialisee(joueur)

            elif choix_menu == '4':
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\n\nRetour au menu précédent...")
            return
