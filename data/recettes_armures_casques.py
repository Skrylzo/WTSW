# data/recettes_armures_casques.py
# Définitions de toutes les recettes de casques
# Utilise des ingrédients réels avec substitution automatique par royaume

# ============================================================================
# ARMURES - CASQUES
# ============================================================================

RECETTES_ARMURES_CASQUES = {
    "casque_cuir_commun": {
        "nom": "Casque de Cuir",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque basique en cuir."
    },
    "casque_cuir_renforce_peu_commun": {
        "nom": "Casque de Cuir Renforcé",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque amélioré en cuir renforcé."
    },
    "casque_mithril_rare": {
        "nom": "Casque de Mithril",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque rare en mithril."
    },
    "casque_adamantium_epique": {
        "nom": "Casque d'Adamantium",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque épique en adamantium."
    },
    "casque_divine_legendaire": {
        "nom": "Casque Divine",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque légendaire d'origine divine."
    },
    "casque_plaques_fer_commun": {
        "nom": "Casque en Plaques de Fer",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque en plaques basique en fer."
    },
    "casque_plaques_argent_peu_commun": {
        "nom": "Casque en Plaques d'Argent",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque en plaques amélioré en argent."
    },
    "casque_plaques_mithril_rare": {
        "nom": "Casque en Plaques de Mithril",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque en plaques rare en mithril."
    },
    "casque_plaques_adamantium_epique": {
        "nom": "Casque en Plaques d'Adamantium",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque en plaques épique en adamantium."
    },
    "casque_plaques_divine_legendaire": {
        "nom": "Casque en Plaques Divine",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque en plaques légendaire d'origine divine."
    },
    "casque_squelettique_fer_commun": {
        "nom": "Casque Squelettique de Fer",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque squelettique basique en fer."
    },
    "casque_squelettique_argent_peu_commun": {
        "nom": "Casque Squelettique d'Argent",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque squelettique amélioré en argent."
    },
    "casque_squelettique_mithril_rare": {
        "nom": "Casque Squelettique de Mithril",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque squelettique rare en mithril."
    },
    "casque_squelettique_adamantium_epique": {
        "nom": "Casque Squelettique d'Adamantium",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque squelettique épique en adamantium."
    },
    "casque_squelettique_divine_legendaire": {
        "nom": "Casque Squelettique Divine",
        "type": "armure",
        "sous_type": "casque",
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
        "description": "Un casque squelettique légendaire d'origine divine."
    }
}
