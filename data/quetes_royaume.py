# data/quetes_royaume.py
# Quêtes spécifiques à chaque royaume

from world.quetes import Quete, ObjectifQuete, TypeQuete, TypeObjectif

# ==================== AERTHOS (Elfe) ====================

QUETES_AERTHOS = [
    Quete(
        id_quete="aerthos_1_disparitions",
        nom="Les Disparitions Mystérieuses",
        description="""Des elfes ont disparu dans la Forêt de Lumière Argentée. Les Gardiens de la Forêt
sont perplexes - aucune trace, aucun indice. Mais vous avez remarqué des symboles étranges gravés
sur les arbres près des lieux de disparition.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer la Forêt de Lumière Argentée", "Silvanus'Heart", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Collecter 3 symboles suspects", "symbole_ombre", 3),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à Faelar Éternelbranche", "Faelar", 1)
        ],
        recompenses={"xp": 600, "or": 250},
        niveau_requis=1
    ),

    Quete(
        id_quete="aerthos_2_rituel_interrompu",
        nom="Un Rituel Interrompu",
        description="""Vous avez découvert un cercle de pierres où un rituel sombre était en cours.
Les symboles de l'Ordre des Ombres Éternelles sont partout. Il semble qu'ils cherchent quelque chose
dans les profondeurs de la forêt. Vous devez découvrir ce qu'ils convoitent.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Explorer le Sanctuaire des Murmures Oubliés", "Ael'doria", 1),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les agents de l'Ordre", "agent_ordre", 3),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer le journal d'un agent", "journal_agent", 1)
        ],
        recompenses={"xp": 1000, "or": 400},
        prerequis=["aerthos_1_disparitions"],
        niveau_requis=3
    ),

    Quete(
        id_quete="aerthos_3_traison_revelee",
        nom="La Trahison Révélée",
        description="""Le journal révèle une vérité choquante : l'un des Quatre Gardiens est un traître !
L'Ordre a ensorcelé ou corrompu l'un des plus proches conseillers du Roi Aerion. Vous devez découvrir
qui c'est avant qu'il ne soit trop tard.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler aux Quatre Gardiens", "gardien", 4),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver la preuve de la trahison", "preuve_trahison", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Confronter le traître", "traître_aerthos", 1)
        ],
        recompenses={"xp": 1500, "or": 600},
        prerequis=["aerthos_2_rituel_interrompu"],
        niveau_requis=5
    ),

    Quete(
        id_quete="aerthos_4_vol_relique",
        nom="La Relique Volée",
        description="""Le traître a été démasqué ! Mais avant que vous ne puissiez l'arrêter,
il a activé un rituel qui corrompt la forêt et lui a permis de voler la relique contenant
l'âme d'Aerion l'Ancien. Malgré vos efforts, le traître réussit à s'enfuir avec la relique
et à rejoindre l'Ordre des Ombres Éternelles. Vous devez arrêter la corruption qui ravage
la forêt, mais la relique est déjà perdue.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les créatures corrompues", "creature_corrompue", 10),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Arrêter le rituel de corruption", "rituel_corruption", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Informer le Roi Aerion de la perte de la relique", "roi_aerion", 1)
        ],
        recompenses={"xp": 2000, "or": 1000},
        prerequis=["aerthos_3_traison_revelee"],
        niveau_requis=8
    )
]

# ==================== KHAZAK-DÛM (Nain) ====================

QUETES_KHAZAK_DUM = [
    Quete(
        id_quete="khazak_1_sabotage_mines",
        nom="Le Sabotage des Mines",
        description="""Les mines de Khazak-Dûm sont attaquées par des créatures inhabituelles.
Mais ce qui est plus troublant, c'est que certains mécanismes de sécurité ont été sabotés de
l'intérieur. Quelqu'un dans les rangs nains travaille pour l'ennemi.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Tunnels de la Basalte", "Tunnels_Basalte", 1),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les créatures des mines", "creature_mine", 5),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à Borina Yer", "Borina", 1)
        ],
        recompenses={"xp": 600, "or": 250},
        niveau_requis=1
    ),

    Quete(
        id_quete="khazak_2_secrets_voles",
        nom="Les Secrets Volés",
        description="""Des plans d'ingénierie anciens ont été volés dans les Galeries du Savoir.
Ces plans contiennent des informations sur les mécanismes de protection des reliques. L'Ordre
cherche à comprendre comment briser les sceaux.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Galeries du Savoir", "Galeries_Savoir", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer les plans volés", "plans_anciens", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à Zamir Oural", "Zamir", 1)
        ],
        recompenses={"xp": 1000, "or": 400},
        prerequis=["khazak_1_sabotage_mines"],
        niveau_requis=3
    ),

    Quete(
        id_quete="khazak_3_traison_clan",
        nom="La Trahison d'un Clan",
        description="""Les preuves pointent vers un membre des Quatre Piliers. L'un des plus
respectés des nains a été corrompu par l'Ordre. Vous devez découvrir qui avant qu'il ne révèle
l'emplacement de la relique de Durin le Fondateur.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler aux Quatre Piliers", "pilier", 4),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver la preuve de la corruption", "preuve_corruption", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Confronter le traître", "traître_khazak", 1)
        ],
        recompenses={"xp": 1500, "or": 600},
        prerequis=["khazak_2_secrets_voles"],
        niveau_requis=5
    ),

    Quete(
        id_quete="khazak_4_vol_relique",
        nom="La Relique Volée",
        description="""Le traître a été démasqué ! Mais avant que vous ne puissiez l'arrêter,
il a activé un mécanisme destructeur qui fait s'effondrer le Caveau des Secrets et lui a permis
de voler la relique contenant l'âme de Durin le Fondateur. Malgré vos efforts, le traître réussit
à s'enfuir avec la relique et à rejoindre l'Ordre des Ombres Éternelles. Vous devez arrêter
le mécanisme destructeur, mais la relique est déjà perdue.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Arrêter le mécanisme destructeur", "mecanisme_destructeur", 1),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les agents de l'Ordre", "agent_ordre", 5),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Informer les dirigeants de la perte de la relique", "dirigeant_khazak", 1)
        ],
        recompenses={"xp": 2000, "or": 1000},
        prerequis=["khazak_3_traison_clan"],
        niveau_requis=8
    )
]

# ==================== LUTHESIA (Humain) ====================

QUETES_LUTHESIA = [
    Quete(
        id_quete="luthesia_1_brigands_organises",
        nom="Des Brigands Trop Organisés",
        description="""Les brigands des Plaines Centrales sont anormalement organisés et bien équipés.
Ils semblent suivre des ordres précis et éviter certaines zones. Quelque chose de plus grand se cache
derrière ces attaques.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Plaines Centrales", "Plaines_Centrales", 1),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer 5 groupes de brigands", "brigand", 5),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer des documents sur les brigands", "document_brigand", 1)
        ],
        recompenses={"xp": 600, "or": 250},
        niveau_requis=1
    ),

    Quete(
        id_quete="luthesia_2_magie_corrompue",
        nom="La Magie Corrompue",
        description="""Les Forêts Luminescentes sont polluées par une magie sombre. Les Académies
magiques sont en alerte - quelqu'un utilise des arts interdits. L'Ordre cherche à comprendre
les secrets de la relique d'Hélios le Premier.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Forêts Luminescentes", "Forets_Luminescentes", 1),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Nettoyer l'Observatoire des Astres", "Observatoire_Astres", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à Dame Seraphina Veritas", "Seraphina", 1)
        ],
        recompenses={"xp": 1000, "or": 400},
        prerequis=["luthesia_1_brigands_organises"],
        niveau_requis=3
    ),

    Quete(
        id_quete="luthesia_3_traison_cour",
        nom="La Trahison à la Cour",
        description="""Les preuves révèlent qu'un membre des Quatre Piliers de Luthesia est un traître.
Pire encore, il pourrait être l'un des plus proches conseillers du Roi Magnus. Vous devez découvrir
qui avant qu'il ne révèle l'emplacement de la relique d'Hélios.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler aux Quatre Piliers", "pilier_luthesia", 4),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver la preuve de la trahison", "preuve_trahison_luthesia", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Confronter le traître", "traître_luthesia", 1)
        ],
        recompenses={"xp": 1500, "or": 600},
        prerequis=["luthesia_2_magie_corrompue"],
        niveau_requis=5
    ),

    Quete(
        id_quete="luthesia_4_vol_relique",
        nom="La Relique Volée",
        description="""Le traître a été démasqué ! Mais avant que vous ne puissiez l'arrêter,
il a lancé un sort qui corrompt les terres autour de l'Observatoire et lui a permis de voler
la relique contenant l'âme d'Hélios le Premier. Malgré vos efforts, le traître réussit à s'enfuir
avec la relique et à rejoindre l'Ordre des Ombres Éternelles. Vous devez purifier les terres,
mais la relique est déjà perdue.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les créatures corrompues", "creature_corrompue", 10),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Purifier l'Observatoire", "purification", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Informer le Roi Magnus de la perte de la relique", "roi_magnus", 1)
        ],
        recompenses={"xp": 2000, "or": 1000},
        prerequis=["luthesia_3_traison_cour"],
        niveau_requis=8
    )
]

# ==================== VRAK'THAR (Démon) ====================

QUETES_VRAKTHAR = [
    Quete(
        id_quete="vrakthar_1_rituels_sombres",
        nom="Les Rituels Sombres",
        description="""Même dans Vrak'thar, royaume des démons, des rituels encore plus sombres
sont pratiqués. Des démons disparaissent, et des runes anciennes - la langue oubliée des anciens
démons - apparaissent dans des endroits sacrés. Quelque chose ne va pas.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Terres Brûlées", "Terres_Brulees", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Collecter 3 runes anciennes", "rune_ancienne", 3),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Consulter un érudit démon sur ces runes", "erudit_demon", 1)
        ],
        recompenses={"xp": 600, "or": 250},
        niveau_requis=1
    ),

    Quete(
        id_quete="vrakthar_2_secret_krathos",
        nom="Le Secret de Krathos",
        description="""Les runes révèlent une vérité choquante : l'ancien Roi Démon Krathos le Sage
a sacrifié son âme pour sceller Zarathos. Cette histoire a été effacée, mais l'Ordre cherche à
comprendre comment briser le sceau de Krathos. Vous devez découvrir où se trouve la relique.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Explorer le Sanctuaire des Flammes Éternelles", "Sanctuaire_Flammes", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver des documents sur Krathos", "document_krathos", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à un gardien ancien", "gardien_ancien", 1)
        ],
        recompenses={"xp": 1000, "or": 400},
        prerequis=["vrakthar_1_rituels_sombres"],
        niveau_requis=3
    ),

    Quete(
        id_quete="vrakthar_3_traison_demons",
        nom="La Trahison des Démons",
        description="""Même parmi les démons, l'Ordre a des agents. Certains croient naïvement qu'ils
seront récompensés par Zarathos, ignorant qu'il ne veut que la destruction. Vous devez découvrir
qui est le traître avant qu'il ne révèle l'emplacement de la relique de Krathos.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler aux conseillers démoniaques", "conseiller_demon", 3),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver la preuve de la trahison", "preuve_trahison_vrakthar", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Confronter le traître", "traître_vrakthar", 1)
        ],
        recompenses={"xp": 1500, "or": 600},
        prerequis=["vrakthar_2_secret_krathos"],
        niveau_requis=5
    ),

    Quete(
        id_quete="vrakthar_4_vol_relique",
        nom="La Relique Volée",
        description="""Le traître a été démasqué ! Mais avant que vous ne puissiez l'arrêter,
il a activé un rituel qui corrompt les flammes éternelles et lui a permis de voler la relique
contenant l'âme de Krathos le Sage. Malgré vos efforts, le traître réussit à s'enfuir avec
la relique et à rejoindre l'Ordre des Ombres Éternelles. Vous devez arrêter le rituel, mais
la relique est déjà perdue.""",
        type_quete=TypeQuete.ROYAUME,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les serviteurs corrompus", "serviteur_corrompu", 10),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Arrêter le rituel de corruption", "rituel_corruption_vrakthar", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Informer les dirigeants démoniaques de la perte de la relique", "dirigeant_vrakthar", 1)
        ],
        recompenses={"xp": 2000, "or": 1000},
        prerequis=["vrakthar_3_traison_demons"],
        niveau_requis=8
    )
]

# Dictionnaire regroupant toutes les quêtes de royaume
TOUTES_LES_QUETES_ROYAUME = {
    "Aerthos": QUETES_AERTHOS,
    "Khazak-Dûm": QUETES_KHAZAK_DUM,
    "Luthesia": QUETES_LUTHESIA,
    "Vrak'thar": QUETES_VRAKTHAR
}

# Traîtres par royaume (à révéler progressivement)
TRAITRES_ROYAUMES = {
    "Aerthos": {
        "nom": "Seraphina Étoileprofonde",  # L'Archiviste de l'Arcane
        "description": "Corrompue par l'Ordre, elle cherche à utiliser ses connaissances magiques pour briser les sceaux",
        "revele_dans": "aerthos_3_traison_revelee"
    },
    "Khazak-Dûm": {
        "nom": "Gelal Sözcü",  # Le Chroniqueur des Sagas
        "description": "Ensorcelé par l'Ordre, il révèle les secrets des anciens rois pour aider l'Ordre",
        "revele_dans": "khazak_3_traison_clan"
    },
    "Luthesia": {
        "nom": "Baron Silas de Monnaie",  # Le Chancelier du Trésor (ou peut-être le Roi lui-même ?)
        "description": "Corrompu par la promesse de pouvoir, il finance secrètement les activités de l'Ordre",
        "revele_dans": "luthesia_3_traison_cour"
    },
    "Vrak'thar": {
        "nom": "Un conseiller démoniaque majeur",
        "description": "Convaincu qu'il sera récompensé par Zarathos, ignorant que le Dévoreur ne veut que destruction",
        "revele_dans": "vrakthar_3_traison_demons"
    }
}
