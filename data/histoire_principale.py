# data/histoire_principale.py
# Histoire principale du jeu : Zarthos le Dévoreur et l'Ordre des Ombres Éternelles

from world.quetes import Quete, ObjectifQuete, TypeQuete, TypeObjectif

# Introduction de l'histoire principale
INTRODUCTION_HISTOIRE_PRINCIPALE = """
Il y a des millénaires, avant que l'histoire ne soit effacée, un être d'une puissance inimaginable
menaçait de détruire tout ce qui existait. Zarthos le Dévoreur, un Ancien Dieu du chaos et de la
destruction pure, cherchait à réduire Valdoria en cendres.

Face à cette menace, les anciens dirigeants des quatre royaumes - même le Roi Démon,
qui reconnaissait que Zarthos menaçait jusqu'à son propre pouvoir - s'unirent au péril de leur vie
pour sceller cette entité maléfique. Chaque roi sacrifia son âme, l'emprisonnant dans une relique
sacrée cachée dans son royaume respectif.

L'histoire de cette époque fut effacée, volontairement oubliée pour éviter que quiconque ne tente
de réveiller Zarthos. Mais aujourd'hui, un ordre secret - l'Ordre des Ombres Éternelles - œuvre
dans l'ombre pour briser les sceaux et libérer le Dévoreur.

Infiltré à tous les niveaux, même parmi les plus hauts dignitaires, l'Ordre manipule, ensorcelle
et corrompt. Certains de ses membres croient naïvement qu'ils seront récompensés par Zarthos,
ignorant qu'il n'est que destruction pure.

Votre mission : découvrir la vérité, démasquer les traîtres, protéger les reliques sacrées,
et empêcher la résurrection de Zarthos avant qu'il ne soit trop tard.
"""

# Quêtes principales (progression globale)
QUETES_PRINCIPALES = {
    "decouverte_ordre": Quete(
        id_quete="decouverte_ordre",
        nom="Les Ombres qui Grandissent",
        description="""Vous avez remarqué des événements étranges dans votre royaume d'origine.
Des disparitions, des objets volés, des rituels suspects. Quelque chose ne tourne pas rond,
mais vous n'avez pas encore de preuves concrètes. Explorez votre royaume et découvrez ce qui se cache derrière ces mystères.""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Compléter 2 zones de votre royaume", "zone", 2),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à votre mentor dans la capitale", "mentor", 1)
        ],
        recompenses={"xp": 500, "or": 200},
        niveau_requis=1
    ),

    "premiere_preuve": Quete(
        id_quete="premiere_preuve",
        nom="La Première Preuve",
        description="""Vous avez découvert des indices troublants : des symboles étranges gravés
sur des objets volés, des références à un "Ordre" dans des documents anciens. Il semble qu'une
organisation secrète soit à l'œuvre. Mais qui sont-ils vraiment ?""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Collecter 3 objets suspects", "symbole_ordre", 3),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Consulter un érudit sur ces symboles", "erudit", 1)
        ],
        recompenses={"xp": 800, "or": 300},
        prerequis=["decouverte_ordre"],
        niveau_requis=3
    ),

    "infiltration_confirmee": Quete(
        id_quete="infiltration_confirmee",
        nom="L'Infiltration Confirmée",
        description="""Après avoir complété votre premier royaume, vous êtes maintenant certain
qu'une organisation secrète - l'Ordre des Ombres Éternelles - infiltre tous les royaumes.
Ils cherchent à réveiller quelque chose d'ancien et de terrifiant. Vous devez découvrir leur véritable objectif.""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Compléter un donjon dans un royaume", "donjon", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver un document de l'Ordre", "document_ordre", 1)
        ],
        recompenses={"xp": 1200, "or": 500},
        prerequis=["premiere_preuve"],
        niveau_requis=5
    ),

    "revelation_zarathos": Quete(
        id_quete="revelation_zarathos",
        nom="La Révélation : Zarthos",
        description="""Vous avez découvert la vérité terrifiante : l'Ordre cherche à réveiller
Zarthos le Dévoreur, un Ancien Dieu du chaos qui fut scellé il y a des millénaires par les anciens
rois au prix de leur vie. Chaque royaume protège une relique contenant l'âme d'un ancien roi,
et l'Ordre veut les voler pour briser les sceaux.""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Découvrir l'emplacement d'une relique", "gardien_relique", 1),
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer la zone où se trouve la relique", "zone_relique", 1)
        ],
        recompenses={"xp": 1500, "or": 800},
        prerequis=["infiltration_confirmee"],
        niveau_requis=8
    ),


    "reliques_volées": Quete(
        id_quete="reliques_volees",
        nom="Les Reliques Perdues",
        description="""Les traîtres ont réussi à voler les quatre reliques sacrées et les ont
livrées à l'Ordre des Ombres Éternelles. L'Ordre a maintenant accès à toutes les reliques et prépare
le rituel final qui réveillera Zarthos le Dévoreur. Vous devez découvrir où l'Ordre prépare ce
rituel de résurrection avant qu'il ne soit trop tard.""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Découvrir l'emplacement du sanctuaire de l'Ordre", "informateur_ordre", 1),
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Localiser le lieu du rituel de résurrection", "sanctuaire_ordre", 1),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Infiltrer le sanctuaire de l'Ordre", "infiltration_sanctuaire", 1)
        ],
        recompenses={"xp": 2000, "or": 1500},
        prerequis=["revelation_zarathos"],
        niveau_requis=12
    ),

    "affrontement_final": Quete(
        id_quete="affrontement_final",
        nom="L'Affrontement Final - Empêcher la Résurrection",
        description="""L'Ordre des Ombres Éternelles a rassemblé les quatre reliques sacrées et
a commencé le rituel de résurrection de Zarthos le Dévoreur. Le rituel est en cours, les sceaux
se brisent progressivement. Vous devez interrompre le rituel AVANT que Zarthos ne soit complètement
réveillé. C'est le combat final épique qui déterminera le sort de Valdoria - vous devez arrêter
la résurrection alors qu'elle est déjà en cours. L'ordre dans lequel vous avez complété les royaumes
influencera le déroulement de cette confrontation finale et les alliés/ennemis que vous rencontrerez.""",
        type_quete=TypeQuete.PRINCIPALE,
        objectifs=[
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Interrompre le rituel de résurrection en cours", "rituel_resurrection_zarathos", 1),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Éliminer les serviteurs de Zarthos et les membres de l'Ordre", "serviteur_zarathos", 15),
            ObjectifQuete(TypeObjectif.TUER_ENNEMI, "Affronter le chef de l'Ordre", "chef_ordre", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer les reliques et renforcer les sceaux", "renforcement_sceaux", 1)
        ],
        recompenses={"xp": 5000, "or": 5000, "objets": ["Artefact_Legendaire"]},
        prerequis=["reliques_volees"],
        niveau_requis=20
    )
}

# Mapping des reliques par royaume
RELIQUES_ROYAUMES = {
    "Aerthos": {
        "nom": "L'Âme d'Aerion l'Ancien",
        "description": "L'âme du premier Roi Elfe, scellée dans un cristal de lune pur",
        "emplacement": "Sanctuaire des Murmures Oubliés",
        "gardien": "Eldrin Racine-éclat"
    },
    "Khazak-Dûm": {
        "nom": "L'Âme de Durin le Fondateur",
        "description": "L'âme du premier Roi Nain, scellée dans une gemme de forge",
        "emplacement": "Caveau des Secrets du Premier Âge",
        "gardien": "L'Archiviste Prime"
    },
    "Luthesia": {
        "nom": "L'Âme d'Hélios le Premier",
        "description": "L'âme du premier Roi Humain, scellée dans une épée sacrée",
        "emplacement": "Observatoire des Astres",
        "gardien": "L'Oracle Astral"
    },
    "Vrak'thar": {
        "nom": "L'Âme de l'Ancien Roi Démon",
        "description": "L'âme de l'ancien Roi Démon, scellée dans une rune de feu ancienne",
        "emplacement": "Sanctuaire des Flammes Éternelles",
        "gardien": "Le Gardien des Abysses"
    }
}

# Informations sur l'Ordre des Ombres Éternelles
ORDRE_OMBRES_ETERNELLES = {
    "nom": "L'Ordre des Ombres Éternelles",
    "description": """Un ordre secret qui œuvre dans l'ombre pour réveiller Zarthos le Dévoreur.
Ils sont infiltrés à tous les niveaux : fidèles convaincus, personnes ensorcelées, ou simplement
corrompues par la promesse de pouvoir.""",
    "objectif": "Réveiller Zarthos le Dévoreur en volant les quatre reliques sacrées",
    "methodes": ["Infiltration", "Envoûtement", "Corruption", "Vol de reliques"],
    "symboles": "Des runes anciennes représentant des ombres entrelacées et un œil démoniaque"
}
