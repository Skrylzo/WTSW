# data/pnjs_zones.py
# Mapping des PNJ présents dans les zones d'exploration

# Mapping {nom_zone: [liste_ids_pnj]}
# Les noms de zones doivent correspondre aux noms exacts des biomes
PNJS_PAR_ZONE = {
    # AERTHOS
    "La Forêt de Lumière Argentée (Silvanus'Heart)": ["Faelar"],
    "Les Lacs Scintillants et les Jardins Lunaires (Selenia's Embrace)": ["esprit_perdu"],
    "Les Montagnes de Cristal et les Salles éthérées (Lumins'Peak)": ["Seraphina"],

    # KHAZAK-DÛM
    "Les Tunnels de la Basalte et les Grandes Mines (Grom's Veins)": ["Borina"],
    "Les Galeries du Savoir et de l'Ingénierie": ["Zamir", "Gelal", "Grom"],

    # LUTHESIA
    "Les Plaines Centrales et les Fiefs du Royaume": [],
    "Les Forêts Luminescentes et les Tours d'Ivoire": ["Seraphina"],
    "Les Ruines du Vieux Royaume et les Terres Bannies": [],

    # VRAK'THAR
    "Les Plaines de Cendres Hurlantes (Phonétique suggérée : Ash'Vaal)": ["erudit_demon"],
    "Les Montagnes Fracturées de la Folie (Phonétique suggérée : Karr'ag-hul)": ["gardien_ancien"],
}

def obtenir_pnjs_zone(nom_zone: str) -> list:
    """
    Retourne la liste des IDs de PNJ présents dans une zone donnée.

    :param nom_zone: Nom exact de la zone/biome
    :return: Liste des IDs de PNJ présents dans cette zone
    """
    return PNJS_PAR_ZONE.get(nom_zone, [])

def zone_contient_pnj(nom_zone: str) -> bool:
    """
    Vérifie si une zone contient des PNJ.

    :param nom_zone: Nom exact de la zone/biome
    :return: True si la zone contient au moins un PNJ
    """
    pnjs = obtenir_pnjs_zone(nom_zone)
    return len(pnjs) > 0
