# menus/utiliser_objets.py
# Système d'utilisation des potions et d'équipement des armes/armures

from typing import Optional
from classes.objet import Objet
from classes.arme import Arme
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

    # Boosts temporaires (à implémenter avec le système d'effets)
    duree_tours = effets.get('duree_tours', 0)
    if duree_tours and duree_tours > 0:
        # TODO: Implémenter les effets temporaires avec le système d'effets existant
        if effets.get('boost_attaque'):
            print(f"⚠️  Les boosts temporaires ne sont pas encore implémentés.")
        if effets.get('boost_defense'):
            print(f"⚠️  Les boosts temporaires ne sont pas encore implémentés.")
        if effets.get('boost_vitesse'):
            print(f"⚠️  Les boosts temporaires ne sont pas encore implémentés.")
        if effets.get('boost_critique'):
            print(f"⚠️  Les boosts temporaires ne sont pas encore implémentés.")

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
                arme = Arme(
                    nom=objet.nom,
                    degats_base=int(stats.get('degats_base', 0)),
                    bonus_force=int(stats.get('bonus_force', 0)),
                    bonus_agilite=int(stats.get('bonus_agilite', 0)),
                    bonus_intelligence=int(stats.get('bonus_intelligence', 0)),
                    bonus_vitalite=int(stats.get('bonus_vitalite', 0)),
                    bonus_mana=int(stats.get('bonus_mana', 0)),
                    bonus_energie=int(stats.get('bonus_energie', 0)),
                    bonus_rage=int(stats.get('bonus_rage', 0))
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
    print(f"Armure actuellement équipée : {joueur.armure.nom if hasattr(joueur, 'armure') and joueur.armure else 'Aucune'}")
    print("\nArmures disponibles :")

    for i, (nom_objet, objet) in enumerate(armures_disponibles, 1):
        print(f"{i}. {objet.nom}")
        if objet.description:
            print(f"   {objet.description}")

    print(f"{len(armures_disponibles) + 1}. Retour")

    try:
        choix = int(input("\nVotre choix : "))
        if 1 <= choix <= len(armures_disponibles):
            nom_objet, objet = armures_disponibles[choix - 1]

            # Équiper l'armure (à implémenter dans Personnage)
            if not hasattr(joueur, 'armure'):
                joueur.armure = None

            # Pour l'instant, on stocke juste l'objet
            # TODO: Créer une classe Armure similaire à Arme
            joueur.armure = objet
            print(f"✅ {objet.nom} équipée !")
            print("⚠️  Note : Les bonus de stats des armures ne sont pas encore appliqués.")
        elif choix == len(armures_disponibles) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
