# world/declenchement_quetes.py
# Système de déclenchement automatique des quêtes

from world.quetes import SystemeQuetes, TypeQuete, StatutQuete
from world import obtenir_royaume_du_joueur


def verifier_et_declencher_quetes_royaume(joueur, royaume_nom: str):
    """
    Vérifie et déclenche automatiquement les quêtes de royaume disponibles.

    :param joueur: Le personnage joueur
    :param royaume_nom: Nom du royaume où se trouve le joueur
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Obtenir toutes les quêtes de royaume pour ce royaume
    quetes_royaume = systeme_quetes.obtenir_quetes_royaume(royaume_nom)

    # Trouver la première quête disponible non acceptée
    for quete in quetes_royaume:
        if quete.statut == StatutQuete.DISPONIBLE:
            peut_accepter, message = quete.peut_etre_acceptee(joueur, systeme_quetes.quetes_completees)
            if peut_accepter:
                # Accepter automatiquement la première quête disponible
                systeme_quetes.accepter_quete(quete.id_quete, joueur)
                print(f"\n📖 Nouvelle quête disponible : {quete.nom}")
                print(f"   {quete.description[:100]}...")
                break


def verifier_et_declencher_quetes_principales(joueur):
    """
    Vérifie et déclenche automatiquement les quêtes principales disponibles.

    :param joueur: Le personnage joueur
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Obtenir toutes les quêtes principales
    quetes_principales = [q for q in systeme_quetes.quetes.values()
                          if q.type_quete == TypeQuete.PRINCIPALE]

    # Trier par niveau requis
    quetes_principales.sort(key=lambda q: q.niveau_requis)

    # Trouver la première quête principale disponible non acceptée
    for quete in quetes_principales:
        if quete.statut == StatutQuete.DISPONIBLE:
            peut_accepter, message = quete.peut_etre_acceptee(joueur, systeme_quetes.quetes_completees)
            if peut_accepter:
                # Accepter automatiquement la première quête principale disponible
                systeme_quetes.accepter_quete(quete.id_quete, joueur)
                print(f"\n📖 Nouvelle quête principale disponible : {quete.nom}")
                print(f"   {quete.description[:100]}...")
                break


def verifier_deblocage_quetes_apres_completion(joueur, quete_completee_id: str):
    """
    Vérifie si de nouvelles quêtes doivent être débloquées après la complétion d'une quête.

    :param joueur: Le personnage joueur
    :param quete_completee_id: ID de la quête qui vient d'être complétée
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Vérifier toutes les quêtes pour voir si leurs prérequis sont maintenant remplis
    for quete in systeme_quetes.quetes.values():
        if quete.statut == StatutQuete.DISPONIBLE:
            # Si cette quête a la quête complétée comme prérequis
            if quete_completee_id in quete.prerequis:
                # Vérifier si tous les prérequis sont remplis
                prerequis_remplis = all(prereq_id in systeme_quetes.quetes_completees
                                       for prereq_id in quete.prerequis)

                if prerequis_remplis:
                    # La quête peut maintenant être acceptée
                    peut_accepter, _ = quete.peut_etre_acceptee(joueur, systeme_quetes.quetes_completees)
                    if peut_accepter:
                        # Accepter automatiquement si c'est une quête principale ou de royaume
                        if quete.type_quete in [TypeQuete.PRINCIPALE, TypeQuete.ROYAUME]:
                            systeme_quetes.accepter_quete(quete.id_quete, joueur)
                            print(f"\n📖 Nouvelle quête débloquée : {quete.nom}")
                            print(f"   {quete.description[:100]}...")


def initialiser_quetes_joueur(joueur):
    """
    Initialise les quêtes pour un nouveau joueur ou lors du chargement.
    Déclenche automatiquement les quêtes disponibles.

    :param joueur: Le personnage joueur
    """
    if not hasattr(joueur, 'systeme_quetes'):
        from menus.quetes import initialiser_systeme_quetes
        joueur.systeme_quetes = initialiser_systeme_quetes()

    # Accepter automatiquement la première quête principale si elle n'est pas déjà acceptée/complétée
    premiere_quete_id = "decouverte_ordre"
    premiere_quete = joueur.systeme_quetes.obtenir_quete(premiere_quete_id)
    if premiere_quete and premiere_quete.statut == StatutQuete.DISPONIBLE:
        joueur.systeme_quetes.accepter_quete(premiere_quete_id, joueur)

    # Déclencher les quêtes de royaume si le joueur est dans un royaume
    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        royaume_actuel = royaume_joueur.nom if royaume_joueur else None

    if royaume_actuel:
        verifier_et_declencher_quetes_royaume(joueur, royaume_actuel)
