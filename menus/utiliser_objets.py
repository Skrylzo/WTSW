# menus/utiliser_objets.py
# Système d'utilisation des potions et d'équipement des armes/armures

from typing import Optional
from classes.objet import Objet
from classes.arme import Arme
from classes.armure import Armure
from data.craft_bonus import calculer_effet_avec_bonus
from data.recettes import obtenir_recette


def utiliser_potion(joueur, objet: Objet) -> bool:
    """
    Utilise une potion sur le joueur.

    :param joueur: Le personnage joueur
    :param objet: L'objet potion à utiliser
    :return: True si la potion a été utilisée avec succès, False sinon
    """
    if objet.type != "potion":
        print(f"❌ {objet.nom} n'est pas une potion.")
        return False

    # Récupérer les effets de la potion depuis l'objet
    # Les effets sont stockés dans l'attribut dynamique `effets` créé lors du craft
    if not hasattr(objet, 'effets'):
        # Si la potion n'a pas d'effets définis, essayer de les récupérer depuis la recette
        from data.recettes import TOUTES_LES_RECETTES
        recette = None
        for rec in TOUTES_LES_RECETTES.values():
            if rec['nom'] == objet.nom:
                recette = rec
                break

        if recette:
            effets = recette.get('effets', {})
        else:
            print(f"❌ Impossible de déterminer les effets de {objet.nom}.")
            return False
    else:
        effets = objet.effets

    # Appliquer les effets
    message_effets = []

    # Soin
    if effets.get('vie'):
        montant_soin = effets['vie']
        vie_recuperee = joueur.soigner(montant_soin, afficher_message=False)
        if vie_recuperee > 0:
            message_effets.append(f"+{vie_recuperee:.0f} PV")

    # Mana
    if effets.get('mana'):
        montant_mana = effets['mana']
        mana_avant = joueur.mana
        joueur.mana = min(joueur.mana + montant_mana, joueur.mana_max)
        mana_recuperee = joueur.mana - mana_avant
        if mana_recuperee > 0:
            message_effets.append(f"+{mana_recuperee:.0f} Mana")

    # Énergie
    if effets.get('energie'):
        montant_energie = effets['energie']
        energie_avant = joueur.energie
        joueur.energie = min(joueur.energie + montant_energie, joueur.energie_max)
        energie_recuperee = joueur.energie - energie_avant
        if energie_recuperee > 0:
            message_effets.append(f"+{energie_recuperee:.0f} Énergie")

    # Boosts temporaires (implémentés avec le système d'effets)
    duree_tours = effets.get('duree_tours', 0)
    if duree_tours and duree_tours > 0:
        # Vérifier s'il y a des boosts à appliquer
        boost_attaque = effets.get('boost_attaque', 0) or 0
        boost_defense = effets.get('boost_defense', 0) or 0
        boost_vitesse = effets.get('boost_vitesse', 0) or 0
        boost_critique = effets.get('boost_critique', 0) or 0

        # Si au moins un boost est présent, créer l'effet temporaire
        if boost_attaque > 0 or boost_defense > 0 or boost_vitesse > 0 or boost_critique > 0:
            # Construire la description de l'effet
            boosts_desc = []
            if boost_attaque > 0:
                boosts_desc.append(f"+{boost_attaque} Attaque")
            if boost_defense > 0:
                boosts_desc.append(f"+{boost_defense} Défense")
            if boost_vitesse > 0:
                boosts_desc.append(f"+{boost_vitesse} Vitesse")
            if boost_critique > 0:
                boosts_desc.append(f"+{boost_critique}% Critique")

            description_effet = f"{', '.join(boosts_desc)} pendant {duree_tours} tours"

            # Créer le dictionnaire d'effet pour le système d'effets
            effet_data = {
                "nom": f"Boost de {objet.nom}",
                "description": description_effet,
                "duree": duree_tours,
                "condition": "tour",  # L'effet s'applique chaque tour
                "effet_attaque": boost_attaque,
                "effet_defense": boost_defense,
                "effet_vitesse": boost_vitesse,
                "effet_critique": boost_critique,
                "effet_vie": 0,
                "effet_regen_mana": 0,
                "effet_regen_energie": 0
            }

            # Appliquer l'effet au joueur
            joueur.appliquer_effet(effet_data)

            # Ajouter au message d'effets
            message_effets.append(f"Boost: {description_effet}")

    if message_effets:
        print(f"✅ {objet.nom} utilisée ! ({', '.join(message_effets)})")
        # Retirer la potion de l'inventaire
        joueur.retirer_objet(objet.nom, 1)
        return True
    else:
        print(f"❌ {objet.nom} n'a eu aucun effet.")
        return False


def equiper_arme_menu(joueur):
    """Menu pour équiper une arme depuis l'inventaire"""
    # Filtrer les armes dans l'inventaire
    armes_disponibles = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "arme":
            armes_disponibles.append((nom_objet, objet))

    if not armes_disponibles:
        print("\n❌ Vous n'avez aucune arme dans votre inventaire.")
        return

    print("\n--- Équiper une Arme ---")
    print(f"Arme actuellement équipée : {joueur.arme.nom if joueur.arme else 'Aucune'}")
    print("\nArmes disponibles :")

    for i, (nom_objet, objet) in enumerate(armes_disponibles, 1):
        print(f"{i}. {objet.nom}")
        if objet.description:
            print(f"   {objet.description}")

    print(f"{len(armes_disponibles) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(armes_disponibles):
            nom_objet, objet = armes_disponibles[choix - 1]

            # Convertir l'objet en Arme
            # Les stats sont stockées dans l'attribut dynamique `stats`
            if hasattr(objet, 'stats'):
                stats = objet.stats

                # Fonction helper pour convertir en int en gérant None
                def safe_int(value, default=0):
                    """Convertit une valeur en int, retourne default si None ou invalide"""
                    if value is None:
                        return default
                    try:
                        return int(value)
                    except (ValueError, TypeError):
                        return default

                arme = Arme(
                    nom=objet.nom,
                    degats_base=safe_int(stats.get('degats_base'), 0),
                    bonus_force=safe_int(stats.get('bonus_force'), 0),
                    bonus_agilite=safe_int(stats.get('bonus_agilite'), 0),
                    bonus_intelligence=safe_int(stats.get('bonus_intelligence'), 0),
                    bonus_vitalite=safe_int(stats.get('bonus_vitalite'), 0),
                    bonus_mana=safe_int(stats.get('bonus_mana'), 0),
                    bonus_energie=safe_int(stats.get('bonus_energie'), 0),
                    bonus_rage=safe_int(stats.get('bonus_rage'), 0)
                )
                joueur.equiper_arme(arme)
                print(f"✅ {objet.nom} équipée !")
            else:
                print(f"❌ Impossible d'équiper {objet.nom} : stats manquantes.")
        elif choix == len(armes_disponibles) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def equiper_armure_menu(joueur):
    """Menu pour équiper une armure depuis l'inventaire"""
    # Filtrer les armures dans l'inventaire
    armures_disponibles = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "armure":
            armures_disponibles.append((nom_objet, objet))

    if not armures_disponibles:
        print("\n❌ Vous n'avez aucune armure dans votre inventaire.")
        return

    print("\n--- Équiper une Armure ---")
    # Afficher les armures équipées
    armures_equipees = []
    if hasattr(joueur, 'armure_torse') and joueur.armure_torse:
        armures_equipees.append(f"Torse: {joueur.armure_torse.nom}")
    if hasattr(joueur, 'armure_casque') and joueur.armure_casque:
        armures_equipees.append(f"Casque: {joueur.armure_casque.nom}")
    if hasattr(joueur, 'armure_bottes') and joueur.armure_bottes:
        armures_equipees.append(f"Bottes: {joueur.armure_bottes.nom}")

    if armures_equipees:
        print(f"Armures équipées : {', '.join(armures_equipees)}")
    else:
        print("Aucune armure équipée")
    print("\nArmures disponibles :")

    for i, (nom_objet, objet) in enumerate(armures_disponibles, 1):
        print(f"{i}. {objet.nom}")
        if objet.description:
            print(f"   {objet.description}")

        # Afficher les stats si disponibles
        if hasattr(objet, 'stats'):
            stats = objet.stats
            stats_str = []
            if stats.get('bonus_defense') is not None:
                stats_str.append(f"Défense: +{stats['bonus_defense']}")
            if stats.get('bonus_force') is not None:
                stats_str.append(f"Force: +{stats['bonus_force']}")
            if stats.get('bonus_agilite') is not None:
                stats_str.append(f"Agilité: +{stats['bonus_agilite']}")
            if stats.get('bonus_vitalite') is not None:
                stats_str.append(f"Vitalité: +{stats['bonus_vitalite']}")
            if stats.get('bonus_intelligence') is not None:
                stats_str.append(f"Intelligence: +{stats['bonus_intelligence']}")

            if stats_str:
                print(f"   Stats : {', '.join(stats_str)}")
            else:
                print(f"   Stats : À définir")

    print(f"{len(armures_disponibles) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(armures_disponibles):
            nom_objet, objet = armures_disponibles[choix - 1]

            # Récupérer le sous_type depuis l'objet ou la recette
            sous_type = None
            if hasattr(objet, 'sous_type'):
                sous_type = objet.sous_type
            else:
                # Essayer de récupérer depuis la recette
                recette = obtenir_recette(objet.nom)
                if recette:
                    sous_type = recette.get('sous_type')

            if not sous_type:
                print(f"❌ Impossible de déterminer le type d'armure pour {objet.nom}.")
                return

            # Convertir l'objet en Armure
            if hasattr(objet, 'stats'):
                stats = objet.stats

                # Fonction helper pour convertir en int en gérant None
                def safe_int(value, default=0):
                    """Convertit une valeur en int, retourne default si None ou invalide"""
                    if value is None:
                        return default
                    try:
                        return int(value)
                    except (ValueError, TypeError):
                        return default

                armure = Armure(
                    nom=objet.nom,
                    sous_type=sous_type,
                    bonus_defense=safe_int(stats.get('bonus_defense'), 0),
                    bonus_force=safe_int(stats.get('bonus_force'), 0),
                    bonus_agilite=safe_int(stats.get('bonus_agilite'), 0),
                    bonus_intelligence=safe_int(stats.get('bonus_intelligence'), 0),
                    bonus_vitalite=safe_int(stats.get('bonus_vitalite'), 0),
                    bonus_mana=safe_int(stats.get('bonus_mana'), 0),
                    bonus_energie=safe_int(stats.get('bonus_energie'), 0),
                    bonus_rage=safe_int(stats.get('bonus_rage'), 0)
                )
                joueur.equiper_armure(armure)
                print(f"✅ {objet.nom} équipée !")
            else:
                print(f"❌ Impossible d'équiper {objet.nom} : stats manquantes.")
        elif choix == len(armures_disponibles) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except Exception as e:
        print(f"❌ Erreur lors de l'équipement : {e}")
        import traceback
        traceback.print_exc()
