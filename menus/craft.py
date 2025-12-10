# menus/craft.py
# Menu de craft fonctionnel

from typing import List, Dict, Optional, Tuple
from classes.objet import Objet
from classes.arme import Arme
from world import obtenir_royaume_du_joueur
from data.recettes import (
    TOUTES_LES_RECETTES,
    obtenir_recette,
    obtenir_recettes_par_type,
    obtenir_recettes_disponibles
)
from data.categories_ingredients import (
    est_categorie_generique,
    est_ingredient_special,
    obtenir_ingredients_par_categorie,
    trouver_equivalents_ingredient
)
from data.ingredients import (
    extraire_nom_base_ingredient,
    extraire_qualite_ingredient,
    compter_ingredient_qualite,
    retirer_ingredient_qualite,
    obtenir_nom_complet_avec_qualite,
    RARETES
)
from data.craft_bonus import (
    calculer_effet_avec_bonus,
    calculer_stats_avec_bonus,
    calculer_niveau_moyen_ingredients
)
from data.categories_ingredients import INGREDIENTS_SPECIAUX


def menu_craft(joueur, hub, features_craft: List):
    """
    Menu principal de craft : fabrication d'objets à partir de matériaux.
    """
    while True:
        print(f"\n{'='*60}")
        print("--- ATELIER DE CRAFT ---")
        print(f"{'='*60}\n")

        # Obtenir le royaume du joueur pour le mapping des catégories
        royaume = obtenir_royaume_du_joueur(joueur)
        royaume_nom = royaume.nom if royaume else "Vrak'thar"  # Fallback

        # Afficher le niveau de craft du joueur (pour l'instant = niveau du joueur)
        niveau_craft = joueur.niveau
        print(f"Niveau de craft : {niveau_craft}")
        print(f"Royaume : {royaume_nom}\n")

        print("Que souhaitez-vous craft ?")
        print("1. Potions")
        print("2. Armes")
        print("3. Armures")
        print("4. Retour")

        choix = input("\nVotre choix : ").strip()

        if choix == '1':
            menu_craft_potions(joueur, royaume_nom, niveau_craft)
        elif choix == '2':
            menu_craft_armes(joueur, royaume_nom, niveau_craft)
        elif choix == '3':
            menu_craft_armures(joueur, royaume_nom, niveau_craft)
        elif choix == '4':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_craft_potions(joueur, royaume_nom: str, niveau_craft: int):
    """Menu de craft des potions"""
    while True:
        print(f"\n{'='*60}")
        print("--- CRAFT DE POTIONS ---")
        print(f"{'='*60}\n")

        # Obtenir les recettes de potions disponibles
        recettes_potions = [r for r in obtenir_recettes_disponibles(niveau_craft)
                           if r.get('type') == 'potion']

        if not recettes_potions:
            print("Aucune recette de potion disponible pour votre niveau.")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        # Grouper par sous-type
        sous_types = {}
        for rec in recettes_potions:
            sous_type = rec.get('sous_type', 'autre')
            if sous_type not in sous_types:
                sous_types[sous_type] = []
            sous_types[sous_type].append(rec)

        print("Types de potions disponibles :")
        options = []
        option_num = 1

        type_names = {
            'soin': 'Potions de Soin',
            'mana': 'Potions de Mana',
            'energie': 'Potions d\'Énergie',
            'boost_force': 'Potions de Force',
            'boost_defense': 'Potions de Protection',
            'boost_vitesse': 'Potions de Vélocité',
            'boost_critique': 'Potions de Précision'
        }

        for sous_type, recettes in sorted(sous_types.items()):
            nom_type = type_names.get(sous_type, sous_type)
            print(f"{option_num}. {nom_type} ({len(recettes)} recettes)")
            options.append(sous_type)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                sous_type_choisi = options[choix_int - 1]
                afficher_recettes_potions(joueur, royaume_nom, sous_types[sous_type_choisi])
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def afficher_recettes_potions(joueur, royaume_nom: str, recettes: List[Dict]):
    """Affiche les recettes de potions et permet de les craft"""
    while True:
        print(f"\n{'='*60}")
        print("--- RECETTES DE POTIONS ---")
        print(f"{'='*60}\n")

        # Trier par rareté (ordre défini)
        ordre_rarete = {r: i for i, r in enumerate(RARETES)}
        recettes_triees = sorted(recettes, key=lambda r: ordre_rarete.get(r.get('rarete', ''), 99))

        print("Recettes disponibles :\n")
        options = []
        option_num = 1

        for rec in recettes_triees:
            nom = rec['nom']
            rarete = rec.get('rarete', 'Inconnu')
            niveau_req = rec.get('niveau_craft_requis', 1)

            # Vérifier si le joueur peut craft cette recette
            peut_crafter, ingredients_manquants = verifier_ingredients_recette(joueur, rec, royaume_nom)
            statut = "✓" if peut_crafter else "✗"

            # Codes couleur ANSI
            VERT = '\033[92m'  # Vert clair
            RESET = '\033[0m'   # Reset

            # Appliquer la couleur verte si craftable
            nom_affiche = f"{VERT}{nom}{RESET}" if peut_crafter else nom
            statut_affiche = f"{VERT}{statut}{RESET}" if peut_crafter else statut

            print(f"{option_num}. {statut_affiche} {nom_affiche} ({rarete}) - Niveau requis : {niveau_req}")

            # Afficher les effets
            effets = rec.get('effets', {})
            effets_str = []
            if effets.get('vie'):
                effets_str.append(f"{effets['vie']} PV")
            if effets.get('mana'):
                effets_str.append(f"{effets['mana']} Mana")
            if effets.get('energie'):
                effets_str.append(f"{effets['energie']} Énergie")
            if effets.get('boost_attaque'):
                effets_str.append(f"+{effets['boost_attaque']} Attaque ({effets.get('duree_tours', 0)} tours)")
            if effets.get('boost_defense'):
                effets_str.append(f"+{effets['boost_defense']} Défense ({effets.get('duree_tours', 0)} tours)")
            if effets.get('boost_vitesse'):
                effets_str.append(f"+{effets['boost_vitesse']} Vitesse ({effets.get('duree_tours', 0)} tours)")
            if effets.get('boost_critique'):
                effets_str.append(f"+{effets['boost_critique']}% Critique ({effets.get('duree_tours', 0)} tours)")

            if effets_str:
                print(f"   Effet : {', '.join(effets_str)}")

            if not peut_crafter and ingredients_manquants:
                print(f"   ⚠️  Ingrédients manquants : {', '.join(ingredients_manquants[:3])}")

            options.append(rec)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                recette_choisie = options[choix_int - 1]
                executer_craft(joueur, recette_choisie, royaume_nom)
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def menu_craft_armes(joueur, royaume_nom: str, niveau_craft: int):
    """Menu de craft des armes"""
    while True:
        print(f"\n{'='*60}")
        print("--- CRAFT D'ARMES ---")
        print(f"{'='*60}\n")

        # Obtenir les recettes d'armes disponibles
        recettes_armes = [r for r in obtenir_recettes_disponibles(niveau_craft)
                         if r.get('type') == 'arme']

        if not recettes_armes:
            print("Aucune recette d'arme disponible pour votre niveau.")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        # Grouper par sous-type
        sous_types = {}
        for rec in recettes_armes:
            sous_type = rec.get('sous_type', 'autre')
            if sous_type not in sous_types:
                sous_types[sous_type] = []
            sous_types[sous_type].append(rec)

        print("Types d'armes disponibles :")
        options = []
        option_num = 1

        type_names = {
            'epee': 'Épées',
            'hache': 'Haches',
            'dague': 'Dagues',
            'baton': 'Bâtons'
        }

        for sous_type, recettes in sorted(sous_types.items()):
            nom_type = type_names.get(sous_type, sous_type)
            print(f"{option_num}. {nom_type} ({len(recettes)} recettes)")
            options.append(sous_type)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                sous_type_choisi = options[choix_int - 1]
                afficher_recettes_armes(joueur, royaume_nom, sous_types[sous_type_choisi])
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def afficher_recettes_armes(joueur, royaume_nom: str, recettes: List[Dict]):
    """Affiche les recettes d'armes et permet de les craft"""
    while True:
        print(f"\n{'='*60}")
        print("--- RECETTES D'ARMES ---")
        print(f"{'='*60}\n")

        # Trier par rareté (ordre défini)
        ordre_rarete = {r: i for i, r in enumerate(RARETES)}
        recettes_triees = sorted(recettes, key=lambda r: ordre_rarete.get(r.get('rarete', ''), 99))

        print("Recettes disponibles :\n")
        options = []
        option_num = 1

        for rec in recettes_triees:
            nom = rec['nom']
            rarete = rec.get('rarete', 'Inconnu')
            niveau_req = rec.get('niveau_craft_requis', 1)

            # Vérifier si le joueur peut craft cette recette
            peut_crafter, ingredients_manquants = verifier_ingredients_recette(joueur, rec, royaume_nom)
            statut = "✓" if peut_crafter else "✗"

            # Codes couleur ANSI
            VERT = '\033[92m'  # Vert clair
            RESET = '\033[0m'   # Reset

            # Appliquer la couleur verte si craftable
            nom_affiche = f"{VERT}{nom}{RESET}" if peut_crafter else nom
            statut_affiche = f"{VERT}{statut}{RESET}" if peut_crafter else statut

            print(f"{option_num}. {statut_affiche} {nom_affiche} ({rarete}) - Niveau requis : {niveau_req}")

            # Afficher les stats
            stats = rec.get('stats', {})
            stats_str = []
            if stats.get('degats_base') is not None:
                stats_str.append(f"Dégâts: {stats['degats_base']}")
            if stats.get('bonus_force') is not None:
                stats_str.append(f"Force: +{stats['bonus_force']}")
            if stats.get('bonus_agilite') is not None:
                stats_str.append(f"Agilité: +{stats['bonus_agilite']}")
            if stats.get('bonus_vitalite') is not None:
                stats_str.append(f"Vitalité: +{stats['bonus_vitalite']}")
            if stats.get('bonus_intelligence') is not None:
                stats_str.append(f"Intelligence: +{stats['bonus_intelligence']}")
            if stats.get('bonus_defense') is not None:
                stats_str.append(f"Défense: +{stats['bonus_defense']}")

            if stats_str:
                print(f"   Stats : {', '.join(stats_str)}")
            else:
                print(f"   Stats : À définir")

            if not peut_crafter and ingredients_manquants:
                print(f"   ⚠️  Ingrédients manquants : {', '.join(ingredients_manquants[:3])}")

            options.append(rec)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                recette_choisie = options[choix_int - 1]
                executer_craft(joueur, recette_choisie, royaume_nom)
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def menu_craft_armures(joueur, royaume_nom: str, niveau_craft: int):
    """Menu de craft des armures"""
    while True:
        print(f"\n{'='*60}")
        print("--- CRAFT D'ARMURES ---")
        print(f"{'='*60}\n")

        # Obtenir les recettes d'armures disponibles
        recettes_armures = [r for r in obtenir_recettes_disponibles(niveau_craft)
                           if r.get('type') == 'armure']

        if not recettes_armures:
            print("Aucune recette d'armure disponible pour votre niveau.")
            input("\nAppuyez sur Entrée pour continuer...")
            return

        # Grouper par sous-type
        sous_types = {}
        for rec in recettes_armures:
            sous_type = rec.get('sous_type', 'autre')
            if sous_type not in sous_types:
                sous_types[sous_type] = []
            sous_types[sous_type].append(rec)

        print("Types d'armures disponibles :")
        options = []
        option_num = 1

        type_names = {
            'torse': 'Armures Torse',
            'casque': 'Casques',
            'bottes': 'Bottes'
        }

        for sous_type, recettes in sorted(sous_types.items()):
            nom_type = type_names.get(sous_type, sous_type)
            print(f"{option_num}. {nom_type} ({len(recettes)} recettes)")
            options.append(sous_type)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                sous_type_choisi = options[choix_int - 1]
                afficher_recettes_armures(joueur, royaume_nom, sous_types[sous_type_choisi])
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def afficher_recettes_armures(joueur, royaume_nom: str, recettes: List[Dict]):
    """Affiche les recettes d'armures et permet de les craft"""
    while True:
        print(f"\n{'='*60}")
        print("--- RECETTES D'ARMURES ---")
        print(f"{'='*60}\n")

        # Trier par rareté (ordre défini)
        ordre_rarete = {r: i for i, r in enumerate(RARETES)}
        recettes_triees = sorted(recettes, key=lambda r: ordre_rarete.get(r.get('rarete', ''), 99))

        print("Recettes disponibles :\n")
        options = []
        option_num = 1

        for rec in recettes_triees:
            nom = rec['nom']
            rarete = rec.get('rarete', 'Inconnu')
            niveau_req = rec.get('niveau_craft_requis', 1)

            # Vérifier si le joueur peut craft cette recette
            peut_crafter, ingredients_manquants = verifier_ingredients_recette(joueur, rec, royaume_nom)
            statut = "✓" if peut_crafter else "✗"

            # Codes couleur ANSI
            VERT = '\033[92m'  # Vert clair
            RESET = '\033[0m'   # Reset

            # Appliquer la couleur verte si craftable
            nom_affiche = f"{VERT}{nom}{RESET}" if peut_crafter else nom
            statut_affiche = f"{VERT}{statut}{RESET}" if peut_crafter else statut

            print(f"{option_num}. {statut_affiche} {nom_affiche} ({rarete}) - Niveau requis : {niveau_req}")

            # Afficher les stats
            stats = rec.get('stats', {})
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
            if stats.get('degats_base') is not None:
                stats_str.append(f"Dégâts: {stats['degats_base']}")

            if stats_str:
                print(f"   Stats : {', '.join(stats_str)}")
            else:
                print(f"   Stats : À définir")

            if not peut_crafter and ingredients_manquants:
                print(f"   ⚠️  Ingrédients manquants : {', '.join(ingredients_manquants[:3])}")

            options.append(rec)
            option_num += 1

        print(f"{option_num}. Retour")

        choix = input("\nVotre choix : ").strip()

        try:
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                recette_choisie = options[choix_int - 1]
                executer_craft(joueur, recette_choisie, royaume_nom)
            elif choix_int == option_num:
                return
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def verifier_ingredients_recette(joueur, recette: Dict, royaume_nom: str) -> Tuple[bool, List[str]]:
    """
    Vérifie si le joueur a tous les ingrédients nécessaires pour une recette.

    :param joueur: Le personnage joueur
    :param recette: Dictionnaire de la recette
    :param royaume_nom: Nom du royaume pour le mapping des catégories
    :return: (peut_crafter, liste_ingredients_manquants)
    """
    ingredients_requis = recette.get('ingredients', {})
    ingredients_manquants = []

    for ingredient_nom, quantite_requise in ingredients_requis.items():
        # Vérifier si c'est une catégorie générique ou un ingrédient spécial
        if est_categorie_generique(ingredient_nom):
            # Obtenir les ingrédients réels pour cette catégorie
            ingredients_reels = obtenir_ingredients_par_categorie(ingredient_nom, royaume_nom)

            # Vérifier si le joueur a au moins un ingrédient de cette catégorie avec la bonne quantité
            total_disponible = 0
            for nom_reel in ingredients_reels:
                # Chercher toutes les qualités de cet ingrédient
                for qualite in RARETES:
                    quantite = compter_ingredient_qualite(joueur, nom_reel, qualite)
                    total_disponible += quantite

            if total_disponible < quantite_requise:
                ingredients_manquants.append(f"{ingredient_nom} x{quantite_requise}")

        elif est_ingredient_special(ingredient_nom):
            # Ingrédient spécial (achetable en boutique)
            quantite_disponible = joueur.compter_objet(ingredient_nom)
            if quantite_disponible < quantite_requise:
                ingredients_manquants.append(f"{ingredient_nom} x{quantite_requise}")

        else:
            # Ingrédient réel spécifique : chercher les équivalents
            equivalents = trouver_equivalents_ingredient(ingredient_nom, royaume_nom)
            total_disponible = 0

            # Compter toutes les qualités de tous les équivalents
            for nom_equiv in equivalents:
                for qualite in RARETES:
                    quantite = compter_ingredient_qualite(joueur, nom_equiv, qualite)
                    total_disponible += quantite

            if total_disponible < quantite_requise:
                ingredients_manquants.append(f"{ingredient_nom} x{quantite_requise}")

    return len(ingredients_manquants) == 0, ingredients_manquants


def executer_craft(joueur, recette: Dict, royaume_nom: str) -> bool:
    """
    Exécute le craft d'un objet selon une recette.

    :param joueur: Le personnage joueur
    :param recette: Dictionnaire de la recette
    :param royaume_nom: Nom du royaume pour le mapping des catégories
    :return: True si le craft a réussi, False sinon
    """
    # Vérifier les ingrédients
    peut_crafter, ingredients_manquants = verifier_ingredients_recette(joueur, recette, royaume_nom)

    if not peut_crafter:
        print(f"\n❌ Vous n'avez pas tous les ingrédients nécessaires.")
        print(f"Ingrédients manquants : {', '.join(ingredients_manquants)}")
        input("\nAppuyez sur Entrée pour continuer...")
        return False

    # Demander confirmation
    print(f"\n{'='*60}")
    print(f"Confirmation de craft : {recette['nom']}")
    print(f"{'='*60}\n")

    print("Ingrédients nécessaires :")
    ingredients_requis = recette.get('ingredients', {})
    for ing_nom, quantite in ingredients_requis.items():
        print(f"  • {ing_nom} : {quantite}")

    confirmation = input("\nConfirmer le craft ? (o/n) : ").strip().lower()

    if confirmation not in ('o', 'oui', 'y', 'yes'):
        print("Craft annulé.")
        return False

    # Retirer les ingrédients et créer l'objet
    ingredients_utilises = []
    niveaux_ingredients = []  # Liste pour stocker tous les niveaux (avec pondération par quantité)
    total_quantite_niveaux = 0

    for ingredient_nom, quantite_requise in ingredients_requis.items():
        if est_categorie_generique(ingredient_nom):
            # Retirer les ingrédients de cette catégorie
            ingredients_reels = obtenir_ingredients_par_categorie(ingredient_nom, royaume_nom)
            quantite_restante = quantite_requise

            for nom_reel in ingredients_reels:
                if quantite_restante <= 0:
                    break

                # Chercher toutes les qualités de cet ingrédient
                for qualite in RARETES:
                    if quantite_restante <= 0:
                        break

                    quantite_disponible = compter_ingredient_qualite(joueur, nom_reel, qualite)
                    quantite_a_retirer = min(quantite_disponible, quantite_restante)

                    if quantite_a_retirer > 0:
                        # Trouver l'objet dans l'inventaire pour obtenir son niveau_biome
                        nom_complet = obtenir_nom_complet_avec_qualite(nom_reel, qualite)
                        objet_ingredient = joueur.avoir_objet(nom_complet)

                        if objet_ingredient:
                            # Ajouter au calcul du niveau moyen (pondéré par quantité)
                            niveau_biome_ing = objet_ingredient.niveau_biome
                            if niveau_biome_ing is not None:
                                niveaux_ingredients.append((niveau_biome_ing, quantite_a_retirer))
                                total_quantite_niveaux += quantite_a_retirer

                            retirer_ingredient_qualite(joueur, nom_reel, qualite, quantite_a_retirer)
                            quantite_restante -= quantite_a_retirer
                            ingredients_utilises.append(f"{nom_complet} x{quantite_a_retirer}")

        elif est_ingredient_special(ingredient_nom):
            # Retirer l'ingrédient spécial (pas de niveau_biome pour les ingrédients spéciaux)
            joueur.retirer_objet(ingredient_nom, quantite_requise)
            ingredients_utilises.append(f"{ingredient_nom} x{quantite_requise}")

        else:
            # Ingrédient réel spécifique : utiliser les équivalents
            equivalents = trouver_equivalents_ingredient(ingredient_nom, royaume_nom)
            quantite_restante = quantite_requise

            for nom_equiv in equivalents:
                if quantite_restante <= 0:
                    break

                # Chercher toutes les qualités de cet équivalent
                for qualite in RARETES:
                    if quantite_restante <= 0:
                        break

                    quantite_disponible = compter_ingredient_qualite(joueur, nom_equiv, qualite)
                    quantite_a_retirer = min(quantite_disponible, quantite_restante)

                    if quantite_a_retirer > 0:
                        # Trouver l'objet dans l'inventaire pour obtenir son niveau_biome
                        nom_complet = obtenir_nom_complet_avec_qualite(nom_equiv, qualite)
                        objet_ingredient = joueur.avoir_objet(nom_complet)

                        if objet_ingredient:
                            # Ajouter au calcul du niveau moyen (pondéré par quantité)
                            niveau_biome_ing = objet_ingredient.niveau_biome
                            if niveau_biome_ing is not None:
                                niveaux_ingredients.append((niveau_biome_ing, quantite_a_retirer))
                                total_quantite_niveaux += quantite_a_retirer

                            retirer_ingredient_qualite(joueur, nom_equiv, qualite, quantite_a_retirer)
                            quantite_restante -= quantite_a_retirer
                            ingredients_utilises.append(f"{nom_complet} x{quantite_a_retirer}")

    # Calculer le niveau moyen final (pondéré par quantité)
    niveau_moyen = None
    if niveaux_ingredients and total_quantite_niveaux > 0:
        somme_ponderee = sum(niveau * quantite for niveau, quantite in niveaux_ingredients)
        niveau_moyen = int(somme_ponderee / total_quantite_niveaux)

    # Créer l'objet avec les effets/stats calculés avec bonus
    objet_cree = creer_objet_depuis_recette(recette, niveau_moyen)

    # Ajouter à l'inventaire
    joueur.ajouter_objet(objet_cree)

    # Afficher le résultat
    print(f"\n✅ Craft réussi !")
    print(f"Objet créé : {objet_cree.nom}")
    print(f"\nIngrédients utilisés :")
    for ing in ingredients_utilises:
        print(f"  • {ing}")

    # Afficher les effets/stats avec bonus si applicable
    if niveau_moyen:
        print(f"\nBonus de niveau appliqué (niveau moyen : {niveau_moyen})")
        if recette.get('type') == 'potion':
            effets = recette.get('effets', {})
            for effet_nom, valeur in effets.items():
                if valeur is not None and effet_nom != 'duree_tours':
                    valeur_finale = calculer_effet_avec_bonus(valeur, niveau_moyen)
                    if valeur_finale != valeur:
                        print(f"  {effet_nom} : {valeur} → {valeur_finale:.0f}")

    input("\nAppuyez sur Entrée pour continuer...")
    return True


def creer_objet_depuis_recette(recette: Dict, niveau_biome: Optional[int] = None) -> Objet:
    """
    Crée un objet depuis une recette avec les effets/stats calculés avec bonus de niveau.

    :param recette: Dictionnaire de la recette
    :param niveau_biome: Niveau moyen du biome d'origine des ingrédients
    :return: Objet créé
    """
    nom = recette['nom']
    type_objet = recette.get('type', 'consommable')
    rarete = recette.get('rarete', 'commun')

    # Calculer les effets/stats avec bonus
    description_parts = []

    if recette.get('type') == 'potion':
        effets = recette.get('effets', {})
        effets_finaux = {}

        for effet_nom, valeur in effets.items():
            if valeur is not None and effet_nom != 'duree_tours':
                valeur_finale = calculer_effet_avec_bonus(valeur, niveau_biome)
                effets_finaux[effet_nom] = valeur_finale

                # Construire la description
                if effet_nom == 'vie':
                    description_parts.append(f"Restaure {valeur_finale:.0f} PV")
                elif effet_nom == 'mana':
                    description_parts.append(f"Restaure {valeur_finale:.0f} Mana")
                elif effet_nom == 'energie':
                    description_parts.append(f"Restaure {valeur_finale:.0f} Énergie")
                elif effet_nom == 'boost_attaque':
                    duree = effets.get('duree_tours', 0)
                    description_parts.append(f"+{valeur_finale:.0f} Attaque ({duree} tours)")
                elif effet_nom == 'boost_defense':
                    duree = effets.get('duree_tours', 0)
                    description_parts.append(f"+{valeur_finale:.0f} Défense ({duree} tours)")
                elif effet_nom == 'boost_vitesse':
                    duree = effets.get('duree_tours', 0)
                    description_parts.append(f"+{valeur_finale:.0f} Vitesse ({duree} tours)")
                elif effet_nom == 'boost_critique':
                    duree = effets.get('duree_tours', 0)
                    description_parts.append(f"+{valeur_finale:.0f}% Critique ({duree} tours)")
            else:
                effets_finaux[effet_nom] = valeur

        description = ". ".join(description_parts) if description_parts else recette.get('description', '')

        # Stocker les effets finaux dans la description ou créer un attribut spécial
        # Pour l'instant, on stocke dans la description
        objet = Objet(
            nom=nom,
            type_objet=type_objet,
            quantite=1,
            description=description,
            rarete=rarete.lower()
        )

        # Stocker les effets finaux dans un attribut personnalisé (à implémenter si nécessaire)
        objet.effets = effets_finaux  # Attribut dynamique

    elif recette.get('type') in ('arme', 'armure'):
        stats_base = recette.get('stats', {})
        stats_finales = calculer_stats_avec_bonus(stats_base, niveau_biome)

        description_parts = []
        for stat_nom, valeur in stats_finales.items():
            if valeur is not None and isinstance(valeur, (int, float)):
                if stat_nom == 'degats_base':
                    description_parts.append(f"+{valeur:.0f} Dégâts")
                elif stat_nom == 'bonus_defense':
                    description_parts.append(f"+{valeur:.0f} Défense")
                elif stat_nom == 'bonus_force':
                    description_parts.append(f"+{valeur:.0f} Force")
                elif stat_nom == 'bonus_agilite':
                    description_parts.append(f"+{valeur:.0f} Agilité")
                elif stat_nom == 'bonus_vitalite':
                    description_parts.append(f"+{valeur:.0f} Vitalité")
                elif stat_nom == 'bonus_intelligence':
                    description_parts.append(f"+{valeur:.0f} Intelligence")

        description = ". ".join(description_parts) if description_parts else recette.get('description', '')

        objet = Objet(
            nom=nom,
            type_objet=type_objet,
            quantite=1,
            description=description,
            rarete=rarete.lower()
        )

        objet.stats = stats_finales  # Attribut dynamique pour les stats
        # Stocker le sous_type pour les armures (torse, casque, bottes)
        if recette.get('type') == 'armure':
            objet.sous_type = recette.get('sous_type')

    else:
        description = recette.get('description', '')
        objet = Objet(
            nom=nom,
            type_objet=type_objet,
            quantite=1,
            description=description,
            rarete=rarete.lower()
        )

    return objet
