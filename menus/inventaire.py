# menus/inventaire.py
# Fonctions de gestion de l'inventaire avec tri, filtrage, recherche et pagination

from typing import List, Tuple, Optional, Dict
from classes.objet import Objet
from .utiliser_objets import utiliser_potion as utiliser_potion_objet
from .commerce import calculer_prix_vente
from utils.affichage import afficher_titre_menu, afficher_titre_menu_avec_emoji, afficher_separateur, afficher_message_confirmation, formater_nombre, COULEURS, effacer_console

# Ordre des raretés pour le tri
ORDRE_RARETE = {
    "commun": 0,
    "peu commun": 1,
    "rare": 2,
    "épique": 3,
    "légendaire": 4
}

# Codes couleur ANSI pour les raretés
COULEURS_RARETE = {
    "commun": "\033[0m",           # Blanc/par défaut
    "peu commun": "\033[92m",      # Vert clair
    "rare": "\033[94m",             # Bleu
    "épique": "\033[95m",           # Magenta/Violet
    "légendaire": "\033[93m"        # Jaune/Doré
}
RESET_COULEUR = "\033[0m"

# Nombre d'objets par page pour la pagination
OBJETS_PAR_PAGE = 15


def menu_inventaire(joueur):
    """Menu de gestion de l'inventaire du joueur avec options améliorées"""
    while True:
        effacer_console()
        afficher_titre_menu(f"INVENTAIRE DE {joueur.nom.upper()}", couleur=COULEURS["CYAN"])

        # Afficher les statistiques rapides
        _afficher_stats_rapides(joueur)

        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print("\nOptions disponibles :")
        print("1. Afficher l'inventaire (avec tri/filtre)")
        print("2. Rechercher un objet")
        print("3. Consulter un objet spécifique")
        print("4. Utiliser une potion")
        print("5. Équiper un équipement")
        print("6. Jeter un objet")
        print("7. ⬅️  Retour au menu personnage (r)")

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            afficher_inventaire_ameliore(joueur)
        elif choix == '2':
            rechercher_objet(joueur)
        elif choix == '3':
            consulter_objet(joueur)
        elif choix == '4':
            utiliser_potion(joueur)
        elif choix == '5':
            from .utiliser_objets import menu_equiper_equipement
            menu_equiper_equipement(joueur)
        elif choix == '6':
            jeter_objet(joueur)
        elif choix == '7' or choix == 'r':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def _afficher_stats_rapides(joueur):
    """Affiche les statistiques rapides de l'inventaire"""
    if not joueur.inventaire:
        print("Inventaire vide")
        return

    total_types = len(joueur.inventaire)
    total_objets = sum(obj.quantite for obj in joueur.inventaire.values())

    # Calculer la valeur totale estimée
    valeur_totale = 0
    for objet in joueur.inventaire.values():
        prix, _ = calculer_prix_vente(objet)
        valeur_totale += prix * objet.quantite

    print(f"📦 {total_types} type(s) d'objets | {total_objets} objet(s) au total | 💰 Valeur estimée : {valeur_totale:,} pièces")


def trier_objets(objets: List[Tuple[str, Objet]], critere: str = "nom", ordre: str = "croissant") -> List[Tuple[str, Objet]]:
    """
    Trie une liste d'objets selon un critère.

    :param objets: Liste de tuples (nom_objet, objet)
    :param critere: Critère de tri ("nom", "rarete", "quantite", "type")
    :param ordre: Ordre de tri ("croissant" ou "decroissant")
    :return: Liste triée
    """
    reverse = (ordre == "decroissant")

    if critere == "nom":
        return sorted(objets, key=lambda x: x[1].nom.lower(), reverse=reverse)
    elif critere == "rarete":
        def cle_rarete(x):
            rarete = x[1].rarete or ""
            return ORDRE_RARETE.get(rarete.lower(), 99)
        return sorted(objets, key=cle_rarete, reverse=reverse)
    elif critere == "quantite":
        return sorted(objets, key=lambda x: x[1].quantite, reverse=reverse)
    elif critere == "type":
        return sorted(objets, key=lambda x: (x[1].type, x[1].nom.lower()), reverse=reverse)
    else:
        return objets


def filtrer_objets(objets: List[Tuple[str, Objet]], filtre_type: Optional[str] = None,
                   filtre_rarete: Optional[str] = None, filtre_sous_type: Optional[str] = None) -> List[Tuple[str, Objet]]:
    """
    Filtre une liste d'objets selon des critères.

    :param objets: Liste de tuples (nom_objet, objet)
    :param filtre_type: Type d'objet à filtrer (ex: "potion", "équipement")
    :param filtre_rarete: Rareté à filtrer (ex: "rare", "épique")
    :param filtre_sous_type: Sous-type à filtrer (ex: "epee", "torse")
    :return: Liste filtrée
    """
    resultat = objets

    if filtre_type:
        resultat = [(nom, obj) for nom, obj in resultat if obj.type.lower() == filtre_type.lower()]

    if filtre_rarete:
        resultat = [(nom, obj) for nom, obj in resultat
                   if obj.rarete and obj.rarete.lower() == filtre_rarete.lower()]

    if filtre_sous_type:
        resultat = [(nom, obj) for nom, obj in resultat
                   if hasattr(obj, 'sous_type') and obj.sous_type == filtre_sous_type]

    return resultat


def rechercher_objets(objets: List[Tuple[str, Objet]], terme: str) -> List[Tuple[str, Objet]]:
    """
    Recherche des objets par nom (recherche partielle, insensible à la casse).

    :param objets: Liste de tuples (nom_objet, objet)
    :param terme: Terme de recherche
    :return: Liste d'objets correspondants
    """
    terme_lower = terme.lower()
    return [(nom, obj) for nom, obj in objets if terme_lower in obj.nom.lower()]


def afficher_inventaire_ameliore(joueur, objets_a_afficher: Optional[List[Tuple[str, Objet]]] = None):
    """
    Affiche l'inventaire avec tri, filtrage et pagination.

    :param joueur: Instance du personnage
    :param objets_a_afficher: Liste optionnelle d'objets à afficher (si None, utilise tout l'inventaire)
    """
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Préparer la liste d'objets
    if objets_a_afficher is None:
        objets_liste = list(joueur.inventaire.items())
    else:
        objets_liste = objets_a_afficher

    if not objets_liste:
        print("\nAucun objet ne correspond aux critères de recherche.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Paramètres par défaut
    critere_tri = "nom"
    ordre_tri = "croissant"
    filtre_type = None
    filtre_rarete = None

    # Menu simplifié
    while True:
        effacer_console()
        print()
        afficher_titre_menu_avec_emoji("AFFICHAGE DE L'INVENTAIRE", "inventaire")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

        # Afficher les paramètres actuels
        print(f"\nTri : {critere_tri.capitalize()} ({ordre_tri})")
        filtres_actifs = []
        if filtre_type:
            filtres_actifs.append(f"Type: {filtre_type}")
        if filtre_rarete:
            filtres_actifs.append(f"Rareté: {filtre_rarete}")
        if filtres_actifs:
            print(f"Filtres : {', '.join(filtres_actifs)}")
        else:
            print("Filtres : Aucun")

        print("\nOptions :")
        print("1. Changer le tri")
        print("2. Filtrer par type")
        print("3. Filtrer par rareté")
        print("4. Réinitialiser les filtres")
        print("5. Afficher l'inventaire")
        print("6. ⬅️  Retour (r)")

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            critere_tri, ordre_tri = _choisir_tri()
        elif choix == '2':
            filtre_type = _choisir_filtre_type()
        elif choix == '3':
            filtre_rarete = _choisir_filtre_rarete()
        elif choix == '4':
            filtre_type = None
            filtre_rarete = None
            print("✓ Filtres reinitialises.")
        elif choix == '5':
            # Appliquer les filtres
            objets_filtres = filtrer_objets(objets_liste, filtre_type, filtre_rarete, None)

            if not objets_filtres:
                print("\n❌ Aucun objet ne correspond aux filtres sélectionnés.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            # Appliquer le tri
            objets_tries = trier_objets(objets_filtres, critere_tri, ordre_tri)

            # Afficher avec pagination
            _afficher_inventaire_pagine(joueur, objets_tries)
        elif choix == '6' or choix == 'r':
            return
        else:
            print("Choix invalide.")


def _choisir_tri() -> Tuple[str, str]:
    """Menu pour choisir le critère et l'ordre de tri."""
    from utils.affichage import afficher_titre_menu_avec_emoji, afficher_separateur
    print()
    afficher_titre_menu_avec_emoji("Choisir le tri", "inventaire")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print("1. Par nom (A-Z)")
    print("2. Par rareté (Commun → Légendaire)")
    print("3. Par quantité (croissant)")
    print("4. Par quantité (décroissant)")
    print("5. Par type")

    choix = input("\nVotre choix : ").strip()

    if choix == '1':
        return ("nom", "croissant")
    elif choix == '2':
        return ("rarete", "croissant")
    elif choix == '3':
        return ("quantite", "croissant")
    elif choix == '4':
        return ("quantite", "decroissant")
    elif choix == '5':
        return ("type", "croissant")
    else:
        print("Choix invalide, utilisation du tri par défaut (nom).")
        return ("nom", "croissant")


def _choisir_filtre_type() -> Optional[str]:
    """Menu pour choisir un filtre de type."""
    print("\nTypes disponibles :")
    print("1. Potion")
    print("2. Équipement")
    print("3. Matériau")
    print("4. Consommable")
    print("5. Annuler")

    choix = input("\nVotre choix : ").strip()
    types_map = {
        '1': 'potion',
        '2': 'équipement',
        '3': 'matériau',
        '4': 'consommable'
    }
    return types_map.get(choix)


def _choisir_filtre_rarete() -> Optional[str]:
    """Menu pour choisir un filtre de rareté."""
    print("\nRaretés disponibles :")
    print("1. Commun")
    print("2. Peu Commun")
    print("3. Rare")
    print("4. Épique")
    print("5. Légendaire")
    print("6. Annuler")

    choix = input("\nVotre choix : ").strip()
    raretes_map = {
        '1': 'commun',
        '2': 'peu commun',
        '3': 'rare',
        '4': 'épique',
        '5': 'légendaire'
    }
    return raretes_map.get(choix)




def _afficher_inventaire_pagine(joueur, objets: List[Tuple[str, Objet]], page: int = 1):
    """
    Affiche l'inventaire avec pagination.

    :param joueur: Instance du personnage
    :param objets: Liste d'objets à afficher
    :param page: Numéro de page (commence à 1)
    """
    if not objets:
        print("\nAucun objet à afficher.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    total_pages = (len(objets) + OBJETS_PAR_PAGE - 1) // OBJETS_PAR_PAGE

    while True:
        effacer_console()
        print()
        afficher_titre_menu_avec_emoji(f"INVENTAIRE (Page {page}/{total_pages})", "inventaire")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()

        # Calculer les indices pour cette page
        debut = (page - 1) * OBJETS_PAR_PAGE
        fin = min(debut + OBJETS_PAR_PAGE, len(objets))
        objets_page = objets[debut:fin]

        # Afficher les objets de la page
        for i, (nom_objet, objet) in enumerate(objets_page, start=debut + 1):
            affichage = f"{i}. {_formater_objet_affichage(objet, joueur)}"
            print(affichage)

        # Statistiques de la page
        print(f"\n{'─'*60}")
        print(f"Objets {debut + 1}-{fin} sur {len(objets)}")

        # Navigation
        print("\nNavigation :")
        if total_pages > 1:
            if page > 1:
                print("  ← Page précédente (p)")
            if page < total_pages:
                print("  → Page suivante (s)")
        print("  Retour (r)")

        choix = input("\nVotre choix : ").strip().lower()

        if choix == 'p' and page > 1:
            page -= 1
        elif choix == 's' and page < total_pages:
            page += 1
        elif choix == 'r':
            return
        else:
            print("Choix invalide.")


def _formater_objet_affichage(objet: Objet, joueur) -> str:
    """
    Formate l'affichage d'un objet avec indicateurs visuels.

    :param objet: Objet à formater
    :param joueur: Instance du personnage (pour vérifier si équipé)
    :return: Chaîne formatée
    """
    # Nom de l'objet
    affichage = objet.nom

    # Indicateur de quantité
    if objet.quantite > 1:
        affichage += f" x{objet.quantite}"

    # Indicateur de rareté avec couleur
    if objet.rarete:
        couleur = COULEURS_RARETE.get(objet.rarete.lower(), RESET_COULEUR)
        affichage += f" [{couleur}{objet.rarete}{RESET_COULEUR}]"

    # Indicateur si équipé
    if objet.type == "équipement":
        if joueur.arme and joueur.arme.nom == objet.nom:
            affichage += " ⚔️ ÉQUIPÉ"
        elif hasattr(objet, 'sous_type'):
            if objet.sous_type == "torse" and joueur.armure_torse and joueur.armure_torse.nom == objet.nom:
                affichage += " 🛡️ ÉQUIPÉ"
            elif objet.sous_type == "casque" and joueur.armure_casque and joueur.armure_casque.nom == objet.nom:
                affichage += " 🛡️ ÉQUIPÉ"
            elif objet.sous_type == "bottes" and joueur.armure_bottes and joueur.armure_bottes.nom == objet.nom:
                affichage += " 🛡️ ÉQUIPÉ"

    # Description courte si disponible
    if objet.description and len(objet.description) < 50:
        affichage += f" - {objet.description}"

    return affichage


def rechercher_objet(joueur):
    """Menu de recherche d'objets par nom."""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    effacer_console()
    print()
    afficher_titre_menu_avec_emoji("RECHERCHE D'OBJET", "inventaire")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    terme = input("Entrez le nom de l'objet à rechercher : ").strip()

    if not terme:
        print("Terme de recherche vide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    objets_liste = list(joueur.inventaire.items())
    resultats = rechercher_objets(objets_liste, terme)

    if not resultats:
        print(f"\nAucun objet trouvé contenant '{terme}'.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    print(f"\n{len(resultats)} objet(s) trouvé(s) :\n")
    for nom_objet, objet in resultats:
        print(f"  • {_formater_objet_affichage(objet, joueur)}")

    input("\nAppuyez sur Entrée pour continuer...")


def consulter_objet(joueur):
    """Permet de consulter les détails d'un objet spécifique"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    effacer_console()
    print()
    afficher_titre_menu_avec_emoji("CONSULTER UN OBJET", "inventaire")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    # Afficher la liste des objets disponibles
    objets_liste = list(joueur.inventaire.items())
    objets_tries = trier_objets(objets_liste, "nom", "croissant")

    for i, (nom_objet, objet) in enumerate(objets_tries, 1):
        affichage = f"{i}. {objet.nom} (x{objet.quantite})"
        # Ajouter la rareté avec couleur si disponible
        if hasattr(objet, 'rarete') and objet.rarete:
            rarete_lower = str(objet.rarete).lower().strip()
            couleur = COULEURS_RARETE.get(rarete_lower, RESET_COULEUR)
            rarete_upper = str(objet.rarete).strip().upper()
            affichage += f" [{couleur}{rarete_upper}{RESET_COULEUR}]"
        print(affichage)

    try:
        choix = int(input("\nChoisissez un objet (numéro) : "))
        if 1 <= choix <= len(objets_tries):
            nom_objet, objet = objets_tries[choix - 1]

            effacer_console()
            print()
            afficher_titre_menu_avec_emoji(f"DÉTAILS DE {objet.nom.upper()}", "inventaire")
            afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
            print()

            print(f"Type : {objet.type.capitalize()}")
            if hasattr(objet, 'sous_type') and objet.sous_type:
                print(f"Sous-type : {objet.sous_type.capitalize()}")
            print(f"Quantité : {objet.quantite}")

            # Afficher la rareté avec couleur (toujours afficher)
            if hasattr(objet, 'rarete') and objet.rarete:
                rarete_lower = str(objet.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, RESET_COULEUR)
                rarete_upper = str(objet.rarete).strip().upper()
                print(f"Rareté : {couleur}{rarete_upper}{RESET_COULEUR}")
            else:
                print(f"Rareté : Aucune")

            if hasattr(objet, 'niveau_biome') and objet.niveau_biome:
                print(f"Niveau biome : {objet.niveau_biome}")

            # Afficher les effets si disponibles
            if hasattr(objet, 'effets') and objet.effets:
                effets = objet.effets
                print("\nEffets :")
                for effet_nom, valeur in effets.items():
                    if valeur is not None and effet_nom != 'duree_tours':
                        print(f"  • {effet_nom}: {valeur}")
                    elif effet_nom == 'duree_tours' and valeur:
                        print(f"  • Durée : {valeur} tours")

            # Afficher les stats si disponibles (priorité sur la description)
            if hasattr(objet, 'stats') and objet.stats:
                stats = objet.stats
                print("\nStats :")
                for stat_nom, valeur in stats.items():
                    if valeur is not None:
                        nom_affiche = stat_nom.replace('_', ' ').title()
                        print(f"  • {nom_affiche}: {valeur}")
            elif objet.description:
                # Afficher la description seulement si pas de stats (pour éviter la duplication)
                print(f"\nDescription :\n{objet.description}")

            # Afficher la valeur estimée
            prix, details = calculer_prix_vente(objet)
            print(f"\n💰 Valeur estimée : {prix:,} pièces (x{objet.quantite} = {prix * objet.quantite:,} pièces)")

            # Proposer d'équiper si c'est un équipement
            est_equipement = objet.type in ["arme", "armure", "équipement"]
            if est_equipement:
                print(f"\n{COULEURS['CYAN']}Options :{COULEURS['RESET']}")
                print(f"1. {COULEURS['VERT']}⚔️  Équiper cet équipement{COULEURS['RESET']}")
                print(f"2. {COULEURS['GRIS']}⬅️  Retour (r){COULEURS['RESET']}")

                choix_action = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

                if choix_action == '1':
                    from .utiliser_objets import menu_equiper_equipement
                    # Filtrer pour ne montrer que cet objet dans le menu d'équipement
                    # On va directement équiper depuis la liste
                    from .utiliser_objets import _filtrer_armes, _filtrer_armures_par_type, _equiper_arme_depuis_liste, _equiper_armure_depuis_liste

                    sous_type = getattr(objet, 'sous_type', None)
                    if not sous_type and objet.type == "équipement":
                        from data.recettes import obtenir_recette
                        recette = obtenir_recette(objet.nom)
                        if recette:
                            sous_type = recette.get('sous_type')

                    # Déterminer le type d'équipement
                    if objet.type == "arme" or (hasattr(objet, 'stats') and objet.stats.get('degats_base')):
                        armes = [(nom_objet, objet)]
                        _equiper_arme_depuis_liste(joueur, armes)
                    elif sous_type == "torse":
                        armures = [(nom_objet, objet)]
                        _equiper_armure_depuis_liste(joueur, armures, "armure")
                    elif sous_type == "casque":
                        casques = [(nom_objet, objet)]
                        _equiper_armure_depuis_liste(joueur, casques, "casque")
                    elif sous_type == "bottes":
                        bottes = [(nom_objet, objet)]
                        _equiper_armure_depuis_liste(joueur, bottes, "bottes")
                    else:
                        print(f"{COULEURS['ROUGE']}❌ Impossible d'équiper cet objet.{COULEURS['RESET']}")
                        input("\nAppuyez sur Entrée pour continuer...")
                elif choix_action == '2' or choix_action == 'r':
                    pass  # Retour
                else:
                    print("Choix invalide.")
                    input("\nAppuyez sur Entrée pour continuer...")
            else:
                input("\nAppuyez sur Entrée pour continuer...")

        else:
            print("Numéro invalide.")
            input("\nAppuyez sur Entrée pour continuer...")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        input("\nAppuyez sur Entrée pour continuer...")
    except (IndexError, KeyError):
        print("Erreur lors de la consultation de l'objet.")
        input("\nAppuyez sur Entrée pour continuer...")


def utiliser_potion(joueur):
    """Menu pour utiliser une potion depuis l'inventaire"""
    # Filtrer les potions dans l'inventaire
    potions_disponibles = []
    for nom_objet, objet in joueur.inventaire.items():
        if objet.type == "potion":
            potions_disponibles.append((nom_objet, objet))

    if not potions_disponibles:
        afficher_message_confirmation("Vous n'avez aucune potion dans votre inventaire.", "erreur")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    effacer_console()
    afficher_titre_menu("UTILISER UNE POTION", couleur=COULEURS["VERT"])
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print("\nPotions disponibles :")
    print("Potions disponibles :")

    # Trier les potions par nom
    potions_triees = trier_objets(potions_disponibles, "nom", "croissant")

    for i, (nom_objet, objet) in enumerate(potions_triees, 1):
        print(f"{i}. {objet.nom} (x{objet.quantite})")
        if objet.description:
            print(f"   {objet.description}")

    print(f"{len(potions_triees) + 1}. ⬅️  Retour (r)")

    try:
        choix_input = input(f"\n{COULEURS['VERT']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            return
        choix = int(choix_input)
        if 1 <= choix <= len(potions_triees):
            nom_objet, objet = potions_triees[choix - 1]
            utiliser_potion_objet(joueur, objet)
        elif choix == len(potions_triees) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

    input("\nAppuyez sur Entrée pour continuer...")


def jeter_objet(joueur):
    """Permet de jeter un objet de l'inventaire avec affichage amélioré"""
    if not joueur.inventaire:
        afficher_message_confirmation("Votre inventaire est vide.", "info")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    effacer_console()
    afficher_titre_menu("JETER UN OBJET", couleur=COULEURS["ROUGE"])
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    # Afficher la liste des objets disponibles (triés)
    objets_liste = list(joueur.inventaire.items())
    objets_tries = trier_objets(objets_liste, "nom", "croissant")

    for i, (nom_objet, objet) in enumerate(objets_tries, 1):
        print(f"{i}. {_formater_objet_affichage(objet, joueur)}")

    try:
        choix = int(input("\nChoisissez un objet à jeter (numéro) : "))
        if 1 <= choix <= len(objets_tries):
            nom_objet, objet = objets_tries[choix - 1]

            if objet.quantite > 1:
                print(f"\nVous avez {objet.quantite} {objet.nom}.")
                quantite_a_jeter = input(f"Combien voulez-vous jeter ? (1-{objet.quantite}) : ")
                try:
                    quantite = int(quantite_a_jeter)
                    if 1 <= quantite <= objet.quantite:
                        joueur.retirer_objet(nom_objet, quantite)
                        afficher_message_confirmation(f"Vous avez jeté {quantite} {objet.nom}.", "succes")
                        if joueur.avoir_objet(nom_objet):
                            print(f"Il vous reste {joueur.compter_objet(nom_objet)} {objet.nom}.")
                        else:
                            print(f"Vous n'avez plus de {objet.nom}.")
                    else:
                        print(f"Quantité invalide. Vous devez entrer un nombre entre 1 et {objet.quantite}.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            else:
                # Confirmation pour jeter le dernier objet
                confirmation = input(f"Êtes-vous sûr de vouloir jeter {objet.nom} ? (o/n) : ").lower()
                if confirmation in ('o', 'oui', 'y', 'yes'):
                    joueur.retirer_objet(nom_objet, 1)
                    print(f"✓ Vous avez jeté {objet.nom}.")
                else:
                    print("Action annulée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except (IndexError, KeyError):
        print("Erreur lors du retrait de l'objet.")

    input("\nAppuyez sur Entrée pour continuer...")


# Fonctions de compatibilité pour l'ancien code
def afficher_inventaire_complet(joueur):
    """Affiche tout l'inventaire du joueur (fonction de compatibilité)"""
    afficher_inventaire_ameliore(joueur)


def afficher_inventaire_par_type(joueur):
    """Affiche l'inventaire organisé par type d'objet (fonction de compatibilité)"""
    if not joueur.inventaire:
        print("\nVotre inventaire est vide.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    objets_liste = list(joueur.inventaire.items())
    objets_tries = trier_objets(objets_liste, "type", "croissant")

    effacer_console()
    print()
    afficher_titre_menu_avec_emoji("INVENTAIRE PAR TYPE", "inventaire")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    type_actuel = None
    for nom_objet, objet in objets_tries:
        if objet.type != type_actuel:
            type_actuel = objet.type
            print(f"\n[{type_actuel.upper()}]")
        print(f"  • {_formater_objet_affichage(objet, joueur)}")

    input("\nAppuyez sur Entrée pour continuer...")
