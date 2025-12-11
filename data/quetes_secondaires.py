# data/quetes_secondaires.py
# Quêtes secondaires pour enrichir le lore

from world.quetes import Quete, ObjectifQuete, TypeQuete, TypeObjectif

# Quêtes secondaires par royaume
QUETES_SECONDAIRES_AERTHOS = [
    Quete(
        id_quete="aerthos_sec_1_esprit_perdu",
        nom="L'Esprit Perdu de la Forêt",
        description="""Un esprit de la forêt ancienne erre dans les Lacs Scintillants, cherchant
sa paix. Il vous raconte des fragments de l'histoire oubliée d'Aerthos, avant que l'histoire ne soit effacée.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Lacs Scintillants", "Selenia's Embrace", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Parler à l'esprit perdu", "esprit_perdu", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer un fragment de mémoire", "fragment_memoire", 1)
        ],
        recompenses={"xp": 400, "or": 150},
        niveau_requis=2
    ),

    Quete(
        id_quete="aerthos_sec_2_cristaux_anciens",
        nom="Les Cristaux Anciens des Montagnes",
        description="""Les Montagnes de Cristal résonnent d'une énergie étrange. Des cristaux
anciens, datant de l'époque où Aerion scella Zarthos, commencent à s'activer. Vous devez découvrir pourquoi.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Aerthos",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Montagnes de Cristal", "Lumins'Peak", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Collecter 5 cristaux résonnants", "cristal_resonnant", 5),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Consulter Seraphina Étoileprofonde", "Seraphina", 1)
        ],
        recompenses={"xp": 600, "or": 300},
        niveau_requis=4
    )
]

QUETES_SECONDAIRES_KHAZAK_DUM = [
    Quete(
        id_quete="khazak_sec_1_legende_durin",
        nom="La Légende de Durin",
        description="""Gelal Sözcü vous raconte des fragments de la légende de Durin le Fondateur,
le premier roi nain qui sacrifia son âme. Mais certaines parties de l'histoire semblent avoir été
modifiées ou effacées...""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Écouter les sagas de Gelal", "Gelal", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver un ancien parchemin sur Durin", "parchemin_durin", 1),
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Galeries du Savoir", "Galeries_Savoir", 1)
        ],
        recompenses={"xp": 400, "or": 150},
        niveau_requis=2
    ),

    Quete(
        id_quete="khazak_sec_2_forge_ancienne",
        nom="La Forge Ancienne Oubliée",
        description="""Une ancienne forge, utilisée par Durin lui-même, a été découverte dans
les profondeurs. Elle contient des secrets de forgeage qui pourraient vous aider à créer des armes
puissantes contre l'Ordre.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Khazak-Dûm",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Trouver la Forge Ancienne", "Forge_Ancienne", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer les plans de forgeage", "plans_forgeage", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Montrer les plans à Grom Starkov", "Grom", 1)
        ],
        recompenses={"xp": 600, "or": 300, "objets": ["Recette_Arme_Legendaire"]},
        niveau_requis=4
    )
]

QUETES_SECONDAIRES_LUTHESIA = [
    Quete(
        id_quete="luthesia_sec_1_histoire_helios",
        nom="L'Histoire d'Hélios le Premier",
        description="""Dans les archives de l'Académie, vous découvrez des fragments de l'histoire
d'Hélios le Premier, le roi humain qui sacrifia son âme. Mais certains documents ont été altérés
ou volés récemment...""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Forêts Luminescentes", "Forets_Luminescentes", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver des documents sur Hélios", "document_helios", 3),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Consulter Dame Seraphina Veritas", "Seraphina", 1)
        ],
        recompenses={"xp": 400, "or": 150},
        niveau_requis=2
    ),

    Quete(
        id_quete="luthesia_sec_2_chevaliers_oublies",
        nom="Les Chevaliers Oubliés",
        description="""Dans les Ruines du Vieux Royaume, vous découvrez la tombe d'un ancien
chevalier qui servit Hélios. Son épée et son armure pourraient vous être utiles dans votre quête.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Luthesia",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Ruines du Vieux Royaume", "Ruines_Vieux_Royaume", 1),
            ObjectifQuete(TypeObjectif.COMPLETER_DONJON, "Nettoyer la Prison des Âmes Dépravées", "Prison_Ames", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Récupérer l'épée du chevalier", "epee_chevalier", 1)
        ],
        recompenses={"xp": 600, "or": 300, "objets": ["Epee_Chevalier_Ancien"]},
        niveau_requis=4
    )
]

QUETES_SECONDAIRES_VRAKTHAR = [
    Quete(
        id_quete="vrakthar_sec_1_langue_ancienne",
        nom="La Langue Ancienne des Démons",
        description="""Les runes anciennes que vous avez trouvées sont écrites dans la langue
oubliée des anciens démons. Un érudit démoniaque peut vous aider à les déchiffrer, révélant
des secrets sur l'ancien Roi Démon et l'époque du scellement.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Collecter 5 runes anciennes", "rune_ancienne", 5),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Trouver un érudit démoniaque", "erudit_demon", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Déchiffrer les runes", "runes_dechiffrees", 1)
        ],
        recompenses={"xp": 400, "or": 150},
        niveau_requis=2
    ),

    Quete(
        id_quete="vrakthar_sec_2_sagesse_krathos",
        nom="La Sagesse de l'Ancien Roi Démon",
        description="""Les runes déchiffrées révèlent des fragments de la sagesse de l'ancien Roi Démon.
Même en tant que démon, il reconnaissait que Zarthos était une menace pour tous. Ces connaissances
pourraient vous aider à comprendre pourquoi même les démons doivent s'opposer à l'Ordre.""",
        type_quete=TypeQuete.SECONDAIRE,
        royaume="Vrak'thar",
        objectifs=[
            ObjectifQuete(TypeObjectif.EXPLORER_ZONE, "Explorer les Terres Brûlées", "Terres_Brulees", 1),
            ObjectifQuete(TypeObjectif.COLLECTER_OBJET, "Trouver un fragment de la sagesse de l'ancien Roi Démon", "fragment_sagesse", 1),
            ObjectifQuete(TypeObjectif.PARLER_PNJ, "Consulter un gardien ancien", "gardien_ancien", 1)
        ],
        recompenses={"xp": 600, "or": 300},
        niveau_requis=4
    )
]

# Dictionnaire regroupant toutes les quêtes secondaires
TOUTES_LES_QUETES_SECONDAIRES = {
    "Aerthos": QUETES_SECONDAIRES_AERTHOS,
    "Khazak-Dûm": QUETES_SECONDAIRES_KHAZAK_DUM,
    "Luthesia": QUETES_SECONDAIRES_LUTHESIA,
    "Vrak'thar": QUETES_SECONDAIRES_VRAKTHAR
}
