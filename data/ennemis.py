# data/ennemis.py
# Définitions des Ennemis

# --- Définitions des Ennemis ---
DEFINITIONS_ENNEMIS = {
    "gobelin_basique": {
        "nom": "Gobelin basique",
        "vie_max": 30,
        "vitesse": 10,
        "attaque": 8,
        "defense": 2,
        "chance_critique": 5,
        "xp_a_donner": 100,
        # Format de loot_table :
        # - Liste simple de strings = 100% de chance pour chaque objet
        # - Liste de dicts {"nom": "...", "chance": 1-100} = probabilité personnalisée
        # - Format mixte possible (strings et dicts)
        "loot_table": [
            {"nom": "Petite bourse", "chance": 100},  # 100% de chance
            {"nom": "Peau de gobelin", "chance": 75}  # 75% de chance
        ]
    },
    "orc_furieux": {
        "nom": "Orc Furieux",
        "vie_max": 60,
        "vitesse": 8,
        "attaque": 15,
        "defense": 5,
        "chance_critique": 10,
        "xp_a_donner": 50,
        "loot_table": [
            {"nom": "Hache rouillée", "chance": 80},  # 80% de chance
            {"nom": "Dent d'orc", "chance": 50}        # 50% de chance
        ]
    },
    "gobelin_chaman": {
        "nom": "Gobelin Chaman",
        "vie_max": 40,
        "vitesse": 12,
        "attaque": 10,
        "defense": 3,
        "chance_critique": 8,
        "xp_a_donner": 35,
        "loot_table": [
            {"nom": "Talisman chamanique", "chance": 30},  # 30% de chance (rare)
            {"nom": "Herbes mystérieuses", "chance": 90}   # 90% de chance
        ]
    }
    # Vous pouvez ajouter d'autres ennemis ici
}
