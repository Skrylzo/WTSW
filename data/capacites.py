# data/capacites.py
# Définition de toutes les capacités du jeu

# --- Définition de toutes les capacités du jeu ---
# Chaque capacité a un ID unique, un nom, une description, un type de cible, des coûts, et un effet/dégâts/soin.
# Les capacités des Rageborn auront un 'cout_rage' au lieu de 'cout_energie'.

TOUTES_LES_CAPACITES_DATA = {
    "frappe_sanglante": {
        "nom": "Frappe Sanglante", "description": "Inflige des dégâts physiques et régénère un peu de vie.",
        "cout_energie": 15, "degats_fixes": 15, "soin_fixe": 5, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "vol_d_ame": {
        "nom": "Vol d'Âme", "description": "Draine la vie d'un ennemi, infligeant des dégâts et vous soignant.",
        "cout_energie": 35, "degats_fixes": 25, "soin_fixe": 15, "type_cible": "unique", "niveau_requis": 5, "peut_critiquer": True
    },
    "hurlement_terrifiant": {
        "nom": "Hurlement Terrifiant", "description": "Terrifie les ennemis proches, réduisant leur attaque.",
        "cout_energie": 40, "type_cible": "aoe", "effet_data": {"nom": "Terreur", "description": "Attaque réduite de 20%", "duree": 2, "effet_attaque": -20}, "niveau_requis": 10
    },
    "chair_corrompue": {
        "nom": "Chair Corrompue", "description": "Vous rend temporairement plus résistant, au coût de votre vie actuelle.",
        "cout_energie": 20, "type_cible": "soi", "effet_data": {"nom": "Résistance Corrompue", "description": "Défense augmentée de 30", "duree": 2, "effet_defense": 30},
        "soin_fixe": -0.10, "niveau_requis": 15
    },
    "festin_d_ames": {
        "nom": "Festin d'Âmes", "description": "Consomme les âmes ennemies pour infliger d'énormes dégâts de zone et vous soigner massivement.",
        "cout_energie": 90, "degats_fixes": 75, "soin_fixe": 50, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    },

    "malediction_affaiblissement": {
        "nom": "Malédiction d'Affaiblissement", "description": "Affaiblit un ennemi, réduisant son attaque.",
        "cout_mana": 20, "type_cible": "unique", "effet_data": {"nom": "Affaiblissement", "description": "Attaque réduite de 15%", "duree": 3, "effet_attaque": -15}, "niveau_requis": 1
    },
    "toucher_corrupteur": {
        "nom": "Toucher Corrupteur", "description": "Inflige des dégâts de ténèbres et applique un effet de poison.",
        "cout_mana": 30, "degats_fixes": 10, "type_cible": "unique", "effet_data": {"nom": "Poison", "description": "Subit 5 dégâts par tour", "duree": 3, "effet_vie": -5, "condition": "tour"}, "niveau_requis": 5, "peut_critiquer": True
    },
    "voile_des_tenebres": {
        "nom": "Voile des Ténèbres", "description": "Vous enveloppe d'un voile protecteur, augmentant votre défense.",
        "cout_mana": 35, "type_cible": "soi", "effet_data": {"nom": "Voile Protecteur", "description": "Défense augmentée de 25", "duree": 2, "effet_defense": 25}, "niveau_requis": 10
    },
    "drain_essence": {
        "nom": "Drain d'Essence", "description": "Draine le mana d'un ennemi pour recharger le vôtre.",
        "cout_mana": 10, "degats_fixes": 5, "type_cible": "unique", "effet_data": {"nom": "Drain Mana", "description": "Vol de 10 Mana", "duree": 1, "effet_regen_mana": 10}, "niveau_requis": 15, "peut_critiquer": True
    },
    "pestilence_demoniaque": {
        "nom": "Pestilence Démoniaque", "description": "Déchaîne une épidémie qui inflige de lourds dégâts de zone et des dégâts sur la durée.",
        "cout_mana": 75, "degats_fixes": 50, "effet_data": {"nom": "Pestilence", "description": "Subit 10 dégâts par tour", "duree": 4, "effet_vie": -10, "condition": "tour"}, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    },

    "lame_incandescente": {
        "nom": "Lame Incandescente", "description": "Votre arme s'embrase. Inflige des dégâts physiques et de feu à un ennemi unique. Chance accrue de coup critique si vie < 50%.",
        "cout_energie": 12, "degats_fixes": 20, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "souffle_de_fournaise": {
        "nom": "Souffle de Fournaise", "description": "Crache un jet de flammes ardentes, infligeant des dégâts de zone et brûlant les ennemis.",
        "cout_energie": 28, "degats_fixes": 15, "effet_data": {"nom": "Brûlure", "description": "Subit 8 dégâts de feu par tour", "duree": 2, "effet_vie": -8, "condition": "tour"}, "type_cible": "aoe", "niveau_requis": 5, "peut_critiquer": True
    },
    "coeur_de_cendres": {
        "nom": "Cœur de Cendres", "description": "Consomme une partie de votre vie (10% actuelle) pour augmenter massivement votre Attaque et Défense.",
        "cout_energie": 38, "type_cible": "soi", "effet_data": {"nom": "Brasier de Destruction", "description": "Attaque +40, Défense +20", "duree": 2, "effet_attaque": 40, "effet_defense": 20},
        "soin_fixe": -0.10, "niveau_requis": 10
    },
    "ruee_cendree": {
        "nom": "Ruée Cendrée", "description": "Transforme en jet de braises, inflige de gros dégâts physiques et laisse une flaque ralentissante et brûlante.",
        "cout_energie": 20, "degats_fixes": 30, "type_cible": "unique", "effet_data": {"nom": "Cendres Ardentes", "description": "Ralenti, subit 5 dégâts de feu par tour", "duree": 1, "effet_vitesse": -10, "effet_vie": -5, "condition": "tour"}, "niveau_requis": 15, "peut_critiquer": True
    },
    "reincarnation_flamboyante": {
        "nom": "Réincarnation Flamboyante", "description": "Si dégâts mortels, explose, renaît avec 50% vie et bonus temporaire Attaque/Vitesse (une fois par combat).",
        "cout_energie": 90, "type_cible": "soi", "effet_data": {"nom": "Renaissance Ardente", "description": "Renaît avec 50% vie, Attaque +50, Vitesse +30", "duree": 1, "effet_attaque": 50, "effet_vitesse": 30, "condition": "mort_imminente"}, "niveau_requis": 20
    },

    "chatiment_sacre": {
        "nom": "Châtiment Sacré", "description": "Inflige des dégâts sacrés à un ennemi unique.",
        "cout_mana": 18, "degats_fixes": 20, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "protection_divine": {
        "nom": "Protection Divine", "description": "Augmente votre défense et vous rend plus résistant.",
        "cout_mana": 25, "type_cible": "soi", "effet_data": {"nom": "Bénédiction Divine", "description": "Défense augmentée de 20", "duree": 2, "effet_defense": 20}, "niveau_requis": 5
    },
    "lumiere_guerisseuse": {
        "nom": "Lumière Guérisseuse", "description": "Restaure une partie de votre vie.",
        "cout_mana": 30, "soin_fixe": 40, "type_cible": "soi", "niveau_requis": 10
    },
    "marteau_de_justice": {
        "nom": "Marteau de Justice", "description": "Lance un marteau qui étourdit et inflige des dégâts à un ennemi.",
        "cout_mana": 40, "degats_fixes": 30, "type_cible": "unique", "effet_data": {"nom": "Étourdissement", "description": "Cible ne peut pas agir", "duree": 1, "condition": "etourdi"}, "niveau_requis": 15, "peut_critiquer": True
    },
    "jugement_dernier": {
        "nom": "Jugement Dernier", "description": "Frappe tous les ennemis avec la fureur divine, infligeant d'énormes dégâts sacrés.",
        "cout_mana": 75, "degats_fixes": 80, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    },

    "invocation_mineure": {
        "nom": "Invocation Mineure", "description": "Invoque une petite créature pour combattre à vos côtés. Augmente temporairement votre attaque.",
        "cout_mana": 20, "type_cible": "soi", "effet_data": {"nom": "Esprit Combattant", "description": "Attaque augmentée de 12 grâce à l'invocation", "duree": 3, "effet_attaque": 12}, "niveau_requis": 1
    },
    "lien_ethere": {
        "nom": "Lien Éthéré", "description": "Partage une partie des dégâts subis par votre invocation avec l'ennemi. Réduit les dégâts reçus.",
        "cout_mana": 15, "type_cible": "soi", "effet_data": {"nom": "Lien Protecteur", "description": "Défense augmentée de 15 grâce au lien", "duree": 2, "effet_defense": 15}, "niveau_requis": 5
    },
    "transfert_douleur": {
        "nom": "Transfert de Douleur", "description": "Transfère une partie des dégâts que vous subissez à votre invocation. Réduit les dégâts reçus.",
        "cout_mana": 25, "type_cible": "soi", "effet_data": {"nom": "Transfert Actif", "description": "Défense augmentée de 20 grâce au transfert", "duree": 2, "effet_defense": 20}, "niveau_requis": 10
    },
    "invocation_majeure": {
        "nom": "Invocation Majeure", "description": "Invoque une créature plus puissante pour vous assister. Augmente temporairement votre attaque et défense.",
        "cout_mana": 40, "type_cible": "soi", "effet_data": {"nom": "Esprit Puissant", "description": "Attaque +25, Défense +20 grâce à l'invocation", "duree": 4, "effet_attaque": 25, "effet_defense": 20}, "niveau_requis": 15
    },
    "essaim_demoniaque": {
        "nom": "Essaim Démoniaque", "description": "Déchaîne un essaim de démons mineurs qui attaquent tous les ennemis.",
        "cout_mana": 80, "degats_fixes": 60, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    },

    "assaut_eclair": {
        "nom": "Assaut Éclair", "description": "Porte une série de coups rapides et précis à un ennemi unique, avec une chance accrue de coup critique.",
        "cout_energie": 12, "degats_fixes": 18, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "feinte_riposte": {
        "nom": "Feinte et Riposte", "description": "Augmente votre chance d'esquive pour le prochain tour. Si vous esquivez, vous contre-attaquez.",
        "cout_energie": 30, "type_cible": "soi", "effet_data": {"nom": "Position Évasive", "description": "Chance d'esquive grandement augmentée", "duree": 1}, "niveau_requis": 5
    },
    "danse_des_lames_duelliste": {
        "nom": "Danse des Lames", "description": "Vous entrez dans un état de fluidité martiale, attaquant tous les ennemis proches.",
        "cout_energie": 40, "degats_fixes": 25, "type_cible": "aoe", "niveau_requis": 10, "peut_critiquer": True
    },
    "maitre_de_l_epee": {
        "nom": "Maître de l'Épée", "description": "Maîtrise parfaite de l'arme, augmentant grandement votre attaque et chance critique.",
        "cout_energie": 25, "type_cible": "soi", "effet_data": {"nom": "Maîtrise Aiguisée", "description": "Attaque +25, Chance critique +15%", "duree": 2, "effet_attaque": 25, "effet_critique": 15}, "niveau_requis": 15
    },
    "tourbillon_mortel": {
        "nom": "Tourbillon Mortel", "description": "Une série de frappes tourbillonnantes dévastatrices sur tous les ennemis, avec invulnérabilité temporaire.",
        "cout_energie": 85, "degats_fixes": 70, "type_cible": "aoe", "effet_data": {"nom": "Invulnérabilité", "description": "Invulnérable pendant 1 tour", "duree": 1, "condition": "invulnerable"}, "niveau_requis": 20, "peut_critiquer": True
    },

    "tir_rapide": {
        "nom": "Tir Rapide", "description": "Décoche plusieurs flèches rapidement, infligeant des dégâts modérés.",
        "cout_energie": 12, "degats_fixes": 15, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "fleche_cramoisie": {
        "nom": "Flèche Cramoisie", "description": "Une flèche qui saigne l'ennemi, infligeant des dégâts sur la durée.",
        "cout_energie": 30, "degats_fixes": 10, "type_cible": "unique", "effet_data": {"nom": "Saignement", "description": "Subit 7 dégâts par tour", "duree": 3, "effet_vie": -7, "condition": "tour"}, "niveau_requis": 5, "peut_critiquer": True
    },
    "salve_de_fleches": {
        "nom": "Salve de Flèches", "description": "Tire une volée de flèches sur une zone, blessant plusieurs ennemis.",
        "cout_energie": 40, "degats_fixes": 25, "type_cible": "aoe", "niveau_requis": 10, "peut_critiquer": True
    },
    "piege_a_epine": {
        "nom": "Piège à Épine", "description": "Pose un piège qui immobilise et blesse le premier ennemi qui l'active. Inflige des dégâts immédiats.",
        "cout_energie": 25, "degats_fixes": 28, "type_cible": "unique", "niveau_requis": 15, "peut_critiquer": True
    },
    "pluie_de_fleches": {
        "nom": "Pluie de Flèches", "description": "Fait pleuvoir une nuée de flèches sur une large zone, infligeant des dégâts massifs.",
        "cout_energie": 85, "degats_fixes": 70, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    },

    "lien_spirituel": {
        "nom": "Lien Spirituel", "description": "Forme un lien avec un esprit pour renforcer un allié ou affaiblir un ennemi. Augmente vos stats.",
        "cout_mana": 18, "type_cible": "soi", "effet_data": {"nom": "Lien Spirituel", "description": "Attaque +12, Défense +8 grâce au lien", "duree": 2, "effet_attaque": 12, "effet_defense": 8}, "niveau_requis": 1
    },
    "projection_astrale": {
        "nom": "Projection Astrale", "description": "Projette une forme astrale qui attaque l'ennemi.",
        "cout_mana": 22, "degats_fixes": 20, "type_cible": "unique", "niveau_requis": 5, "peut_critiquer": True
    },
    "danse_des_ames": {
        "nom": "Danse des Âmes", "description": "Libère des esprits dansants qui soignent les alliés proches.",
        "cout_mana": 35, "soin_fixe": 30, "type_cible": "aoe_amis", "niveau_requis": 10
    },
    "bouclier_de_lumiere": {
        "nom": "Bouclier de Lumière", "description": "Crée un bouclier protecteur qui absorbe les dégâts.",
        "cout_mana": 45, "type_cible": "soi", "effet_data": {"nom": "Bouclier Absorbant", "description": "Absorbe 50 dégâts", "duree": 1, "effet_vie": 50}, "niveau_requis": 15
    },
    "sanctuaire_ethere": {
        "nom": "Sanctuaire Éthéré", "description": "Crée une zone sacrée qui soigne continuellement les alliés et blesse les ennemis.",
        "cout_mana": 70, "soin_fixe": 10, "degats_fixes": 10, "type_cible": "aoe_mixte", "effet_data": {"nom": "Sanctuaire", "description": "Soigne/blesse de 10 chaque tour", "duree": 3, "condition": "tour"}, "niveau_requis": 20, "peut_critiquer": True
    },

    "frappe_celeste": {
        "nom": "Frappe Céleste", "description": "Décoche une flèche imprégnée de lumière du soleil, infligeant des dégâts physiques et de feu. Laisse une brûlure légère.",
        "cout_energie": 15, "degats_fixes": 15, "type_cible": "unique", "effet_data": {"nom": "Brûlure Légère", "description": "Subit 5 dégâts de feu par tour", "duree": 1, "effet_vie": -5, "condition": "tour"}, "niveau_requis": 1, "peut_critiquer": True
    },
    "lance_solaire": {
        "nom": "Lance Solaire", "description": "Projette un rayon concentré sur un ennemi, infligeant des dégâts de feu importants et réduisant sa Défense.",
        "cout_energie": 35, "degats_fixes": 25, "type_cible": "unique", "effet_data": {"nom": "Défense Réduite", "description": "Défense -15", "duree": 2, "effet_defense": -15}, "niveau_requis": 5, "peut_critiquer": True
    },
    "explosion_radieuse": {
        "nom": "Explosion Radieuse", "description": "Libère une onde de lumière qui vous purifie d'un malus aléatoire et augmente temporairement votre Vitesse.",
        "cout_energie": 45, "type_cible": "soi", "effet_data": {"nom": "Vitesse Accrue", "description": "Vitesse +10", "duree": 1, "effet_vitesse": 10}, "niveau_requis": 10
    },
    "aura_de_guerison": {
        "nom": "Aura de Guérison", "description": "Dégage une aura de lumière qui vous soigne légèrement chaque tour et augmente votre Attaque.",
        "cout_energie": 30, "type_cible": "soi", "effet_data": {"nom": "Aura Radiante", "description": "Soin de 5 par tour, Attaque +15", "duree": 3, "effet_vie": 5, "effet_attaque": 15, "condition": "tour"}, "niveau_requis": 15
    },
    "jugement_celeste": {
        "nom": "Jugement Céleste", "description": "Devient une source de lumière aveuglante. Tous les ennemis subissent de gros dégâts de feu et sont aveuglés. Dégâts de feu bonus et bouclier temporaire.",
        "cout_energie": 95, "degats_fixes": 60, "type_cible": "aoe", "effet_data": {"nom": "Aveuglement", "description": "Chance de rater les attaques", "duree": 1, "effet_critique": -100}, "niveau_requis": 20, "peut_critiquer": True
    },

    "frappe_frenetique": {
        "nom": "Frappe Frénétique", "description": "Une attaque rapide et brutale qui blesse l'ennemi.",
        "cout_rage": 10, "degats_fixes": 18, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "cri_de_guerre": {
        "nom": "Cri de Guerre", "description": "Pousse un cri qui terrifie les ennemis et augmente votre attaque.",
        "cout_rage": 25, "type_cible": "soi", "effet_data": {"nom": "Fureur", "description": "Attaque augmentée de 20", "duree": 2, "effet_attaque": 20}, "niveau_requis": 5
    },
    "tourbillon_de_fureur": {
        "nom": "Tourbillon de Fureur", "description": "Tournoie sur soi-même, frappant tous les ennemis proches.",
        "cout_rage": 35, "degats_fixes": 30, "type_cible": "aoe", "niveau_requis": 10, "peut_critiquer": True
    },
    "soif_de_sang": {
        "nom": "Soif de Sang", "description": "Consomme une partie de votre vie (5% actuelle) pour augmenter considérablement vos dégâts pendant un court instant.",
        "cout_rage": 20, "type_cible": "soi", "effet_data": {"nom": "Rage Sanglante", "description": "Attaque +30", "duree": 1, "effet_attaque": 30},
        "soin_fixe": -0.05, "niveau_requis": 15
    },
    "mode_berserker": {
        "nom": "Mode Berserker", "description": "Entre dans une rage folle, augmentant massivement l'attaque et la vitesse, mais réduisant la défense.",
        "cout_rage": 80, "type_cible": "soi", "effet_data": {"nom": "Berserker", "description": "Attaque +60, Vitesse +30, Défense -20", "duree": 3, "effet_attaque": 60, "effet_vitesse": 30, "effet_defense": -20}, "niveau_requis": 20
    },

    "poing_de_roc": {
        "nom": "Poing de Roc", "description": "Frappe l'ennemi avec un poing renforcé par la roche, infligeant des dégâts physiques.",
        "cout_energie": 10, "degats_fixes": 15, "type_cible": "unique", "niveau_requis": 1, "peut_critiquer": True
    },
    "racine_du_monde": {
        "nom": "Racine du Monde", "description": "Invoque des racines qui étourdissent un ennemi.",
        "cout_energie": 30, "type_cible": "unique", "effet_data": {"nom": "Étourdissement", "description": "Cible étourdie, ne peut pas agir", "duree": 2, "condition": "etourdi"}, "niveau_requis": 5
    },
    "ebranlement_terrestre": {
        "nom": "Ébranlement Terrestre", "description": "Frappe le sol, étourdissant et blessant les ennemis proches.",
        "cout_energie": 40, "degats_fixes": 25, "type_cible": "aoe", "effet_data": {"nom": "Étourdissement", "description": "Cible étourdie", "duree": 1, "condition": "etourdi"}, "niveau_requis": 10, "peut_critiquer": True
    },
    "bastion_du_clan": {
        "nom": "Bastion du Clan", "description": "Crée un bouclier de pierre qui protège tous les alliés.",
        "cout_energie": 50, "type_cible": "aoe_amis", "effet_data": {"nom": "Peau de Pierre", "description": "Défense augmentée de 20", "duree": 2, "effet_defense": 20}, "niveau_requis": 15
    },
    "colosse_de_granite": {
        "nom": "Colosse de Granite", "description": "Se transforme en un puissant colosse de pierre, augmentant massivement la vitalité et la défense.",
        "cout_energie": 90, "type_cible": "soi", "effet_data": {"nom": "Colosse", "description": "Vie Max +100, Défense +50", "duree": 4, "effet_vie": 100, "effet_defense": 50}, "niveau_requis": 20
    },

    "deploiement_tourelle_minotaure": {
        "nom": "Déploiement de Tourelle Minotaure", "description": "Déploie une tourelle qui attaque automatiquement les ennemis. Augmente temporairement votre attaque.",
        "cout_mana": 15, "type_cible": "soi", "effet_data": {"nom": "Tourelle Active", "description": "Attaque augmentée de 12 grâce à la tourelle", "duree": 3, "effet_attaque": 12}, "niveau_requis": 1
    },
    "grenade_fumigene": {
        "nom": "Grenade Fumigène", "description": "Lance une grenade qui ralentit les ennemis et réduit leur précision.",
        "cout_mana": 20, "type_cible": "aoe", "effet_data": {"nom": "Fumée", "description": "Vitesse -15, Précision -10%", "duree": 2, "effet_vitesse": -15}, "niveau_requis": 5
    },
    "champ_repulsif": {
        "nom": "Champ Répulsif", "description": "Crée un champ qui repousse et étourdit les ennemis proches.",
        "cout_mana": 25, "type_cible": "aoe", "effet_data": {"nom": "Repulsion", "description": "Cible étourdie, repoussée", "duree": 1, "condition": "etourdi"}, "niveau_requis": 10
    },
    "rechargement_express": {
        "nom": "Rechargement Express", "description": "Réduit le temps de recharge d'une capacité ou répare une tourelle. Régénère rapidement votre mana.",
        "cout_mana": 10, "type_cible": "soi", "effet_data": {"nom": "Rechargement", "description": "Régénération de mana augmentée", "duree": 1, "effet_regen_mana": 30}, "niveau_requis": 15
    },
    "artillerie_l_ourde": {
        "nom": "Artillerie Lourde", "description": "Déploie un mortier qui inflige de très gros dégâts de zone avec un effet de feu persistant.",
        "cout_mana": 60, "degats_fixes": 50, "effet_data": {"nom": "Feu Persistant", "description": "Subit 10 dégâts de feu par tour", "duree": 3, "effet_vie": -10, "condition": "tour"}, "type_cible": "aoe", "niveau_requis": 20, "peut_critiquer": True
    }
}
