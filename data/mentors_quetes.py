# data/mentors_quetes.py
# Mapping des mentors qui donnent les quêtes de royaume une par une

# Mapping : {royaume: [liste des (mentor_id, quete_id) dans l'ordre]}
# Chaque mentor donne la quête suivante après complétion de la précédente
MENTORS_QUETES_ROYAUME = {
    "Aerthos": [
        ("Faelar", "aerthos_1_disparitions"),  # Mentor donne la première quête
        ("Faelar", "aerthos_2_rituel_interrompu"),  # Après complétion de la quête 1, Faelar donne la quête 2
        ("gardien", "aerthos_3_traison_revelee"),  # Après complétion de la quête 2, le gardien donne la quête 3
        ("roi_aerion", "aerthos_4_vol_relique"),  # Après complétion de la quête 3, le roi donne la quête 4
    ],
    "Khazak-Dûm": [
        ("Borina", "khazak_1_sabotage_mines"),
        ("Zamir", "khazak_2_secrets_voles"),
        ("dirigeant_khazak", "khazak_3_traison_clan"),
        ("dirigeant_khazak", "khazak_4_vol_relique"),
    ],
    "Luthesia": [
        ("pilier_luthesia", "luthesia_1_brigands_organises"),
        ("Seraphina", "luthesia_2_magie_corrompue"),
        ("roi_magnus", "luthesia_3_traison_cour"),
        ("roi_magnus", "luthesia_4_vol_relique"),
    ],
    "Vrak'thar": [
        ("erudit_demon", "vrakthar_1_rituels_sombres"),
        ("conseiller_demon", "vrakthar_2_secret_krathos"),
        ("dirigeant_vrakthar", "vrakthar_3_traison_demons"),
        ("dirigeant_vrakthar", "vrakthar_4_vol_relique"),
    ],
}


def obtenir_mentor_quete(royaume: str, quete_id: str) -> str:
    """
    Retourne l'ID du mentor qui donne une quête spécifique.

    :param royaume: Nom du royaume
    :param quete_id: ID de la quête
    :return: ID du mentor ou None
    """
    mentors = MENTORS_QUETES_ROYAUME.get(royaume, [])
    for mentor_id, q_id in mentors:
        if q_id == quete_id:
            return mentor_id
    return None


def obtenir_quete_suivante_mentor(royaume: str, quete_completee_id: str) -> tuple:
    """
    Retourne la quête suivante et son mentor après complétion d'une quête.

    :param royaume: Nom du royaume
    :param quete_completee_id: ID de la quête complétée
    :return: (mentor_id, quete_id) ou (None, None) si pas de quête suivante
    """
    mentors = MENTORS_QUETES_ROYAUME.get(royaume, [])
    for i, (mentor_id, q_id) in enumerate(mentors):
        if q_id == quete_completee_id and i + 1 < len(mentors):
            return mentors[i + 1]
    return (None, None)


def obtenir_premiere_quete_royaume(royaume: str) -> tuple:
    """
    Retourne la première quête du royaume et son mentor.

    :param royaume: Nom du royaume
    :return: (mentor_id, quete_id) ou (None, None) si pas de quête
    """
    mentors = MENTORS_QUETES_ROYAUME.get(royaume, [])
    if mentors:
        return mentors[0]
    return (None, None)
