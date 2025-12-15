# menus/debug.py
# Système de debug pour faciliter les tests

from classes.objet import Objet

def appliquer_bonus_debug(joueur, nom_personnage: str):
    """
    Applique des bonus de debug si le nom du personnage correspond à un pseudo de debug.

    Pseudos de debug :
    - "SKR" : Niveau 20, 100 000 or

    :param joueur: Instance du personnage joueur
    :param nom_personnage: Nom du personnage créé
    """
    if nom_personnage.upper() == "SKR":
        print("\n🔧 MODE DEBUG ACTIVÉ (SKR)")
        print("   Bonus appliqués : Niveau 20, 100 000 or")

        # Monter le niveau à 20
        joueur.niveau = 20
        joueur.xp = 0
        # Calculer l'XP requise pour le niveau 21 (pour la progression future)
        joueur.xp_requise = int(100 * (1.5 ** 19))  # Formule de progression

        # Ajouter de l'or
        joueur.or_ = 100000

        # Réinitialiser les points d'attribut (le joueur aura gagné des points en montant de niveau)
        # Niveau 1 à 20 = 19 niveaux * 3 points = 57 points
        joueur.points_attribut = 57

        # Allouer automatiquement les points d'attribut : 40 en force, le reste en agilité
        points_force = 40
        points_agilite = 57 - points_force  # 17 points restants

        joueur.force += points_force
        joueur.agilite += points_agilite
        joueur.points_attribut = 0  # Tous les points sont alloués

        # Recalculer les stats avec le nouveau niveau et les attributs alloués
        joueur.mettre_a_jour_stats_apres_attributs()

        # Remettre la vie au maximum
        joueur.vie = joueur.vie_max

        # Remettre les ressources au maximum
        if joueur.specialisation.type_ressource == "Mana":
            joueur.mana = joueur.mana_max
        elif joueur.specialisation.type_ressource == "Energie":
            joueur.energie = joueur.energie_max
        elif joueur.specialisation.type_ressource == "Rage":
            joueur.rage = joueur.rage_max

        # Marquer le royaume comme complété pour débloquer la téléportation
        joueur.royaume_complete = True

        print(f"   ✅ Niveau : {joueur.niveau}")
        print(f"   ✅ Or : {joueur.or_:,} pièces")
        print(f"   ✅ Attributs alloués : {points_force} Force, {points_agilite} Agilité")
        print(f"   ✅ Force totale : {joueur.force}, Agilité totale : {joueur.agilite}")
        print(f"   ✅ Royaume complété : Oui (téléportation débloquée)")

        # Ajouter des objets de test pour tester le système de vente
        ajouter_objets_test_vente(joueur)

        print()


def ajouter_objets_test_vente(joueur):
    """
    Ajoute des objets de test dans l'inventaire pour tester le système de vente.
    Ces objets ont différentes raretés, stats et niveaux de biome.

    :param joueur: Instance du personnage joueur
    """
    print("   📦 Ajout d'objets de test pour le système de vente...")

    # 1. Potion commune basique (sans effets spéciaux)
    potion_commune = Objet(
        nom="Potion de Soin Mineure [TEST]",
        type_objet="potion",
        quantite=1,
        description="Restaure 50 PV",
        rarete="commun"
    )
    potion_commune.effets = {"vie": 50}
    joueur.ajouter_objet(potion_commune)

    # 2. Potion rare avec effets (niveau biome moyen)
    potion_rare = Objet(
        nom="Potion de Soin Supérieure [TEST]",
        type_objet="potion",
        quantite=1,
        description="Restaure 200 PV",
        rarete="rare",
        niveau_biome=10
    )
    potion_rare.effets = {"vie": 200}
    joueur.ajouter_objet(potion_rare)

    # 3. Potion épique avec boost temporaire (niveau biome élevé)
    potion_epique = Objet(
        nom="Potion de Force Épique [TEST]",
        type_objet="potion",
        quantite=1,
        description="+50 Attaque (5 tours)",
        rarete="épique",
        niveau_biome=15
    )
    potion_epique.effets = {"boost_attaque": 50, "duree_tours": 5}
    joueur.ajouter_objet(potion_epique)

    # 4. Potion légendaire avec plusieurs boosts (niveau biome très élevé)
    potion_legendaire = Objet(
        nom="Potion Légendaire de Puissance [TEST]",
        type_objet="potion",
        quantite=1,
        description="+100 Attaque, +50 Défense, +30% Critique (10 tours)",
        rarete="légendaire",
        niveau_biome=20
    )
    potion_legendaire.effets = {
        "boost_attaque": 100,
        "boost_defense": 50,
        "boost_critique": 30,
        "duree_tours": 10
    }
    joueur.ajouter_objet(potion_legendaire)

    # 5. Arme commune (sans stats)
    arme_commune = Objet(
        nom="Épée de Fer [TEST]",
        type_objet="équipement",
        quantite=1,
        description="Épée basique",
        rarete="commun"
    )
    arme_commune.stats = {"degats_base": None, "bonus_force": None}
    joueur.ajouter_objet(arme_commune)

    # 6. Arme rare avec dégâts (niveau biome moyen)
    arme_rare = Objet(
        nom="Katana Aiguisé [TEST]",
        type_objet="équipement",
        quantite=1,
        description="+30 Dégâts",
        rarete="rare",
        niveau_biome=10
    )
    arme_rare.stats = {"degats_base": 30, "bonus_force": 0}
    joueur.ajouter_objet(arme_rare)

    # 7. Arme épique avec dégâts et bonus (niveau biome élevé)
    arme_epique = Objet(
        nom="Lame Épique du Guerrier [TEST]",
        type_objet="équipement",
        quantite=1,
        description="+80 Dégâts, +15 Force, +10 Agilité",
        rarete="épique",
        niveau_biome=15
    )
    arme_epique.stats = {
        "degats_base": 80,
        "bonus_force": 15,
        "bonus_agilite": 10,
        "bonus_vitalite": 0,
        "bonus_intelligence": 0
    }
    joueur.ajouter_objet(arme_epique)

    # 8. Armure légendaire de torse avec tous les bonus (niveau biome très élevé)
    armure_legendaire = Objet(
        nom="Armure Légendaire Complète [TEST]",
        type_objet="équipement",
        quantite=1,
        description="+100 Défense, +25 Force, +25 Agilité, +25 Vitalité, +25 Intelligence",
        rarete="légendaire",
        niveau_biome=20
    )
    armure_legendaire.stats = {
        "bonus_defense": 100,
        "bonus_force": 25,
        "bonus_agilite": 25,
        "bonus_vitalite": 25,
        "bonus_intelligence": 25
    }
    armure_legendaire.sous_type = "torse"
    joueur.ajouter_objet(armure_legendaire)

    # 8b. Casque épique (niveau biome élevé)
    casque_epique = Objet(
        nom="Casque Épique du Guerrier [TEST]",
        type_objet="équipement",
        quantite=1,
        description="+50 Défense, +10 Force, +10 Vitalité",
        rarete="épique",
        niveau_biome=15
    )
    casque_epique.stats = {
        "bonus_defense": 50,
        "bonus_force": 10,
        "bonus_vitalite": 10,
        "bonus_agilite": 0,
        "bonus_intelligence": 0
    }
    casque_epique.sous_type = "casque"
    joueur.ajouter_objet(casque_epique)

    # 8c. Bottes rares (niveau biome moyen)
    bottes_rares = Objet(
        nom="Bottes de Course Rapide [TEST]",
        type_objet="équipement",
        quantite=1,
        description="+30 Défense, +15 Agilité",
        rarete="rare",
        niveau_biome=10
    )
    bottes_rares.stats = {
        "bonus_defense": 30,
        "bonus_agilite": 15,
        "bonus_force": 0,
        "bonus_vitalite": 0,
        "bonus_intelligence": 0
    }
    bottes_rares.sous_type = "bottes"
    joueur.ajouter_objet(bottes_rares)

    # 9. Matériau commun (pour comparaison)
    materiau_commun = Objet(
        nom="Fragment d'Os Spectral [TEST]",
        type_objet="matériau",
        quantite=5,
        description="Matériau de base",
        rarete="commun"
    )
    joueur.ajouter_objet(materiau_commun)

    # 10. Matériau peu commun (nouvelle rareté)
    materiau_peu_commun = Objet(
        nom="Cristal Magique [TEST]",
        type_objet="matériau",
        quantite=3,
        description="Cristal chargé d'énergie",
        rarete="peu commun"
    )
    joueur.ajouter_objet(materiau_peu_commun)

    print("   ✅ 12 objets de test ajoutés à l'inventaire")
    print("      → Potions : Commun, Rare, Épique, Légendaire")
    print("      → Armes : Commun, Rare, Épique")
    print("      → Armures : Torse Légendaire, Casque Épique, Bottes Rare")
    print("      → Matériaux : Commun, Peu Commun")
