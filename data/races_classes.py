# data/races_classes.py
# Dictionnaire des définitions des races et de leurs spécialisations associées

DEFINITIONS_RACES_CLASSES = {
    "Humain": {
        "description": "Les Humains sont des êtres polyvalents, capables de s'adapter à de nombreux rôles.",
        "classes": {
            "Paladin": {
                "description": "Un combattant divin qui manie l'épée et la magie sacrée. Excellente défense et capacités de soin.",
                "stats_depart": {"force": 3, "agilite": 2, "vitalite": 7, "intelligence": 8},
                "capacites_ids": ["chatiment_sacre", "protection_divine", "lumiere_guerisseuse", "marteau_de_justice", "jugement_dernier"],
                "type_ressource": "Mana"
            },
            "Invocateur": {
                "description": "Maître des arts arcaniques, l'Invocateur conjure des créatures et lance des sorts puissants.",
                "stats_depart": {"force": 2, "agilite": 3, "vitalite": 7, "intelligence": 8},
                "capacites_ids": ["invocation_mineure", "lien_ethere", "transfert_douleur", "invocation_majeure", "essaim_demoniaque"],
                "type_ressource": "Mana"
            },
            "Duelliste": {
                "description": "Un maître de l'épée, rapide et précis, qui exploite les faiblesses de ses ennemis.",
                "stats_depart": {"force": 7, "agilite": 8, "vitalite": 3, "intelligence": 2},
                "capacites_ids": ["assaut_eclair", "feinte_riposte", "danse_des_lames_duelliste", "maitre_de_l_epee", "tourbillon_mortel"],
                "type_ressource": "Energie"
            }
        }
    },
    "Démon": {
        "description": "Les Démons sont des êtres de puissance brute, capables de drainer la vie ou de corrompre leurs ennemis.",
        "classes": {
            "Dévoreur d'Âme": {
                "description": "Un démon qui se nourrit de la vie de ses ennemis pour se renforcer.",
                "stats_depart": {"force": 8, "agilite": 3, "vitalite": 7, "intelligence": 2},
                "capacites_ids": ["frappe_sanglante", "vol_d_ame", "hurlement_terrifiant", "chair_corrompue", "festin_d_ames"],
                "type_ressource": "Energie"
            },
            "Corrupteur": {
                "description": "Un lanceur de sorts démoniaque qui inflige des malédictions et des dégâts sur la durée.",
                "stats_depart": {"force": 2, "agilite": 7, "vitalite": 3, "intelligence": 8},
                "capacites_ids": ["malediction_affaiblissement", "toucher_corrupteur", "voile_des_tenebres", "drain_essence", "pestilence_demoniaque"],
                "type_ressource": "Mana"
            },
            "Cendrelame": {
                "description": "Un démon guerrier maniant des flammes infernales, spécialisé dans les dégâts de zone.",
                "stats_depart": {"force": 7, "agilite": 8, "vitalite": 3, "intelligence": 2},
                "capacites_ids": ["lame_incandescente", "souffle_de_fournaise", "coeur_de_cendres", "ruee_cendree", "reincarnation_flamboyante"],
                "type_ressource": "Energie"
            }
        }
    },
    "Elfe": {
        "description": "Agiles et en harmonie avec la nature, les Elfes sont d'excellents archers ou des mages sylvestres.",
        "classes": {
            "Archer Sylvestre": {
                "description": "Un maître archer qui chasse ses proies avec une précision mortelle et des pièges.",
                "stats_depart": {"force": 7, "agilite": 8, "vitalite": 3, "intelligence": 2},
                "capacites_ids": ["tir_rapide", "fleche_cramoisie", "salve_de_fleches", "piege_a_epine", "pluie_de_fleches"],
                "type_ressource": "Energie"
            },
            "Sentinelle des Esprits": {
                "description": "Un Elfe qui se connecte aux esprits de la forêt pour lancer des sorts de soutien et d'attaque.",
                "stats_depart": {"force": 2, "agilite": 3, "vitalite": 7, "intelligence": 8},
                "capacites_ids": ["lien_spirituel", "projection_astrale", "danse_des_ames", "bouclier_de_lumiere", "sanctuaire_ethere"],
                "type_ressource": "Mana"
            },
            "Moissonneur d'Aube": {
                "description": "Un Elfe mystique qui canalise l'énergie solaire pour aveugler ses ennemis et guérir ses alliés.",
                "stats_depart": {"force": 8, "agilite": 7, "vitalite": 3, "intelligence": 2},
                "capacites_ids": ["frappe_celeste", "lance_solaire", "explosion_radieuse", "aura_de_guerison", "jugement_celeste"],
                "type_ressource": "Energie"
            }
        }
    },
    "Nain": {
        "description": "Robustes et endurants, les Nains sont des guerriers féroces ou des gardiens inébranlables.",
        "classes": {
            "Rageborn": {
                "description": "Un guerrier qui puise sa force dans la rage, dévastateur en mêlée.",
                "stats_depart": {"force": 8, "agilite": 3, "vitalite": 7, "intelligence": 2},
                "capacites_ids": ["frappe_frenetique", "cri_de_guerre", "tourbillon_de_fureur", "soif_de_sang", "mode_berserker"],
                "type_ressource": "Rage"
            },
            "Marchepierre": {
                "description": "Un nain lié à la terre, capable de manipuler la roche pour se défendre ou attaquer.",
                "stats_depart": {"force": 7, "agilite": 3, "vitalite": 8, "intelligence": 2},
                "capacites_ids": ["poing_de_roc", "racine_du_monde", "ebranlement_terrestre", "bastion_du_clan", "colosse_de_granite"],
                "type_ressource": "Energie"
            },
            "Innovateur Gnomique": {
                "description": "Un esprit brillant qui déploie des inventions mécaniques et des gadgets explosifs.",
                "stats_depart": {"force": 2, "agilite": 3, "vitalite": 7, "intelligence": 8},
                "capacites_ids": ["deploiement_tourelle_minotaure", "grenade_fumigene", "champ_repulsif", "rechargement_express", "artillerie_l_ourde"],
                "type_ressource": "Mana"
            }
        }
    }
}
