# data/recettes_armures_bottes.py
# Définitions de toutes les recettes de bottes
# Utilise des ingrédients réels avec substitution automatique par royaume

# ============================================================================
# ARMURES - BOTTES
# ============================================================================

RECETTES_ARMURES_BOTTES = {
    "bottes_cuir_commun": {
        "nom": "Bottes de Cuir",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Commun",
        "ingredients": {
            "Linceul Spectral": 3,
            "Fragment d'Os Spectral": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "Des bottes basiques en cuir."
    },
    "bottes_cuir_renforce_peu_commun": {
        "nom": "Bottes de Cuir Renforcé",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Peu Commun",
        "ingredients": {
            "Fragment d'Os de Géant": 3,
            "Griffe de Traqueur": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "Des bottes améliorées en cuir renforcé."
    },
    "bottes_mithril_rare": {
        "nom": "Bottes de Mithril",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Mycelium": 3,
            "Essence d'Écho": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "Des bottes rares en mithril."
    },
    "bottes_adamantium_epique": {
        "nom": "Bottes d'Adamantium",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Épique",
        "ingredients": {
            "Fragment du Chaos Immuable": 3,
            "Essence Dimensionnelle": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "Des bottes épiques en adamantium."
    },
    "bottes_divine_legendaire": {
        "nom": "Bottes Divine",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Cœur Pur": 3,
            "Essence Originelle": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "Des bottes légendaires d'origine divine."
    },
    "bottes_plaques_fer_commun": {
        "nom": "Bottes en Plaques de Fer",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 2,
            "Linceul Spectral": 2,
            "Cendre Maudite": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "Des bottes en plaques basiques en fer."
    },
    "bottes_plaques_argent_peu_commun": {
        "nom": "Bottes en Plaques d'Argent",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 2,
            "Fragment d'Os de Géant": 2,
            "Sang Maudit": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "Des bottes en plaques améliorées en argent."
    },
    "bottes_plaques_mithril_rare": {
        "nom": "Bottes en Plaques de Mithril",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 2,
            "Membrane de Mycelium": 2,
            "Essence Scintillante": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "Des bottes en plaques rares en mithril."
    },
    "bottes_plaques_adamantium_epique": {
        "nom": "Bottes en Plaques d'Adamantium",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 2,
            "Fragment du Chaos Immuable": 2,
            "Essence Gravitationnelle": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "Des bottes en plaques épiques en adamantium."
    },
    "bottes_plaques_divine_legendaire": {
        "nom": "Bottes en Plaques Divine",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 2,
            "Fragment de Cœur Pur": 2,
            "Essence Originelle": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "Des bottes en plaques légendaires d'origine divine."
    },
    "bottes_squelettique_fer_commun": {
        "nom": "Bottes Squelettiques de Fer",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Commun",
        "ingredients": {
            "Linceul Spectral": 3,
            "Cendre Maudite": 2,
            "Fragment d'Os Spectral": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "Des bottes squelettiques basiques en fer."
    },
    "bottes_squelettique_argent_peu_commun": {
        "nom": "Bottes Squelettiques d'Argent",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Peu Commun",
        "ingredients": {
            "Fragment d'Os de Géant": 3,
            "Sang Maudit": 2,
            "Griffe de Traqueur": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "Des bottes squelettiques améliorées en argent."
    },
    "bottes_squelettique_mithril_rare": {
        "nom": "Bottes Squelettiques de Mithril",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Mycelium": 3,
            "Essence d'Écho": 2,
            "Fragment de Miroir": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "Des bottes squelettiques rares en mithril."
    },
    "bottes_squelettique_adamantium_epique": {
        "nom": "Bottes Squelettiques d'Adamantium",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Épique",
        "ingredients": {
            "Fragment du Chaos Immuable": 3,
            "Essence Dimensionnelle": 2,
            "Fragment de Fracture": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "Des bottes squelettiques épiques en adamantium."
    },
    "bottes_squelettique_divine_legendaire": {
        "nom": "Bottes Squelettiques Divine",
        "type": "armure",
        "sous_type": "bottes",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Cœur Pur": 3,
            "Essence Originelle": 2,
            "Fragment de Distorsion": 1
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": None,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "Des bottes squelettiques légendaires d'origine divine."
    }
}
