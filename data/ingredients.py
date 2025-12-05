# data/ingredients.py
# Définitions de tous les ingrédients du système de craft
# Généré automatiquement depuis DESIGN_CRAFT.md

from typing import Dict, List, Optional
from classes.objet import Objet

# Niveaux de rareté
RARETES = [
    'Commun',
    'Peu Commun',
    'Rare',
    'Épique',
    'Légendaire'
]

# Distribution de rareté (pour le loot)
DISTRIBUTION_RARETE = {
    'Commun': 0.49,      # 49%
    'Peu Commun': 0.30,  # 30%
    'Rare': 0.15,        # 15%
    'Épique': 0.05,      # 5%
    'Légendaire': 0.01   # 1%
}

# Types d'usage
USAGE_POTIONS = 'Potions'
USAGE_ARMES = 'Armes'
USAGE_ARMURES = 'Armures'

# Structure des ingrédients
# Format : {
#     'nom': {
#         'usage': 'Potions' | 'Armes' | 'Armures',
#         'sources': [
#             {'mob': 'Nom du Mob', 'royaume': 'Nom du Royaume', 'biome': 'Nom du Biome'},
#             ...
#         ]
#     }
# }

DEFINITIONS_INGREDIENTS: Dict[str, Dict] = {
    "aile_scintillante": {
        'nom': "Aile Scintillante",
        'usage': "Armes",
        'sources': [
            {'mob': "Libellules d'Éclat", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "aile_de_fee": {
        'nom': "Aile de Fée",
        'usage': "Armes",
        'sources': [
            {'mob': "Fées-Pipettes", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "bois_sacre": {
        'nom': "Bois Sacré",
        'usage': "Armes",
        'sources': [
            {'mob': "Dryades Protectrices", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "bois_de_cerf": {
        'nom': "Bois de Cerf",
        'usage': "Armes",
        'sources': [
            {'mob': "Cerfs Lumina", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "bois_de_cur": {
        'nom': "Bois de Cœur",
        'usage': "Armes",
        'sources': [
            {'mob': "Arbres-Cœur", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "bton_de_professeur": {
        'nom': "Bâton de Professeur",
        'usage': "Armes",
        'sources': [
            {'mob': "Professeurs Reniés", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "bton_de_sorciere": {
        'nom': "Bâton de Sorcière",
        'usage': "Armes",
        'sources': [
            {'mob': "Guenaudes des Landes", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "carapace_lithique": {
        'nom': "Carapace Lithique",
        'usage': "Armures",
        'sources': [
            {'mob': "Murmures Lithiques", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "carapace_mecanique": {
        'nom': "Carapace Mécanique",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Horloge Dément, Cogsworth", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "carapace_metallique": {
        'nom': "Carapace Métallique",
        'usage': "Armes",
        'sources': [
            {'mob': "Scarabées de Minerai", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "carapace_runique": {
        'nom': "Carapace Runique",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardiens Runiques", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "carapace_dautomate": {
        'nom': "Carapace d'Automate",
        'usage': "Armures",
        'sources': [
            {'mob': "Automates d'Entraînement", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "carapace_declat": {
        'nom': "Carapace d'Éclat",
        'usage': "Armures",
        'sources': [
            {'mob': "Libellules d'Éclat", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "carapace_de_cendres": {
        'nom': "Carapace de Cendres",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Titan de Cendres, Ignis Primus", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "carapace_de_drone": {
        'nom': "Carapace de Drone",
        'usage': "Armures",
        'sources': [
            {'mob': "Nuées de Micro-Drones", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "carapace_de_gardien": {
        'nom': "Carapace de Gardien",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Gardien de la Frontière, Golem-Rempart", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "carapace_de_jais": {
        'nom': "Carapace de Jais",
        'usage': "Armes",
        'sources': [
            {'mob': "Scorpions de Jais", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "carapace_de_laiton": {
        'nom': "Carapace de Laiton",
        'usage': "Armures",
        'sources': [
            {'mob': "Golem de Laiton (Prototype)", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "carapace_de_larve": {
        'nom': "Carapace de Larve",
        'usage': "Armes",
        'sources': [
            {'mob': "Larves de Corruption", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "carapace_de_magma": {
        'nom': "Carapace de Magma",
        'usage': "Armures",
        'sources': [
            {'mob': "Golems de Magma", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "carapace_de_pierre": {
        'nom': "Carapace de Pierre",
        'usage': "Armures",
        'sources': [
            {'mob': "Grimpeurs de Pierre", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "carapace_de_quartz": {
        'nom': "Carapace de Quartz",
        'usage': "Armures",
        'sources': [
            {'mob': "Sentinelles de Quartz Noir", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "carapace_de_quartz_lumineux": {
        'nom': "Carapace de Quartz Lumineux",
        'usage': "Armures",
        'sources': [
            {'mob': "Sentinelles de Quartz", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "carapace_de_roche": {
        'nom': "Carapace de Roche",
        'usage': "Armures",
        'sources': [
            {'mob': "Roches Vivantes", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "carapace_de_stalactite": {
        'nom': "Carapace de Stalactite",
        'usage': "Armures",
        'sources': [
            {'mob': "Créatures de Stalactite", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "carapace_de_selenite": {
        'nom': "Carapace de Sélénite",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardiens de Sélénite", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "carapace_de_tombeau": {
        'nom': "Carapace de Tombeau",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardiens de Tombeaux", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "carapace_de_tresor": {
        'nom': "Carapace de Trésor",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardiens de Trésor", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "carapace_de_ver": {
        'nom': "Carapace de Ver",
        'usage': "Armes",
        'sources': [
            {'mob': "Vers de Poussière", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "cendre_maudite": {
        'nom': "Cendre Maudite",
        'usage': "Potions",
        'sources': [
            {'mob': "Spectres Cendrés", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "charbon": {
        'nom': "Charbon",
        'usage': "Potions",
        'sources': [
            {'mob': "Gobs-Mineurs", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "criniere_dether": {
        'nom': "Crinière d'Éther",
        'usage': "Armures",
        'sources': [
            {'mob': "Chevaux Ailés d'Éther", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "cristal_corrompu": {
        'nom': "Cristal Corrompu",
        'usage': "Potions",
        'sources': [
            {'mob': "Charognards de Cristaux", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "cristal_de_soufre": {
        'nom': "Cristal de Soufre",
        'usage': "Armures",
        'sources': [
            {'mob': "Élémentaires de Soufre", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "cuir_use": {
        'nom': "Cuir Usé",
        'usage': "Armures",
        'sources': [
            {'mob': "Brigands de Grand Chemin", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "cuir_de_horslaloi": {
        'nom': "Cuir de Hors-la-Loi",
        'usage': "Armures",
        'sources': [
            {'mob': "Maraudeurs et Hors-la-Loi", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "dard_de_jais": {
        'nom': "Dard de Jais",
        'usage': "Armures",
        'sources': [
            {'mob': "Scorpions de Jais", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "defense_de_mammouth": {
        'nom': "Défense de Mammouth",
        'usage': "Armes",
        'sources': [
            {'mob': "Mammouths des Glaces Naines", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "engrenage_de_maitre": {
        'nom': "Engrenage de Maître",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Horloge Dément, Cogsworth", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "essence_aquatique": {
        'nom': "Essence Aquatique",
        'usage': "Potions",
        'sources': [
            {'mob': "Nymphes des Eaux", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "essence_arcanique": {
        'nom': "Essence Arcanique",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Souffle Arcanique, Silvaris Lumina", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "essence_astral": {
        'nom': "Essence Astral",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Oracle Astral", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "essence_celeste": {
        'nom': "Essence Céleste",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardes Célestes", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "essence_dimensionnelle": {
        'nom': "Essence Dimensionnelle",
        'usage': "Potions",
        'sources': [
            {'mob': "Déchireurs Dimensionnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "essence_gravitationnelle": {
        'nom': "Essence Gravitationnelle",
        'usage': "Potions",
        'sources': [
            {'mob': "Rôdeurs Gravitationnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "essence_lithique": {
        'nom': "Essence Lithique",
        'usage': "Potions",
        'sources': [
            {'mob': "Murmures Lithiques", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "essence_mecanique": {
        'nom': "Essence Mécanique",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Horloge Dément, Cogsworth", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "essence_originelle": {
        'nom': "Essence Originelle",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Écho Originel, Vis'khara", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "essence_psionique": {
        'nom': "Essence Psionique",
        'usage': "Potions",
        'sources': [
            {'mob': "Noyés Psioniques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "essence_runique": {
        'nom': "Essence Runique",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardiens Runiques", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "essence_scintillante": {
        'nom': "Essence Scintillante",
        'usage': "Potions",
        'sources': [
            {'mob': "Guetteurs Scintillants", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "essence_spectrale": {
        'nom': "Essence Spectrale",
        'usage': "Potions",
        'sources': [
            {'mob': "Spectres des Ruines", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "essence_sylvestre": {
        'nom': "Essence Sylvestre",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Gardien Sylvestre, Eldrin Racinéclat", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "essence_darchitecte": {
        'nom': "Essence d'Architecte",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Architecte des Murmures, Xyl'thos", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "essence_dautomate": {
        'nom': "Essence d'Automate",
        'usage': "Potions",
        'sources': [
            {'mob': "Automates d'Entraînement", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "essence_dobsidienne": {
        'nom': "Essence d'Obsidienne",
        'usage': "Potions",
        'sources': [
            {'mob': "Trognes de l'Obsidienne", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "essence_decho": {
        'nom': "Essence d'Écho",
        'usage': "Potions",
        'sources': [
            {'mob': "Échos Aquatiques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "essence_declat": {
        'nom': "Essence d'Éclat",
        'usage': "Potions",
        'sources': [
            {'mob': "Libellules d'Éclat", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "essence_dether": {
        'nom': "Essence d'Éther",
        'usage': "Potions",
        'sources': [
            {'mob': "Chevaux Ailés d'Éther", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "essence_de_bandit": {
        'nom': "Essence de Bandit",
        'usage': "Potions",
        'sources': [
            {'mob': "Maraudeurs et Hors-la-Loi", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "essence_de_brise": {
        'nom': "Essence de Brise",
        'usage': "Potions",
        'sources': [
            {'mob': "Sentinelles de Brise", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "essence_de_brume": {
        'nom': "Essence de Brume",
        'usage': "Potions",
        'sources': [
            {'mob': "Les Murmurants de Brume", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "essence_de_cendres": {
        'nom': "Essence de Cendres",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Titan de Cendres, Ignis Primus", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "essence_de_chant": {
        'nom': "Essence de Chant",
        'usage': "Potions",
        'sources': [
            {'mob': "Sirènes de Dérision", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "essence_de_chien": {
        'nom': "Essence de Chien",
        'usage': "Potions",
        'sources': [
            {'mob': "Chiens de Guerre Sauvages", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "essence_de_chimere": {
        'nom': "Essence de Chimère",
        'usage': "Potions",
        'sources': [
            {'mob': "Chimères d'Expérience", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "essence_de_corruption": {
        'nom': "Essence de Corruption",
        'usage': "Potions",
        'sources': [
            {'mob': "Larves de Corruption", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "essence_de_drone": {
        'nom': "Essence de Drone",
        'usage': "Potions",
        'sources': [
            {'mob': "Nuées de Micro-Drones", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "essence_de_fantome": {
        'nom': "Essence de Fantôme",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Baron Fantôme", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "essence_de_fantome_mecanique": {
        'nom': "Essence de Fantôme Mécanique",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Ascenseur Fantôme", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "essence_de_flamme": {
        'nom': "Essence de Flamme",
        'usage': "Potions",
        'sources': [
            {'mob': "Salamandres de Flamme", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "essence_de_gardien": {
        'nom': "Essence de Gardien",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardiens de Tombeaux", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "essence_de_glace": {
        'nom': "Essence de Glace",
        'usage': "Potions",
        'sources': [
            {'mob': "Mammouths des Glaces Naines", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "essence_de_golem": {
        'nom': "Essence de Golem",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Gardien de la Frontière, Golem-Rempart", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "essence_de_guerrier": {
        'nom': "Essence de Guerrier",
        'usage': "Potions",
        'sources': [
            {'mob': "Chevaliers Renégats", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "essence_de_jais": {
        'nom': "Essence de Jais",
        'usage': "Potions",
        'sources': [
            {'mob': "Scorpions de Jais", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "essence_de_laiton": {
        'nom': "Essence de Laiton",
        'usage': "Potions",
        'sources': [
            {'mob': "Golem de Laiton (Prototype)", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "essence_de_loup": {
        'nom': "Essence de Loup",
        'usage': "Potions",
        'sources': [
            {'mob': "Loups de Canyon", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "essence_de_lumiere": {
        'nom': "Essence de Lumière",
        'usage': "Potions",
        'sources': [
            {'mob': "Spectres de Lumière", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "essence_de_magma": {
        'nom': "Essence de Magma",
        'usage': "Potions",
        'sources': [
            {'mob': "Golems de Magma", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "essence_de_minerai": {
        'nom': "Essence de Minerai",
        'usage': "Potions",
        'sources': [
            {'mob': "Scarabées de Minerai", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "essence_de_pierre": {
        'nom': "Essence de Pierre",
        'usage': "Potions",
        'sources': [
            {'mob': "Grimpeurs de Pierre", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "essence_de_poussiere": {
        'nom': "Essence de Poussière",
        'usage': "Potions",
        'sources': [
            {'mob': "Vers de Poussière", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "essence_de_penitence": {
        'nom': "Essence de Pénitence",
        'usage': "Potions",
        'sources': [
            {'mob': "Inquisiteurs de Pénitence", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "essence_de_quartz": {
        'nom': "Essence de Quartz",
        'usage': "Potions",
        'sources': [
            {'mob': "Sentinelles de Quartz", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "essence_de_quartz_noir": {
        'nom': "Essence de Quartz Noir",
        'usage': "Potions",
        'sources': [
            {'mob': "Sentinelles de Quartz Noir", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "essence_de_roche": {
        'nom': "Essence de Roche",
        'usage': "Potions",
        'sources': [
            {'mob': "Roches Vivantes", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "essence_de_sagesse": {
        'nom': "Essence de Sagesse",
        'usage': "Potions",
        'sources': [
            {'mob': "Acolytes de la Sagesse Perdue", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "essence_de_savoir": {
        'nom': "Essence de Savoir",
        'usage': "Potions",
        'sources': [
            {'mob': "Professeurs Reniés", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "essence_de_soufre": {
        'nom': "Essence de Soufre",
        'usage': "Potions",
        'sources': [
            {'mob': "Élémentaires de Soufre", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "essence_de_stalactite": {
        'nom': "Essence de Stalactite",
        'usage': "Potions",
        'sources': [
            {'mob': "Créatures de Stalactite", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "essence_de_selenite": {
        'nom': "Essence de Sélénite",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardiens de Sélénite", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "essence_de_troll": {
        'nom': "Essence de Troll",
        'usage': "Potions",
        'sources': [
            {'mob': "Trolls de Quartz", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "essence_de_tresor": {
        'nom': "Essence de Trésor",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardiens de Trésor", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "essence_des_rafales": {
        'nom': "Essence des Rafales",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Maître des Rafales, Zephyros Sombreplume", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "essence_des_songes": {
        'nom': "Essence des Songes",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Architecte des Songes, Lunarae Noctis", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "essence_du_chaos": {
        'nom': "Essence du Chaos",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Chaos Immuable, Vorlag'Ghul", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "essence_du_cur_battant": {
        'nom': "Essence du Cœur Battant",
        'usage': "Potions",
        'sources': [
            {'mob': ":Le Cœur Battant, Xyl'thrak", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "essence_du_juge": {
        'nom': "Essence du Juge",
        'usage': "Potions",
        'sources': [
            {'mob': "Le Juge Déchu, Caelus Mortis", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "essence_du_savoir": {
        'nom': "Essence du Savoir",
        'usage': "Potions",
        'sources': [
            {'mob': "L'Archiviste", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fourrure_argentee": {
        'nom': "Fourrure Argentée",
        'usage': "Armures",
        'sources': [
            {'mob': "Cerfs Lumina", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "fourrure_de_canyon": {
        'nom': "Fourrure de Canyon",
        'usage': "Armures",
        'sources': [
            {'mob': "Loups de Canyon", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "fourrure_de_chien": {
        'nom': "Fourrure de Chien",
        'usage': "Armures",
        'sources': [
            {'mob': "Chiens de Guerre Sauvages", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "fourrure_de_mammouth": {
        'nom': "Fourrure de Mammouth",
        'usage': "Armures",
        'sources': [
            {'mob': "Mammouths des Glaces Naines", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "fragment_astral": {
        'nom': "Fragment Astral",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Oracle Astral", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "fragment_celeste": {
        'nom': "Fragment Céleste",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardes Célestes", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "fragment_daile": {
        'nom': "Fragment d'Aile",
        'usage': "Armes",
        'sources': [
            {'mob': "Fées Gardiennes", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "fragment_dargent": {
        'nom': "Fragment d'Argent",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardiens de Trésor", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "fragment_dascenseur": {
        'nom': "Fragment d'Ascenseur",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Ascenseur Fantôme", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "fragment_dautomate": {
        'nom': "Fragment d'Automate",
        'usage': "Armes",
        'sources': [
            {'mob': "Automates d'Entraînement", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "fragment_dobsidienne": {
        'nom': "Fragment d'Obsidienne",
        'usage': "Armes",
        'sources': [
            {'mob': "Trognes de l'Obsidienne", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "fragment_dos_spectral": {
        'nom': "Fragment d'Os Spectral",
        'usage': "Armes",
        'sources': [
            {'mob': "Spectres Cendrés", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "fragment_dos_de_geant": {
        'nom': "Fragment d'Os de Géant",
        'usage': "Armures",
        'sources': [
            {'mob': "Géants Squelettiques", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "fragment_dme_noyee": {
        'nom': "Fragment d'Âme Noyée",
        'usage': "Armes",
        'sources': [
            {'mob': "Noyés Psioniques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "fragment_de_baron": {
        'nom': "Fragment de Baron",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Baron Fantôme", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "fragment_de_cur_pur": {
        'nom': "Fragment de Cœur Pur",
        'usage': "Armes",
        'sources': [
            {'mob': ":Le Cœur Battant, Xyl'thrak", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "fragment_de_distorsion": {
        'nom': "Fragment de Distorsion",
        'usage': "Armes",
        'sources': [
            {'mob': "Rôdeurs Gravitationnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "fragment_de_drone": {
        'nom': "Fragment de Drone",
        'usage': "Armes",
        'sources': [
            {'mob': "Nuées de Micro-Drones", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fragment_de_fracture": {
        'nom': "Fragment de Fracture",
        'usage': "Armes",
        'sources': [
            {'mob': "Déchireurs Dimensionnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "fragment_de_jugement": {
        'nom': "Fragment de Jugement",
        'usage': "Armes",
        'sources': [
            {'mob': "Inquisiteurs de Pénitence", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "fragment_de_jugement_dechu": {
        'nom': "Fragment de Jugement Déchu",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Juge Déchu, Caelus Mortis", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "fragment_de_laiton": {
        'nom': "Fragment de Laiton",
        'usage': "Armes",
        'sources': [
            {'mob': "Golem de Laiton (Prototype)", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fragment_de_lumiere": {
        'nom': "Fragment de Lumière",
        'usage': "Armes",
        'sources': [
            {'mob': "Guetteurs Scintillants", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "fragment_de_lumiere_pure": {
        'nom': "Fragment de Lumière Pure",
        'usage': "Armes",
        'sources': [
            {'mob': "Spectres de Lumière", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "fragment_de_magma": {
        'nom': "Fragment de Magma",
        'usage': "Armes",
        'sources': [
            {'mob': "Golems de Magma", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "fragment_de_miroir": {
        'nom': "Fragment de Miroir",
        'usage': "Armes",
        'sources': [
            {'mob': "Échos Aquatiques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "fragment_de_murmure_pur": {
        'nom': "Fragment de Murmure Pur",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Architecte des Murmures, Xyl'thos", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "fragment_de_mycelium": {
        'nom': "Fragment de Mycelium",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardes de Mycelium", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "fragment_de_memoire": {
        'nom': "Fragment de Mémoire",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Archiviste", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fragment_de_pierre_vivante": {
        'nom': "Fragment de Pierre Vivante",
        'usage': "Armes",
        'sources': [
            {'mob': "Murmures Lithiques", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "fragment_de_quartz": {
        'nom': "Fragment de Quartz",
        'usage': "Armes",
        'sources': [
            {'mob': "Sentinelles de Quartz", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "fragment_de_quartz_brut": {
        'nom': "Fragment de Quartz Brut",
        'usage': "Armes",
        'sources': [
            {'mob': "Trolls de Quartz", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "fragment_de_quartz_noir": {
        'nom': "Fragment de Quartz Noir",
        'usage': "Armes",
        'sources': [
            {'mob': "Sentinelles de Quartz Noir", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "fragment_de_rempart": {
        'nom': "Fragment de Rempart",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Gardien de la Frontière, Golem-Rempart", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "fragment_de_roche": {
        'nom': "Fragment de Roche",
        'usage': "Armes",
        'sources': [
            {'mob': "Grimpeurs de Pierre", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "fragment_de_roche_vivante": {
        'nom': "Fragment de Roche Vivante",
        'usage': "Armes",
        'sources': [
            {'mob': "Roches Vivantes", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "fragment_de_ruine": {
        'nom': "Fragment de Ruine",
        'usage': "Armes",
        'sources': [
            {'mob': "Spectres des Ruines", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "fragment_de_rune": {
        'nom': "Fragment de Rune",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardiens Runiques", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fragment_de_reve_pur": {
        'nom': "Fragment de Rêve Pur",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Architecte des Songes, Lunarae Noctis", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "fragment_de_savoir": {
        'nom': "Fragment de Savoir",
        'usage': "Armes",
        'sources': [
            {'mob': "Acolytes de la Sagesse Perdue", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "fragment_de_souffle": {
        'nom': "Fragment de Souffle",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Souffle Arcanique, Silvaris Lumina", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "fragment_de_soufre": {
        'nom': "Fragment de Soufre",
        'usage': "Armes",
        'sources': [
            {'mob': "Élémentaires de Soufre", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "fragment_de_stalactite": {
        'nom': "Fragment de Stalactite",
        'usage': "Armes",
        'sources': [
            {'mob': "Créatures de Stalactite", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "fragment_de_selenite": {
        'nom': "Fragment de Sélénite",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardiens de Sélénite", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "fragment_de_titan": {
        'nom': "Fragment de Titan",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Titan de Cendres, Ignis Primus", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "fragment_de_tombeau": {
        'nom': "Fragment de Tombeau",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardiens de Tombeaux", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "fragment_de_vent": {
        'nom': "Fragment de Vent",
        'usage': "Armes",
        'sources': [
            {'mob': "Sentinelles de Brise", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "fragment_de_voix": {
        'nom': "Fragment de Voix",
        'usage': "Armes",
        'sources': [
            {'mob': "Les Murmurants de Brume", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "fragment_du_chaos_immuable": {
        'nom': "Fragment du Chaos Immuable",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Chaos Immuable, Vorlag'Ghul", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "fragment_du_miroir_originel": {
        'nom': "Fragment du Miroir Originel",
        'usage': "Armes",
        'sources': [
            {'mob': "L'Écho Originel, Vis'khara", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "griffe_de_charognard": {
        'nom': "Griffe de Charognard",
        'usage': "Armes",
        'sources': [
            {'mob': "Charognards de Cristaux", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "griffe_de_chien": {
        'nom': "Griffe de Chien",
        'usage': "Armes",
        'sources': [
            {'mob': "Chiens de Guerre Sauvages", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "griffe_de_chimere": {
        'nom': "Griffe de Chimère",
        'usage': "Armes",
        'sources': [
            {'mob': "Chimères d'Expérience", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "griffe_de_loup": {
        'nom': "Griffe de Loup",
        'usage': "Armes",
        'sources': [
            {'mob': "Loups de Canyon", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "griffe_de_traqueur": {
        'nom': "Griffe de Traqueur",
        'usage': "Armes",
        'sources': [
            {'mob': "Traqueurs Sanguins", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "herbe_commune": {
        'nom': "Herbe Commune",
        'usage': "Potions",
        'sources': [
            {'mob': "Brigands de Grand Chemin", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "herbe_lumineuse": {
        'nom': "Herbe Lumineuse",
        'usage': "Potions",
        'sources': [
            {'mob': "Cerfs Lumina", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "herbe_de_sorciere": {
        'nom': "Herbe de Sorcière",
        'usage': "Potions",
        'sources': [
            {'mob': "Guenaudes des Landes", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "lame_brisee": {
        'nom': "Lame Brisée",
        'usage': "Armes",
        'sources': [
            {'mob': "Brigands de Grand Chemin", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "lame_de_chevalier": {
        'nom': "Lame de Chevalier",
        'usage': "Armes",
        'sources': [
            {'mob': "Chevaliers Renégats", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "lame_de_maraudeur": {
        'nom': "Lame de Maraudeur",
        'usage': "Armes",
        'sources': [
            {'mob': "Maraudeurs et Hors-la-Loi", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "linceul_aquatique": {
        'nom': "Linceul Aquatique",
        'usage': "Armures",
        'sources': [
            {'mob': "Noyés Psioniques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "linceul_spectral": {
        'nom': "Linceul Spectral",
        'usage': "Armures",
        'sources': [
            {'mob': "Spectres Cendrés", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "linceul_de_ruine": {
        'nom': "Linceul de Ruine",
        'usage': "Armures",
        'sources': [
            {'mob': "Spectres des Ruines", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "membrane_de_mycelium": {
        'nom': "Membrane de Mycelium",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardes de Mycelium", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "membrane_du_cur": {
        'nom': "Membrane du Cœur",
        'usage': "Armures",
        'sources': [
            {'mob': ":Le Cœur Battant, Xyl'thrak", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "minerai_de_fer": {
        'nom': "Minerai de Fer",
        'usage': "Armes",
        'sources': [
            {'mob': "Gobs-Mineurs", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "moelle_de_geant": {
        'nom': "Moelle de Géant",
        'usage': "Potions",
        'sources': [
            {'mob': "Géants Squelettiques", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "os_de_geant": {
        'nom': "Os de Géant",
        'usage': "Armes",
        'sources': [
            {'mob': "Géants Squelettiques", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "peau_de_chimere": {
        'nom': "Peau de Chimère",
        'usage': "Armures",
        'sources': [
            {'mob': "Chimères d'Expérience", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "peau_de_gobelin": {
        'nom': "Peau de Gobelin",
        'usage': "Armures",
        'sources': [
            {'mob': "Gobs-Mineurs", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "peau_de_larve": {
        'nom': "Peau de Larve",
        'usage': "Armures",
        'sources': [
            {'mob': "Larves de Corruption", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "peau_de_salamandre": {
        'nom': "Peau de Salamandre",
        'usage': "Armures",
        'sources': [
            {'mob': "Salamandres de Flamme", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "peau_de_traqueur": {
        'nom': "Peau de Traqueur",
        'usage': "Armures",
        'sources': [
            {'mob': "Traqueurs Sanguins", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "peau_de_troll": {
        'nom': "Peau de Troll",
        'usage': "Armures",
        'sources': [
            {'mob': "Trolls de Quartz", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "peau_de_ver": {
        'nom': "Peau de Ver",
        'usage': "Armures",
        'sources': [
            {'mob': "Vers de Poussière", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
    "plaque_darmure": {
        'nom': "Plaque d'Armure",
        'usage': "Armures",
        'sources': [
            {'mob': "Chevaliers Renégats", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "plume_cristalline": {
        'nom': "Plume Cristalline",
        'usage': "Potions",
        'sources': [
            {'mob': "Aigles-Cristal", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "plume_celeste": {
        'nom': "Plume Céleste",
        'usage': "Armes",
        'sources': [
            {'mob': "Chevaux Ailés d'Éther", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "plume_sombre": {
        'nom': "Plume Sombre",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Maître des Rafales, Zephyros Sombreplume", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "plume_dacier": {
        'nom': "Plume d'Acier",
        'usage': "Potions",
        'sources': [
            {'mob': "Vautours à Crête d'Acier", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "plume_de_crete": {
        'nom': "Plume de Crête",
        'usage': "Armures",
        'sources': [
            {'mob': "Vautours à Crête d'Acier", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "plume_de_garde": {
        'nom': "Plume de Garde",
        'usage': "Armures",
        'sources': [
            {'mob': "Aigles-Cristal", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "pollen_siffleur": {
        'nom': "Pollen Siffleur",
        'usage': "Potions",
        'sources': [
            {'mob': "Fleurs Siffleuses", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "pollen_de_lotus": {
        'nom': "Pollen de Lotus",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardes de Lotus", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "pollen_de_reve": {
        'nom': "Pollen de Rêve",
        'usage': "Potions",
        'sources': [
            {'mob': "Fleurs de Rêves", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "poussiere_de_fee": {
        'nom': "Poussière de Fée",
        'usage': "Potions",
        'sources': [
            {'mob': "Fées Gardiennes", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "poussiere_de_pipette": {
        'nom': "Poussière de Pipette",
        'usage': "Potions",
        'sources': [
            {'mob': "Fées-Pipettes", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "petale_de_lotus": {
        'nom': "Pétale de Lotus",
        'usage': "Armes",
        'sources': [
            {'mob': "Gardes de Lotus", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "petale_de_reve": {
        'nom': "Pétale de Rêve",
        'usage': "Armes",
        'sources': [
            {'mob': "Fleurs de Rêves", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "petale_de_vent": {
        'nom': "Pétale de Vent",
        'usage': "Armes",
        'sources': [
            {'mob': "Fleurs Siffleuses", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "racine_vivante": {
        'nom': "Racine Vivante",
        'usage': "Armes",
        'sources': [
            {'mob': "Anciens Racinaires", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "racine_de_gardien": {
        'nom': "Racine de Gardien",
        'usage': "Armes",
        'sources': [
            {'mob': "Le Gardien Sylvestre, Eldrin Racinéclat", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "sang_maudit": {
        'nom': "Sang Maudit",
        'usage': "Potions",
        'sources': [
            {'mob': "Traqueurs Sanguins", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "serre_dacier": {
        'nom': "Serre d'Acier",
        'usage': "Armes",
        'sources': [
            {'mob': "Vautours à Crête d'Acier", 'royaume': "Khazak-Dûm", 'biome': "Les Cr�tes Balay�es par le Vent"},
        ]
    },
    "serre_de_cristal": {
        'nom': "Serre de Cristal",
        'usage': "Armes",
        'sources': [
            {'mob': "Aigles-Cristal", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "spores_de_mycelium": {
        'nom': "Spores de Mycelium",
        'usage': "Potions",
        'sources': [
            {'mob': "Gardes de Mycelium", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "seve_ancienne": {
        'nom': "Sève Ancienne",
        'usage': "Potions",
        'sources': [
            {'mob': "Anciens Racinaires", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "seve_corrompue": {
        'nom': "Sève Corrompue",
        'usage': "Potions",
        'sources': [
            {'mob': "Arbres-Cœur", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "seve_magique": {
        'nom': "Sève Magique",
        'usage': "Potions",
        'sources': [
            {'mob': "Dryades Protectrices", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "tige_aerienne": {
        'nom': "Tige Aérienne",
        'usage': "Armures",
        'sources': [
            {'mob': "Fleurs Siffleuses", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "tige_de_lotus": {
        'nom': "Tige de Lotus",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardes de Lotus", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "tige_de_reve": {
        'nom': "Tige de Rêve",
        'usage': "Armures",
        'sources': [
            {'mob': "Fleurs de Rêves", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "voile_aquatique": {
        'nom': "Voile Aquatique",
        'usage': "Armures",
        'sources': [
            {'mob': "Échos Aquatiques", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "voile_arcanique": {
        'nom': "Voile Arcanique",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Souffle Arcanique, Silvaris Lumina", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "voile_astral": {
        'nom': "Voile Astral",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Oracle Astral", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "voile_celeste": {
        'nom': "Voile Céleste",
        'usage': "Armures",
        'sources': [
            {'mob': "Gardes Célestes", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "voile_dimensionnel": {
        'nom': "Voile Dimensionnel",
        'usage': "Armures",
        'sources': [
            {'mob': "Déchireurs Dimensionnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "voile_feerique": {
        'nom': "Voile Féerique",
        'usage': "Armures",
        'sources': [
            {'mob': "Fées Gardiennes", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "voile_gravitationnel": {
        'nom': "Voile Gravitationnel",
        'usage': "Armures",
        'sources': [
            {'mob': "Rôdeurs Gravitationnels", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "voile_lumineux": {
        'nom': "Voile Lumineux",
        'usage': "Armures",
        'sources': [
            {'mob': "Spectres de Lumière", 'royaume': "Aerthos", 'biome': "Les Montagnes de Cristal et les Salles �th�r�es"},
        ]
    },
    "voile_lunaire": {
        'nom': "Voile Lunaire",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Architecte des Songes, Lunarae Noctis", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "voile_mecanique": {
        'nom': "Voile Mécanique",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Ascenseur Fantôme", 'royaume': "Luthesia", 'biome': "Les Monts H�riss�s et les Mines d'Argent"},
        ]
    },
    "voile_darchitecte": {
        'nom': "Voile d'Architecte",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Architecte des Murmures, Xyl'thos", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "voile_dinquisiteur": {
        'nom': "Voile d'Inquisiteur",
        'usage': "Armures",
        'sources': [
            {'mob': "Inquisiteurs de Pénitence", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "voile_de_baron": {
        'nom': "Voile de Baron",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Baron Fantôme", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "voile_de_brise": {
        'nom': "Voile de Brise",
        'usage': "Armures",
        'sources': [
            {'mob': "Sentinelles de Brise", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "voile_de_brume": {
        'nom': "Voile de Brume",
        'usage': "Armures",
        'sources': [
            {'mob': "Les Murmurants de Brume", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "voile_de_derision": {
        'nom': "Voile de Dérision",
        'usage': "Armures",
        'sources': [
            {'mob': "Sirènes de Dérision", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "voile_de_nymphe": {
        'nom': "Voile de Nymphe",
        'usage': "Armures",
        'sources': [
            {'mob': "Nymphes des Eaux", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "voile_de_pipette": {
        'nom': "Voile de Pipette",
        'usage': "Armures",
        'sources': [
            {'mob': "Fées-Pipettes", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "voile_de_sagesse": {
        'nom': "Voile de Sagesse",
        'usage': "Armures",
        'sources': [
            {'mob': "Acolytes de la Sagesse Perdue", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "voile_de_savoir": {
        'nom': "Voile de Savoir",
        'usage': "Armures",
        'sources': [
            {'mob': "Professeurs Reniés", 'royaume': "Luthesia", 'biome': "Les For�ts Luminescentes et les Tours d'Ivoire"},
        ]
    },
    "voile_de_sorciere": {
        'nom': "Voile de Sorcière",
        'usage': "Armures",
        'sources': [
            {'mob': "Guenaudes des Landes", 'royaume': "Luthesia", 'biome': "Les Plaines Centrales et les Fiefs du Royaume"},
        ]
    },
    "voile_de_larchiviste": {
        'nom': "Voile de l'Archiviste",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Archiviste", 'royaume': "Khazak-Dûm", 'biome': "Les Galeries du Savoir et de l'Ing�nierie"},
        ]
    },
    "voile_de_lme_originelle": {
        'nom': "Voile de l'Âme Originelle",
        'usage': "Armures",
        'sources': [
            {'mob': "L'Écho Originel, Vis'khara", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "voile_des_rafales": {
        'nom': "Voile des Rafales",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Maître des Rafales, Zephyros Sombreplume", 'royaume': "Aerthos", 'biome': "Les Plaines C�lestes"},
        ]
    },
    "voile_du_chaos": {
        'nom': "Voile du Chaos",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Chaos Immuable, Vorlag'Ghul", 'royaume': "Vrak'thar", 'biome': "Les Montagnes Fractur�es de la Folie"},
        ]
    },
    "voile_du_juge": {
        'nom': "Voile du Juge",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Juge Déchu, Caelus Mortis", 'royaume': "Luthesia", 'biome': "Les Ruines du Vieux Royaume et les Terres Bannies"},
        ]
    },
    "ecaille_de_flamme": {
        'nom': "Écaille de Flamme",
        'usage': "Armes",
        'sources': [
            {'mob': "Salamandres de Flamme", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "ecailles_cristallines": {
        'nom': "Écailles Cristallines",
        'usage': "Armures",
        'sources': [
            {'mob': "Charognards de Cristaux", 'royaume': "Vrak'thar", 'biome': "Les Plaines de Cendres Hurlantes"},
        ]
    },
    "ecailles_scintillantes": {
        'nom': "Écailles Scintillantes",
        'usage': "Armes",
        'sources': [
            {'mob': "Nymphes des Eaux", 'royaume': "Aerthos", 'biome': "Les Lacs Scintillants et les Jardins Lunaires"},
        ]
    },
    "ecailles_de_sirene": {
        'nom': "Écailles de Sirène",
        'usage': "Armes",
        'sources': [
            {'mob': "Sirènes de Dérision", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "eclat_dobsidienne": {
        'nom': "Éclat d'Obsidienne",
        'usage': "Armures",
        'sources': [
            {'mob': "Trognes de l'Obsidienne", 'royaume': "Khazak-Dûm", 'biome': "Les Cavernes de Lave Ardente"},
        ]
    },
    "eclat_de_garde": {
        'nom': "Éclat de Garde",
        'usage': "Armures",
        'sources': [
            {'mob': "Guetteurs Scintillants", 'royaume': "Vrak'thar", 'biome': "Les Lacs Miroirs de l'�me"},
        ]
    },
    "ecorce_ancienne": {
        'nom': "Écorce Ancienne",
        'usage': "Armures",
        'sources': [
            {'mob': "Anciens Racinaires", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "ecorce_protectrice": {
        'nom': "Écorce Protectrice",
        'usage': "Armures",
        'sources': [
            {'mob': "Dryades Protectrices", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "ecorce_de_cur": {
        'nom': "Écorce de Cœur",
        'usage': "Armures",
        'sources': [
            {'mob': "Arbres-Cœur", 'royaume': "Vrak'thar", 'biome': "Les For�ts de Chair et d'Os"},
        ]
    },
    "ecorce_de_gardien": {
        'nom': "Écorce de Gardien",
        'usage': "Armures",
        'sources': [
            {'mob': "Le Gardien Sylvestre, Eldrin Racinéclat", 'royaume': "Aerthos", 'biome': "La For�t de Lumi�re Argent�e"},
        ]
    },
    "elytre_de_minerai": {
        'nom': "Élytre de Minerai",
        'usage': "Armures",
        'sources': [
            {'mob': "Scarabées de Minerai", 'royaume': "Khazak-Dûm", 'biome': "Les Tunnels de la Basalte et les Grandes Mines"},
        ]
    },
}


# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def obtenir_ingredient(slug: str) -> Optional[Dict]:
    """
    Obtient les informations d'un ingrédient par son slug.

    :param slug: Slug de l'ingrédient (ex: 'cendre_maudite')
    :return: Dictionnaire avec les informations de l'ingrédient ou None
    """
    return DEFINITIONS_INGREDIENTS.get(slug)


def obtenir_ingredient_par_nom(nom: str) -> Optional[Dict]:
    """
    Obtient les informations d'un ingrédient par son nom exact.

    :param nom: Nom exact de l'ingrédient (ex: 'Cendre Maudite')
    :return: Dictionnaire avec les informations de l'ingrédient ou None
    """
    for slug, data in DEFINITIONS_INGREDIENTS.items():
        if data['nom'] == nom:
            return data
    return None


def obtenir_ingredients_par_usage(usage: str) -> List[Dict]:
    """
    Obtient tous les ingrédients d'un usage spécifique.

    :param usage: 'Potions', 'Armes' ou 'Armures'
    :return: Liste de dictionnaires avec les informations des ingrédients
    """
    return [
        {'slug': slug, **data}
        for slug, data in DEFINITIONS_INGREDIENTS.items()
        if data['usage'] == usage
    ]


def obtenir_nom_complet_avec_qualite(nom: str, qualite: str) -> str:
    """
    Obtient le nom complet d'un ingrédient avec sa qualité.

    :param nom: Nom de l'ingrédient (ex: 'Cendre Maudite')
    :param qualite: Qualité de l'ingrédient (ex: 'Commun')
    :return: Nom complet avec qualité (ex: 'Cendre Maudite (Commun)')
    """
    return f"{nom} ({qualite})"


def obtenir_slug_par_nom(nom: str) -> Optional[str]:
    """
    Obtient le slug d'un ingrédient par son nom.

    :param nom: Nom exact de l'ingrédient
    :return: Slug de l'ingrédient ou None
    """
    for slug, data in DEFINITIONS_INGREDIENTS.items():
        if data['nom'] == nom:
            return slug
    return None


def obtenir_ingredients_par_mob(nom_mob: str) -> List[Dict]:
    """
    Obtient tous les ingrédients dropés par un mob spécifique.

    :param nom_mob: Nom du mob
    :return: Liste de dictionnaires avec les informations des ingrédients
    """
    resultats = []
    for slug, data in DEFINITIONS_INGREDIENTS.items():
        for source in data['sources']:
            if source['mob'] == nom_mob:
                resultats.append({'slug': slug, **data})
                break
    return resultats


def generer_slug(nom: str) -> str:
    """
    Génère un slug à partir d'un nom d'ingrédient.

    :param nom: Nom de l'ingrédient
    :return: Slug généré
    """
    import unicodedata
    import re

    # Normaliser les caractères Unicode
    nom = unicodedata.normalize('NFD', nom)
    # Convertir en minuscules
    nom = nom.lower()
    # Remplacer les espaces et caractères spéciaux
    nom = re.sub(r'[^\w\s-]', '', nom)
    nom = re.sub(r'[-\s]+', '_', nom)
    return nom.strip('_')


def verifier_ingredient_existe(nom: str) -> bool:
    """
    Vérifie si un ingrédient existe.

    :param nom: Nom de l'ingrédient
    :return: True si l'ingrédient existe, False sinon
    """
    return obtenir_ingredient_par_nom(nom) is not None


# ============================================================================
# FONCTIONS UTILITAIRES POUR LA GESTION DES QUALITÉS D'INGRÉDIENTS
# ============================================================================

def extraire_nom_base_ingredient(nom_complet: str) -> str:
    """
    Extrait le nom de base d'un ingrédient en enlevant la qualité.

    Exemple : "Cendre Maudite (Commun)" → "Cendre Maudite"

    :param nom_complet: Nom complet de l'ingrédient avec qualité
    :return: Nom de base sans qualité
    """
    if " (" in nom_complet and nom_complet.endswith(")"):
        return nom_complet.rsplit(" (", 1)[0]
    return nom_complet


def extraire_qualite_ingredient(nom_complet: str) -> Optional[str]:
    """
    Extrait la qualité d'un ingrédient depuis son nom complet.

    Exemple : "Cendre Maudite (Commun)" → "Commun"

    :param nom_complet: Nom complet de l'ingrédient avec qualité
    :return: Qualité de l'ingrédient ou None si pas de qualité trouvée
    """
    if " (" in nom_complet and nom_complet.endswith(")"):
        qualite = nom_complet.rsplit(" (", 1)[1].rstrip(")")
        if qualite in RARETES:
            return qualite
    return None


def compter_ingredients_par_nom_base(joueur, nom_base: str) -> Dict[str, int]:
    """
    Compte les ingrédients d'un nom de base dans l'inventaire du joueur,
    groupés par qualité.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :return: Dictionnaire {qualite: quantite} pour chaque qualité trouvée
    """
    resultats = {}

    for nom_objet, objet in joueur.inventaire.items():
        nom_base_objet = extraire_nom_base_ingredient(nom_objet)
        if nom_base_objet == nom_base:
            qualite = extraire_qualite_ingredient(nom_objet)
            if qualite:
                resultats[qualite] = resultats.get(qualite, 0) + objet.quantite

    return resultats


def compter_total_ingredient_toutes_qualites(joueur, nom_base: str) -> int:
    """
    Compte le total d'un ingrédient dans l'inventaire, toutes qualités confondues.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :return: Quantité totale de l'ingrédient (toutes qualités)
    """
    total = 0
    for nom_objet, objet in joueur.inventaire.items():
        nom_base_objet = extraire_nom_base_ingredient(nom_objet)
        if nom_base_objet == nom_base:
            total += objet.quantite
    return total


def avoir_ingredient_qualite(joueur, nom_base: str, qualite: str) -> Optional[Objet]:
    """
    Vérifie si le joueur possède un ingrédient d'une qualité spécifique.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :param qualite: Qualité recherchée (ex: "Commun", "Rare")
    :return: L'objet ingrédient si trouvé, None sinon
    """
    nom_complet = obtenir_nom_complet_avec_qualite(nom_base, qualite)
    return joueur.avoir_objet(nom_complet)


def compter_ingredient_qualite(joueur, nom_base: str, qualite: str) -> int:
    """
    Compte la quantité d'un ingrédient d'une qualité spécifique.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :param qualite: Qualité recherchée (ex: "Commun", "Rare")
    :return: Quantité de l'ingrédient de cette qualité (0 si absent)
    """
    nom_complet = obtenir_nom_complet_avec_qualite(nom_base, qualite)
    return joueur.compter_objet(nom_complet)


def lister_ingredients_par_nom_base(joueur, nom_base: str) -> List[Dict]:
    """
    Liste tous les ingrédients d'un nom de base dans l'inventaire,
    avec leurs qualités et quantités.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :return: Liste de dictionnaires {'qualite': str, 'quantite': int, 'objet': Objet}
    """
    resultats = []

    for nom_objet, objet in joueur.inventaire.items():
        nom_base_objet = extraire_nom_base_ingredient(nom_objet)
        if nom_base_objet == nom_base:
            qualite = extraire_qualite_ingredient(nom_objet)
            resultats.append({
                'qualite': qualite,
                'quantite': objet.quantite,
                'objet': objet,
                'nom_complet': nom_objet
            })

    return resultats


def retirer_ingredient_qualite(joueur, nom_base: str, qualite: str, quantite: int = 1) -> bool:
    """
    Retire une quantité d'un ingrédient d'une qualité spécifique.

    :param joueur: Le personnage joueur
    :param nom_base: Nom de base de l'ingrédient (sans qualité)
    :param qualite: Qualité de l'ingrédient à retirer
    :param quantite: Quantité à retirer (défaut: 1)
    :return: True si l'ingrédient a été retiré, False sinon
    """
    nom_complet = obtenir_nom_complet_avec_qualite(nom_base, qualite)
    return joueur.retirer_objet(nom_complet, quantite)
