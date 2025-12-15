# combat/deroulement.py
# Fonctions de déroulement du combat

import random
from classes.base_combatant import Personnage, Ennemi
from classes.capacite import Capacite
from classes.objet import Objet
from data.ennemis import DEFINITIONS_ENNEMIS
from data.objets import DEFINITIONS_OBJETS
from .calculs import calculer_degats_finaux, esquive, creer_barre_vie
from .selection import choisir_cible, choisir_capacite
from .actions import executer_attaque, executer_capacite, determiner_cibles_capacite
from .affichage import (
    afficher_tour_joueur, afficher_menu_actions, afficher_resultat_attaque,
    afficher_resultat_capacite, afficher_message_erreur,
    afficher_tour_ennemis, afficher_attaque_ennemi, afficher_fin_combat
)
from .loot import ajouter_ingredients_a_inventaire
from world import teleporter_joueur_vers_capitale
from world.progression_quetes import progresser_quetes_collecter_objet


def calculer_or_ennemi(ennemi_data, xp_a_donner):
    """
    Calcule l'or donné par un ennemi.
    Utilise or_a_donner si défini (manuel), sinon valeur par défaut basée sur les stats.

    IMPORTANT : Pour un équilibrage manuel, définir "or_a_donner" dans DEFINITIONS_ENNEMIS
    pour chaque ennemi. La valeur par défaut est seulement un fallback.

    :param ennemi_data: Dict de DEFINITIONS_ENNEMIS pour cet ennemi
    :param xp_a_donner: XP donnée par cet ennemi (non utilisée pour le calcul d'or maintenant)
    :return: Montant d'or calculé
    """
    # Valeur manuelle définie (prioritaire pour équilibrage)
    if "or_a_donner" in ennemi_data:
        return ennemi_data["or_a_donner"]

    # Valeur par défaut basée sur les stats (fallback si or_a_donner non défini)
    # Formule : vie_max + attaque*2 + defense (pour éviter les erreurs si champ manquant)
    vie_max = ennemi_data.get("vie_max", 30)
    attaque = ennemi_data.get("attaque", 10)
    defense = ennemi_data.get("defense", 5)

    or_par_defaut = int(vie_max + attaque * 2 + defense * 1.5)
    return max(1, or_par_defaut)  # Minimum 1 pièce d'or

def debut_combat(joueur, ennemis):
    from utils.affichage import COULEURS, effacer_console
    effacer_console()
    print(f"\n{COULEURS['MAGENTA']}{'='*60}{COULEURS['RESET']}")
    print(f"{COULEURS['MAGENTA']}--- DEBUT DU COMBAT ---{COULEURS['RESET']}")
    print(f"{COULEURS['MAGENTA']}{'='*60}{COULEURS['RESET']}")
    # Appliquer les effets avec condition "debut"
    joueur.appliquer_effets(phase='debut')
    for ennemi in ennemis:
        ennemi.appliquer_effets(phase='debut')

    barre_vie_joueur = creer_barre_vie(joueur.vie, joueur.vie_max)
    print(f"\n{COULEURS['CYAN']}[JOUEUR] {joueur.nom}{COULEURS['RESET']} - Vie: {barre_vie_joueur} {int(joueur.vie)}/{int(joueur.vie_max)}")
    print(f"\n{COULEURS['ROUGE']}VS{COULEURS['RESET']}\n")
    for ennemi in ennemis:
        barre_vie_ennemi = creer_barre_vie(ennemi.vie, ennemi.vie_max)
        print(f"{COULEURS['ROUGE']}[ENNEMI] {ennemi.nom}{COULEURS['RESET']} - Vie: {barre_vie_ennemi} {int(ennemi.vie)}/{int(ennemi.vie_max)}")
        print(f"  Attaque: {int(ennemi.attaque)} | Défense: {int(ennemi.defense)} | Vitesse: {int(ennemi.vitesse)}")
    print(f"{COULEURS['MAGENTA']}{'-'*60}{COULEURS['RESET']}")

def tour_joueur(joueur, ennemis):
    """
    Gère le tour du joueur (interface solo avec input(), utilise les fonctions pures pour la logique).
    Pour le multijoueur, cette fonction sera remplacée par des appels réseau aux fonctions pures.
    """
    # Appliquer les effets
    if joueur.vie <= (joueur.vie_max * 0.3):
        joueur.appliquer_effets(phase='sous_30hp')
    joueur.appliquer_effets(phase='tour')

    # Vérifier l'étourdissement
    if joueur.est_etourdi():
        print(f"{joueur.nom} est étourdi et ne peut pas agir ce tour !")
        joueur.retirer_effets_expires()
        return True

    ennemis_vivants = [e for e in ennemis if e.est_vivant]
    if not ennemis_vivants:
        print("Il n'y a plus d'ennemis vivants. Fin du combat pour le joueur.")
        return False

    # Affichage du tour (séparé de la logique)
    afficher_tour_joueur(joueur, ennemis)

    action_choisie = False
    while not action_choisie:
        # Affichage du menu (séparé de la logique)
        afficher_menu_actions()
        choix = input("Votre action : ")  # Garde input() pour compatibilité solo

        if choix == '1':
            # Attaque : utilise la fonction pure
            if not ennemis_vivants:
                afficher_message_erreur("Il n'y a personne à attaquer !")
                continue

            # Choix de la cible (garde input() pour solo)
            cible_ennemi = choisir_cible(joueur, ennemis_vivants)
            if cible_ennemi is None:
                continue

            # Exécuter l'attaque (logique pure)
            resultat_attaque = executer_attaque(joueur, cible_ennemi)

            # Afficher le résultat (séparé de la logique)
            afficher_resultat_attaque(resultat_attaque)

            action_choisie = True

        elif choix == '2':
            # Capacité : utilise la fonction pure
            capacite_choisie = choisir_capacite(joueur)  # Garde input() pour solo
            if capacite_choisie is None:
                continue

            # Déterminer les cibles selon le type de capacité
            cible_pour_capacite = None
            if capacite_choisie.type_cible in ("ennemi", "unique"):
                # Nécessite une cible ennemie unique (choix utilisateur)
                if not ennemis_vivants:
                    afficher_message_erreur("Il n'y a pas d'ennemis à cibler.")
                    continue
                cible_unique = choisir_cible(joueur, ennemis_vivants)  # Garde input() pour solo
                if cible_unique is None:
                    continue
                cible_pour_capacite = [cible_unique]
            else:
                # Cibles automatiques selon le type
                cible_pour_capacite = determiner_cibles_capacite(capacite_choisie, joueur, ennemis_vivants)
                if cible_pour_capacite is None:
                    afficher_message_erreur("Impossible de déterminer les cibles pour cette capacité.")
                    continue

            # Exécuter la capacité (logique pure)
            resultat_capacite = executer_capacite(joueur, capacite_choisie, cible_pour_capacite)

            # Afficher le résultat (séparé de la logique)
            if resultat_capacite["success"]:
                afficher_resultat_capacite(resultat_capacite)
                action_choisie = True
            else:
                afficher_resultat_capacite(resultat_capacite)

        elif choix == '3':
            # Utiliser un objet (potions)
            from menus.utiliser_objets import choisir_objet_combat
            objet_utilise = choisir_objet_combat(joueur)
            if objet_utilise:
                action_choisie = True

        elif choix == '4':
            joueur.afficher_stats()
        elif choix == '5':
            joueur.afficher_capacites()
        else:
            afficher_message_erreur("Action invalide. Veuillez réessayer.")
    return True

def tour_ennemis(joueur, ennemis):
    """
    Gère le tour de tous les ennemis vivants.
    :param joueur: Le personnage joueur
    :param ennemis: Liste des ennemis (doit déjà être filtrée pour ne contenir que les vivants)
    :return: True si le joueur est toujours vivant, False sinon
    """
    print("\n--- TOUR DES ENNEMIS ---")

    # Filtrer une dernière fois pour s'assurer qu'on ne traite que les ennemis vivants
    ennemis_vivants = [e for e in ennemis if e.est_vivant]

    if not ennemis_vivants:
        return True  # Aucun ennemi vivant, le joueur a gagné

    for ennemi in ennemis_vivants:
        # Double vérification (au cas où un ennemi serait mort entre-temps)
        if not ennemi.est_vivant:
            continue

        ennemi.appliquer_effets(phase='tour')

        # Vérifier l'étourdissement
        if ennemi.est_etourdi():
            print(f"{ennemi.nom} est étourdi et ne peut pas agir ce tour !")
            ennemi.retirer_effets_expires()
            continue

        # Affichage du début de l'attaque (séparé de la logique)
        afficher_tour_ennemis(joueur, ennemi)

        # Vérifier l'esquive
        a_esquive = esquive(ennemi.vitesse, joueur.vitesse)
        if a_esquive:
            afficher_attaque_ennemi(ennemi, joueur, 0, critique=False, esquive=True)
            ennemi.retirer_effets_expires()
            continue

        # Calculer les dégâts
        degats_bruts = ennemi.calculer_attaque_totale()
        critique = False
        if random.randint(1, 100) <= ennemi.calculer_chance_critique_totale():
            degats_bruts *= 1.5
            critique = True

        degats_finaux = calculer_degats_finaux(ennemi, joueur, degats_bruts, est_capacite=False)

        # Appliquer les dégâts
        joueur.prendre_degats(degats_finaux)

        # Afficher le résultat (séparé de la logique)
        afficher_attaque_ennemi(ennemi, joueur, degats_finaux, critique=critique, esquive=False)

        # Vérifier les effets "mort_imminente" (comme réincarnation)
        if not joueur.est_vivant:
            # Vérifier s'il y a un effet de réincarnation ou similaire
            joueur.appliquer_effets(phase='mort_imminente')
            # Si l'effet a restauré la vie, le joueur est toujours vivant
            if joueur.est_vivant:
                print(f"{joueur.nom} a été sauvé par un effet spécial !")
            else:
                print(f"{joueur.nom} est tombé au combat.")
                return False

        ennemi.retirer_effets_expires()

    return True

def resoudre_effets_fin_tour(combatants):
    for combatant in combatants:
        combatant.retirer_effets_expires()

def _ajuster_stats_ennemi_pour_biome(ennemi: Ennemi, niveau_biome: int):
    """
    Nerf simple : -30% sur toutes les stats des ennemis/boss pour les biomes 1 à 3.
    Aucun changement au-delà du biome 3.
    """
    if not niveau_biome or niveau_biome <= 0 or niveau_biome > 3:
        return

    factor = 0.70  # -30% sur toutes les stats clés

    ennemi.vie_max = max(1, int(ennemi.vie_max * factor))
    ennemi.vie = ennemi.vie_max
    ennemi.base_attaque = ennemi.base_attaque * factor
    ennemi.base_defense = ennemi.base_defense * factor
    ennemi.base_vitesse = ennemi.base_vitesse * factor


def deroulement_combat(joueur, ennemis_a_combattre_ids, reinitialiser_vie=False, reinitialiser_ressources=False, niveau_biome=None):
    """
    Déroule un combat entre le joueur et une liste d'ennemis.

    :param joueur: Le personnage joueur
    :param ennemis_a_combattre_ids: Liste des IDs d'ennemis à combattre
    :param reinitialiser_vie: Si True, remet la vie du joueur à max au début du combat (défaut: False)
    :param reinitialiser_ressources: Si True, remet les ressources (mana/énergie/rage) à max au début (défaut: False)
    :param niveau_biome: Niveau minimum du biome d'origine (pour calculer les bonus de craft sur les ingrédients)
    """
    # Recréer les instances d'ennemis à chaque nouveau combat à partir de leurs IDs
    # Cela garantit qu'ils commencent toujours avec leur vie max
    ennemis_actuels = []
    for ennemi_id in ennemis_a_combattre_ids:
        ennemi = Ennemi.from_data(ennemi_id)
        if ennemi: # S'assurer que l'ennemi a été créé avec succès
            _ajuster_stats_ennemi_pour_biome(ennemi, niveau_biome)
            ennemis_actuels.append(ennemi)

    if not ennemis_actuels:
        print("Aucun ennemi valide à combattre. Le combat ne peut pas commencer.")
        return

    # Réinitialisation optionnelle de la vie et des ressources du joueur
    if reinitialiser_vie:
        joueur.vie = joueur.vie_max
        print(f"{joueur.nom} a été soigné avant le combat. Vie: {joueur.vie:.1f}/{joueur.vie_max:.1f}")

    if reinitialiser_ressources:
        if joueur.specialisation.type_ressource == "Mana":
            joueur.mana = joueur.mana_max
        elif joueur.specialisation.type_ressource == "Energie":
            joueur.energie = joueur.energie_max
        elif joueur.specialisation.type_ressource == "Rage":
            joueur.rage = 0

    # S'assurer que les stats sont à jour (sans modifier la vie si elle n'a pas été réinitialisée)
    joueur.mettre_a_jour_stats_apres_attributs()

    debut_combat(joueur, ennemis_actuels)
    tour_numero = 1

    # Stocker les ennemis initiaux pour calculer l'XP et le butin à la fin
    ennemis_initiaux = list(ennemis_actuels)

    # Filtrer les ennemis vivants au début
    ennemis_actuels = [e for e in ennemis_actuels if e.est_vivant]

    while joueur.est_vivant and ennemis_actuels:
        from utils.affichage import effacer_console
        effacer_console()
        print(f"\n===== TOUR {tour_numero} =====")

        # Tour du joueur
        if not tour_joueur(joueur, ennemis_actuels):
            break

        # Filtrer les ennemis morts après le tour du joueur
        ennemis_actuels = [e for e in ennemis_actuels if e.est_vivant]
        if not ennemis_actuels:
            print("\nTous les ennemis ont été vaincus !")
            break

        # Tour des ennemis (seuls les vivants attaquent)
        if not tour_ennemis(joueur, ennemis_actuels):
            break

        # Filtrer à nouveau après le tour des ennemis (au cas où un effet les aurait tués)
        ennemis_actuels = [e for e in ennemis_actuels if e.est_vivant]

        # Résoudre les effets en fin de tour
        resoudre_effets_fin_tour([joueur] + ennemis_actuels)

        tour_numero += 1

    # Affichage de la fin du combat (séparé de la logique)
    afficher_fin_combat(joueur, victoire=joueur.est_vivant)

    if joueur.est_vivant:
        # Calculer les récompenses pour chaque ennemi vaincu
        ennemis_vaincus = [e for e in ennemis_initiaux if not e.est_vivant]
        total_xp_gagnee = 0
        total_or_gagne = 0
        objets_obtenus = []  # Liste pour stocker les objets obtenus

        print("\n--- Récompenses ---")

        # Détail par ennemi
        for ennemi in ennemis_vaincus:
            xp_ennemi = ennemi.xp_a_donner
            total_xp_gagnee += xp_ennemi

            # Calculer l'or pour cet ennemi
            ennemi_data = DEFINITIONS_ENNEMIS.get(ennemi.id_ennemi, {})
            or_ennemi = calculer_or_ennemi(ennemi_data, xp_ennemi)
            total_or_gagne += or_ennemi

            # Afficher les récompenses de cet ennemi avec couleurs
            from utils.affichage import COULEURS, formater_nombre
            print(f"\n{COULEURS['CYAN']}{ennemi.nom}:{COULEURS['RESET']}")
            print(f"  {COULEURS['VERT']}✓ +{formater_nombre(xp_ennemi)} XP{COULEURS['RESET']}")
            print(f"  {COULEURS['JAUNE']}✓ +{formater_nombre(or_ennemi)} pièces d'or{COULEURS['RESET']}")

            # Gérer le loot de cet ennemi
            if ennemi.loot_table:
                objets_ennemi = []
                for loot_entry in ennemi.loot_table:
                    # Gérer les deux formats : string (100% chance) ou dict (chance personnalisée)
                    if isinstance(loot_entry, str):
                        nom_loot = loot_entry
                        chance_drop = 100
                    elif isinstance(loot_entry, dict):
                        nom_loot = loot_entry.get("nom", "")
                        chance_drop = loot_entry.get("chance", 100)
                        chance_drop = max(1, min(100, chance_drop))
                    else:
                        continue

                    # Vérifier si l'objet est dropé selon la probabilité
                    roll = random.randint(1, 100)
                    if roll > chance_drop:
                        continue

                    # Chercher l'objet dans DEFINITIONS_OBJETS
                    # D'abord par ID (si nom_loot est un ID), puis par nom
                    objet_data = None
                    obj_id_trouve = None

                    # Essayer de trouver par ID d'abord (cas où nom_loot = "rune_ancienne")
                    if nom_loot in DEFINITIONS_OBJETS:
                        obj_id_trouve = nom_loot
                        objet_data = DEFINITIONS_OBJETS[nom_loot]
                    else:
                        # Sinon chercher par nom (cas où nom_loot = "Rune Ancienne")
                        for obj_id, obj_def in DEFINITIONS_OBJETS.items():
                            if obj_def["nom"] == nom_loot:
                                objet_data = obj_def
                                obj_id_trouve = obj_id
                                break

                    # Déterminer le nom d'affichage de l'objet
                    nom_affichage = objet_data["nom"] if objet_data else nom_loot

                    # Vérifier la quantité avant ajout (utiliser le nom d'affichage)
                    quantite_avant = joueur.compter_objet(nom_affichage)

                    # Créer un nouvel objet avec les données de DEFINITIONS_OBJETS si disponible
                    if objet_data:
                        nouvel_objet = Objet(
                            nom=objet_data["nom"],
                            type_objet=objet_data["type"],
                            quantite=1,
                            description=objet_data.get("description", ""),
                            rarete=objet_data.get("rarete", None)
                        )
                    else:
                        # Fallback : créer un objet par défaut si non trouvé dans DEFINITIONS_OBJETS
                        nouvel_objet = Objet(
                            nom=nom_loot,
                            type_objet="matériau",
                            quantite=1,
                            description=""
                        )

                    # Ajouter l'objet à l'inventaire
                    joueur.ajouter_objet(nouvel_objet)

                    # Faire progresser les quêtes si l'objet a un ID (objets de quête)
                    if obj_id_trouve:
                        progresser_quetes_collecter_objet(joueur, obj_id_trouve, quantite=1)

                    # Afficher l'objet obtenu avec couleur selon la rareté
                    from utils.affichage import COULEURS
                    from menus.inventaire import COULEURS_RARETE, RESET_COULEUR
                    quantite_apres = joueur.compter_objet(nom_affichage)
                    rarete_objet = objet_data.get("rarete", "commun") if objet_data else "commun"
                    couleur_rarete = COULEURS_RARETE.get(rarete_objet.lower(), COULEURS['RESET'])
                    if quantite_avant == 0:
                        print(f"  {COULEURS['VERT']}✓ {couleur_rarete}{nom_affichage}{RESET_COULEUR} ajouté à l'inventaire{COULEURS['RESET']}")
                    else:
                        print(f"  {COULEURS['VERT']}✓ {couleur_rarete}{nom_affichage}{RESET_COULEUR} (quantité: {quantite_avant} → {quantite_apres}){COULEURS['RESET']}")

                    objets_ennemi.append(nom_loot)
                    objets_obtenus.append(nom_loot)

            # Gérer le loot d'ingrédients pour cet ennemi (1 ingrédient aléatoire parmi les 3 possibles)
            ingredients_obtenus = ajouter_ingredients_a_inventaire(joueur, ennemi.nom, niveau_biome)
            if ingredients_obtenus:
                from utils.affichage import COULEURS, formater_nombre
                ingredient = ingredients_obtenus[0]  # Un seul ingrédient est obtenu
                quantite = joueur.compter_objet(ingredient.nom)
                if quantite == 1:
                    print(f"  {COULEURS['VERT']}✓ Ingrédient obtenu : {ingredient.nom}{COULEURS['RESET']}")
                else:
                    print(f"  {COULEURS['VERT']}✓ Ingrédient obtenu : {ingredient.nom} (quantité: {formater_nombre(quantite)}){COULEURS['RESET']}")
                objets_obtenus.append(ingredient.nom)

            # Afficher "Aucun objet obtenu" seulement si vraiment aucun objet n'a été obtenu
            if not objets_obtenus:
                print("  (Aucun objet obtenu)")

        # Distribuer XP et Or au joueur avec formatage
        if total_xp_gagnee > 0:
            from utils.affichage import COULEURS, formater_nombre
            joueur.gagner_xp(total_xp_gagnee)
            print(f"\n{COULEURS['VERT']}Total gagné : +{formater_nombre(total_xp_gagnee)} XP{COULEURS['RESET']}")

        if total_or_gagne > 0:
            # Import local pour éviter la dépendance circulaire
            from menus.monnaie import ajouter_or, obtenir_or_joueur
            from utils.affichage import COULEURS, formater_nombre
            ajouter_or(joueur, total_or_gagne)
            print(f"{COULEURS['JAUNE']}Total gagné : +{formater_nombre(total_or_gagne)} pièces d'or{COULEURS['RESET']}")

        # Progresser les quêtes : ennemis tués
        if hasattr(joueur, 'systeme_quetes'):
            from world.progression_quetes import progresser_quetes_tuer_ennemi
            for ennemi in ennemis_vaincus:
                progresser_quetes_tuer_ennemi(joueur, ennemi.id_ennemi, 1)

        # Afficher le total
        print(f"\n{'='*40}")
        print("--- RÉSUMÉ DES RÉCOMPENSES ---")
        print(f"{'='*40}")
        print(f"Total XP gagnée : {total_xp_gagnee}")
        print(f"Total or gagné : {total_or_gagne} pièces")
        # Import local pour éviter la dépendance circulaire
        from menus.monnaie import obtenir_or_joueur
        print(f"Or actuel : {obtenir_or_joueur(joueur)} pièces")
        if objets_obtenus:
            objets_unique = {}
            for obj in objets_obtenus:
                objets_unique[obj] = objets_unique.get(obj, 0) + 1
            print(f"Objets obtenus : {len(objets_obtenus)} objet(s)")
            for nom_obj, qte in objets_unique.items():
                if qte > 1:
                    print(f"  - {nom_obj} x{qte}")
                else:
                    print(f"  - {nom_obj}")
        else:
            print("Aucun objet obtenu.")
        print(f"{'='*40}")
    else:
        # Le joueur a été vaincu (même après vérification des effets de réincarnation)
        print(f"{joueur.nom} a été vaincu...")
        # Téléporter le joueur vers sa capitale (soins gratuits, restauration des ressources)
        print("\nVous êtes transporté vers votre capitale...")
        teleporter_joueur_vers_capitale(joueur)
        # Note : Après téléportation, le joueur est soigné et est_vivant = True
        # La boucle principale pourra continuer normalement
