# data/pnjs_quetes.py
# Définitions des PNJ mentionnés dans les quêtes

from world.pnj import PNJ, enregistrer_pnj

# ==================== PNJ AERTHOS ====================

def initialiser_pnjs():
    """Initialise tous les PNJ du jeu."""

    # AERTHOS
    enregistrer_pnj(PNJ(
        id_pnj="Faelar",
        nom="Faelar Éternelbranche",
        description="Un Gardien de la Forêt d'Aerthos, expert en mystères sylvestres.",
        royaume="Aerthos",
        dialogue_par_defaut="Les disparitions dans la forêt sont troublantes. J'ai vu ces symboles étranges gravés sur les arbres...",
        quetes_liees=["aerthos_1_disparitions"],
        dialogues_quetes={
            "aerthos_1_disparitions": "Ces symboles que vous avez trouvés... Ils sont l'œuvre de l'Ordre des Ombres Éternelles. Je les ai vus gravés près des lieux de disparition. Explorez la Forêt de Lumière Argentée, mais soyez prudent.",
            "aerthos_1_disparitions_complete": "Merci d'avoir découvert la vérité sur ces disparitions. Ces symboles confirment que l'Ordre agit dans notre royaume. Restez vigilant."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="gardien",
        nom="Les Quatre Gardiens",
        description="Les quatre gardiens les plus proches du Roi Aerion.",
        royaume="Aerthos",
        dialogue_par_defaut="Nous sommes les gardiens d'Aerthos. L'un de nous cache quelque chose...",
        quetes_liees=["aerthos_3_traison_revelee"],
        dialogues_quetes={
            "aerthos_3_traison_revelee": "Le journal révèle une vérité choquante... L'un de nous est un traître. Parlez à chacun de nous et cherchez les preuves. La sécurité d'Aerthos en dépend.",
            "aerthos_3_traison_revelee_complete": "Vous avez découvert le traître parmi nous. Seraphina Étoileprofonde... Nous ne l'aurions jamais soupçonnée. Merci pour votre vigilance."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="traître_aerthos",
        nom="Seraphina Étoileprofonde",
        description="L'Archiviste de l'Arcane, révélée comme traître.",
        royaume="Aerthos",
        dialogue_par_defaut="Vous avez découvert mon secret... Mais il est trop tard ! La relique est déjà entre les mains de l'Ordre !"
    ))

    enregistrer_pnj(PNJ(
        id_pnj="roi_aerion",
        nom="Roi Aerion",
        description="Le Roi d'Aerthos, dirigeant des elfes.",
        royaume="Aerthos",
        dialogue_par_defaut="Bienvenue dans Aerthos. Des événements troublants se produisent dans notre royaume.",
        quetes_liees=["aerthos_4_vol_relique", "decouverte_ordre"],
        dialogues_quetes={
            "decouverte_ordre": "Des événements étranges se produisent dans notre royaume. Des disparitions, des objets volés... Explorez et découvrez ce qui se cache derrière ces mystères.",
            "aerthos_4_vol_relique": "La perte de la relique contenant l'âme d'Aerion l'Ancien est une catastrophe. Malgré vos efforts, le traître a réussi à s'enfuir avec elle. Nous devons empêcher l'Ordre de compléter son rituel avant qu'il ne soit trop tard.",
            "aerthos_4_vol_relique_complete": "Merci pour votre aide. Même si la relique est perdue, vous avez sauvé notre royaume de la corruption. L'Ordre doit être arrêté avant qu'il ne soit trop tard."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="Seraphina",
        nom="Seraphina Étoileprofonde",
        description="L'Archiviste de l'Arcane d'Aerthos.",
        royaume="Aerthos",
        dialogue_par_defaut="Ces cristaux résonnent d'une énergie ancienne... Ils datent de l'époque du scellement.",
        quetes_liees=["aerthos_sec_2_cristaux_anciens"],
        dialogues_quetes={
            "aerthos_sec_2_cristaux_anciens": "Ces cristaux résonnants que vous avez collectés... Ils datent de l'époque où Aerion scella Zarathos. Leur activation est un signe que quelque chose perturbe les anciens sceaux.",
            "aerthos_sec_2_cristaux_anciens_complete": "Ces cristaux révèlent des fragments de l'histoire oubliée. Merci de les avoir collectés. Ils confirment que les anciens sceaux sont en danger."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="esprit_perdu",
        nom="Esprit Perdu",
        description="Un esprit de la forêt ancienne errant dans les Lacs Scintillants.",
        royaume="Aerthos",
        dialogue_par_defaut="Je me souviens... avant que l'histoire ne soit effacée... Aerion... Zarathos...",
        quetes_liees=["aerthos_sec_1_esprit_perdu"],
        dialogues_quetes={
            "aerthos_sec_1_esprit_perdu": "Je me souviens... avant que l'histoire ne soit effacée... Aerion l'Ancien... Zarathos le Dévoreur... Le fragment de mémoire que vous cherchez contient ces souvenirs perdus.",
            "aerthos_sec_1_esprit_perdu_complete": "Merci d'avoir récupéré mon fragment de mémoire. Je peux maintenant trouver la paix. L'histoire ne doit pas être oubliée..."
        }
    ))

    # KHAZAK-DÛM
    enregistrer_pnj(PNJ(
        id_pnj="Borina",
        nom="Borina Yer",
        description="Une naine experte en mécanismes et sécurité des mines.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Les sabotages viennent de l'intérieur. Quelqu'un connaît nos mécanismes de sécurité...",
        quetes_liees=["khazak_1_sabotage_mines"],
        dialogues_quetes={
            "khazak_1_sabotage_mines": "Les créatures des mines sont un problème, mais ce qui m'inquiète vraiment, c'est que certains mécanismes de sécurité ont été sabotés de l'intérieur. Explorez les Tunnels de la Basalte et découvrez qui est responsable.",
            "khazak_1_sabotage_mines_complete": "Merci d'avoir sécurisé les mines. Les mécanismes sont maintenant réparés. Mais nous devons découvrir qui les a sabotés..."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="Zamir",
        nom="Zamir Oural",
        description="Un érudit nain gardien des Galeries du Savoir.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Les plans volés contiennent des secrets sur les mécanismes de protection des reliques...",
        quetes_liees=["khazak_2_secrets_voles"],
        dialogues_quetes={
            "khazak_2_secrets_voles": "Les plans d'ingénierie anciens qui ont été volés... Ils contiennent des informations cruciales sur les mécanismes de protection des reliques. L'Ordre cherche à comprendre comment briser les sceaux. Récupérez ces plans dans les Galeries du Savoir.",
            "khazak_2_secrets_voles_complete": "Merci d'avoir récupéré les plans. Ces informations sont cruciales pour protéger nos reliques. Mais l'Ordre a déjà vu ces secrets..."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="pilier",
        nom="Les Quatre Piliers",
        description="Les quatre piliers les plus respectés des nains.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Nous sommes les piliers de Khazak-Dûm. L'un de nous a été corrompu...",
        quetes_liees=["khazak_3_traison_clan"],
        dialogues_quetes={
            "khazak_3_traison_clan": "Les preuves pointent vers un membre des Quatre Piliers. L'un des plus respectés d'entre nous a été corrompu par l'Ordre. Parlez à chacun de nous et trouvez la preuve de la corruption.",
            "khazak_3_traison_clan_complete": "Gelal Sözcü... Nous ne pouvions pas imaginer qu'il trahirait ainsi notre peuple. Merci de l'avoir démasqué."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="traître_khazak",
        nom="Gelal Sözcü",
        description="Le Chroniqueur des Sagas, révélé comme traître.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="J'ai révélé les secrets des anciens rois à l'Ordre... La relique de Durin est perdue !"
    ))

    enregistrer_pnj(PNJ(
        id_pnj="dirigeant_khazak",
        nom="Dirigeants de Khazak-Dûm",
        description="Les dirigeants nains.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Bienvenue dans Khazak-Dûm. Des événements troublants se produisent dans nos mines.",
        quetes_liees=["khazak_4_vol_relique"],
        dialogues_quetes={
            "khazak_4_vol_relique": "La relique contenant l'âme de Durin le Fondateur a été volée. Malgré vos efforts, le traître a réussi à s'enfuir avec elle. Arrêtez le mécanisme destructeur avant qu'il ne détruise tout.",
            "khazak_4_vol_relique_complete": "Merci pour votre aide. Vous avez arrêté le mécanisme destructeur, mais la relique de Durin est perdue. L'Ordre doit être arrêté avant qu'il ne soit trop tard."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="Gelal",
        nom="Gelal Sözcü",
        description="Le Chroniqueur des Sagas de Khazak-Dûm.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Je connais les légendes de Durin... Mais certaines parties ont été effacées...",
        quetes_liees=["khazak_sec_1_legende_durin"],
        dialogues_quetes={
            "khazak_sec_1_legende_durin": "Je vous raconterai des fragments de la légende de Durin le Fondateur, le premier roi nain qui sacrifia son âme. Mais certaines parties de l'histoire semblent avoir été modifiées ou effacées... Trouvez un ancien parchemin dans les Galeries du Savoir.",
            "khazak_sec_1_legende_durin_complete": "Le parchemin que vous avez trouvé révèle la vérité sur Durin. Merci de l'avoir récupéré. L'histoire ne doit pas être oubliée."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="Grom",
        nom="Grom Starkov",
        description="Un maître forgeron nain.",
        royaume="Khazak-Dûm",
        dialogue_par_defaut="Ces plans de forgeage sont anciens... Ils permettront de créer des armes légendaires.",
        quetes_liees=["khazak_sec_2_forge_ancienne"],
        dialogues_quetes={
            "khazak_sec_2_forge_ancienne": "Une ancienne forge utilisée par Durin lui-même a été découverte dans les profondeurs. Elle contient des secrets de forgeage qui pourraient vous aider à créer des armes puissantes contre l'Ordre. Montrez-moi les plans que vous avez trouvés.",
            "khazak_sec_2_forge_ancienne_complete": "Ces plans de forgeage sont extraordinaires ! Avec ces techniques anciennes, nous pourrons créer des armes légendaires. Merci de les avoir récupérés."
        }
    ))

    # LUTHESIA
    enregistrer_pnj(PNJ(
        id_pnj="Seraphina",
        nom="Dame Seraphina Veritas",
        description="Une académicienne magique de Luthesia.",
        royaume="Luthesia",
        dialogue_par_defaut="La magie corrompue dans les forêts est l'œuvre de l'Ordre. Ils cherchent les secrets de la relique d'Hélios.",
        quetes_liees=["luthesia_2_magie_corrompue", "luthesia_sec_1_histoire_helios"],
        dialogues_quetes={
            "luthesia_2_magie_corrompue": "Les Forêts Luminescentes sont polluées par une magie sombre. L'Ordre utilise des arts interdits pour comprendre les secrets de la relique d'Hélios le Premier. Nettoyez l'Observatoire des Astres.",
            "luthesia_2_magie_corrompue_complete": "Merci d'avoir nettoyé l'Observatoire. La magie sombre a été purifiée, mais l'Ordre a déjà obtenu les informations qu'il cherchait...",
            "luthesia_sec_1_histoire_helios": "Dans les archives de l'Académie, vous trouverez des fragments de l'histoire d'Hélios le Premier. Mais certains documents ont été altérés ou volés récemment... Explorez les Forêts Luminescentes et trouvez la vérité.",
            "luthesia_sec_1_histoire_helios_complete": "Les documents que vous avez trouvés révèlent la vérité sur Hélios le Premier. Merci de les avoir récupérés. L'histoire ne doit pas être altérée."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="pilier_luthesia",
        nom="Les Quatre Piliers de Luthesia",
        description="Les quatre piliers de la cour de Luthesia.",
        royaume="Luthesia",
        dialogue_par_defaut="Nous sommes les piliers de Luthesia. L'un de nous est un traître...",
        quetes_liees=["luthesia_3_traison_cour"],
        dialogues_quetes={
            "luthesia_3_traison_cour": "Les preuves révèlent qu'un membre des Quatre Piliers est un traître. Pire encore, il pourrait être l'un des plus proches conseillers du Roi Magnus. Parlez à chacun de nous et trouvez la preuve de la trahison.",
            "luthesia_3_traison_cour_complete": "Baron Silas de Monnaie... Le Chancelier du Trésor était un traître. Merci de l'avoir démasqué avant qu'il ne cause plus de dégâts."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="traître_luthesia",
        nom="Baron Silas de Monnaie",
        description="Le Chancelier du Trésor, révélé comme traître.",
        royaume="Luthesia",
        dialogue_par_defaut="J'ai financé les activités de l'Ordre... La relique d'Hélios est maintenant entre leurs mains !"
    ))

    enregistrer_pnj(PNJ(
        id_pnj="roi_magnus",
        nom="Roi Magnus",
        description="Le Roi de Luthesia, dirigeant des humains.",
        royaume="Luthesia",
        dialogue_par_defaut="Bienvenue dans Luthesia. Des brigands trop organisés menacent notre royaume.",
        quetes_liees=["luthesia_4_vol_relique"],
        dialogues_quetes={
            "luthesia_4_vol_relique": "La perte de la relique contenant l'âme d'Hélios le Premier est un désastre. Le traître a réussi à s'enfuir avec elle malgré vos efforts. Purifiez les terres autour de l'Observatoire, mais la relique est déjà perdue.",
            "luthesia_4_vol_relique_complete": "Merci pour votre aide. Vous avez purifié nos terres, mais la relique est perdue. L'Ordre doit être arrêté avant qu'il ne réveille Zarathos."
        }
    ))

    # VRAK'THAR
    enregistrer_pnj(PNJ(
        id_pnj="erudit_demon",
        nom="Érudit Démoniaque",
        description="Un érudit démon expert en runes anciennes.",
        royaume="Vrak'thar",
        dialogue_par_defaut="Ces runes sont écrites dans la langue oubliée des anciens démons... Elles parlent de Krathos le Sage.",
        quetes_liees=["vrakthar_1_rituels_sombres", "vrakthar_sec_1_langue_ancienne"],
        dialogues_quetes={
            "vrakthar_1_rituels_sombres": "Ces runes anciennes que vous avez trouvées... Elles sont écrites dans la langue oubliée des anciens démons. Elles révèlent que même dans Vrak'thar, des rituels encore plus sombres sont pratiqués. Explorez les Terres Brûlées.",
            "vrakthar_1_rituels_sombres_complete": "Merci d'avoir découvert la vérité sur ces rituels. Même dans notre royaume, l'Ordre agit dans l'ombre.",
            "vrakthar_sec_1_langue_ancienne": "Les runes que vous avez collectées sont écrites dans la langue oubliée des anciens démons. Je peux vous aider à les déchiffrer, révélant des secrets sur Krathos le Sage et l'époque du scellement.",
            "vrakthar_sec_1_langue_ancienne_complete": "Les runes déchiffrées révèlent des fragments de l'histoire oubliée. Merci de les avoir déchiffrées. Même nous, les démons, devons nous opposer à l'Ordre."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="gardien_ancien",
        nom="Gardien Ancien",
        description="Un gardien ancien des secrets de Vrak'thar.",
        royaume="Vrak'thar",
        dialogue_par_defaut="Krathos le Sage a sacrifié son âme pour sceller Zarathos... Cette histoire a été effacée.",
        quetes_liees=["vrakthar_2_secret_krathos", "vrakthar_sec_2_sagesse_krathos"],
        dialogues_quetes={
            "vrakthar_2_secret_krathos": "Les runes révèlent une vérité choquante : l'ancien Roi Démon Krathos le Sage a sacrifié son âme pour sceller Zarathos. Cette histoire a été effacée, mais l'Ordre cherche à comprendre comment briser le sceau de Krathos.",
            "vrakthar_sec_2_sagesse_krathos": "Les runes déchiffrées révèlent des fragments de la sagesse de Krathos le Sage. Même en tant que démon, il reconnaissait que Zarathos était une menace pour tous. Trouvez un fragment de sa sagesse dans les Terres Brûlées.",
            "vrakthar_sec_2_sagesse_krathos_complete": "Le fragment de sagesse de Krathos que vous avez trouvé confirme que même les démons doivent s'opposer à l'Ordre. Merci de l'avoir récupéré."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="conseiller_demon",
        nom="Conseillers Démoniaques",
        description="Les conseillers les plus proches des dirigeants démoniaques.",
        royaume="Vrak'thar",
        dialogue_par_defaut="Même parmi nous, l'Ordre a des agents. Certains croient naïvement qu'ils seront récompensés...",
        quetes_liees=["vrakthar_3_traison_demons"],
        dialogues_quetes={
            "vrakthar_3_traison_demons": "Même parmi nous, l'Ordre a des agents. Certains croient naïvement qu'ils seront récompensés par Zarathos, ignorant qu'il ne veut que la destruction. Parlez à chacun de nous et trouvez la preuve de la trahison.",
            "vrakthar_3_traison_demons_complete": "Le traître a été démasqué. Merci de l'avoir découvert avant qu'il ne révèle l'emplacement de la relique de Krathos."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="traître_vrakthar",
        nom="Traître Démoniaque",
        description="Un conseiller démoniaque majeur révélé comme traître.",
        royaume="Vrak'thar",
        dialogue_par_defaut="Je croyais que Zarathos me récompenserait... Mais la relique de Krathos est maintenant perdue !"
    ))

    enregistrer_pnj(PNJ(
        id_pnj="dirigeant_vrakthar",
        nom="Dirigeants Démoniaques",
        description="Les dirigeants de Vrak'thar.",
        royaume="Vrak'thar",
        dialogue_par_defaut="Bienvenue dans Vrak'thar. Des rituels encore plus sombres sont pratiqués dans notre royaume.",
        quetes_liees=["vrakthar_4_vol_relique"],
        dialogues_quetes={
            "vrakthar_4_vol_relique": "La relique contenant l'âme de Krathos le Sage a été volée. Malgré vos efforts, le traître a réussi à s'enfuir avec elle. Arrêtez le rituel de corruption avant qu'il ne détruise tout.",
            "vrakthar_4_vol_relique_complete": "Merci pour votre aide. Même nous, les démons, reconnaissons que Zarathos est une menace. La relique de Krathos est perdue, mais vous avez arrêté le rituel. L'Ordre doit être stoppé."
        }
    ))

    # PNJ GÉNÉRIQUES (pour quêtes principales)
    enregistrer_pnj(PNJ(
        id_pnj="roi",
        nom="Dirigeant du Royaume",
        description="Le dirigeant de votre royaume d'origine.",
        royaume=None,
        dialogue_par_defaut="Des événements étranges se produisent dans notre royaume. Nous avons besoin de votre aide.",
        quetes_liees=["decouverte_ordre"],
        dialogues_quetes={
            "decouverte_ordre": "Des événements étranges se produisent dans notre royaume. Des disparitions, des objets volés, des rituels suspects... Explorez notre royaume et découvrez ce qui se cache derrière ces mystères.",
            "decouverte_ordre_complete": "Merci d'avoir découvert la vérité. L'Ordre des Ombres Éternelles agit dans l'ombre. Restez vigilant."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="erudit",
        nom="Érudit",
        description="Un érudit expert en symboles et histoire ancienne.",
        royaume=None,
        dialogue_par_defaut="Ces symboles sont anciens... Ils représentent un ordre secret qui cherche à réveiller quelque chose de terrifiant.",
        quetes_liees=["premiere_preuve"],
        dialogues_quetes={
            "premiere_preuve": "Ces symboles que vous avez trouvés... Ils sont anciens et représentent l'Ordre des Ombres Éternelles. Cet ordre secret cherche à réveiller quelque chose de terrifiant. Collectez plus d'objets suspects pour comprendre leurs plans.",
            "premiere_preuve_complete": "Les objets que vous avez collectés confirment l'existence de l'Ordre. Merci de m'avoir apporté ces preuves. Nous devons découvrir leur véritable objectif."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="gardien_relique",
        nom="Gardien de Relique",
        description="Un gardien protégeant une relique sacrée.",
        royaume=None,
        dialogue_par_defaut="La relique que je protège contient l'âme d'un ancien roi. L'Ordre cherche à la voler...",
        quetes_liees=["revelation_zarathos"],
        dialogues_quetes={
            "revelation_zarathos": "La relique que je protège contient l'âme d'un ancien roi qui sacrifia sa vie pour sceller Zarathos le Dévoreur. L'Ordre des Ombres Éternelles cherche à voler toutes les reliques pour briser les sceaux et réveiller cette entité maléfique. Explorez la zone où se trouve la relique, mais soyez vigilant."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="informateur_ordre",
        nom="Informateur",
        description="Un informateur connaissant l'emplacement du sanctuaire de l'Ordre.",
        royaume=None,
        dialogue_par_defaut="Le sanctuaire de l'Ordre se trouve dans un lieu secret... Ils préparent le rituel de résurrection de Zarathos.",
        quetes_liees=["reliques_volees"],
        dialogues_quetes={
            "reliques_volees": "Les traîtres ont réussi à voler les quatre reliques sacrées. L'Ordre les a rassemblées dans leur sanctuaire secret et prépare le rituel de résurrection de Zarathos. Vous devez localiser ce sanctuaire et infiltrer le lieu du rituel avant qu'il ne soit trop tard."
        }
    ))

    enregistrer_pnj(PNJ(
        id_pnj="informateur",
        nom="Informateur",
        description="Un informateur connaissant les mouvements des traîtres.",
        royaume=None,
        dialogue_par_defaut="Le traître s'est enfui vers un point de rendez-vous avec l'Ordre..."
    ))
