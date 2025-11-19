# data/objets.py
# Définitions des Objets et Recettes de Crafting

DEFINITIONS_OBJETS = {
    # Matériaux de base (loot des ennemis)
    "petite_bourse": {
        "nom": "Petite bourse",
        "type": "matériau",
        "description": "Une petite bourse en cuir contenant quelques pièces. Peut être utilisée pour le crafting.",
        "rarete": "commun"
    },
    "peau_de_gobelin": {
        "nom": "Peau de gobelin",
        "type": "matériau",
        "description": "Une peau tannée de gobelin. Matériau de base pour le crafting d'armures légères.",
        "rarete": "commun"
    },
    "hache_rouillee": {
        "nom": "Hache rouillée",
        "type": "matériau",
        "description": "Une vieille hache couverte de rouille. Peut être fondue pour récupérer du métal.",
        "rarete": "commun"
    },
    "dent_d_orc": {
        "nom": "Dent d'orc",
        "type": "matériau",
        "description": "Une dent d'orc, souvent utilisée comme composant dans les potions ou les amulettes.",
        "rarete": "commun"
    },
    "talisman_chamanique": {
        "nom": "Talisman chamanique",
        "type": "matériau",
        "description": "Un talisman chargé d'énergie mystique. Composant précieux pour les objets magiques.",
        "rarete": "rare"
    },
    "herbes_mysterieuses": {
        "nom": "Herbes mystérieuses",
        "type": "matériau",
        "description": "Des herbes aux propriétés magiques inconnues. Essentielles pour la préparation de potions.",
        "rarete": "commun"
    },

    # Potions (exemples pour le futur)
    "potion_de_vie_mineure": {
        "nom": "Potion de Vie Mineure",
        "type": "potion",
        "description": "Restaure 50 points de vie.",
        "rarete": "commun",
        "effet_vie": 50
    },
    "potion_de_mana_mineure": {
        "nom": "Potion de Mana Mineure",
        "type": "potion",
        "description": "Restaure 30 points de mana.",
        "rarete": "commun",
        "effet_mana": 30
    },

    # Équipements (exemples pour le futur)
    "casque_en_cuir": {
        "nom": "Casque en Cuir",
        "type": "équipement",
        "description": "Un casque simple en cuir. Augmente légèrement la défense.",
        "rarete": "commun",
        "bonus_defense": 2
    },

    # Consommables (exemples pour le futur)
    "pierre_de_forge": {
        "nom": "Pierre de Forge",
        "type": "consommable",
        "description": "Une pierre magique utilisée pour améliorer les équipements.",
        "rarete": "rare"
    }
}

# --- Structure pour les Recettes de Crafting ---
# Structure extensible pour définir les recettes de crafting
# Format : {
#     "id_recette": {
#         "nom": "Nom de l'objet créé",
#         "type_resultat": "matériau" | "potion" | "équipement" | "consommable",
#         "ingredients": {
#             "nom_objet_1": quantite_requise,
#             "nom_objet_2": quantite_requise,
#             ...
#         },
#         "niveau_requis": niveau_minimum_pour_crafter (optionnel),
#         "description": "Description de la recette"
#     }
# }

RECETTES_CRAFTING = {
    # Exemples de recettes (à implémenter plus tard)
    # "potion_vie_basique": {
    #     "nom": "Potion de Vie Basique",
    #     "type_resultat": "potion",
    #     "ingredients": {
    #         "herbes_mysterieuses": 2,
    #         "petite_bourse": 1
    #     },
    #     "niveau_requis": 1,
    #     "description": "Crée une potion de vie basique à partir d'herbes et d'une bourse."
    # },
    # "armure_cuir_gobelin": {
    #     "nom": "Armure en Cuir de Gobelin",
    #     "type_resultat": "équipement",
    #     "ingredients": {
    #         "peau_de_gobelin": 5,
    #         "dent_d_orc": 2
    #     },
    #     "niveau_requis": 3,
    #     "description": "Crée une armure légère à partir de peaux de gobelin."
    # }
}
