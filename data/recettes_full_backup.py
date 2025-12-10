# data/recettes.py
# Définitions de toutes les recettes de craft
# Basé sur DESIGN_CRAFT.md

from typing import Dict, List, Optional
from data.ingredients import RARETES

# Structure d'une recette :
# {
#     "id_recette": {
#         "nom": "Nom de l'objet créé",
#         "type": "potion" | "arme" | "armure",
#         "sous_type": "soin" | "mana" | "energie" | "boost_force" | "boost_defense" | "boost_vitesse" | "boost_critique" | "epee" | "hache" | "dague" | "baton" | "torse" | "casque" | "bottes",
#         "rarete": "Commun" | "Peu Commun" | "Rare" | "Épique" | "Légendaire",
#         "ingredients": {
#             "nom_base_ingredient": quantite_requise,
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
#             "duree_tours": int | None,  # Pour les potions de boost
#         },
#         "stats": {  # Pour armes et armures
#             "degats_base": int | None,
#             "bonus_defense": int | None,
#             "bonus_force": int | None,
#             "bonus_agilite": int | None,
#             "bonus_vitalite": int | None,
#             "bonus_intelligence": int | None,
#         },
#         "prix_vente": int,
#         "niveau_craft_requis": int,  # Optionnel, défaut 1
#         "description": str
#     }
# }

# ============================================================================
# POTIONS DE SOIN
# ============================================================================

# Note: Les potions de soin ne sont pas définies dans DESIGN_CRAFT.md
# On les ajoute ici avec une structure similaire aux potions de mana

RECETTES_POTIONS_SOIN = {
    "potion_soin_mineure_commun": {
        "nom": "Potion de Soin Mineure",
        "type": "potion",
        "sous_type": "soin",
        "rarete": "Commun",
        "ingredients": {
            "Ingrédient Potion Niveau 1-5": 2,
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
            "Ingrédient Potion Niveau 1-5": 3,
            "Ingrédient Potion Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Potion Niveau 10-15": 1,
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 1-5": 2,
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
            "Ingrédient Potion Niveau 1-5": 3,
            "Ingrédient Potion Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Potion Niveau 10-15": 1,
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 1-5": 2,
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
            "Ingrédient Potion Niveau 1-5": 3,
            "Ingrédient Potion Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Potion Niveau 10-15": 1,
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Potion Niveau 15-20": 1,
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
            "Ingrédient Potion Niveau 1-5": 2,
            "Ingrédient Arme Niveau 1-5": 1,
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
            "Ingrédient Potion Niveau 5-10": 2,
            "Ingrédient Arme Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Arme Niveau 10-15": 1,
            "Ingrédient Potion Niveau 10-15": 1
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 1-5": 2,
            "Ingrédient Arme Niveau 1-5": 1,
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
            "Ingrédient Potion Niveau 5-10": 2,
            "Ingrédient Arme Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Arme Niveau 10-15": 1,
            "Ingrédient Potion Niveau 10-15": 1
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 1-5": 2,
            "Ingrédient Arme Niveau 1-5": 1,
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
            "Ingrédient Potion Niveau 5-10": 2,
            "Ingrédient Arme Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Arme Niveau 10-15": 1,
            "Ingrédient Potion Niveau 10-15": 1
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 1-5": 2,
            "Ingrédient Arme Niveau 1-5": 1,
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
            "Ingrédient Potion Niveau 5-10": 2,
            "Ingrédient Arme Niveau 5-10": 1,
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
            "Ingrédient Potion Niveau 5-10": 3,
            "Ingrédient Arme Niveau 10-15": 1,
            "Ingrédient Potion Niveau 10-15": 1
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
            "Ingrédient Potion Niveau 10-15": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Potion Niveau 15-20": 3,
            "Ingrédient Arme Niveau 15-20": 1,
            "Ingrédient Potion Niveau 15-20": 1
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
            "Ingrédient Arme Niveau 1-5": 5,
            "Ingrédient Armure Niveau 1-5": 2
        },
        "effets": {},
        "stats": {
            "degats_base": 3,
            "bonus_defense": None,
            "bonus_force": 1,
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
            "Ingrédient Arme Niveau 5-10": 5,
            "Ingrédient Armure Niveau 5-10": 2
        },
        "effets": {},
        "stats": {
            "degats_base": 8,
            "bonus_defense": None,
            "bonus_force": 3,
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
            "Ingrédient Arme Niveau 10-15": 5,
            "Ingrédient Potion Niveau 10-15": 2
        },
        "effets": {},
        "stats": {
            "degats_base": 15,
            "bonus_defense": None,
            "bonus_force": 6,
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
            "Ingrédient Arme Niveau 15-20": 5,
            "Ingrédient Potion Niveau 15-20": 2
        },
        "effets": {},
        "stats": {
            "degats_base": 28,
            "bonus_defense": None,
            "bonus_force": 12,
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
            "Ingrédient Arme Niveau 15-20": 5,
            "Ingrédient Potion Niveau 15-20": 2
        },
        "effets": {},
        "stats": {
            "degats_base": 45,
            "bonus_defense": None,
            "bonus_force": 20,
            "bonus_agilite": None,
            "bonus_vitalite": None,
            "bonus_intelligence": None
        },
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une épée légendaire d'origine divine."
    }
}

# ============================================================================
# ARMURES - TORSE
# ============================================================================

RECETTES_ARMURES_TORSE = {
    "armure_cuir_commun": {
        "nom": "Armure de Cuir",
        "type": "armure",
        "sous_type": "torse",
        "rarete": "Commun",
        "ingredients": {
            "Ingrédient Armure Niveau 1-5": 5,
            "Ingrédient Arme Niveau 1-5": 2
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": 3,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": 1,
            "bonus_intelligence": None
        },
        "prix_vente": 100,
        "niveau_craft_requis": 1,
        "description": "Une armure basique en cuir."
    },
    "armure_cuir_renforce_peu_commun": {
        "nom": "Armure de Cuir Renforcé",
        "type": "armure",
        "sous_type": "torse",
        "rarete": "Peu Commun",
        "ingredients": {
            "Ingrédient Armure Niveau 5-10": 5,
            "Ingrédient Arme Niveau 5-10": 2
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": 8,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": 3,
            "bonus_intelligence": None
        },
        "prix_vente": 300,
        "niveau_craft_requis": 2,
        "description": "Une armure améliorée en cuir renforcé."
    },
    "armure_mithril_rare": {
        "nom": "Armure de Mithril",
        "type": "armure",
        "sous_type": "torse",
        "rarete": "Rare",
        "ingredients": {
            "Ingrédient Arme Niveau 10-15": 5,
            "Ingrédient Potion Niveau 10-15": 2
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": 15,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": 6,
            "bonus_intelligence": None
        },
        "prix_vente": 600,
        "niveau_craft_requis": 3,
        "description": "Une armure rare en mithril."
    },
    "armure_adamantium_epique": {
        "nom": "Armure d'Adamantium",
        "type": "armure",
        "sous_type": "torse",
        "rarete": "Épique",
        "ingredients": {
            "Ingrédient Arme Niveau 15-20": 5,
            "Ingrédient Potion Niveau 15-20": 2
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": 28,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": 12,
            "bonus_intelligence": None
        },
        "prix_vente": 1200,
        "niveau_craft_requis": 5,
        "description": "Une armure épique en adamantium."
    },
    "armure_divine_legendaire": {
        "nom": "Armure Divine",
        "type": "armure",
        "sous_type": "torse",
        "rarete": "Légendaire",
        "ingredients": {
            "Ingrédient Arme Niveau 15-20": 5,
            "Ingrédient Potion Niveau 15-20": 2
        },
        "effets": {},
        "stats": {
            "degats_base": None,
            "bonus_defense": 45,
            "bonus_force": None,
            "bonus_agilite": None,
            "bonus_vitalite": 20,
            "bonus_intelligence": None
        },
        "prix_vente": 3000,
        "niveau_craft_requis": 10,
        "description": "Une armure légendaire d'origine divine."
    }
}

# ============================================================================
# REGROUPEMENT DE TOUTES LES RECETTES
# ============================================================================

TOUTES_LES_RECETTES: Dict[str, Dict] = {}
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_SOIN)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_MANA)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_ENERGIE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_FORCE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_DEFENSE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_VITESSE)
TOUTES_LES_RECETTES.update(RECETTES_POTIONS_BOOST_CRITIQUE)
TOUTES_LES_RECETTES.update(RECETTES_ARMES_EPEES)
TOUTES_LES_RECETTES.update(RECETTES_ARMURES_TORSE)

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def obtenir_recette(id_recette: str) -> Optional[Dict]:
    """
    Obtient une recette par son ID.

    :param id_recette: ID de la recette
    :return: Dictionnaire de la recette ou None si non trouvée
    """
    return TOUTES_LES_RECETTES.get(id_recette)


def obtenir_recettes_par_type(type_recette: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'un type donné.

    :param type_recette: Type de recette ("potion", "arme", "armure")
    :return: Liste des recettes du type demandé
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("type") == type_recette
    ]


def obtenir_recettes_par_sous_type(sous_type: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'un sous-type donné.

    :param sous_type: Sous-type de recette (ex: "soin", "mana", "epee", "torse")
    :return: Liste des recettes du sous-type demandé
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("sous_type") == sous_type
    ]


def obtenir_recettes_par_rarete(rarete: str) -> List[Dict]:
    """
    Obtient toutes les recettes d'une rareté donnée.

    :param rarete: Rareté ("Commun", "Peu Commun", "Rare", "Épique", "Légendaire")
    :return: Liste des recettes de la rareté demandée
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("rarete") == rarete
    ]


def obtenir_recettes_disponibles(niveau_craft: int = 1) -> List[Dict]:
    """
    Obtient toutes les recettes disponibles pour un niveau de craft donné.

    :param niveau_craft: Niveau de craft du joueur
    :return: Liste des recettes accessibles
    """
    return [
        recette for recette in TOUTES_LES_RECETTES.values()
        if recette.get("niveau_craft_requis", 1) <= niveau_craft
    ]
