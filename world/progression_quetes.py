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


def progresser_quetes_explorer_zone(joueur, zone_id: str):
    """
    Fait progresser les quêtes liées à explorer une zone.

    :param joueur: Le personnage joueur
    :param zone_id: ID de la zone explorée
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes
    systeme_quetes.progresser_objectif(TypeObjectif.EXPLORER_ZONE, zone_id, 1)

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
        if quete and quete.statut.value == "en_cours" and quete.est_complete():
            # Compléter la quête et obtenir les récompenses
            succes, recompenses = systeme_quetes.completer_quete(quete_id)

            if succes and recompenses:
                _appliquer_recompenses(joueur, quete, recompenses)

                # Vérifier si de nouvelles quêtes doivent être débloquées
                from world.declenchement_quetes import verifier_deblocage_quetes_apres_completion
                verifier_deblocage_quetes_apres_completion(joueur, quete_id)


def _appliquer_recompenses(joueur, quete, recompenses: dict):
    """
    Applique les récompenses d'une quête complétée au joueur.

    :param joueur: Le personnage joueur
    :param quete: La quête complétée
    :param recompenses: Dictionnaire des récompenses
    """
    print(f"\n{'='*60}")
    print(f"🎉 QUÊTE COMPLÉTÉE : {quete.nom}")
    print(f"{'='*60}")
    print("Récompenses obtenues :")

    # XP
    if "xp" in recompenses and recompenses["xp"] > 0:
        xp_gagnee = recompenses["xp"]
        joueur.gagner_xp(xp_gagnee)
        print(f"  ✓ +{xp_gagnee} XP")

    # Or
    if "or" in recompenses and recompenses["or"] > 0:
        or_gagne = recompenses["or"]
        from menus.monnaie import ajouter_or
        ajouter_or(joueur, or_gagne)
        print(f"  ✓ +{or_gagne} pièces d'or")

    # Objets
    if "objets" in recompenses and recompenses["objets"]:
        from classes.objet import Objet
        objets_obtenus = []
        for objet_nom in recompenses["objets"]:
            # Créer l'objet et l'ajouter à l'inventaire
            objet = Objet(nom=objet_nom, type_objet="équipement", quantite=1)
            if objet_nom in joueur.inventaire:
                joueur.inventaire[objet_nom].quantite += 1
            else:
                joueur.inventaire[objet_nom] = objet
            objets_obtenus.append(objet_nom)
            print(f"  ✓ {objet_nom}")

        if objets_obtenus:
            print(f"\n{len(objets_obtenus)} objet(s) ajouté(s) à votre inventaire.")

    print(f"{'='*60}\n")
