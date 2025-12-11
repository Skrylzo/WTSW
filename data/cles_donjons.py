# data/cles_donjons.py
# Mapping des clés nécessaires pour accéder aux donjons

def _normaliser_nom_donjon(nom: str) -> str:
    """
    Normalise un nom de donjon pour la comparaison (supprime espaces, normalise apostrophes, gère les caractères mal encodés).
    """
    if not nom:
        return ""
    import unicodedata
    import re

    # Supprimer les espaces en début/fin
    nom = nom.strip()

    # Normaliser les apostrophes
    nom = nom.replace("'", "'").replace("'", "'")

    # Remplacer les caractères de remplacement Unicode (� = U+FFFD) par leurs équivalents probables
    # Cela gère les cas où le fichier a été mal encodé
    replacements = {
        'Mausol�e': 'Mausolée',
        'G�ants': 'Géants',
        'Bris�s': 'Brisés',
        'C�lestes': 'Célestes',
        'Oubli�': 'Oublié',
        'Oubli�s': 'Oubliés',
        'M�moire': 'Mémoire',
        'Fractur�e': 'Fracturée',
        'M�c�ne': 'Mécène',
        '�mes': 'Âmes',
        'D�prav�es': 'Dépravées',
    }

    for old, new in replacements.items():
        nom = nom.replace(old, new)

    # Normaliser les caractères Unicode (NFD -> NFC)
    nom = unicodedata.normalize('NFC', nom)

    return nom


# Mapping : {nom_donjon: id_cle}
# Le nom du donjon doit correspondre exactement à biome_cible.donjon_nom (après normalisation)
CLES_DONJONS = {
    # AERTHOS
    "Le Sanctuaire des Murmures Oubliés (Ael'doria)": "cle_donjon_aerthos_1",
    "Le Cœur Corrompu de la Forêt": "cle_donjon_aerthos_2",
    "Les Profondeurs Célestes (Astrea's Veins)": "cle_donjon_aerthos_3",
    "Le Sanctuaire du Songe Lunaire (Somnus'Shrine)": "cle_donjon_aerthos_4",
    "Le Bastion des Vents Anciens (Ael'wyn's Roost)": "cle_donjon_aerthos_5",

    # KHAZAK-DÛM
    "La Redoute d'Obscurité (Skala-Kara)": "cle_donjon_khazak_1",
    "Le Caveau des Secrets du Premier Âge": "cle_donjon_khazak_2",
    "Le Puits Oublié des Forgerons": "cle_donjon_khazak_3",
    "Les Forges Interdites (Durn's Maw)": "cle_donjon_khazak_4",

    # LUTHESIA
    "L'Observatoire des Astres": "cle_donjon_luthesia_1",
    "Les Ruines du Vieux Bastion": "cle_donjon_luthesia_2",
    "La Gueule du Mécène": "cle_donjon_luthesia_3",
    "La Prison des Âmes Dépravées": "cle_donjon_luthesia_4",

    # VRAK'THAR
    "Le Sanctuaire des Flammes Éternelles": "cle_donjon_vrakthar_1",
    "Le Cœur des Flammes Corrompues": "cle_donjon_vrakthar_2",
    "Le Mausolée des Géants Brisés": "cle_donjon_vrakthar_3",
    "Les Entrailles Mutantes (Phonétique suggérée : Ghar'gul)": "cle_donjon_vrakthar_4",
    "Les Archives de la Mémoire Fracturée (Phonétique suggérée : Mnemos'Kai)": "cle_donjon_vrakthar_5",
    "La Gueule de l'Oubli (Phonétique suggérée : Ka'rul-Zar)": "cle_donjon_vrakthar_6",

    # DONJON FINAL
    "Le Sanctuaire des Ombres Éternelles": "cle_donjon_final",
    "Le Cœur du Sanctuaire": "cle_donjon_final",
}


def obtenir_cle_donjon(nom_donjon: str) -> str:
    """
    Retourne l'ID de la clé nécessaire pour accéder à un donjon.

    :param nom_donjon: Nom du donjon
    :return: ID de la clé ou None si aucune clé requise
    """
    nom_normalise = _normaliser_nom_donjon(nom_donjon)
    # Chercher d'abord avec le nom exact
    if nom_donjon in CLES_DONJONS:
        return CLES_DONJONS[nom_donjon]
    # Chercher avec le nom normalisé
    for donjon_key, cle_id in CLES_DONJONS.items():
        if _normaliser_nom_donjon(donjon_key) == nom_normalise:
            return cle_id
    return None


def donjon_requiert_cle(nom_donjon: str) -> bool:
    """
    Vérifie si un donjon nécessite une clé pour y accéder.

    :param nom_donjon: Nom du donjon
    :return: True si une clé est requise, False sinon
    """
    if not nom_donjon:
        return False
    # Vérifier d'abord avec le nom exact
    if nom_donjon in CLES_DONJONS:
        return True
    # Vérifier avec le nom normalisé
    nom_normalise = _normaliser_nom_donjon(nom_donjon)
    for donjon_key in CLES_DONJONS.keys():
        if _normaliser_nom_donjon(donjon_key) == nom_normalise:
            return True
    return False


def joueur_possede_cle_donjon(joueur, nom_donjon: str) -> bool:
    """
    Vérifie si le joueur possède la clé nécessaire pour accéder au donjon.

    :param joueur: Le personnage joueur
    :param nom_donjon: Nom du donjon
    :return: True si le joueur possède la clé, False sinon
    """
    # Vérifier d'abord si ce donjon nécessite une clé
    if not donjon_requiert_cle(nom_donjon):
        # Si le donjon n'est pas dans CLES_DONJONS, par sécurité on bloque l'accès
        # Cela force l'ajout de tous les donjons dans CLES_DONJONS
        return False

    cle_id = obtenir_cle_donjon(nom_donjon)
    if not cle_id:
        # Si le donjon n'est pas dans le mapping mais qu'on arrive ici, c'est une erreur
        # Par sécurité, on bloque l'accès
        return False

    # Chercher la clé dans l'inventaire par son ID ou son nom
    from data.objets import DEFINITIONS_OBJETS
    cle_data = DEFINITIONS_OBJETS.get(cle_id)
    if not cle_data:
        return False

    nom_cle = cle_data.get("nom")
    if not nom_cle:
        return False

    # Vérifier si le joueur possède la clé dans son inventaire
    # L'inventaire utilise le nom de l'objet comme clé
    # avoir_objet retourne l'objet si présent, None sinon
    return joueur.avoir_objet(nom_cle) is not None
