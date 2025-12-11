# data/mapping_zones_quetes.py
# Mapping entre les IDs utilisés dans les quêtes et les zones/donjons réels du jeu

# Mapping des zones (biomes) par ID de quête
MAPPING_ZONES_QUETES = {
    # AERTHOS
    "Silvanus'Heart": "La Forêt de Lumière Argentée (Silvanus'Heart)",
    "Ael'doria": "Le Sanctuaire des Murmures Oubliés (Ael'doria)",  # Donjon
    "Selenia's Embrace": "Les Lacs Scintillants et les Jardins Lunaires (Selenia's Embrace)",
    "Lumins'Peak": "Les Montagnes de Cristal et les Salles éthérées (Lumins'Peak)",

    # KHAZAK-DÛM
    "Tunnels_Basalte": "Les Tunnels de la Basalte et les Grandes Mines (Grom's Veins)",
    "Galeries_Savoir": "Les Galeries du Savoir et de l'Ingénierie",
    "Forge_Ancienne": "Les Galeries du Savoir et de l'Ingénierie",  # Zone spéciale dans les Galeries

    # LUTHESIA
    "Plaines_Centrales": "Les Plaines Centrales et les Fiefs du Royaume",
    "Forets_Luminescentes": "Les Forêts Luminescentes et les Tours d'Ivoire",
    "Observatoire_Astres": "L'Observatoire des Astres",  # Donjon
    "Ruines_Vieux_Royaume": "Les Ruines du Vieux Royaume et les Terres Bannies",
    "Prison_Ames": "La Prison des Âmes Dépravées",  # Donjon

    # VRAK'THAR
    "Terres_Brulees": "Les Plaines de Cendres Hurlantes (Phonétique suggérée : Ash'Vaal)",  # Premier biome
    "Sanctuaire_Flammes": "Le Sanctuaire des Flammes Éternelles",  # Donjon - à vérifier dans les fichiers détaillés

    # Zones génériques (pour quêtes principales)
    "zone": None,  # Zone générique - sera remplacée par n'importe quelle zone du royaume
    "zone_relique": None,  # Zone où se trouve une relique - dépend du royaume
    "sanctuaire_ordre": None,  # Sanctuaire de l'Ordre - zone spéciale finale
}

# Mapping des donjons par ID de quête
MAPPING_DONJONS_QUETES = {
    # AERTHOS
    "Ael'doria": "Le Sanctuaire des Murmures Oubliés (Ael'doria)",
    "rituel_corruption": "Le Sanctuaire des Murmures Oubliés (Ael'doria)",  # Utilise le même donjon

    # KHAZAK-DÛM
    "mecanisme_destructeur": "Le Caveau des Secrets du Premier âge",  # Donjon des Galeries

    # LUTHESIA
    "Observatoire_Astres": "L'Observatoire des Astres",  # À vérifier
    "purification": "L'Observatoire des Astres",  # Utilise le même donjon
    "Prison_Ames": "La Prison des Âmes Dépravées",  # À vérifier

    # VRAK'THAR
    "Sanctuaire_Flammes": "Le Sanctuaire des Flammes Éternelles",  # À vérifier
    "rituel_corruption_vrakthar": "Le Sanctuaire des Flammes Éternelles",  # Utilise le même donjon

    # Donjons génériques (pour quêtes principales)
    "donjon": None,  # Donjon générique - sera remplacé par n'importe quel donjon du royaume
    "infiltration_sanctuaire": "Le Sanctuaire de l'Ordre",  # Donjon final spécial
    "rituel_resurrection_zarathos": "Le Sanctuaire de l'Ordre",  # Donjon final - même lieu
}

def obtenir_zone_par_id_quete(id_zone: str, royaume: str = None) -> str:
    """
    Retourne le nom réel de la zone correspondant à l'ID utilisé dans les quêtes.

    :param id_zone: ID de la zone utilisé dans les quêtes
    :param royaume: Nom du royaume (optionnel, pour les zones génériques)
    :return: Nom réel de la zone ou None si introuvable
    """
    zone = MAPPING_ZONES_QUETES.get(id_zone)

    # Si la zone est générique, retourner None (sera géré par le système de progression)
    if zone is None:
        return None

    return zone

def obtenir_donjon_par_id_quete(id_donjon: str, royaume: str = None) -> str:
    """
    Retourne le nom réel du donjon correspondant à l'ID utilisé dans les quêtes.

    :param id_donjon: ID du donjon utilisé dans les quêtes
    :param royaume: Nom du royaume (optionnel, pour les donjons génériques)
    :return: Nom réel du donjon ou None si introuvable
    """
    donjon = MAPPING_DONJONS_QUETES.get(id_donjon)

    # Si le donjon est générique, retourner None (sera géré par le système de progression)
    if donjon is None:
        return None

    return donjon

def est_zone_donjon(id_zone: str) -> bool:
    """
    Vérifie si l'ID correspond à un donjon plutôt qu'à une zone normale.

    :param id_zone: ID de la zone/donjon
    :return: True si c'est un donjon, False sinon
    """
    return id_zone in MAPPING_DONJONS_QUETES
