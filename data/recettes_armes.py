
# data/recettes_armes.py
# Définitions de toutes les recettes d'armes (épées, haches, dagues, bâtons)
# Utilise des ingrédients réels avec substitution automatique par royaume

# ============================================================================
# ARMES - ÉPÉES
# ============================================================================

RECETTES_ARMES_EPEES = {
    "epee_fer_commun": {
        "nom": "Épée de Fer",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 5,
            "Linceul Spectral": 2
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Une épée basique en fer."
    },
    "epee_argent_peu_commun": {
        "nom": "Épée d'Argent",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 5,
            "Fragment d'Os de Géant": 2
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
        "niveau_craft_requis": 2,
        "description": "Une épée améliorée en argent."
    },
    "epee_mithril_rare": {
        "nom": "Épée de Mithril",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 5,
            "Essence d'Écho": 2
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
        "niveau_craft_requis": 3,
        "description": "Une épée rare en mithril."
    },
    "epee_adamantium_epique": {
        "nom": "Épée d'Adamantium",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 5,
            "Essence Dimensionnelle": 2
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Une épée épique en adamantium."
    },
    "epee_divine_legendaire": {
        "nom": "Épée Divine",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 5,
            "Essence Originelle": 2
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une épée légendaire d'origine divine."
    },
    "katana_fer_commun": {
        "nom": "Katana de Fer",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 3,
            "Cendre Maudite": 2,
            "Linceul Spectral": 1
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Un katana basique en fer."
    },
    "katana_argent_peu_commun": {
        "nom": "Katana d'Argent",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 4,
            "Sang Maudit": 2,
            "Fragment d'Os de Géant": 1
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
        "niveau_craft_requis": 2,
        "description": "Un katana amélioré en argent."
    },
    "katana_mithril_rare": {
        "nom": "Katana de Mithril",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 4,
            "Essence Scintillante": 2,
            "Fragment de Mycelium": 1
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
        "niveau_craft_requis": 3,
        "description": "Un katana rare en mithril."
    },
    "katana_adamantium_epique": {
        "nom": "Katana d'Adamantium",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 4,
            "Essence Gravitationnelle": 2,
            "Fragment du Chaos Immuable": 1
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Un katana épique en adamantium."
    },
    "katana_divine_legendaire": {
        "nom": "Katana Divin",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 4,
            "Essence du Chaos": 2,
            "Fragment de Cœur Pur": 1
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Un katana légendaire d'origine divine."
    },
    "double_epee_fer_commun": {
        "nom": "Double Épée de Fer",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 5,
            "Griffe de Charognard": 2,
            "Cristal Corrompu": 1
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Une paire d'épées basiques en fer."
    },
    "double_epee_argent_peu_commun": {
        "nom": "Double Épée d'Argent",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 6,
            "Sève Corrompue": 1
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
        "niveau_craft_requis": 2,
        "description": "Une paire d'épées améliorées en argent."
    },
    "double_epee_mithril_rare": {
        "nom": "Double Épée de Mithril",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 6,
            "Essence de Chant": 1,
            "Membrane de Mycelium": 1
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
        "niveau_craft_requis": 3,
        "description": "Une paire d'épées rares en mithril."
    },
    "double_epee_adamantium_epique": {
        "nom": "Double Épée d'Adamantium",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 6,
            "Essence du Chaos": 1,
            "Fragment du Chaos Immuable": 1
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Une paire d'épées épiques en adamantium."
    },
    "double_epee_divine_legendaire": {
        "nom": "Double Épée Divine",
        "type": "arme",
        "sous_type": "epee",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 6,
            "Essence Originelle": 1,
            "Fragment de Cœur Pur": 1
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une paire d'épées légendaires d'origine divine."
    }
}

# ============================================================================
# ARMES - HACHES
# ============================================================================

RECETTES_ARMES_HACHES = {
    "hache_fer_commun": {
        "nom": "Hache de Fer",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 5,
            "Linceul Spectral": 2
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Une hache basique en fer."
    },
    "hache_argent_peu_commun": {
        "nom": "Hache d'Argent",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 5,
            "Fragment d'Os de Géant": 2
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
        "niveau_craft_requis": 2,
        "description": "Une hache améliorée en argent."
    },
    "hache_mithril_rare": {
        "nom": "Hache de Mithril",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 5,
            "Essence d'Écho": 2
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
        "niveau_craft_requis": 3,
        "description": "Une hache rare en mithril."
    },
    "hache_adamantium_epique": {
        "nom": "Hache d'Adamantium",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 5,
            "Essence Dimensionnelle": 2
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Une hache épique en adamantium."
    },
    "hache_divine_legendaire": {
        "nom": "Hache Divine",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 5,
            "Essence Originelle": 2
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une hache légendaire d'origine divine."
    },
    "gundao_fer_commun": {
        "nom": "Gundao de Fer",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Commun",
        "ingredients": {
            "Griffe de Charognard": 4,
            "Cendre Maudite": 3,
            "Écailles Cristallines": 2
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Un gundao basique en fer."
    },
    "gundao_argent_peu_commun": {
        "nom": "Gundao d'Argent",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Peu Commun",
        "ingredients": {
            "Os de Géant": 4,
            "Sang Maudit": 3,
            "Peau de Gobelin": 2
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
        "niveau_craft_requis": 2,
        "description": "Un gundao amélioré en argent."
    },
    "gundao_mithril_rare": {
        "nom": "Gundao de Mithril",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Rare",
        "ingredients": {
            "Fragment d'Âme Noyée": 4,
            "Essence Scintillante": 3,
            "Fragment de Mycelium": 2
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
        "niveau_craft_requis": 3,
        "description": "Un gundao rare en mithril."
    },
    "gundao_adamantium_epique": {
        "nom": "Gundao d'Adamantium",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Distorsion": 4,
            "Essence Gravitationnelle": 3,
            "Fragment du Chaos Immuable": 2
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Un gundao épique en adamantium."
    },
    "gundao_divine_legendaire": {
        "nom": "Gundao Divin",
        "type": "arme",
        "sous_type": "hache",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Cœur Pur": 4,
            "Essence du Chaos": 3,
            "Fragment de Cœur Pur": 2
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Un gundao légendaire d'origine divine."
    }
}

# ============================================================================
# ARMES - DAGUES
# ============================================================================

RECETTES_ARMES_DAGUES = {
    "dague_fer_commun": {
        "nom": "Dague de Fer",
        "type": "arme",
        "sous_type": "dague",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 4,
            "Cristal Corrompu": 2,
            "Linceul Spectral": 1
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Une dague basique en fer."
    },
    "dague_argent_peu_commun": {
        "nom": "Dague d'Argent",
        "type": "arme",
        "sous_type": "dague",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 4,
            "Sève Corrompue": 2,
            "Fragment d'Os de Géant": 1
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
        "niveau_craft_requis": 2,
        "description": "Une dague améliorée en argent."
    },
    "dague_mithril_rare": {
        "nom": "Dague de Mithril",
        "type": "arme",
        "sous_type": "dague",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 4,
            "Essence de Chant": 2,
            "Membrane de Mycelium": 1
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
        "niveau_craft_requis": 3,
        "description": "Une dague rare en mithril."
    },
    "dague_adamantium_epique": {
        "nom": "Dague d'Adamantium",
        "type": "arme",
        "sous_type": "dague",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 4,
            "Essence du Chaos": 2,
            "Fragment du Chaos Immuable": 1
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Une dague épique en adamantium."
    },
    "dague_divine_legendaire": {
        "nom": "Dague Divine",
        "type": "arme",
        "sous_type": "dague",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 4,
            "Essence Originelle": 2,
            "Fragment de Cœur Pur": 1
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une dague légendaire d'origine divine."
    }
}

# ============================================================================
# ARMES - BÂTONS
# ============================================================================

RECETTES_ARMES_BATONS = {
    "baton_fer_commun": {
        "nom": "Bâton de Fer",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 4,
            "Essence de Brume": 2,
            "Écailles Cristallines": 1
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Un bâton basique en fer."
    },
    "baton_argent_peu_commun": {
        "nom": "Bâton d'Argent",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Peu Commun",
        "ingredients": {
            "Os de Géant": 4,
            "Essence de Corruption": 2,
            "Peau de Gobelin": 1
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
        "niveau_craft_requis": 2,
        "description": "Un bâton amélioré en argent."
    },
    "baton_mithril_rare": {
        "nom": "Bâton de Mithril",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Rare",
        "ingredients": {
            "Fragment d'Âme Noyée": 4,
            "Essence Scintillante": 2,
            "Fragment de Mycelium": 1
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
        "niveau_craft_requis": 3,
        "description": "Un bâton rare en mithril."
    },
    "baton_adamantium_epique": {
        "nom": "Bâton d'Adamantium",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 4,
            "Essence Gravitationnelle": 2,
            "Fragment du Chaos Immuable": 1
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Un bâton épique en adamantium."
    },
    "baton_divine_legendaire": {
        "nom": "Bâton Divin",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 4,
            "Essence Originelle": 2,
            "Fragment de Cœur Pur": 1
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Un bâton légendaire d'origine divine."
    },
    "baton_magique_fer_commun": {
        "nom": "Bâton Magique de Fer",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Commun",
        "ingredients": {
            "Fragment d'Os Spectral": 3,
            "Cristal Corrompu": 3,
            "Essence de Brume": 1
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
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Un bâton magique basique en fer."
    },
    "baton_magique_argent_peu_commun": {
        "nom": "Bâton Magique d'Argent",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Peu Commun",
        "ingredients": {
            "Griffe de Traqueur": 3,
            "Sève Corrompue": 3,
            "Essence de Corruption": 1
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
        "niveau_craft_requis": 2,
        "description": "Un bâton magique amélioré en argent."
    },
    "baton_magique_mithril_rare": {
        "nom": "Bâton Magique de Mithril",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Rare",
        "ingredients": {
            "Fragment de Miroir": 3,
            "Essence Scintillante": 3,
            "Essence de Chant": 1
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
        "niveau_craft_requis": 3,
        "description": "Un bâton magique rare en mithril."
    },
    "baton_magique_adamantium_epique": {
        "nom": "Bâton Magique d'Adamantium",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Épique",
        "ingredients": {
            "Fragment de Fracture": 3,
            "Essence Gravitationnelle": 3,
            "Essence du Chaos": 1
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
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Un bâton magique épique en adamantium."
    },
    "baton_magique_divine_legendaire": {
        "nom": "Bâton Magique Divin",
        "type": "arme",
        "sous_type": "baton",
        "rarete": "Légendaire",
        "ingredients": {
            "Fragment de Distorsion": 3,
            "Essence Originelle": 3,
            "Fragment de Cœur Pur": 1
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
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Un bâton magique légendaire d'origine divine."
    }
}
