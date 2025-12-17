# menus/utiliser_objets.py
# Système d'utilisation des potions et d'équipement des armes/armures

from typing import Optional
from classes.objet import Objet
from classes.arme import Arme
from classes.armure import Armure
from data.craft_bonus import calculer_effet_avec_bonus
from data.recettes import obtenir_recette
from utils.affichage import (
    afficher_message_confirmation, effacer_console, afficher_titre_menu,
    afficher_separateur, COULEURS, COULEURS_RARETE, afficher_titre_menu_avec_emoji
)


def choisir_objet_combat(joueur) -> bool:
    """
    Permet au joueur de choisir et utiliser un objet (potion) en combat.

    :param joueur: Le personnage joueur
    :return: True si un objet a été utilisé, False sinon
    """

    # Filtrer les objets utilisables (potions)
    objets_utilisables = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "potion":
            objets_utilisables.append((nom_objet, objet))

    if not objets_utilisables:
        print(f"\n{COULEURS['ROUGE']}❌ Vous n'avez aucune potion dans votre inventaire.{COULEURS['RESET']}")
        input("\nAppuyez sur Entrée pour continuer...")
        return False

    print(f"\n{COULEURS['VERT']}🧪 Potions disponibles :{COULEURS['RESET']}")
    print()
    for i, (nom_objet, objet) in enumerate(objets_utilisables, 1):
        # Afficher les effets de la potion
        effets_desc = []
        if hasattr(objet, 'effets') and objet.effets:
            effets = objet.effets
            if effets.get('vie'):
                effets_desc.append(f"+{effets['vie']:.0f} PV")
            if effets.get('mana'):
                effets_desc.append(f"+{effets['mana']:.0f} Mana")
            if effets.get('energie'):
                effets_desc.append(f"+{effets['energie']:.0f} Énergie")
            if effets.get('duree_tours', 0) > 0:
                boosts = []
                if effets.get('boost_attaque'):
                    boosts.append(f"+{effets['boost_attaque']} Att")
                if effets.get('boost_defense'):
                    boosts.append(f"+{effets['boost_defense']} Déf")
                if boosts:
                    effets_desc.append(f"{', '.join(boosts)} ({effets['duree_tours']} tours)")

        effets_str = f" - {', '.join(effets_desc)}" if effets_desc else ""
        quantite = f" (x{objet.quantite})" if objet.quantite > 1 else ""
        print(f"{COULEURS['CYAN']}{i}. {nom_objet}{quantite}{effets_str}{COULEURS['RESET']}")
        print()

    print(f"{COULEURS['GRIS']}{len(objets_utilisables) + 1}. Annuler (r){COULEURS['RESET']}")
    print()

    while True:
        try:
            choix_input = input(f"{COULEURS['VERT']}Votre choix : {COULEURS['RESET']}").strip().lower()
            if choix_input == 'r':
                effacer_console()
                return False

            choix = int(choix_input)
            if 1 <= choix <= len(objets_utilisables):
                nom_objet, objet = objets_utilisables[choix - 1]
                if utiliser_potion(joueur, objet):
                    return True
                else:
                    input("\nAppuyez sur Entrée pour continuer...")
                    return False
            else:
                print(f"{COULEURS['ROUGE']}Choix invalide. Veuillez réessayer.{COULEURS['RESET']}")
        except ValueError:
            print(f"{COULEURS['ROUGE']}Entrée invalide. Veuillez entrer un numéro.{COULEURS['RESET']}")


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


def _filtrer_armes(joueur):
    """Filtre les armes disponibles dans l'inventaire"""
    armes_disponibles = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "arme":
            armes_disponibles.append((nom_objet, objet))
        elif objet.type == "équipement" and hasattr(objet, 'stats'):
            stats = objet.stats
            sous_type = getattr(objet, 'sous_type', None)
            if (stats.get('degats_base') is not None and stats.get('degats_base') != 0) or \
               (sous_type and sous_type in ['epee', 'hache', 'dague', 'baton']):
                armes_disponibles.append((nom_objet, objet))
    return armes_disponibles


def _filtrer_armures_par_type(joueur, sous_type_cible):
    """Filtre les armures d'un type spécifique (torse, casque, bottes)"""
    armures_disponibles = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "armure":
            # Si c'est une armure générique, vérifier le sous_type
            sous_type = getattr(objet, 'sous_type', None)
            if sous_type == sous_type_cible:
                armures_disponibles.append((nom_objet, objet))
        elif objet.type == "équipement" and hasattr(objet, 'stats'):
            stats = objet.stats
            sous_type = getattr(objet, 'sous_type', None)
            if sous_type == sous_type_cible:
                armures_disponibles.append((nom_objet, objet))
    return armures_disponibles


def _afficher_objet_equipement(objet, index, avec_sous_type=False):
    """Affiche un objet équipement avec sa rareté et ses stats"""
    affichage = f"{index}. {objet.nom}"

    # Ajouter la rareté avec couleur
    if hasattr(objet, 'rarete') and objet.rarete:
        rarete_lower = str(objet.rarete).lower().strip()
        couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
        rarete_upper = str(objet.rarete).strip().upper()
        affichage += f" [{couleur}{rarete_upper}{COULEURS["RESET"]}]"

    # Ajouter le sous-type si demandé
    if avec_sous_type:
        sous_type = getattr(objet, 'sous_type', None)
        if sous_type:
            affichage += f" ({sous_type.capitalize()})"

    print(affichage)

    # Afficher les stats
    if hasattr(objet, 'stats'):
        stats = objet.stats
        stats_str = []

        if stats.get('degats_base') is not None and stats.get('degats_base') != 0:
            stats_str.append(f"Dégâts: +{stats['degats_base']}")
        if stats.get('bonus_defense') is not None and stats.get('bonus_defense') != 0:
            stats_str.append(f"Défense: +{stats['bonus_defense']}")
        if stats.get('bonus_force') is not None and stats.get('bonus_force') != 0:
            stats_str.append(f"Force: +{stats['bonus_force']}")
        if stats.get('bonus_agilite') is not None and stats.get('bonus_agilite') != 0:
            stats_str.append(f"Agilité: +{stats['bonus_agilite']}")
        if stats.get('bonus_vitalite') is not None and stats.get('bonus_vitalite') != 0:
            stats_str.append(f"Vitalité: +{stats['bonus_vitalite']}")
        if stats.get('bonus_intelligence') is not None and stats.get('bonus_intelligence') != 0:
            stats_str.append(f"Intelligence: +{stats['bonus_intelligence']}")

        if stats_str:
            print(f"   Stats : {', '.join(stats_str)}")
        else:
            print(f"   Stats : À définir")
    elif objet.description:
        print(f"   {objet.description}")


def _equiper_arme_depuis_liste(joueur, armes_disponibles):
    """Équipe une arme depuis une liste d'armes disponibles"""
    if not armes_disponibles:
        print("\n❌ Vous n'avez aucune arme dans votre inventaire.")
        return False

    effacer_console()
    print()
    afficher_titre_menu_avec_emoji("Armes disponibles", "equipement")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()
    for i, (nom_objet, objet) in enumerate(armes_disponibles, 1):
        _afficher_objet_equipement(objet, i)
        print()

    print(f"{len(armes_disponibles) + 1}. ⬅️  Retour (r)")
    print()

    try:
        choix_input = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            effacer_console()
            return False
        choix = int(choix_input)
        if 1 <= choix <= len(armes_disponibles):
            nom_objet, objet = armes_disponibles[choix - 1]

            if hasattr(objet, 'stats'):
                stats = objet.stats

                def safe_int(value, default=0):
                    if value is None:
                        return default
                    try:
                        return int(value)
                    except (ValueError, TypeError):
                        return default

                rarete_objet = getattr(objet, 'rarete', None)

                arme = Arme(
                    nom=objet.nom,
                    degats_base=safe_int(stats.get('degats_base'), 0),
                    bonus_force=safe_int(stats.get('bonus_force'), 0),
                    bonus_agilite=safe_int(stats.get('bonus_agilite'), 0),
                    bonus_intelligence=safe_int(stats.get('bonus_intelligence'), 0),
                    bonus_vitalite=safe_int(stats.get('bonus_vitalite'), 0),
                    bonus_mana=safe_int(stats.get('bonus_mana'), 0),
                    bonus_energie=safe_int(stats.get('bonus_energie'), 0),
                    bonus_rage=safe_int(stats.get('bonus_rage'), 0),
                    rarete=rarete_objet
                )

                joueur.retirer_objet(nom_objet, 1)
                joueur.equiper_arme(arme)
                afficher_message_confirmation(f"Vous avez équipé {arme.nom}.", "succes")
                input("\nAppuyez sur Entrée pour continuer...")
                return True
            else:
                print(f"❌ Impossible d'équiper {objet.nom} : stats manquantes.")
                input("\nAppuyez sur Entrée pour continuer...")
                return False
        elif choix == len(armes_disponibles) + 1:
            return False
        else:
            print("Choix invalide.")
            input("\nAppuyez sur Entrée pour continuer...")
            return False
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return False


def _equiper_armure_depuis_liste(joueur, armures_disponibles, type_nom):
    """Équipe une armure depuis une liste d'armures disponibles"""
    if not armures_disponibles:
        print(f"\n❌ Vous n'avez aucune {type_nom} dans votre inventaire.")
        input("\nAppuyez sur Entrée pour continuer...")
        return False

    effacer_console()
    print()
    afficher_titre_menu_avec_emoji(f"{type_nom.capitalize()}s disponibles", "equipement")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()
    for i, (nom_objet, objet) in enumerate(armures_disponibles, 1):
        _afficher_objet_equipement(objet, i, avec_sous_type=True)
        print()

    print(f"{len(armures_disponibles) + 1}. ⬅️  Retour (r)")
    print()

    try:
        choix_input = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            effacer_console()
            return False
        choix = int(choix_input)
        if 1 <= choix <= len(armures_disponibles):
            nom_objet, objet = armures_disponibles[choix - 1]

            sous_type = getattr(objet, 'sous_type', None)
            if not sous_type:
                recette = obtenir_recette(objet.nom)
                if recette:
                    sous_type = recette.get('sous_type')

            if not sous_type:
                print(f"❌ Impossible de déterminer le type d'armure pour {objet.nom}.")
                input("\nAppuyez sur Entrée pour continuer...")
                return False

            if hasattr(objet, 'stats'):
                stats = objet.stats

                def safe_int(value, default=0):
                    if value is None:
                        return default
                    try:
                        return int(value)
                    except (ValueError, TypeError):
                        return default

                rarete_objet = getattr(objet, 'rarete', None)

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
                    bonus_rage=safe_int(stats.get('bonus_rage'), 0),
                    rarete=rarete_objet
                )

                joueur.retirer_objet(nom_objet, 1)
                joueur.equiper_armure(armure)
                afficher_message_confirmation(f"Vous avez équipé {armure.nom}.", "succes")
                input("\nAppuyez sur Entrée pour continuer...")
                return True
            else:
                print(f"❌ Impossible d'équiper {objet.nom} : stats manquantes.")
                input("\nAppuyez sur Entrée pour continuer...")
                return False
        elif choix == len(armures_disponibles) + 1:
            return False
        else:
            print("Choix invalide.")
            input("\nAppuyez sur Entrée pour continuer...")
            return False
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return False


def menu_equiper_equipement(joueur):
    """Menu unifié pour équiper tous les types d'équipements"""
    while True:
        effacer_console()
        afficher_titre_menu("ÉQUIPER UN ÉQUIPEMENT", couleur=COULEURS["CYAN"])
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()

        # Afficher les équipements actuellement équipés
        print("Équipements actuellement équipés :")
        if joueur.arme:
            rarete_affichage = ""
            if joueur.arme.rarete:
                rarete_lower = str(joueur.arme.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                rarete_affichage = f" [{couleur}{joueur.arme.rarete.upper()}{COULEURS["RESET"]}]"
            print(f"  ⚔️  Arme : {joueur.arme.nom}{rarete_affichage}")
        else:
            print(f"  ⚔️  Arme : Aucune")

        if joueur.armure_torse:
            rarete_affichage = ""
            if joueur.armure_torse.rarete:
                rarete_lower = str(joueur.armure_torse.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                rarete_affichage = f" [{couleur}{joueur.armure_torse.rarete.upper()}{COULEURS["RESET"]}]"
            print(f"  🛡️  Torse : {joueur.armure_torse.nom}{rarete_affichage}")
        else:
            print(f"  🛡️  Torse : Aucune")

        if joueur.armure_casque:
            rarete_affichage = ""
            if joueur.armure_casque.rarete:
                rarete_lower = str(joueur.armure_casque.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                rarete_affichage = f" [{couleur}{joueur.armure_casque.rarete.upper()}{COULEURS["RESET"]}]"
            print(f"  🪖 Casque : {joueur.armure_casque.nom}{rarete_affichage}")
        else:
            print(f"  🪖 Casque : Aucun")

        if joueur.armure_bottes:
            rarete_affichage = ""
            if joueur.armure_bottes.rarete:
                rarete_lower = str(joueur.armure_bottes.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                rarete_affichage = f" [{couleur}{joueur.armure_bottes.rarete.upper()}{COULEURS["RESET"]}]"
            print(f"  👢 Bottes : {joueur.armure_bottes.nom}{rarete_affichage}")
        else:
            print(f"  👢 Bottes : Aucunes")

        print()
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()
        print("Choisissez une catégorie :")
        print()
        print("1. ⚔️  Armes")
        print()
        print("2. 🛡️  Armures (Torse)")
        print()
        print("3. 🪖 Casques")
        print()
        print("4. 👢 Bottes")
        print()
        print("5. ⬅️  Retour au menu inventaire (r)")
        print()

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            armes = _filtrer_armes(joueur)
            _equiper_arme_depuis_liste(joueur, armes)
        elif choix == '2':
            armures_torse = _filtrer_armures_par_type(joueur, 'torse')
            _equiper_armure_depuis_liste(joueur, armures_torse, "armure")
        elif choix == '3':
            casques = _filtrer_armures_par_type(joueur, 'casque')
            _equiper_armure_depuis_liste(joueur, casques, "casque")
        elif choix == '4':
            bottes = _filtrer_armures_par_type(joueur, 'bottes')
            _equiper_armure_depuis_liste(joueur, bottes, "bottes")
        elif choix == '5' or choix == 'r':
            break
        else:
            print("Choix invalide. Veuillez reessayer.")
            input("\nAppuyez sur Entree pour continuer...")


# Fonctions de compatibilité (dépréciées mais conservées pour compatibilité)
def equiper_arme_menu(joueur):
    """Menu pour équiper une arme depuis l'inventaire (déprécié, utiliser menu_equiper_equipement)"""
    armes = _filtrer_armes(joueur)
    _equiper_arme_depuis_liste(joueur, armes)


def equiper_armure_menu(joueur):
    """Menu pour équiper une armure depuis l'inventaire (déprécié, utiliser menu_equiper_equipement)"""
    # Utiliser le nouveau système unifié mais seulement pour les armures de torse
    armures_torse = _filtrer_armures_par_type(joueur, 'torse')
    _equiper_armure_depuis_liste(joueur, armures_torse, "armure")
