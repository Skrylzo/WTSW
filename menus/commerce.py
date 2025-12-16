# menus/commerce.py
# Système de commerce : achat et vente d'objets

from typing import List

from world import HubFeature, HubCapital
from classes.objet import Objet
from data.objets import DEFINITIONS_OBJETS
from data.categories_ingredients import INGREDIENTS_SPECIAUX
from .monnaie import obtenir_or_joueur, ajouter_or, retirer_or, afficher_or
from utils.affichage import effacer_console, afficher_titre_menu, afficher_separateur, afficher_message_confirmation, formater_nombre, COULEURS


def calculer_prix_vente(objet: Objet) -> tuple[int, dict]:
    """
    Calcule le prix de vente d'un objet basé sur sa rareté, ses stats/effets réels et son niveau_biome.

    :param objet: L'objet à évaluer
    :return: Tuple (prix_final, details) où details contient les informations sur le calcul
    """
    details = {
        "prix_base": 0,
        "bonus_stats": 0,
        "bonus_niveau": 0,
        "multiplicateur_type": 1.0,
        "prix_final": 0
    }

    # Normaliser la rareté (gérer les variations de casse et les valeurs None)
    rarete_normalisee = None
    if objet.rarete:
        rarete_normalisee = objet.rarete.lower()

    # Prix de base selon la rareté (incluant "peu commun")
    prix_base_rarete = {
        "commun": 10,
        "peu commun": 25,
        "rare": 50,
        "épique": 200,
        "légendaire": 1000
    }

    base = prix_base_rarete.get(rarete_normalisee, 5)
    details["prix_base"] = base

    # Bonus basé sur les stats/effets réels de l'objet
    bonus_stats = 0

    # Pour les potions : évaluer les effets
    if objet.type == "potion" and hasattr(objet, 'effets') and objet.effets:
        effets = objet.effets
        # Valeur des effets de soin
        if effets.get('vie'):
            bonus_stats += int(effets['vie'] * 0.5)  # 0.5 pièce par PV
        if effets.get('mana'):
            bonus_stats += int(effets['mana'] * 0.3)  # 0.3 pièce par Mana
        if effets.get('energie'):
            bonus_stats += int(effets['energie'] * 0.3)  # 0.3 pièce par Énergie

        # Valeur des boosts temporaires (plus précieux)
        duree = effets.get('duree_tours', 0)
        if duree > 0:
            if effets.get('boost_attaque'):
                bonus_stats += int(effets['boost_attaque'] * duree * 2)  # 2 pièces par point par tour
            if effets.get('boost_defense'):
                bonus_stats += int(effets['boost_defense'] * duree * 2)
            if effets.get('boost_vitesse'):
                bonus_stats += int(effets['boost_vitesse'] * duree * 1.5)
            if effets.get('boost_critique'):
                bonus_stats += int(effets['boost_critique'] * duree * 3)  # Critique très précieux

    # Pour les armes/armures : évaluer les stats
    elif objet.type == "équipement" and hasattr(objet, 'stats') and objet.stats:
        stats = objet.stats
        # Valeur des dégâts (pour les armes)
        if stats.get('degats_base') is not None and stats['degats_base'] > 0:
            bonus_stats += int(stats['degats_base'] * 3)  # 3 pièces par point de dégât

        # Valeur des bonus de défense
        if stats.get('bonus_defense') is not None and stats['bonus_defense'] > 0:
            bonus_stats += int(stats['bonus_defense'] * 2)  # 2 pièces par point de défense

        # Valeur des bonus d'attributs (très précieux)
        if stats.get('bonus_force') is not None and stats['bonus_force'] > 0:
            bonus_stats += int(stats['bonus_force'] * 5)  # 5 pièces par point de force
        if stats.get('bonus_agilite') is not None and stats['bonus_agilite'] > 0:
            bonus_stats += int(stats['bonus_agilite'] * 5)
        if stats.get('bonus_vitalite') is not None and stats['bonus_vitalite'] > 0:
            bonus_stats += int(stats['bonus_vitalite'] * 5)
        if stats.get('bonus_intelligence') is not None and stats['bonus_intelligence'] > 0:
            bonus_stats += int(stats['bonus_intelligence'] * 5)

    details["bonus_stats"] = bonus_stats

    # Bonus basé sur le niveau_biome (pour les objets craftés)
    bonus_niveau = 0
    if hasattr(objet, 'niveau_biome') and objet.niveau_biome is not None:
        # 8% de bonus par niveau de biome (objets craftés avec ingrédients de haut niveau valent plus)
        bonus_niveau = int((base + bonus_stats) * (objet.niveau_biome * 0.08))
        details["bonus_niveau"] = bonus_niveau

    # Multiplicateur selon le type
    multiplicateur_type = {
        "matériau": 1.0,
        "potion": 1.5,
        "équipement": 2.0,
        "consommable": 1.2
    }

    multi = multiplicateur_type.get(objet.type, 1.0)
    details["multiplicateur_type"] = multi

    # Calcul du prix final
    prix_final = int((base + bonus_stats + bonus_niveau) * multi)
    details["prix_final"] = prix_final

    return prix_final, details


def menu_commerce(joueur, hub: HubCapital, features_commerce: List[HubFeature]):
    """
    Menu de commerce : achat et vente d'objets.
    """
    while True:
        effacer_console()
        afficher_titre_menu("COMMERCE", couleur=COULEURS["CYAN"])
        afficher_or(joueur)
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print("\nOptions disponibles :")
        print()
        print(f"1. {COULEURS['VERT']}🛒 Acheter des objets{COULEURS['RESET']}")
        print()
        print(f"2. {COULEURS['JAUNE']}💵 Vendre des objets{COULEURS['RESET']}")
        print()
        print(f"3. {COULEURS['GRIS']}⬅️  Retour (r){COULEURS['RESET']}")
        print()

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            menu_achat(joueur, hub, features_commerce)
        elif choix == '2':
            menu_vente(joueur)
        elif choix == '3' or choix == 'r':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_achat(joueur, hub: HubCapital, features_commerce: List[HubFeature]):
    """
    Menu d'achat d'objets.
    TODO: Intégrer les objets disponibles dans les features de commerce.
    """
    effacer_console()
    afficher_titre_menu("ACHAT", couleur=COULEURS["VERT"])
    afficher_or(joueur)
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    # Liste d'objets de base disponibles à l'achat
    objets_disponibles = {
        "Potion de Vie Mineure": {"prix": 50, "id": "potion_de_vie_mineure"},
        "Potion de Mana Mineure": {"prix": 50, "id": "potion_de_mana_mineure"},
    }

    # Ajouter les ingrédients spéciaux (achetables en boutique)
    for nom_ingredient, data_ingredient in INGREDIENTS_SPECIAUX.items():
        if data_ingredient.get("achetable", False):
            prix = data_ingredient.get("prix_base", 10)
            objets_disponibles[nom_ingredient] = {
                "prix": prix,
                "id": None,  # Pas d'ID dans DEFINITIONS_OBJETS, c'est un ingrédient spécial
                "type": "ingredient_special"
            }

    print(f"\n{COULEURS['VERT']}🛒 Objets disponibles :{COULEURS['RESET']}")
    print()
    for i, (nom, data) in enumerate(objets_disponibles.items(), 1):
        emoji_objet = "🧪" if "potion" in nom.lower() else "💎" if "ingredient" in nom.lower() or "eau" in nom.lower() else "📦"
        print(f"{COULEURS['CYAN']}{i}.{COULEURS['RESET']} {emoji_objet} {COULEURS['BLEU']}{nom}{COULEURS['RESET']} - {COULEURS['JAUNE']}{data['prix']} pièces{COULEURS['RESET']}")
        print()  # Espace entre chaque objet

    print(f"\n{COULEURS['GRIS']}{len(objets_disponibles) + 1}. ⬅️  Retour (r){COULEURS['RESET']}")

    try:
        choix_input = input(f"\n{COULEURS['VERT']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            return
        choix = int(choix_input)
        if 1 <= choix <= len(objets_disponibles):
            nom_objet = list(objets_disponibles.keys())[choix - 1]
            objet_data = objets_disponibles[nom_objet]

            quantite = int(input(f"Combien de {nom_objet} voulez-vous acheter ? "))
            if quantite <= 0:
                print("Quantité invalide.")
                return

            prix_total = objet_data["prix"] * quantite
            or_actuel = obtenir_or_joueur(joueur)

            if or_actuel >= prix_total:
                # Créer l'objet
                obj_id = objet_data.get("id")
                type_objet = objet_data.get("type", "consommable")

                if type_objet == "ingredient_special":
                    # C'est un ingrédient spécial (comme "Eau Pure")
                    description = INGREDIENTS_SPECIAUX.get(nom_objet, {}).get("description", "")
                    nouvel_objet = Objet(
                        nom=nom_objet,
                        type_objet="matériau",
                        quantite=quantite,
                        description=description,
                        rarete=None  # Les ingrédients spéciaux n'ont pas de rareté
                    )
                    joueur.ajouter_objet(nouvel_objet)
                    retirer_or(joueur, prix_total)
                    afficher_message_confirmation(f"Vous avez acheté {quantite}x {nom_objet} pour {formater_nombre(prix_total)} pièces.", "succes")
                    print(f"Or restant : {formater_nombre(obtenir_or_joueur(joueur))} pièces")
                    input("\nAppuyez sur Entrée pour continuer...")
                elif obj_id and obj_id in DEFINITIONS_OBJETS:
                    obj_def = DEFINITIONS_OBJETS[obj_id]
                    nouvel_objet = Objet(
                        nom=obj_def["nom"],
                        type_objet=obj_def["type"],
                        quantite=quantite,
                        description=obj_def.get("description", ""),
                        rarete=obj_def.get("rarete")
                    )
                    joueur.ajouter_objet(nouvel_objet)
                    retirer_or(joueur, prix_total)
                    print(f"\n✓ Vous avez acheté {quantite}x {nom_objet} pour {prix_total} pièces.")
                    print(f"Or restant : {obtenir_or_joueur(joueur)} pièces")
                else:
                    print("Erreur : Objet introuvable dans les définitions.")
            else:
                afficher_message_confirmation(f"Vous n'avez pas assez d'or. Prix : {formater_nombre(prix_total)}, Or actuel : {formater_nombre(or_actuel)}", "erreur")
                input("\nAppuyez sur Entrée pour continuer...")
        elif choix == len(objets_disponibles) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def menu_vente(joueur):
    """
    Menu de vente d'objets avec affichage détaillé des prix.
    """
    effacer_console()
    afficher_titre_menu("VENTE", couleur=COULEURS["JAUNE"])
    afficher_or(joueur)
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        return

    # Codes couleur ANSI pour les raretés
    COULEURS_RARETE = {
        "commun": "\033[0m",           # Blanc/par défaut
        "peu commun": "\033[92m",      # Vert clair
        "rare": "\033[94m",             # Bleu
        "épique": "\033[95m",           # Magenta/Violet
        "légendaire": "\033[93m"        # Jaune/Doré
    }
    RESET_COULEUR = "\033[0m"

    # Couleur ocre/dorée pour les prix (jaune foncé)
    COULEUR_OR = "\033[33m"  # Jaune foncé/ocre

    print(f"\n{COULEURS['JAUNE']}💵 Objets à vendre :{COULEURS['RESET']}")
    print()
    objets_liste = list(joueur.inventaire.items())
    for i, (nom, objet) in enumerate(objets_liste, 1):
        prix_vente, details = calculer_prix_vente(objet)

        # Emoji selon le type d'objet
        emoji_objet = "🧪" if objet.type == "potion" else "⚔️" if objet.type == "arme" else "🛡️" if objet.type == "armure" or objet.type == "équipement" else "💎"

        # Couleur de l'objet selon sa rareté
        couleur_objet = RESET_COULEUR
        if hasattr(objet, 'rarete') and objet.rarete:
            rarete_lower = str(objet.rarete).lower().strip()
            couleur_objet = COULEURS_RARETE.get(rarete_lower, RESET_COULEUR)

        print(f"{COULEURS['CYAN']}{i}.{COULEURS['RESET']} {emoji_objet} {couleur_objet}{objet}{RESET_COULEUR}")
        print(f"   {COULEURS['GRIS']}Prix :{COULEURS['RESET']} {COULEUR_OR}{prix_vente} pièces{RESET_COULEUR}")

        print()  # Espace entre chaque objet

    print(f"{len(objets_liste) + 1}. ⬅️  Retour (r)")

    try:
        choix_input = input(f"\n{COULEURS['JAUNE']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            return
        choix = int(choix_input)
        if 1 <= choix <= len(objets_liste):
            nom_objet, objet = objets_liste[choix - 1]

            quantite_max = objet.quantite
            quantite = int(input(f"Combien de {nom_objet} voulez-vous vendre (max: {quantite_max}) ? "))

            if quantite <= 0 or quantite > quantite_max:
                print("Quantité invalide.")
                return

            prix_unitaire, details = calculer_prix_vente(objet)
            prix_total = prix_unitaire * quantite

            # Afficher un résumé détaillé avant confirmation
            afficher_separateur(couleur=COULEURS["CYAN"])
            print(f"\n{COULEURS['CYAN']}Résumé de la vente :{COULEURS['RESET']}")
            afficher_separateur(style="simple", couleur=COULEURS["CYAN"])
            print(f"Objet : {nom_objet}")
            print(f"Quantité : {quantite}")
            print(f"Prix unitaire : {formater_nombre(prix_unitaire)} pièces")
            if details["bonus_stats"] > 0 or details["bonus_niveau"] > 0:
                print(f"\nDétail du prix unitaire :")
                print(f"  • Prix de base ({objet.rarete or 'sans rareté'}) : {details['prix_base']} pièces")
                if details["bonus_stats"] > 0:
                    print(f"  • Bonus stats/effets : +{details['bonus_stats']} pièces")
                if details["bonus_niveau"] > 0:
                    print(f"  • Bonus niveau biome ({objet.niveau_biome}) : +{details['bonus_niveau']} pièces")
                print(f"  • Multiplicateur type ({objet.type}) : x{details['multiplicateur_type']}")
            print(f"\n{COULEURS['VERT']}Prix total : {formater_nombre(prix_total)} pièces{COULEURS['RESET']}")
            afficher_separateur(couleur=COULEURS["CYAN"])

            confirmation = input(f"\n{COULEURS['JAUNE']}Confirmer la vente ? (o/n) : {COULEURS['RESET']}").strip().lower()
            if confirmation not in ('o', 'oui', 'y', 'yes'):
                afficher_message_confirmation("Vente annulée.", "info")
                input("\nAppuyez sur Entrée pour continuer...")
                return

            # Retirer l'objet
            joueur.retirer_objet(nom_objet, quantite)

            # Ajouter l'or
            ajouter_or(joueur, prix_total)

            afficher_message_confirmation(f"Vous avez vendu {quantite}x {nom_objet} pour {formater_nombre(prix_total)} pièces.", "succes")
            print(f"Or actuel : {formater_nombre(obtenir_or_joueur(joueur))} pièces")
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == len(objets_liste) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
