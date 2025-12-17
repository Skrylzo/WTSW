# menus/exploration.py
# Menu d'exploration de Valdoria avec système de chapitres

from world import (
    obtenir_royaume_du_joueur,
    obtenir_hub_du_joueur,
    SystemeChapitres,
    Chapitre,
    TypeChapitre,
)
from utils.affichage import effacer_console, afficher_titre_menu_avec_emoji, afficher_separateur, COULEURS
from world.data_loader import attacher_biomes_depuis_valdoria
from combat import deroulement_combat
import re


def nettoyer_caracteres_mal_encodes(texte):
    """Remplace les caractères mal encodés par leurs équivalents corrects."""
    # Essayer de corriger les encodages courants (Windows-1252 mal interprété en utf-8)
    try:
        # Si le texte contient des caractères mal encodés, essayer de les corriger
        # en encodant en latin1 puis décodant en utf-8
        texte_corrige = texte.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
        # Si ça a changé quelque chose, utiliser le texte corrigé
        if texte_corrige != texte:
            texte = texte_corrige
    except:
        pass

    # Remplacements manuels pour les cas spécifiques
    # Caractères mal encodés courants (Windows-1252 -> UTF-8)
    replacements = {
        '\x82': 'é',  # é mal encodé (Windows-1252)
        '\x83': 'é',  # é mal encodé (autre)
        '\x88': 'è',  # è mal encodé
        '\x89': 'é',  # é mal encodé
        '\x8a': 'ê',  # ê mal encodé
        '\x8c': 'î',  # î mal encodé
        '\x8e': 'î',  # î mal encodé
        '\x95': '•',  # • mal encodé
        '\x96': '–',  # – mal encodé
        '\x97': '—',  # — mal encodé
        '\xa0': ' ',  # espace insécable
    }
    for mal_encode, correct in replacements.items():
        texte = texte.replace(mal_encode, correct)

    # Remplacement générique pour les caractères de remplacement Unicode (U+FFFD)
    # qui apparaissent parfois lors de mauvais encodages
    texte = texte.replace('\ufffd', 'é')  # Caractère de remplacement -> é (le plus courant)

    return texte


def menu_exploration_valdoria(joueur):
    """
    Menu principal d'exploration de Valdoria.
    Permet d'explorer les zones débloquées selon les chapitres.
    """
    attacher_biomes_depuis_valdoria()
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    if not royaume_joueur:
        print("Erreur : Impossible de trouver votre royaume.")
        return

    # Pour l'instant, on crée un système de chapitres de base
    # TODO: Charger les chapitres depuis un fichier de configuration
    systeme_chapitres = creer_systeme_chapitres_base(joueur, royaume_joueur)

    while True:
        effacer_console()
        chapitre_actuel = systeme_chapitres.obtenir_chapitre_actuel()

        if not chapitre_actuel:
            print("\nErreur : Aucun chapitre actuel disponible.")
            break

        afficher_titre_menu_avec_emoji("EXPLORATION DE VALDORIA", "exploration")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

        # Afficher les informations du chapitre actuel
        chapitre_actuel.afficher_info(nom_royaume=royaume_joueur.nom if royaume_joueur else None)

        # Afficher les options
        print(f"\n{COULEURS['BLEU']}Que voulez-vous faire ?{COULEURS['RESET']}")
        print()
        print("1. 🌍 Explorer une zone")
        print()
        print("2. 📚 Informations sur les royaumes")
        print()
        print("3. ⬅️  Retour au menu principal (r)")

        choix = input(f"\n{COULEURS['BLEU']}Votre choix : {COULEURS['RESET']}").strip().lower()

        if choix == '1':
            menu_selection_zone(joueur, royaume_joueur, systeme_chapitres)
        elif choix == '2':
            afficher_infos_royaumes(joueur)
        elif choix == '3' or choix == 'r':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_selection_zone(joueur, royaume, systeme_chapitres: SystemeChapitres):
    """
    Menu de sélection de zone à explorer.
    """
    effacer_console()
    chapitre_actuel = systeme_chapitres.obtenir_chapitre_actuel()
    if not chapitre_actuel:
        print("\nAucune zone disponible pour l'instant.")
        return

    zones_accessibles = chapitre_actuel.zones_accessibles

    if not zones_accessibles:
        print("\nAucune zone disponible dans ce chapitre.")
        print("Complétez les objectifs pour débloquer de nouvelles zones.")
        return

    afficher_titre_menu_avec_emoji("SÉLECTION DE ZONE", "zone")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    print()

    # Afficher les zones avec leurs niveaux recommandés
    zones_liste = []

    for i, zone_id in enumerate(zones_accessibles, 1):
        est_completee = zone_id in chapitre_actuel.zones_completees
        statut = "✓" if est_completee else "○"

        # Corriger les caractères mal encodés
        zone_nom_affichage = nettoyer_caracteres_mal_encodes(zone_id)

        # Extraire le nom phonétique et transformer "(Phonétique suggérée : X)" en "(X)"
        # Pattern flexible pour détecter "(Phonétique suggérée : ...)" avec ou sans caractères mal encodés
        # Le pattern accepte n'importe quel caractère entre les lettres pour gérer les encodages
        pattern_phonetique = r'\([Pp]hon[^\s)]*tique\s+sugg[^\s)]*r[^\s)]*e\s*:\s*([^)]+)\)'
        match = re.search(pattern_phonetique, zone_nom_affichage, re.IGNORECASE)
        if match:
            nom_phonetique = match.group(1).strip()
            # Corriger aussi les caractères mal encodés dans le nom phonétique
            nom_phonetique = nettoyer_caracteres_mal_encodes(nom_phonetique)
            # Remplacer toute la partie "(Phonétique suggérée : X)" par juste "(X)"
            zone_nom_affichage = re.sub(pattern_phonetique, f'({nom_phonetique})', zone_nom_affichage, flags=re.IGNORECASE)

        # Trouver le biome pour afficher le niveau recommandé
        biome_zone = trouver_biome_par_nom(royaume, zone_id)
        niveau_info = ""
        if biome_zone:
            niveau_info = f" ({biome_zone.afficher_niveau_recommande()})"

        print(f"{i}. {zone_nom_affichage}{niveau_info} {statut}")
        print()  # Saut de ligne entre chaque zone
        zones_liste.append(zone_id)

    print(f"{len(zones_liste) + 1}. ⬅️  Retour (r)")

    try:
        choix_input = input(f"\n{COULEURS['BLEU']}Votre choix : {COULEURS['RESET']}").strip().lower()
        if choix_input == 'r':
            return
        choix = int(choix_input)

        if 1 <= choix <= len(zones_liste):
            zone_choisie = zones_liste[choix - 1]
            explorer_zone(joueur, royaume, zone_choisie, systeme_chapitres)
        elif choix == len(zones_liste) + 1:
            return
        else:
            print("Choix invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


def explorer_zone(joueur, royaume, zone_id: str, systeme_chapitres: SystemeChapitres):
    """
    Explore une zone : menu d'actions (combat, parler aux PNJ, donjon).
    """
    effacer_console()
    try:
        biome_cible = trouver_biome_par_nom(royaume, zone_id)
    except Exception as e:
        print(f"\n⚠️  Erreur lors de la recherche du biome : {e}")
        print("Retour au menu précédent...")
        import traceback
        traceback.print_exc()
        return

    # Progresser les quêtes "explorer zone" dès l'entrée dans la zone
    # "Explorer" signifie entrer dans la zone, pas la compléter
    if hasattr(joueur, 'systeme_quetes'):
        from world.progression_quetes import progresser_quetes_explorer_zone
        progresser_quetes_explorer_zone(joueur, zone_id)

    # Afficher les informations du biome
    if biome_cible:
        if biome_cible.description:
            print(f"Description: {biome_cible.description[:200]}...")  # Afficher les 200 premiers caractères
        print(f"Niveau recommandé: {biome_cible.afficher_niveau_recommande()}")
        print(f"Votre niveau actuel: {joueur.niveau}")

        # Afficher un avertissement et demander confirmation si le niveau est trop faible
        if joueur.niveau < biome_cible.niveau_min:
            print(f"⚠️  Attention: Cette zone est recommandée pour les niveaux {biome_cible.niveau_min}-{biome_cible.niveau_max}. "
                  f"Votre niveau ({joueur.niveau}) est inférieur au minimum recommandé.")
            print()

            while True:
                reponse = input("Voulez-vous continuer malgré tout ? (o/n): ").strip().lower()
                if reponse in ('o', 'oui', 'y', 'yes'):
                    print("Vous décidez de continuer malgré les risques...")
                    print()
                    break
                elif reponse in ('n', 'non', 'no'):
                    print("Vous rebroussez chemin. Il est peut-être sage d'attendre d'être plus fort...")
                    print()
                    return
                else:
                    print("Réponse invalide. Veuillez répondre par 'o' (oui) ou 'n' (non).")
        else:
            print()

    # Menu d'actions dans la zone
    while True:
        # Nettoyer le nom de la zone (enlever "phonétique suggérée" et corriger les caractères mal encodés)
        zone_nom_affichage = nettoyer_caracteres_mal_encodes(zone_id)

        # Extraire le nom phonétique et transformer "(Phonétique suggérée : X)" en "(X)"
        pattern_phonetique = r'\([Pp]hon[^\s)]*tique\s+sugg[^\s)]*r[^\s)]*e\s*:\s*([^)]+)\)'
        match = re.search(pattern_phonetique, zone_nom_affichage, re.IGNORECASE)
        if match:
            nom_phonetique = match.group(1).strip()
            nom_phonetique = nettoyer_caracteres_mal_encodes(nom_phonetique)
            zone_nom_affichage = re.sub(pattern_phonetique, f'({nom_phonetique})', zone_nom_affichage, flags=re.IGNORECASE)

        try:
            zone_id_upper = zone_nom_affichage.upper()
        except Exception:
            zone_id_upper = zone_nom_affichage
        afficher_titre_menu_avec_emoji(zone_id_upper, "zone")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

        # Vérifier les PNJ présents dans la zone
        from data.pnjs_zones import obtenir_pnjs_zone, zone_contient_pnj
        pnjs_zone = obtenir_pnjs_zone(zone_id)
        a_des_pnj = zone_contient_pnj(zone_id)

        # Vérifier si la zone a un donjon
        a_donjon = biome_cible and biome_cible.donjon_nom

        # Afficher les options disponibles
        options = []
        option_num = 1

        print(f"\n{COULEURS['BLEU']}Que voulez-vous faire ?{COULEURS['RESET']}\n")

        # Option 1 : Combattre
        print(f"{option_num}. ⚔️  Combattre des ennemis")
        print()  # Saut de ligne
        options.append('combat')
        option_num += 1

        # Option 3 : Explorer le donjon (si disponible)
        if a_donjon:
            from data.cles_donjons import joueur_possede_cle_donjon, donjon_requiert_cle, obtenir_cle_donjon
            from data.objets import DEFINITIONS_OBJETS

            # Nettoyer le nom du donjon
            donjon_nom_affichage = nettoyer_caracteres_mal_encodes(biome_cible.donjon_nom)
            match_donjon = re.search(pattern_phonetique, donjon_nom_affichage, re.IGNORECASE)
            if match_donjon:
                nom_phonetique_donjon = match_donjon.group(1).strip()
                nom_phonetique_donjon = nettoyer_caracteres_mal_encodes(nom_phonetique_donjon)
                donjon_nom_affichage = re.sub(pattern_phonetique, f'({nom_phonetique_donjon})', donjon_nom_affichage, flags=re.IGNORECASE)

            # Vérifier si ce donjon nécessite une clé
            if donjon_requiert_cle(biome_cible.donjon_nom):
                # Ce donjon nécessite une clé, vérifier si le joueur l'a
                possede_cle = joueur_possede_cle_donjon(joueur, biome_cible.donjon_nom)

                if possede_cle:
                    print(f"{option_num}. 🏰 Explorer le donjon : {donjon_nom_affichage}")
                    print()  # Saut de ligne
                    options.append('donjon')
                    option_num += 1
                else:
                    # Afficher l'option mais indiquer qu'une clé est nécessaire
                    cle_id = obtenir_cle_donjon(biome_cible.donjon_nom)
                    nom_cle = "clé"
                    if cle_id:
                        cle_data = DEFINITIONS_OBJETS.get(cle_id)
                        if cle_data:
                            nom_cle = cle_data.get("nom", "clé")
                    print(f"{option_num}. 🏰 Explorer le donjon : {donjon_nom_affichage} {COULEURS['ROUGE']}🔒{COULEURS['RESET']} (Clé requise : {nom_cle})")
                    print()  # Saut de ligne
                    options.append('donjon_verrouille')
                    option_num += 1
            else:
                # Ce donjon ne nécessite pas de clé (donjon non listé dans CLES_DONJONS)
                print(f"{option_num}. 🏰 Explorer le donjon : {donjon_nom_affichage}")
                print()  # Saut de ligne
                options.append('donjon')
                option_num += 1

        # Option retour
        print(f"{option_num}. ⬅️  Retour (r)")
        options.append('retour')

        choix = input(f"\n{COULEURS['BLEU']}Votre choix : {COULEURS['RESET']}").strip().lower()

        try:
            if choix == 'r':
                return
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                action = options[choix_int - 1]

                if action == 'combat':
                    _lancer_combat_zone(joueur, biome_cible, zone_id, systeme_chapitres)
                elif action == 'pnj':
                    _parler_pnj_zone(joueur, pnjs_zone)
                elif action == 'donjon':
                    _explorer_donjon(joueur, biome_cible, zone_id, systeme_chapitres)
                elif action == 'donjon_verrouille':
                    from data.cles_donjons import obtenir_cle_donjon
                    from data.objets import DEFINITIONS_OBJETS
                    cle_id = obtenir_cle_donjon(biome_cible.donjon_nom)
                    nom_cle = "cle"
                    if cle_id:
                        cle_data = DEFINITIONS_OBJETS.get(cle_id)
                        if cle_data:
                            nom_cle = cle_data.get("nom", "cle")
                    print(f"\n🔒 Ce donjon est verrouille !")
                    print(f"Vous avez besoin de la {nom_cle} pour y acceder.")
                    print(f"Completez les quetes de royaume pour obtenir cette cle.")
                    input("\nAppuyez sur Entree pour continuer...")
                elif action == 'retour':
                    return
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def _lancer_combat_zone(joueur, biome_cible, zone_id: str, systeme_chapitres: SystemeChapitres):
    """
    Lance un combat dans la zone.
    """
    if biome_cible and biome_cible.mobs_ids:
        ennemis_a_combattre_ids = biome_cible.obtenir_mobs_aleatoires(nombre=1)
    else:
        print("(Aucun biome trouvé ou pas de mobs définis, combat de secours)")
        ennemis_a_combattre_ids = ["gobelin_basique"]

    # Lancer le combat
    niveau_biome = biome_cible.niveau_min if biome_cible else None
    resultat_combat = deroulement_combat(joueur, ennemis_a_combattre_ids, niveau_biome=niveau_biome)

    # Après le combat, vérifier si le joueur a gagné ou a fui
    if joueur.est_vivant:
        # Si le combat a été quitté volontairement (resultat_combat == False), afficher le message de fuite
        if resultat_combat is False:
            print(f"\n{COULEURS['ROUGE']}Vous avez fui le combat comme un lâche...{COULEURS['RESET']}")
            print()
            input("Appuyez sur Entrée pour continuer...")
            effacer_console()
            return

        # Nettoyer le nom de la zone (enlever "phonétique suggérée" mais garder le nom phonétique)
        zone_nom_affichage = nettoyer_caracteres_mal_encodes(zone_id)

        # Extraire le nom phonétique et transformer "(Phonétique suggérée : X)" en "(X)"
        pattern_phonetique = r'\([Pp]hon[^\s)]*tique\s+sugg[^\s)]*r[^\s)]*e\s*:\s*([^)]+)\)'
        match = re.search(pattern_phonetique, zone_nom_affichage, re.IGNORECASE)
        if match:
            nom_phonetique = match.group(1).strip()
            nom_phonetique = nettoyer_caracteres_mal_encodes(nom_phonetique)
            zone_nom_affichage = re.sub(pattern_phonetique, f'({nom_phonetique})', zone_nom_affichage, flags=re.IGNORECASE)

        print(f"\nVous avez vaincu les ennemis de {zone_nom_affichage}.")
        print()

        # Proposer de combattre à nouveau ou retourner au menu
        print(f"{COULEURS['CYAN']}1. ⚔️  Affronter un autre groupe d'ennemis{COULEURS['RESET']}")
        print()
        print(f"{COULEURS['GRIS']}Appuyez sur Entrée pour retourner au menu{COULEURS['RESET']}")
        print()

        choix = input(f"{COULEURS['BLEU']}Votre choix : {COULEURS['RESET']}").strip()

        if choix == '1':
            # Relancer un combat
            _lancer_combat_zone(joueur, biome_cible, zone_id, systeme_chapitres)
        else:
            # Retour au menu avec clear
            effacer_console()
            return
    else:
        # Le joueur est déjà téléporté à sa capitale par deroulement_combat
        return


def _parler_pnj_zone(joueur, pnjs_zone: list):
    """
    Permet de parler aux PNJ présents dans la zone.
    """
    if not pnjs_zone:
        print("\nAucun PNJ présent dans cette zone.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    from world.pnj import obtenir_pnj
    from menus.pnj import parler_a_pnj

    while True:
        effacer_console()
        print()
        afficher_titre_menu_avec_emoji("HABITANTS DE LA ZONE", "pnj")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()

        options = []
        option_num = 1

        for pnj_id in pnjs_zone:
            pnj = obtenir_pnj(pnj_id)
            if pnj:
                print(f"{option_num}. {pnj.nom}")
                if pnj.description:
                    print(f"   {pnj.description}")
                options.append(pnj_id)
                option_num += 1

        print(f"{option_num}. ⬅️  Retour (r)")

        choix = input(f"\n{COULEURS['CYAN']}Votre choix : {COULEURS['RESET']}").strip().lower()

        try:
            if choix == 'r':
                return
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                pnj_id = options[choix_int - 1]
                parler_a_pnj(joueur, pnj_id)
                input("\nAppuyez sur Entrée pour continuer...")
            elif choix_int == len(options) + 1:
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def _explorer_donjon(joueur, biome_cible, zone_id: str, systeme_chapitres: SystemeChapitres):
    """
    Explore le donjon de la zone.
    Le donjon consiste en une série de combats contre des mobs du biome, puis le boss final.
    Nécessite une clé pour y accéder.
    """
    if not biome_cible or not biome_cible.donjon_nom:
        print("\nAucun donjon disponible dans cette zone.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    # Vérifier si le joueur possède la clé nécessaire
    from data.cles_donjons import joueur_possede_cle_donjon, donjon_requiert_cle, obtenir_cle_donjon
    from data.objets import DEFINITIONS_OBJETS

    # Vérifier si ce donjon nécessite une clé
    if donjon_requiert_cle(biome_cible.donjon_nom):
        # Ce donjon nécessite une clé, vérifier si le joueur l'a
        if not joueur_possede_cle_donjon(joueur, biome_cible.donjon_nom):
            cle_id = obtenir_cle_donjon(biome_cible.donjon_nom)
            nom_cle = "clé"
            if cle_id:
                cle_data = DEFINITIONS_OBJETS.get(cle_id)
                if cle_data:
                    nom_cle = cle_data.get("nom", "clé")
            print(f"\n🔒 Ce donjon est verrouillé !")
            print(f"Vous avez besoin de la {nom_cle} pour y accéder.")
            print(f"Complétez les quêtes de royaume pour obtenir cette clé.")
            input("\nAppuyez sur Entrée pour continuer...")
            return

    # Demander confirmation avant d'entrer dans le donjon
    print(f"\n{'='*60}")
    try:
        donjon_nom_upper = biome_cible.donjon_nom.upper()
    except Exception:
        # En cas d'erreur avec upper() (caractères spéciaux), utiliser le nom tel quel
        donjon_nom_upper = biome_cible.donjon_nom
    afficher_titre_menu_avec_emoji(donjon_nom_upper, "donjon")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    if biome_cible.description:
        print(f"\n{biome_cible.description}\n")

    print(f"{COULEURS['JAUNE']}⚠️  Attention : Entrer dans ce donjon vous mènera à travers une série de combats{COULEURS['RESET']}")
    print(f"{COULEURS['JAUNE']}   contre les créatures qui y résident, puis vous affronterez le gardien final.{COULEURS['RESET']}")
    print(f"{COULEURS['JAUNE']}   Assurez-vous d'être prêt avant de continuer.{COULEURS['RESET']}\n")

    while True:
        reponse = input("Voulez-vous entrer dans le donjon ? (o/n): ").strip().lower()
        if reponse in ('n', 'non', 'no'):
            print("Vous rebroussez chemin. Il est peut-être sage de mieux vous préparer...")
            return
        elif reponse in ('o', 'oui', 'y', 'yes'):
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'o' (oui) ou 'n' (non).")

    print(f"\nVous pénétrez dans les profondeurs de {biome_cible.donjon_nom}...")
    print("L'air devient lourd et menaçant...\n")

    # Déterminer le nombre de combats avant le boss (selon la difficulté du biome)
    # Biome 1-2 : 2 combats, Biome 3-4 : 3 combats
    nombre_combats_mobs = 2 if biome_cible.difficulte <= 2 else 3

    # Vérifier qu'il y a des mobs disponibles
    if not biome_cible.mobs_ids:
        print("⚠️  Aucun ennemi défini pour ce biome. Passage direct au boss.")
    else:
        # Série de combats contre les mobs du biome
        print(f"Vous allez devoir affronter {nombre_combats_mobs} groupes d'ennemis avant d'atteindre le gardien.\n")
        input("Appuyez sur Entrée pour commencer...")

        for combat_num in range(1, nombre_combats_mobs + 1):
            afficher_titre_menu_avec_emoji(f"COMBAT {combat_num}/{nombre_combats_mobs}", "combat")
            afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
            print()

            # Obtenir des mobs aléatoires du biome (1-2 mobs par combat selon la difficulté)
            nombre_mobs = 1 if biome_cible.difficulte <= 2 else 2
            ennemis_ids = biome_cible.obtenir_mobs_aleatoires(nombre=nombre_mobs)

            if ennemis_ids:
                print(f"Des créatures hostiles apparaissent devant vous !")
                deroulement_combat(joueur, ennemis_ids, niveau_biome=biome_cible.niveau_min)

                # Si le joueur meurt, on sort du donjon
                if not joueur.est_vivant:
                    print(f"\n💀 Vous avez été vaincu dans {biome_cible.donjon_nom}...")
                    print("Vous êtes transporté à votre capitale pour récupérer.")
                    return

                # Si ce n'est pas le dernier combat, proposer de continuer ou se retirer
                if combat_num < nombre_combats_mobs:
                    print(f"\n✓ Combat {combat_num} terminé. Vous pouvez continuer ou vous retirer.")
                    while True:
                        choix = input("Continuer ? (o/n): ").strip().lower()
                        if choix in ('n', 'non', 'no'):
                            print("Vous décidez de vous retirer du donjon pour mieux vous préparer...")
                            return
                        elif choix in ('o', 'oui', 'y', 'yes'):
                            break
                        else:
                            print("Réponse invalide. Veuillez répondre par 'o' (oui) ou 'n' (non).")

        effacer_console()
        print()
        afficher_titre_menu_avec_emoji("VOUS ATTEIGNEZ LA SALLE DU GARDIEN", "donjon")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()
        print("Vous avez survécu aux épreuves du donjon.")
        print("Le gardien final vous attend dans la salle principale...\n")
        input("Appuyez sur Entrée pour affronter le gardien...")

    # Combat final contre le boss
    if biome_cible.boss_id:
        afficher_titre_menu_avec_emoji("AFFRONTEMENT FINAL", "combat")
        afficher_separateur(style="simple", couleur=COULEURS["ROUGE"])
        print()
        print(f"Le gardien de {biome_cible.donjon_nom} se dresse devant vous !")
        print("C'est maintenant ou jamais...\n")

        deroulement_combat(joueur, [biome_cible.boss_id], niveau_biome=biome_cible.niveau_min)

        if joueur.est_vivant:
            print(f"\n{'='*60}")
            print(f"🎉 VICTOIRE ! 🎉")
            print(f"{'='*60}\n")
            print(f"Vous avez vaincu le gardien de {biome_cible.donjon_nom} !")
            print(f"La zone {zone_id} est maintenant considérée comme explorée et sécurisée.\n")

            # Compléter la zone après avoir battu le boss
            chapitre = systeme_chapitres.obtenir_chapitre_actuel()
            if chapitre:
                chapitre.completer_zone(zone_id)

            # Progresser les quêtes : donjon complété
            # Note : La progression "explorer zone" pour les quêtes de royaume est déjà faite à l'entrée dans la zone
            # Pour les quêtes principales, "explorer zone" signifie compléter le biome (donjon terminé)
            if hasattr(joueur, 'systeme_quetes'):
                from world.progression_quetes import progresser_quetes_completer_donjon, progresser_quetes_explorer_zone_principale
                progresser_quetes_completer_donjon(joueur, biome_cible.donjon_nom)
                # Progresser les quêtes principales "explorer zone" après complétion du donjon
                progresser_quetes_explorer_zone_principale(joueur, zone_id)
        else:
            print(f"\n💀 Vous avez été vaincu par le gardien...")
            print("Vous êtes transporté à votre capitale pour récupérer.")
            return
    else:
        print("⚠️  Aucun boss défini pour ce donjon.")
        print("Cette zone ne peut pas être complétée sans boss.")

    input("\nAppuyez sur Entrée pour continuer...")


def afficher_infos_royaumes(joueur):
    """
    Affiche des informations sur les royaumes.
    """
    royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
    hub_joueur = obtenir_hub_du_joueur(joueur.race)

    effacer_console()
    afficher_titre_menu_avec_emoji("INFORMATIONS SUR LES ROYAUMES", "zone")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])

    if royaume_joueur:
        print(f"\n{COULEURS['MAGENTA']}🏛️  Votre royaume :{COULEURS['RESET']} {COULEURS['CYAN']}{royaume_joueur.nom}{COULEURS['RESET']}")
        print(f"{COULEURS['BLEU']}👤 Race associée :{COULEURS['RESET']} {COULEURS['JAUNE']}{royaume_joueur.race_associee}{COULEURS['RESET']}")
        print(f"{COULEURS['VERT']}🏰 Capitale :{COULEURS['RESET']} {COULEURS['CYAN']}{royaume_joueur.capitale}{COULEURS['RESET']}")
        if royaume_joueur.description:
            print(f"\n{COULEURS['GRIS']}{royaume_joueur.description}{COULEURS['RESET']}")

        if hub_joueur:
            print(f"\n{COULEURS['MAGENTA']}📍 Capitale actuelle :{COULEURS['RESET']} {COULEURS['CYAN']}{hub_joueur.nom}{COULEURS['RESET']}")
            print(f"{COULEURS['GRIS']}{hub_joueur.description}{COULEURS['RESET']}")

    print(f"\n")
    afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
    input(f"\n{COULEURS['CYAN']}Appuyez sur Entrée pour continuer...{COULEURS['RESET']}")


def creer_systeme_chapitres_base(joueur, royaume_joueur):
    """
    Crée un système de chapitres de base pour le démarrage.
    TODO: Remplacer par un chargement depuis fichier de configuration.
    """
    systeme = SystemeChapitres()

    if royaume_joueur and royaume_joueur.biomes:
        zones_royaume = [biome.nom for biome in royaume_joueur.biomes]
    else:
        nom_royaume = royaume_joueur.nom if royaume_joueur else "votre royaume"
        zones_royaume = [
            f"Biome 1 de {nom_royaume}",
            f"Biome 2 de {nom_royaume}",
        ]

    chapitre1 = Chapitre(
        numero=1,
        titre="Les Premiers Pas",
        type_chapitre=TypeChapitre.EXPLORATION_LIBRE,
        description=f"Vous commencez votre aventure dans {royaume_joueur.nom if royaume_joueur else 'Valdoria'}. "
                   f"Explorez les zones de votre royaume pour progresser.",
        zones_accessibles=zones_royaume,
        objectifs=[],
        chapitre_suivant=2,
    )
    chapitre1.est_debloque = True
    systeme.ajouter_chapitre(chapitre1)
    systeme.chapitre_actuel_numero = 1

    return systeme


def trouver_biome_par_nom(royaume, nom_biome):
    if not royaume:
        return None
    for biome in royaume.biomes:
        if biome.nom == nom_biome:
            return biome
    return None
