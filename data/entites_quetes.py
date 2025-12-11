# data/entites_quetes.py
# Définitions des ennemis, objets et entités spéciales pour les quêtes

# ==================== ENNEMIS SPÉCIAUX POUR LES QUÊTES ====================

ENNEMIS_QUETES = {
    # Agents de l'Ordre des Ombres Éternelles
    "agent_ordre": {
        "nom": "Agent de l'Ordre",
        "vie_max": 80,
        "vitesse": 15,
        "attaque": 25,
        "defense": 10,
        "chance_critique": 8,
        "xp_a_donner": 100,
        "or_a_donner": 150,
        "loot_table": [
            {"nom": "symbole_ombre", "chance": 30},
            {"nom": "journal_agent", "chance": 15}
        ],
    },

    # Créatures corrompues par l'Ordre
    "creature_corrompue": {
        "nom": "Créature Corrompue",
        "vie_max": 120,
        "vitesse": 12,
        "attaque": 30,
        "defense": 15,
        "chance_critique": 5,
        "xp_a_donner": 150,
        "or_a_donner": 200,
        "loot_table": [
            {"nom": "symbole_ombre", "chance": 25}
        ],
    },

    # Créatures des mines (Khazak-Dûm)
    "creature_mine": {
        "nom": "Créature des Mines",
        "vie_max": 100,
        "vitesse": 10,
        "attaque": 20,
        "defense": 12,
        "chance_critique": 4,
        "xp_a_donner": 80,
        "or_a_donner": 120,
        "loot_table": [],
    },

    # Brigands organisés (Luthesia)
    "brigand": {
        "nom": "Brigand Organisé",
        "vie_max": 70,
        "vitesse": 18,
        "attaque": 22,
        "defense": 8,
        "chance_critique": 10,
        "xp_a_donner": 90,
        "or_a_donner": 130,
        "loot_table": [
            {"nom": "document_brigand", "chance": 20}
        ],
    },

    # Serviteurs corrompus (Vrak'thar)
    "serviteur_corrompu": {
        "nom": "Serviteur Corrompu",
        "vie_max": 110,
        "vitesse": 14,
        "attaque": 28,
        "defense": 12,
        "chance_critique": 6,
        "xp_a_donner": 140,
        "or_a_donner": 180,
        "loot_table": [
            {"nom": "rune_ancienne", "chance": 30}
        ],
    },

    # Serviteurs de Zarthos (combat final)
    "serviteur_zarathos": {
        "nom": "Serviteur de Zarthos",
        "vie_max": 200,
        "vitesse": 20,
        "attaque": 40,
        "defense": 20,
        "chance_critique": 12,
        "xp_a_donner": 300,
        "or_a_donner": 500,
        "loot_table": [
            {"nom": "renforcement_sceaux", "chance": 10}
        ],
    },

    # Chef de l'Ordre (boss final)
    "chef_ordre": {
        "nom": "Le Chef de l'Ordre",
        "vie_max": 500,
        "vitesse": 25,
        "attaque": 60,
        "defense": 30,
        "chance_critique": 15,
        "xp_a_donner": 1000,
        "or_a_donner": 2000,
        "loot_table": [
            {"nom": "Artefact_Legendaire", "chance": 100}
        ],
    },
}

# ==================== OBJETS SPÉCIAUX POUR LES QUÊTES ====================

OBJETS_QUETES = {
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
