# data/pnjs_deblocage.py
# Mapping des conditions de déblocage des PNJ dans les capitales

# Mapping : {pnj_id: [liste des IDs de quêtes qui doivent être complétées pour débloquer ce PNJ]}
# Si la liste est vide, le PNJ est visible dès le début
PNJS_DEBLOCAGE = {
    # AERTHOS
    "Faelar": [],  # Mentor - toujours visible
    "gardien": ["aerthos_2_rituel_interrompu"],  # Débloqué après la quête 2
    "traître_aerthos": ["aerthos_3_traison_revelee"],  # Débloqué après la quête 3
    "roi_aerion": ["aerthos_3_traison_revelee"],  # Débloqué après la quête 3
    "Seraphina": ["aerthos_1_disparitions"],  # Débloqué après la quête 1
    "esprit_perdu": [],  # PNJ de zone - toujours visible dans sa zone

    # KHAZAK-DÛM
    "Borina": [],  # Mentor - toujours visible
    "Zamir": ["khazak_1_sabotage_mines"],  # Débloqué après la quête 1
    "pilier": ["khazak_2_secrets_voles"],  # Débloqué après la quête 2
    "traître_khazak": ["khazak_3_traison_clan"],  # Débloqué après la quête 3
    "dirigeant_khazak": ["khazak_3_traison_clan"],  # Débloqué après la quête 3
    "Gelal": ["khazak_2_secrets_voles"],  # Débloqué après la quête 2
    "Grom": ["khazak_1_sabotage_mines"],  # Débloqué après la quête 1

    # LUTHESIA
    "pilier_luthesia": [],  # Mentor - toujours visible
    "Seraphina": ["luthesia_1_brigands_organises"],  # Débloqué après la quête 1 (Dame Seraphina Veritas)
    "roi_magnus": ["luthesia_2_magie_corrompue"],  # Débloqué après la quête 2
    "traître_luthesia": ["luthesia_3_traison_cour"],  # Débloqué après la quête 3
    "chevalier_oublie": [],  # PNJ de zone - toujours visible dans sa zone

    # VRAK'THAR
    "erudit_demon": [],  # Mentor - toujours visible
    "conseiller_demon": ["vrakthar_1_rituels_sombres"],  # Débloqué après la quête 1
    "traître_vrakthar": ["vrakthar_3_traison_demons"],  # Débloqué après la quête 3
    "dirigeant_vrakthar": ["vrakthar_3_traison_demons"],  # Débloqué après la quête 3
    "gardien_ancien": [],  # PNJ de zone - toujours visible dans sa zone

    # PNJ génériques (pour quêtes principales) - Ne sont PAS dans les capitales
    # Ils apparaissent dans les zones d'exploration, pas dans le menu "Parler aux habitants"
    # Donc pas besoin de les gérer ici
}


def pnj_est_visible(joueur, pnj_id: str) -> bool:
    """
    Vérifie si un PNJ est visible pour le joueur dans la capitale.

    :param joueur: Le personnage joueur
    :param pnj_id: ID du PNJ
    :return: True si le PNJ est visible, False sinon
    """
    # Si le PNJ n'est pas dans la liste de déblocage, il n'est PAS visible dans la capitale
    # (sauf s'il s'agit d'un PNJ de zone qui ne devrait pas apparaître ici)
    if pnj_id not in PNJS_DEBLOCAGE:
        return False  # PNJ non listé = pas visible dans la capitale par défaut

    conditions = PNJS_DEBLOCAGE[pnj_id]

    # Si aucune condition (liste vide), le PNJ est toujours visible (mentors)
    if not conditions:
        return True

    # Vérifier que le joueur a un système de quêtes
    if not hasattr(joueur, 'systeme_quetes'):
        return False

    # Vérifier que toutes les quêtes requises sont complétées
    quetes_completees = joueur.systeme_quetes.quetes_completees
    return all(quete_id in quetes_completees for quete_id in conditions)


def obtenir_pnjs_visibles_capitale(joueur) -> list:
    """
    Retourne la liste des PNJ visibles dans la capitale du joueur.

    :param joueur: Le personnage joueur
    :return: Liste des IDs de PNJ visibles
    """
    from world.pnj import PNJS, obtenir_pnj
    from world.royaumes import obtenir_royaume_du_joueur

    # Obtenir le royaume actuel du joueur
    royaume_actuel = getattr(joueur, 'royaume_actuel', None)
    if not royaume_actuel:
        royaume_joueur = obtenir_royaume_du_joueur(joueur.race)
        if royaume_joueur:
            royaume_actuel = royaume_joueur.nom

    pnjs_visibles = []

    # Parcourir tous les PNJ et trouver ceux du royaume actuel qui sont visibles
    for pnj_id, pnj in PNJS.items():
        # Inclure uniquement les PNJ du royaume actuel (exclure les PNJ génériques sans royaume)
        # Les PNJ génériques apparaissent dans les zones d'exploration, pas dans la capitale
        if pnj.royaume == royaume_actuel and pnj_est_visible(joueur, pnj_id):
            pnjs_visibles.append(pnj_id)

    return pnjs_visibles
