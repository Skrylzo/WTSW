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
    },

    # ==================== OBJETS SPÉCIAUX POUR LES QUÊTES ====================
    # Symboles et indices de l'Ordre
    "symbole_ombre": {
        "nom": "Symbole de l'Ombre",
        "type": "matériau",
        "description": "Un symbole étrange gravé représentant des ombres entrelacées. L'emblème de l'Ordre des Ombres Éternelles.",
        "rarete": "rare"
    },

    "symbole_ordre": {
        "nom": "Symbole de l'Ordre",
        "type": "matériau",
        "description": "Un symbole mystérieux trouvé sur des objets volés. Preuve de l'activité de l'Ordre.",
        "rarete": "rare"
    },

    "journal_agent": {
        "nom": "Journal d'un Agent",
        "type": "matériau",
        "description": "Le journal d'un agent de l'Ordre, révélant des informations sur leurs plans.",
        "rarete": "épique"
    },

    # Documents et preuves
    "document_ordre": {
        "nom": "Document de l'Ordre",
        "type": "matériau",
        "description": "Un document secret de l'Ordre révélant leurs objectifs.",
        "rarete": "épique"
    },

    "document_brigand": {
        "nom": "Document sur les Brigands",
        "type": "matériau",
        "description": "Des documents révélant l'organisation anormale des brigands.",
        "rarete": "rare"
    },

    "document_krathos": {
        "nom": "Document sur l'Ancien Roi Démon",
        "type": "matériau",
        "description": "Des documents anciens révélant l'histoire de l'ancien Roi Démon.",
        "rarete": "épique"
    },

    "document_helios": {
        "nom": "Document sur Hélios",
        "type": "matériau",
        "description": "Des fragments de l'histoire d'Hélios le Premier.",
        "rarete": "rare"
    },

    "preuve_trahison": {
        "nom": "Preuve de Trahison",
        "type": "matériau",
        "description": "Une preuve irréfutable de la trahison d'un haut dignitaire.",
        "rarete": "légendaire"
    },

    "preuve_corruption": {
        "nom": "Preuve de Corruption",
        "type": "matériau",
        "description": "Des preuves de corruption par l'Ordre.",
        "rarete": "légendaire"
    },

    "preuve_trahison_luthesia": {
        "nom": "Preuve de Trahison (Luthesia)",
        "type": "matériau",
        "description": "Une preuve de trahison à la cour de Luthesia.",
        "rarete": "légendaire"
    },

    "preuve_trahison_vrakthar": {
        "nom": "Preuve de Trahison (Vrak'thar)",
        "type": "matériau",
        "description": "Une preuve de trahison parmi les démons.",
        "rarete": "légendaire"
    },

    # Plans et secrets
    "plans_anciens": {
        "nom": "Plans Anciens",
        "type": "matériau",
        "description": "Des plans d'ingénierie anciens volés par l'Ordre.",
        "rarete": "épique"
    },

    "plans_forgeage": {
        "nom": "Plans de Forgeage",
        "type": "matériau",
        "description": "Des plans de forgeage secrets de Durin.",
        "rarete": "légendaire"
    },

    # Reliques sacrées
    "relique_aerion": {
        "nom": "Relique d'Aerion",
        "type": "équipement",
        "description": "L'âme d'Aerion l'Ancien scellée dans un cristal de lune pur.",
        "rarete": "légendaire"
    },

    "relique_durin": {
        "nom": "Relique de Durin",
        "type": "équipement",
        "description": "L'âme de Durin le Fondateur scellée dans une gemme de forge.",
        "rarete": "légendaire"
    },

    "relique_helios": {
        "nom": "Relique d'Hélios",
        "type": "équipement",
        "description": "L'âme d'Hélios le Premier scellée dans une épée sacrée.",
        "rarete": "légendaire"
    },

    "relique_krathos": {
        "nom": "Relique de l'Ancien Roi Démon",
        "type": "équipement",
        "description": "L'âme de l'ancien Roi Démon scellée dans une rune de feu ancienne.",
        "rarete": "légendaire"
    },

    "renforcement_sceaux": {
        "nom": "Renforcement des Sceaux",
        "type": "matériau",
        "description": "Un artefact permettant de renforcer les sceaux de Zarthos.",
        "rarete": "légendaire"
    },

    # Fragments et artefacts
    "fragment_memoire": {
        "nom": "Fragment de Mémoire",
        "type": "matériau",
        "description": "Un fragment de mémoire d'un esprit ancien.",
        "rarete": "rare"
    },

    "cristal_resonnant": {
        "nom": "Cristal Résonnant",
        "type": "matériau",
        "description": "Un cristal ancien qui résonne d'énergie magique.",
        "rarete": "rare"
    },

    "parchemin_durin": {
        "nom": "Parchemin sur Durin",
        "type": "matériau",
        "description": "Un ancien parchemin racontant la légende de Durin.",
        "rarete": "rare"
    },

    "rune_ancienne": {
        "nom": "Rune Ancienne",
        "type": "matériau",
        "description": "Une rune écrite dans la langue oubliée des anciens démons.",
        "rarete": "rare"
    },

    "runes_dechiffrees": {
        "nom": "Runes Déchiffrées",
        "type": "matériau",
        "description": "Des runes anciennes déchiffrées révélant des secrets.",
        "rarete": "épique"
    },

    "fragment_sagesse": {
        "nom": "Fragment de Sagesse",
        "type": "matériau",
        "description": "Un fragment de la sagesse de l'ancien Roi Démon.",
        "rarete": "épique"
    },

    # Équipements spéciaux
    "epee_chevalier": {
        "nom": "Épée du Chevalier",
        "type": "équipement",
        "description": "L'épée d'un ancien chevalier qui servit Hélios.",
        "rarete": "épique"
    },

    "Epee_Chevalier_Ancien": {
        "nom": "Épée du Chevalier Ancien",
        "type": "équipement",
        "description": "Une épée légendaire d'un chevalier oublié.",
        "rarete": "légendaire"
    },

    "Artefact_Legendaire": {
        "nom": "Artefact Légendaire",
        "type": "équipement",
        "description": "Un artefact légendaire obtenu après avoir empêché la résurrection de Zarthos.",
        "rarete": "légendaire"
    },

    "Recette_Arme_Legendaire": {
        "nom": "Recette d'Arme Légendaire",
        "type": "matériau",
        "description": "Une recette secrète pour forger une arme légendaire.",
        "rarete": "légendaire"
    },

    # Clés de donjons
    "cle_donjon_aerthos_1": {
        "nom": "Clé du Sanctuaire des Murmures",
        "type": "cle_donjon",
        "description": "Une clé ancienne permettant d'accéder au Sanctuaire des Murmures Oubliés.",
        "rarete": "rare"
    },
    "cle_donjon_aerthos_2": {
        "nom": "Clé du Cœur Corrompu",
        "type": "cle_donjon",
        "description": "Une clé sombre permettant d'accéder au Cœur Corrompu de la Forêt.",
        "rarete": "épique"
    },
    "cle_donjon_khazak_1": {
        "nom": "Clé de la Redoute d'Obscurité",
        "type": "cle_donjon",
        "description": "Une clé runique permettant d'accéder à la Redoute d'Obscurité.",
        "rarete": "rare"
    },
    "cle_donjon_khazak_2": {
        "nom": "Clé du Caveau des Secrets",
        "type": "cle_donjon",
        "description": "Une clé ancienne permettant d'accéder au Caveau des Secrets du Premier Âge.",
        "rarete": "épique"
    },
    "cle_donjon_luthesia_1": {
        "nom": "Clé de l'Observatoire des Astres",
        "type": "cle_donjon",
        "description": "Une clé céleste permettant d'accéder à l'Observatoire des Astres.",
        "rarete": "rare"
    },
    "cle_donjon_vrakthar_1": {
        "nom": "Clé du Sanctuaire des Flammes",
        "type": "cle_donjon",
        "description": "Une clé de feu permettant d'accéder au Sanctuaire des Flammes Éternelles.",
        "rarete": "rare"
    },
    "cle_donjon_vrakthar_2": {
        "nom": "Clé du Cœur des Flammes",
        "type": "cle_donjon",
        "description": "Une clé corrompue permettant d'accéder au Cœur des Flammes Corrompues.",
        "rarete": "épique"
    },
    "cle_donjon_vrakthar_3": {
        "nom": "Clé du Mausolée des Géants",
        "type": "cle_donjon",
        "description": "Une clé ancienne permettant d'accéder au Mausolée des Géants Brisés.",
        "rarete": "rare"
    },
    "cle_donjon_vrakthar_4": {
        "nom": "Clé des Entrailles Mutantes",
        "type": "cle_donjon",
        "description": "Une clé mutante permettant d'accéder aux Entrailles Mutantes.",
        "rarete": "rare"
    },
    "cle_donjon_vrakthar_5": {
        "nom": "Clé des Archives de la Mémoire",
        "type": "cle_donjon",
        "description": "Une clé fragmentée permettant d'accéder aux Archives de la Mémoire Fracturée.",
        "rarete": "épique"
    },
    "cle_donjon_vrakthar_6": {
        "nom": "Clé de la Gueule de l'Oubli",
        "type": "cle_donjon",
        "description": "Une clé oubliée permettant d'accéder à la Gueule de l'Oubli.",
        "rarete": "épique"
    },
    "cle_donjon_final": {
        "nom": "Clé du Sanctuaire des Ombres",
        "type": "cle_donjon",
        "description": "Une clé légendaire permettant d'accéder au Sanctuaire des Ombres Éternelles.",
        "rarete": "légendaire"
    },

    # Reliques de récompense (mentionnées dans les quêtes)
    "Cristal_de_Lune_Pur": {
        "nom": "Cristal de Lune Pur",
        "type": "équipement",
        "description": "Un cristal de lune purifié, fragment de la relique d'Aerion.",
        "rarete": "légendaire"
    },

    "Gemme_de_Forge": {
        "nom": "Gemme de Forge",
        "type": "équipement",
        "description": "Une gemme de forge sacrée, fragment de la relique de Durin.",
        "rarete": "légendaire"
    },

    "Epee_Sacree": {
        "nom": "Épée Sacrée",
        "type": "équipement",
        "description": "Une épée sacrée, fragment de la relique d'Hélios.",
        "rarete": "légendaire"
    },

    "Rune_de_Feu_Ancienne": {
        "nom": "Rune de Feu Ancienne",
        "type": "équipement",
        "description": "Une rune de feu ancienne, fragment de la relique de l'ancien Roi Démon.",
        "rarete": "légendaire"
    },
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
