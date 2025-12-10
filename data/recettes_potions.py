# data/recettes_potions.py
# Définitions de toutes les recettes de potions
# Utilise des ingrédients réels avec substitution automatique par royaume

# Structure d'une recette :
# {
#     "id_recette": {
#         "nom": "Nom de l'objet créé",
#         "type": "potion",
#         "sous_type": "soin" | "mana" | "energie" | "boost_force" | "boost_defense" | "boost_vitesse" | "boost_critique",
#         "rarete": "Commun" | "Peu Commun" | "Rare" | "Épique" | "Légendaire",
#         "ingredients": {
#             "nom_ingredient_reel": quantite_requise,  # Utilise des noms réels d'ingrédients
#             ...
#         },
#         "effets": {
#             "vie": int | None,
#             "mana": int | None,
#             "energie": int | None,
#             "boost_attaque": int | None,
#             "boost_defense": int | None,
#             "boost_vitesse": int | None,
#             "boost_critique": int | None,
#             "duree_tours": int | None,
#         },
#         "prix_vente": int,
#         "niveau_craft_requis": int,
#         "description": str
#     }
# }

# ============================================================================
# POTIONS DE SOIN
# ============================================================================

RECETTES_POTIONS_SOIN = {
    "potion_soin_mineure_commun": {
        "nom": "Potion de Soin Mineure",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Commun",
        "ingredients": {
            "Cendre Maudite": 2,
            "Eau Pure": 1
        },
        "effets": {
            "vie": 50,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 25,
        "niveau_craft_requis": 1,
        "description": "Restaure 50 points de vie."
    },
    "potion_soin_normale_peu_commun": {
        "nom": "Potion de Soin Normale",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Peu Commun",
        "ingredients": {
            "Cendre Maudite": 3,
            "Sang Maudit": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": 120,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 75,
        "niveau_craft_requis": 1,
        "description": "Restaure 120 points de vie."
    },
    "potion_soin_majeure_rare": {
        "nom": "Potion de Soin Majeure",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Rare",
        "ingredients": {
            "Sang Maudit": 3,
            "Essence d'Écho": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": 250,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 3,
        "description": "Restaure 250 points de vie."
    },
    "potion_soin_epique_epique": {
        "nom": "Potion de Soin Épique",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Épique",
        "ingredients": {
            "Essence d'Écho": 3,
            "Essence Dimensionnelle": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": 500,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 5,
        "description": "Restaure 500 points de vie."
    },
    "potion_soin_legendaire_legendaire": {
        "nom": "Potion de Soin Légendaire",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Dimensionnelle": 3,
            "Essence Originelle": 1,
            "Eau Pure": 3
        },
        "effets": {
            "vie": 1000,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 750,
        "niveau_craft_requis": 10,
        "description": "Restaure 1000 points de vie."
    }
}

# ============================================================================
# POTIONS DE MANA
# ============================================================================

RECETTES_POTIONS_MANA = {
    "potion_mana_mineure_commun": {
        "nom": "Potion de Mana Mineure",
        "type": "potion",
        "sous_type": "mana",
        "rarete": "Commun",
        "ingredients": {
            "Cristal Corrompu": 2,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": 30,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 25,
        "niveau_craft_requis": 1,
        "description": "Restaure 30 points de mana."
    },
    "potion_mana_normale_peu_commun": {
        "nom": "Potion de Mana Normale",
        "type": "potion",
        "sous_type": "mana",
        "rarete": "Peu Commun",
        "ingredients": {
            "Cristal Corrompu": 3,
            "Sève Corrompue": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": 80,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 75,
        "niveau_craft_requis": 1,
        "description": "Restaure 80 points de mana."
    },
    "potion_mana_majeure_rare": {
        "nom": "Potion de Mana Majeure",
        "type": "potion",
        "sous_type": "mana",
        "rarete": "Rare",
        "ingredients": {
            "Sève Corrompue": 3,
            "Essence Scintillante": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": None,
            "mana": 150,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 3,
        "description": "Restaure 150 points de mana."
    },
    "potion_mana_epique_epique": {
        "nom": "Potion de Mana Épique",
        "type": "potion",
        "sous_type": "mana",
        "rarete": "Épique",
        "ingredients": {
            "Essence Scintillante": 3,
            "Essence Gravitationnelle": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": None,
            "mana": 250,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 5,
        "description": "Restaure 250 points de mana."
    },
    "potion_mana_legendaire_legendaire": {
        "nom": "Potion de Mana Légendaire",
        "type": "potion",
        "sous_type": "mana",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Gravitationnelle": 3,
            "Essence Originelle": 1,
            "Eau Pure": 3
        },
        "effets": {
            "vie": None,
            "mana": 500,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 750,
        "niveau_craft_requis": 10,
        "description": "Restaure 500 points de mana."
    }
}

# ============================================================================
# POTIONS D'ÉNERGIE
# ============================================================================

RECETTES_POTIONS_ENERGIE = {
    "potion_energie_mineure_commun": {
        "nom": "Potion d'Énergie Mineure",
        "type": "potion",
        "sous_type": "energie",
        "rarete": "Commun",
        "ingredients": {
            "Essence de Brume": 2,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": 20,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 25,
        "niveau_craft_requis": 1,
        "description": "Restaure 20 points d'énergie."
    },
    "potion_energie_normale_peu_commun": {
        "nom": "Potion d'Énergie Normale",
        "type": "potion",
        "sous_type": "energie",
        "rarete": "Peu Commun",
        "ingredients": {
            "Essence de Brume": 3,
            "Essence de Corruption": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": 50,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 75,
        "niveau_craft_requis": 1,
        "description": "Restaure 50 points d'énergie."
    },
    "potion_energie_majeure_rare": {
        "nom": "Potion d'Énergie Majeure",
        "type": "potion",
        "sous_type": "energie",
        "rarete": "Rare",
        "ingredients": {
            "Essence de Corruption": 3,
            "Essence de Chant": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": 100,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 150,
        "niveau_craft_requis": 3,
        "description": "Restaure 100 points d'énergie."
    },
    "potion_energie_epique_epique": {
        "nom": "Potion d'Énergie Épique",
        "type": "potion",
        "sous_type": "energie",
        "rarete": "Épique",
        "ingredients": {
            "Essence de Chant": 3,
            "Essence du Chaos": 1,
            "Eau Pure": 2
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": 200,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 5,
        "description": "Restaure 200 points d'énergie."
    },
    "potion_energie_legendaire_legendaire": {
        "nom": "Potion d'Énergie Légendaire",
        "type": "potion",
        "sous_type": "energie",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence du Chaos": 3,
            "Essence Originelle": 1,
            "Eau Pure": 3
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": 400,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": None
        },
        "prix_vente": 750,
        "niveau_craft_requis": 10,
        "description": "Restaure 400 points d'énergie."
    }
}

# ============================================================================
# POTIONS DE BOOST - FORCE
# ============================================================================

RECETTES_POTIONS_BOOST_FORCE = {
    "potion_force_mineure_commun": {
        "nom": "Potion de Force Mineure",
        "type": "potion",
        "sous_type": "boost_force",
        "rarete": "Commun",
        "ingredients": {
            "Cendre Maudite": 2,
            "Fragment d'Os Spectral": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": 5,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 3
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "+5 Attaque pendant 3 tours"
    },
    "potion_force_normale_peu_commun": {
        "nom": "Potion de Force Normale",
        "type": "potion",
        "sous_type": "boost_force",
        "rarete": "Peu Commun",
        "ingredients": {
            "Sang Maudit": 2,
            "Griffe de Traqueur": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": 10,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 5
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "+10 Attaque pendant 5 tours"
    },
    "potion_force_majeure_rare": {
        "nom": "Potion de Force Majeure",
        "type": "potion",
        "sous_type": "boost_force",
        "rarete": "Rare",
        "ingredients": {
            "Sève Corrompue": 3,
            "Fragment de Miroir": 1,
            "Essence d'Écho": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": 20,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 7
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "+20 Attaque pendant 7 tours"
    },
    "potion_force_epique_epique": {
        "nom": "Potion de Force Épique",
        "type": "potion",
        "sous_type": "boost_force",
        "rarete": "Épique",
        "ingredients": {
            "Essence Scintillante": 3,
            "Fragment de Fracture": 1,
            "Essence Dimensionnelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": 35,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 10
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "+35 Attaque pendant 10 tours"
    },
    "potion_force_legendaire_legendaire": {
        "nom": "Potion de Force Légendaire",
        "type": "potion",
        "sous_type": "boost_force",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Dimensionnelle": 3,
            "Fragment du Chaos Immuable": 1,
            "Essence Originelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": 50,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 15
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "+50 Attaque pendant 15 tours"
    }
}

# ============================================================================
# POTIONS DE BOOST - DÉFENSE
# ============================================================================

RECETTES_POTIONS_BOOST_DEFENSE = {
    "potion_protection_mineure_commun": {
        "nom": "Potion de Protection Mineure",
        "type": "potion",
        "sous_type": "boost_defense",
        "rarete": "Commun",
        "ingredients": {
            "Cendre Maudite": 2,
            "Fragment d'Os Spectral": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": 3,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 3
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "+3 Défense pendant 3 tours"
    },
    "potion_protection_normale_peu_commun": {
        "nom": "Potion de Protection Normale",
        "type": "potion",
        "sous_type": "boost_defense",
        "rarete": "Peu Commun",
        "ingredients": {
            "Sang Maudit": 2,
            "Griffe de Traqueur": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": 6,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 5
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "+6 Défense pendant 5 tours"
    },
    "potion_protection_majeure_rare": {
        "nom": "Potion de Protection Majeure",
        "type": "potion",
        "sous_type": "boost_defense",
        "rarete": "Rare",
        "ingredients": {
            "Sève Corrompue": 3,
            "Fragment de Miroir": 1,
            "Essence d'Écho": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": 12,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 7
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "+12 Défense pendant 7 tours"
    },
    "potion_protection_epique_epique": {
        "nom": "Potion de Protection Épique",
        "type": "potion",
        "sous_type": "boost_defense",
        "rarete": "Épique",
        "ingredients": {
            "Essence Scintillante": 3,
            "Fragment de Fracture": 1,
            "Essence Dimensionnelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": 20,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 10
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "+20 Défense pendant 10 tours"
    },
    "potion_protection_legendaire_legendaire": {
        "nom": "Potion de Protection Légendaire",
        "type": "potion",
        "sous_type": "boost_defense",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Dimensionnelle": 3,
            "Fragment du Chaos Immuable": 1,
            "Essence Originelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": 30,
            "boost_vitesse": None,
            "boost_critique": None,
            "duree_tours": 15
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "+30 Défense pendant 15 tours"
    }
}

# ============================================================================
# POTIONS DE BOOST - VITESSE
# ============================================================================

RECETTES_POTIONS_BOOST_VITESSE = {
    "potion_velocite_mineure_commun": {
        "nom": "Potion de Vélocité Mineure",
        "type": "potion",
        "sous_type": "boost_vitesse",
        "rarete": "Commun",
        "ingredients": {
            "Cendre Maudite": 2,
            "Fragment d'Os Spectral": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": 5,
            "boost_critique": None,
            "duree_tours": 3
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "+5 Vitesse pendant 3 tours"
    },
    "potion_velocite_normale_peu_commun": {
        "nom": "Potion de Vélocité Normale",
        "type": "potion",
        "sous_type": "boost_vitesse",
        "rarete": "Peu Commun",
        "ingredients": {
            "Sang Maudit": 2,
            "Griffe de Traqueur": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": 10,
            "boost_critique": None,
            "duree_tours": 5
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "+10 Vitesse pendant 5 tours"
    },
    "potion_velocite_majeure_rare": {
        "nom": "Potion de Vélocité Majeure",
        "type": "potion",
        "sous_type": "boost_vitesse",
        "rarete": "Rare",
        "ingredients": {
            "Sève Corrompue": 3,
            "Fragment de Miroir": 1,
            "Essence d'Écho": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": 20,
            "boost_critique": None,
            "duree_tours": 7
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "+20 Vitesse pendant 7 tours"
    },
    "potion_velocite_epique_epique": {
        "nom": "Potion de Vélocité Épique",
        "type": "potion",
        "sous_type": "boost_vitesse",
        "rarete": "Épique",
        "ingredients": {
            "Essence Scintillante": 3,
            "Fragment de Fracture": 1,
            "Essence Dimensionnelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": 35,
            "boost_critique": None,
            "duree_tours": 10
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "+35 Vitesse pendant 10 tours"
    },
    "potion_velocite_legendaire_legendaire": {
        "nom": "Potion de Vélocité Légendaire",
        "type": "potion",
        "sous_type": "boost_vitesse",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Dimensionnelle": 3,
            "Fragment du Chaos Immuable": 1,
            "Essence Originelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": 50,
            "boost_critique": None,
            "duree_tours": 15
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "+50 Vitesse pendant 15 tours"
    }
}

# ============================================================================
# POTIONS DE BOOST - CRITIQUE
# ============================================================================

RECETTES_POTIONS_BOOST_CRITIQUE = {
    "potion_precision_mineure_commun": {
        "nom": "Potion de Précision Mineure",
        "type": "potion",
        "sous_type": "boost_critique",
        "rarete": "Commun",
        "ingredients": {
            "Cendre Maudite": 2,
            "Fragment d'Os Spectral": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": 5,
            "duree_tours": 3
        },
        "prix_vente": 50,
        "niveau_craft_requis": 1,
        "description": "+5% Critique pendant 3 tours"
    },
    "potion_precision_normale_peu_commun": {
        "nom": "Potion de Précision Normale",
        "type": "potion",
        "sous_type": "boost_critique",
        "rarete": "Peu Commun",
        "ingredients": {
            "Sang Maudit": 2,
            "Griffe de Traqueur": 1,
            "Eau Pure": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": 10,
            "duree_tours": 5
        },
        "prix_vente": 150,
        "niveau_craft_requis": 2,
        "description": "+10% Critique pendant 5 tours"
    },
    "potion_precision_majeure_rare": {
        "nom": "Potion de Précision Majeure",
        "type": "potion",
        "sous_type": "boost_critique",
        "rarete": "Rare",
        "ingredients": {
            "Sève Corrompue": 3,
            "Fragment de Miroir": 1,
            "Essence d'Écho": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": 15,
            "duree_tours": 7
        },
        "prix_vente": 300,
        "niveau_craft_requis": 3,
        "description": "+15% Critique pendant 7 tours"
    },
    "potion_precision_epique_epique": {
        "nom": "Potion de Précision Épique",
        "type": "potion",
        "sous_type": "boost_critique",
        "rarete": "Épique",
        "ingredients": {
            "Essence Scintillante": 3,
            "Fragment de Fracture": 1,
            "Essence Dimensionnelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": 25,
            "duree_tours": 10
        },
        "prix_vente": 600,
        "niveau_craft_requis": 5,
        "description": "+25% Critique pendant 10 tours"
    },
    "potion_precision_legendaire_legendaire": {
        "nom": "Potion de Précision Légendaire",
        "type": "potion",
        "sous_type": "boost_critique",
        "rarete": "Légendaire",
        "ingredients": {
            "Essence Dimensionnelle": 3,
            "Fragment du Chaos Immuable": 1,
            "Essence Originelle": 1
        },
        "effets": {
            "vie": None,
            "mana": None,
            "energie": None,
            "boost_attaque": None,
            "boost_defense": None,
            "boost_vitesse": None,
            "boost_critique": 35,
            "duree_tours": 15
        },
        "prix_vente": 1500,
        "niveau_craft_requis": 10,
        "description": "+35% Critique pendant 15 tours"
    }
}
