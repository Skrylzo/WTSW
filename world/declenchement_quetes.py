# world/declenchement_quetes.py
# Système de déclenchement automatique des quêtes

from world.quetes import SystemeQuetes, TypeQuete, StatutQuete
from world import obtenir_royaume_du_joueur


def verifier_et_declencher_quetes_royaume(joueur, royaume_nom: str):
    """
    Vérifie et déclenche automatiquement UNIQUEMENT la première quête de royaume disponible
    (celle sans prérequis). Les autres quêtes seront données par les mentors après complétion.

    :param joueur: Le personnage joueur
    :param royaume_nom: Nom du royaume où se trouve le joueur
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes

    # Obtenir toutes les quêtes de royaume pour ce royaume
    quetes_royaume = systeme_quetes.obtenir_quetes_royaume(royaume_nom)

    # Trouver UNIQUEMENT la première quête disponible (sans prérequis)
    # Les autres seront données par les mentors après complétion
    for quete in quetes_royaume:
        if quete.statut == StatutQuete.DISPONIBLE:
            # Ne déclencher que les quêtes sans prérequis (première quête de la chaîne)
            if not quete.prerequis:
                peut_accepter, message = quete.peut_etre_acceptee(joueur, systeme_quetes.quetes_completees)
                if peut_accepter:
                    # Ne pas accepter automatiquement - sera donné par le mentor
                    # On marque juste qu'elle est disponible pour le mentor
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
    Pour les quêtes principales : débloque automatiquement.
    Pour les quêtes de royaume : débloque mais ne les accepte pas (seront données par les mentors).

    :param joueur: Le personnage joueur
    :param quete_completee_id: ID de la quête qui vient d'être complétée
    """
    if not hasattr(joueur, 'systeme_quetes'):
        return

    systeme_quetes: SystemeQuetes = joueur.systeme_quetes
    quete_completee = systeme_quetes.obtenir_quete(quete_completee_id)

    if not quete_completee:
        return

    # Pour les quêtes de royaume : débloquer la quête suivante dans la chaîne des mentors
    if quete_completee.type_quete == TypeQuete.ROYAUME and quete_completee.royaume:
        from data.mentors_quetes import obtenir_quete_suivante_mentor
        mentor_id, quete_suivante_id = obtenir_quete_suivante_mentor(quete_completee.royaume, quete_completee_id)

        if quete_suivante_id:
            quete_suivante = systeme_quetes.obtenir_quete(quete_suivante_id)
            if quete_suivante and quete_suivante.statut == StatutQuete.DISPONIBLE:
                # Vérifier que tous les prérequis sont remplis
                prerequis_remplis = all(prereq_id in systeme_quetes.quetes_completees
                                       for prereq_id in quete_suivante.prerequis)
                if prerequis_remplis:
                    # La quête est débloquée mais pas acceptée - le mentor la donnera
                    # On peut juste afficher un message informatif
                    from world.pnj import obtenir_pnj
                    mentor = obtenir_pnj(mentor_id) if mentor_id else None
                    if mentor:
                        VERT = "\033[92m"
                        RESET = "\033[0m"
                        print(f"\n{VERT}💡 {mentor.nom} a une nouvelle mission pour vous. Retournez lui parler dans la capitale pour la recevoir.{RESET}")

    # Pour les quêtes principales : débloquer et accepter automatiquement
    elif quete_completee.type_quete == TypeQuete.PRINCIPALE:
        # Vérifier toutes les quêtes principales pour voir si leurs prérequis sont maintenant remplis
        for quete in systeme_quetes.quetes.values():
            if quete.type_quete == TypeQuete.PRINCIPALE and quete.statut == StatutQuete.DISPONIBLE:
                if quete_completee_id in quete.prerequis:
                    prerequis_remplis = all(prereq_id in systeme_quetes.quetes_completees
                                           for prereq_id in quete.prerequis)
                    if prerequis_remplis:
                        peut_accepter, _ = quete.peut_etre_acceptee(joueur, systeme_quetes.quetes_completees)
                        if peut_accepter:
                            systeme_quetes.accepter_quete(quete.id_quete, joueur)
                            print(f"\n📖 Nouvelle quête principale débloquée : {quete.nom}")
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
