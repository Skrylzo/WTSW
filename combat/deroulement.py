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
from world import teleporter_joueur_vers_capitale


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
    print("\n--- DÉBUT DU COMBAT ---")
    # Appliquer les effets avec condition "debut"
    joueur.appliquer_effets(phase='debut')
    for ennemi in ennemis:
        ennemi.appliquer_effets(phase='debut')

    barre_vie_joueur = creer_barre_vie(joueur.vie, joueur.vie_max)
    print(f"{joueur.nom} - Vie: {barre_vie_joueur} {joueur.vie:.1f}/{joueur.vie_max:.1f}")
    print(f"\n{joueur.nom} affronte :")
    for ennemi in ennemis:
        barre_vie_ennemi = creer_barre_vie(ennemi.vie, ennemi.vie_max)
        print(f"{ennemi.nom} - Vie: {barre_vie_ennemi} {ennemi.vie:.1f}/{ennemi.vie_max:.1f}")
        print(f"  Attaque: {ennemi.attaque:.1f} | Défense: {ennemi.defense:.1f} | Vitesse: {ennemi.vitesse:.1f}")
    print("-" * 30)

def tour_joueur(joueur, ennemis):
    resource_display = ""
    if joueur.specialisation.type_ressource == "Mana":
        resource_display = f"Mana: {joueur.mana:.1f}/{joueur.mana_max:.1f}"
    elif joueur.specialisation.type_ressource == "Energie":
        resource_display = f"Énergie: {joueur.energie:.1f}/{joueur.energie_max:.1f}"
    elif joueur.specialisation.type_ressource == "Rage":
        resource_display = f"Rage: {joueur.rage:.1f}/{joueur.rage_max:.1f}"

    # Affichage avec barre de vie
    barre_vie_joueur = creer_barre_vie(joueur.vie, joueur.vie_max)
    print(f"\n--- TOUR DE {joueur.nom} ---")
    print(f"Vie: {barre_vie_joueur} {joueur.vie:.1f}/{joueur.vie_max:.1f} | {resource_display}")

    # Vérifier et appliquer les effets conditionnels (sous_30hp)
    if joueur.vie <= (joueur.vie_max * 0.3):
        joueur.appliquer_effets(phase='sous_30hp')

    joueur.appliquer_effets(phase='tour')

    ennemis_vivants = [e for e  in ennemis if e.est_vivant]
    if not ennemis_vivants:
        print("Il n'y a plus d'ennemis vivants. Fin du combat pour le joueur.")
        return False

    print("\nEnnemis actuels :")
    for i, ennemi in enumerate(ennemis_vivants):
        barre_vie_ennemi = creer_barre_vie(ennemi.vie, ennemi.vie_max)
        print(f"{i+1}. {ennemi.nom} - Vie: {barre_vie_ennemi} {ennemi.vie:.1f}/{ennemi.vie_max:.1f}")

    action_choisie = False
    while not action_choisie:
        print("\nChoisissez votre action :")
        print("1. Attaquer")
        print("2. Utiliser une Capacité")
        print("3. Afficher les Stats")
        print("4. Afficher les Capacités")
        choix = input("Votre action : ")

        if choix == '1':
            if not ennemis_vivants:
                print("Il n'y a personne à attaquer !")
                continue
            cible_ennemi = choisir_cible(joueur, ennemis_vivants)
            if cible_ennemi is None:
                continue

            degats_bruts = joueur.attaquer(cible_ennemi)

            # Vérifier l'esquive
            if esquive(joueur.vitesse, cible_ennemi.vitesse):
                print(f"  {cible_ennemi.nom} a esquivé votre attaque !")
                action_choisie = True
                continue

            critique = False
            if random.randint(1, 100) <= joueur.calculer_chance_critique_totale():
                degats_bruts *= 1.5
                critique = True
                print("  Coup critique !")

            degats_finaux = calculer_degats_finaux(joueur, cible_ennemi, degats_bruts, est_capacite=False)

            print(f"  {joueur.nom} inflige {degats_finaux:.1f} points de dégâts à {cible_ennemi.nom}.")
            cible_ennemi.prendre_degats(degats_finaux)
            action_choisie = True

        elif choix == '2':
            capacite_choisie = choisir_capacite(joueur)
            if capacite_choisie is None:
                continue

            cible_pour_capacite = None
            if capacite_choisie.type_cible == "ennemi" or capacite_choisie.type_cible == "unique":
                # "unique" et "ennemi" nécessitent de choisir une cible ennemie
                if not ennemis_vivants:
                    print("Il n'y a pas d'ennemis à cibler.")
                    continue
                cible_pour_capacite = choisir_cible(joueur, ennemis_vivants)
                if cible_pour_capacite is None:
                    continue
            elif capacite_choisie.type_cible == "aoe":
                cible_pour_capacite = ennemis_vivants
            elif capacite_choisie.type_cible == "soi":
                cible_pour_capacite = joueur
            elif capacite_choisie.type_cible == "aoe_amis":
                cible_pour_capacite = [joueur]
            elif capacite_choisie.type_cible == "aoe_mixte":
                cible_pour_capacite = [joueur] + ennemis_vivants

            # Appel de la méthode 'utiliser' de l'objet Capacite.
            # L'application des dégâts et des soins se fait DANS la méthode 'utiliser'.
            # La méthode utiliser appellera maintenant calculer_degats_finaux pour les dégâts.
            if capacite_choisie.utiliser(joueur, cible_pour_capacite):
                action_choisie = True
            else:
                pass

        elif choix == '3':
            joueur.afficher_stats()
        elif choix == '4':
            joueur.afficher_capacites()
        else:
            print("Action invalide. Veuillez réessayer.")
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

        print(f"{ennemi.nom} attaque {joueur.nom}!")

        # Vérifier l'esquive
        if esquive(ennemi.vitesse, joueur.vitesse):
            print(f"  Vous avez esquivé l'attaque de {ennemi.nom} !")
            ennemi.retirer_effets_expires()
            continue

        degats_bruts = ennemi.calculer_attaque_totale()
        critique = False
        if random.randint(1, 100) <= ennemi.calculer_chance_critique_totale():
            degats_bruts *= 1.5
            critique = True

        degats_finaux = calculer_degats_finaux(ennemi, joueur, degats_bruts, est_capacite=False)

        if critique:
            print("  Coup critique !")
        print(f"  {ennemi.nom} inflige {degats_finaux:.1f} points de dégâts à {joueur.nom}.")
        joueur.prendre_degats(degats_finaux)

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

def deroulement_combat(joueur, ennemis_a_combattre_ids, reinitialiser_vie=False, reinitialiser_ressources=False):
    """
    Déroule un combat entre le joueur et une liste d'ennemis.

    :param joueur: Le personnage joueur
    :param ennemis_a_combattre_ids: Liste des IDs d'ennemis à combattre
    :param reinitialiser_vie: Si True, remet la vie du joueur à max au début du combat (défaut: False)
    :param reinitialiser_ressources: Si True, remet les ressources (mana/énergie/rage) à max au début (défaut: False)
    """
    # Recréer les instances d'ennemis à chaque nouveau combat à partir de leurs IDs
    # Cela garantit qu'ils commencent toujours avec leur vie max
    ennemis_actuels = []
    for ennemi_id in ennemis_a_combattre_ids:
        ennemi = Ennemi.from_data(ennemi_id)
        if ennemi: # S'assurer que l'ennemi a été créé avec succès
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

    print("-" * 30)
    print("\n--- FIN DU COMBAT ---")
    if joueur.est_vivant:
        print(f"{joueur.nom} est victorieux !")

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

            # Afficher les récompenses de cet ennemi
            print(f"\n{ennemi.nom}:")
            print(f"  ✓ +{xp_ennemi} XP")
            print(f"  ✓ +{or_ennemi} pièces d'or")

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

                    # Vérifier la quantité avant ajout
                    quantite_avant = joueur.compter_objet(nom_loot)

                    # Chercher l'objet dans DEFINITIONS_OBJETS par nom
                    objet_data = None
                    for obj_id, obj_def in DEFINITIONS_OBJETS.items():
                        if obj_def["nom"] == nom_loot:
                            objet_data = obj_def
                            break

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

                    # Afficher l'objet obtenu
                    quantite_apres = joueur.compter_objet(nom_loot)
                    if quantite_avant == 0:
                        print(f"  ✓ {nom_loot} ajouté à l'inventaire")
                    else:
                        print(f"  ✓ {nom_loot} (quantité: {quantite_avant} → {quantite_apres})")

                    objets_ennemi.append(nom_loot)
                    objets_obtenus.append(nom_loot)

                if not objets_ennemi:
                    print("  (Aucun objet obtenu)")
            else:
                print("  (Aucun objet obtenu)")

        # Distribuer XP et Or au joueur
        if total_xp_gagnee > 0:
            joueur.gagner_xp(total_xp_gagnee)

        if total_or_gagne > 0:
            # Import local pour éviter la dépendance circulaire
            from menus.capitale import ajouter_or, obtenir_or_joueur
            ajouter_or(joueur, total_or_gagne)

        # Afficher le total
        print(f"\n{'='*40}")
        print("--- RÉSUMÉ DES RÉCOMPENSES ---")
        print(f"{'='*40}")
        print(f"Total XP gagnée : {total_xp_gagnee}")
        print(f"Total or gagné : {total_or_gagne} pièces")
        # Import local pour éviter la dépendance circulaire
        from menus.capitale import obtenir_or_joueur
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
