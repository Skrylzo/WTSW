# world/progression_quetes.py
# Système de progression automatique des quêtes

from typing import Optional
from world.quetes import SystemeQuetes, TypeObjectif


def progresser_quetes_tuer_ennemi(joueur, ennemi_id: str, quantite: int = 1):
    """
    Fait progresser les quêtes liées à tuer un ennemi.

    :param joueur: Le personnage joueur
    :param ennemi_id: ID de l'ennemi tué
    :param quantite: Nombre d'ennemis tués (défaut: 1)
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes
    systeme_quetes.progresser_objectif(TypeObjectif.TUER_ENNEMI, ennemi_id, quantite)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_explorer_zone(joueur, zone_id: str, types_quetes=None):
    """
    Fait progresser les quêtes liées à explorer une zone.
    Par défaut, ne progresse que les quêtes de royaume (pour éviter les dépendances circulaires).

    :param joueur: Le personnage joueur
    :param zone_id: Nom réel de la zone explorée (ex: "Les Plaines de Cendres Hurlantes")
    :param types_quetes: Liste des types de quêtes à progresser (par défaut: seulement ROYAUME)
    """
    if not hasattr(joueur, 'systeme_quetes'):
        print(f"[DEBUG] Joueur n'a pas de systeme_quetes")
        return

    from world.quetes import TypeQuete, TypeObjectif
    if types_quetes is None:
        types_quetes = [TypeQuete.ROYAUME]

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Convertir le nom réel de la zone en ID de quête si nécessaire
    from data.mapping_zones_quetes import MAPPING_ZONES_QUETES
    import unicodedata

    def normaliser_zone(nom: str) -> str:
        """Normalise un nom de zone pour la comparaison (gère les problèmes d'encodage)."""
        if not nom:
            return ""
        # Remplacer les caractères de remplacement Unicode (� = U+FFFD) par leurs équivalents probables
        replacements = {
            'Phon�tique': 'Phonétique',
            'sugg�r�e': 'suggérée',
            'Phon�tique sugg�r�e': 'Phonétique suggérée',
            'For�t': 'Forêt',
            'Lumi�re': 'Lumière',
            'Argent�e': 'Argentée',
            'For�t de Lumi�re Argent�e': 'Forêt de Lumière Argentée',
        }
        for old, new in replacements.items():
            nom = nom.replace(old, new)
        # Normaliser les caractères Unicode (NFD -> NFC)
        nom = unicodedata.normalize('NFC', nom)
        # Convertir en minuscules pour la comparaison (insensible à la casse)
        nom = nom.lower()
        return nom.strip()

    zone_id_normalise = normaliser_zone(zone_id)
    zone_id_quete = zone_id

    # Chercher l'ID de quête correspondant au nom réel de la zone
    for id_quete, nom_reel in MAPPING_ZONES_QUETES.items():
        if nom_reel:
            nom_reel_normalise = normaliser_zone(nom_reel)
            # Comparer avec le nom normalisé (plus robuste)
            if nom_reel_normalise == zone_id_normalise:
                zone_id_quete = id_quete
                break
        # Aussi essayer la correspondance exacte au cas où
        elif nom_reel == zone_id:
            zone_id_quete = id_quete
            break

    # Progresser seulement les quêtes du type spécifié
    for quete_id in systeme_quetes.quetes_acceptees:
        quete = systeme_quetes.obtenir_quete(quete_id)
        if quete and quete.statut.value == "en_cours" and quete.type_quete in types_quetes:
            for objectif in quete.objectifs:
                if objectif.type_objectif == TypeObjectif.EXPLORER_ZONE:
                    # Normaliser aussi la cible de l'objectif pour la comparaison
                    cible_normalisee = normaliser_zone(objectif.cible) if objectif.cible else ""
                    # Vérifier la correspondance avec zone_id_quete (ID de quête) ou zone_id (nom réel)
                    correspondance = (
                        objectif.cible == zone_id_quete or
                        objectif.cible == zone_id or
                        cible_normalisee == zone_id_normalise or
                        cible_normalisee == normaliser_zone(zone_id_quete)
                    )

                    if correspondance:
                        objectif.progresser(1)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_explorer_zone_principale(joueur, zone_id: str):
    """
    Fait progresser UNIQUEMENT les quêtes principales liées à explorer une zone.
    Cette fonction est appelée après la complétion complète d'un biome (donjon terminé).
    Pour les quêtes principales, "explorer" signifie compléter le biome, pas juste y entrer.

    NOTE: Les quêtes de royaume progressent à l'entrée dans la zone (via progresser_quetes_explorer_zone),
    pas après la complétion du donjon, pour éviter les dépendances circulaires avec les clés.

    :param joueur: Le personnage joueur
    :param zone_id: Nom réel de la zone explorée (ex: "Les Plaines de Cendres Hurlantes")
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    from world.quetes import TypeQuete, TypeObjectif
    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Convertir le nom réel de la zone en ID de quête si nécessaire
    from data.mapping_zones_quetes import MAPPING_ZONES_QUETES
    zone_id_quete = zone_id

    # Chercher l'ID de quête correspondant au nom réel de la zone
    for id_quete, nom_reel in MAPPING_ZONES_QUETES.items():
        if nom_reel == zone_id:
            zone_id_quete = id_quete
            break

    # Progresser UNIQUEMENT les quêtes principales après complétion du donjon
    for quete_id in systeme_quetes.quetes_acceptees:
        quete = systeme_quetes.obtenir_quete(quete_id)
        if quete and quete.statut.value == "en_cours" and quete.type_quete == TypeQuete.PRINCIPALE:
            for objectif in quete.objectifs:
                if objectif.type_objectif == TypeObjectif.EXPLORER_ZONE:
                    # Pour les quêtes principales, progresser si :
                    # 1. L'objectif correspond exactement au zone_id ou zone_id_quete
                    # 2. OU si l'objectif est "zone" (générique) - n'importe quelle zone complétée progresse
                    if (objectif.cible == zone_id_quete or
                        objectif.cible == zone_id or
                        objectif.cible == "zone"):
                        objectif.progresser(1)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_completer_donjon(joueur, donjon_id: str):
    """
    Fait progresser les quêtes liées à compléter un donjon.

    :param joueur: Le personnage joueur
    :param donjon_id: ID du donjon complété
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes
    systeme_quetes.progresser_objectif(TypeObjectif.COMPLETER_DONJON, donjon_id, 1)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_collecter_objet(joueur, objet_id: str, quantite: int = 1):
    """
    Fait progresser les quêtes liées à collecter un objet.

    :param joueur: Le personnage joueur
    :param objet_id: ID de l'objet collecté
    :param quantite: Quantité collectée (défaut: 1)
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes
    systeme_quetes.progresser_objectif(TypeObjectif.COLLECTER_OBJET, objet_id, quantite)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_parler_pnj(joueur, pnj_id: str):
    """
    Fait progresser les quêtes liées à parler à un PNJ.

    :param joueur: Le personnage joueur
    :param pnj_id: ID du PNJ avec qui on a parlé
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Gérer le cas spécial "mentor" : vérifier si le PNJ avec qui on a parlé est le mentor du royaume
    from data.mentors_quetes import obtenir_premiere_quete_royaume
    from world import obtenir_royaume_du_joueur

    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        royaume_actuel = royaume_joueur.nom if royaume_joueur else None

    if royaume_actuel:
        mentor_id, _ = obtenir_premiere_quete_royaume(royaume_actuel)
        # Si le PNJ avec qui on a parlé est le mentor, progresser aussi l'objectif "mentor"
        if mentor_id == pnj_id:
            systeme_quetes.progresser_objectif(TypeObjectif.PARLER_PNJ, "mentor", 1)

    # Toujours progresser avec l'ID réel du PNJ
    systeme_quetes.progresser_objectif(TypeObjectif.PARLER_PNJ, pnj_id, 1)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def progresser_quetes_atteindre_niveau(joueur, nouveau_niveau: int):
    """
    Fait progresser les quêtes liées à atteindre un niveau.

    :param joueur: Le personnage joueur
    :param nouveau_niveau: Le nouveau niveau atteint
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Pour chaque quête en cours, vérifier si le niveau requis est atteint
    for quete_id in systeme_quetes.quetes_acceptees:
        quete = systeme_quetes.obtenir_quete(quete_id)
        if quete and quete.statut.value == "en_cours":
            for objectif in quete.objectifs:
                if objectif.type_objectif == TypeObjectif.ATTEINDRE_NIVEAU:
                    # La cible contient le niveau requis
                    niveau_requis = int(objectif.cible) if objectif.cible.isdigit() else 0
                    if nouveau_niveau >= niveau_requis and not objectif.est_complete():
                        objectif.progresser(1)

    # Vérifier si des quêtes ont été complétées
    _verifier_et_completer_quetes(joueur, systeme_quetes)


def _verifier_et_completer_quetes(joueur, systeme_quetes: SystemeQuetes):
    """
    Vérifie toutes les quêtes en cours et complète celles qui sont terminées.
    Applique automatiquement les récompenses.

    :param joueur: Le personnage joueur
    :param systeme_quetes: Le système de quêtes
    """
    quetes_a_verifier = list(systeme_quetes.quetes_acceptees)

    for quete_id in quetes_a_verifier:
        quete = systeme_quetes.obtenir_quete(quete_id)
        from world.quetes import StatutQuete
        if quete and quete.statut == StatutQuete.EN_COURS and quete.est_complete():
            # Compléter la quête et obtenir les récompenses
            succes, recompenses = systeme_quetes.completer_quete(quete_id)

            if succes and recompenses:
                _appliquer_recompenses(joueur, quete, recompenses)

                # Vérifier si de nouvelles quêtes doivent être débloquées
                from world.declenchement_quetes import verifier_deblocage_quetes_apres_completion
                verifier_deblocage_quetes_apres_completion(joueur, quete_id)

                # Les PNJ se débloquent automatiquement via pnj_est_visible()
                # Pas besoin d'action supplémentaire ici


def _appliquer_recompenses(joueur, quete, recompenses: dict):
    """
    Applique les récompenses d'une quête complétée au joueur.

    :param joueur: Le personnage joueur
    :param quete: La quête complétée
    :param recompenses: Dictionnaire des récompenses
    """
    from utils.affichage import COULEURS, formater_nombre, COULEUR_OR

    print(f"\n{COULEURS['VERT']}{'='*60}{COULEURS['RESET']}")
    print(f"{COULEURS['VERT']}🎉 QUÊTE COMPLÉTÉE : {quete.nom}{COULEURS['RESET']}")
    print(f"{COULEURS['VERT']}{'='*60}{COULEURS['RESET']}")
    print(f"{COULEURS['VERT']}Récompenses obtenues :{COULEURS['RESET']}")

    # XP
    if "xp" in recompenses and recompenses["xp"] > 0:
        xp_gagnee = recompenses["xp"]
        joueur.gagner_xp(xp_gagnee)
        print(f"  {COULEURS['VERT']}✓ +{formater_nombre(xp_gagnee)} XP{COULEURS['RESET']}")

    # Or
    if "or" in recompenses and recompenses["or"] > 0:
        or_gagne = recompenses["or"]
        from menus.monnaie import ajouter_or
        ajouter_or(joueur, or_gagne)
        print(f"  {COULEUR_OR}✓ +{formater_nombre(or_gagne)} pièces d'or{COULEURS['RESET']}")

    # Objets
    if "objets" in recompenses and recompenses["objets"]:
        from classes.objet import Objet
        from data.objets import DEFINITIONS_OBJETS
        objets_obtenus = []
        for objet_id in recompenses["objets"]:
            # Chercher l'objet dans DEFINITIONS_OBJETS par ID
            objet_data = DEFINITIONS_OBJETS.get(objet_id)
            if objet_data:
                nom_objet = objet_data.get("nom", objet_id)
                type_objet = objet_data.get("type", "matériau")
                description = objet_data.get("description", "")
                rarete = objet_data.get("rarete", None)

                # Créer l'objet avec toutes ses propriétés
                objet = Objet(
                    nom=nom_objet,
                    type_objet=type_objet,
                    quantite=1,
                    description=description,
                    rarete=rarete
                )

                # Ajouter à l'inventaire
                joueur.ajouter_objet(objet)
                objets_obtenus.append(nom_objet)
                # Afficher avec couleur selon la rareté
                from utils.affichage import COULEURS_RARETE
                couleur_rarete = COULEURS_RARETE.get(rarete.lower() if rarete else "commun", COULEURS["RESET"])
                print(f"  {COULEURS['VERT']}✓ {couleur_rarete}{nom_objet}{COULEURS['RESET']} ajouté à l'inventaire")
            else:
                # Fallback : créer un objet par défaut si non trouvé
                objet = Objet(nom=objet_id, type_objet="matériau", quantite=1)
                joueur.ajouter_objet(objet)
                objets_obtenus.append(objet_id)
                print(f"  {COULEURS['VERT']}✓ {objet_id}{COULEURS['RESET']}")

        if objets_obtenus:
            print(f"\n{len(objets_obtenus)} objet(s) ajouté(s) à votre inventaire.")
        print(f"\n{COULEURS['VERT']}Retournez parler au donneur de quête pour découvrir la suite de l'histoire.{COULEURS['RESET']}")
        print(f"{COULEURS['VERT']}{'='*60}{COULEURS['RESET']}\n")
