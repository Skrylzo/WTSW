# menus/debug.py
# Système de debug pour faciliter les tests

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

        # Recalculer les stats avec le nouveau niveau
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
        print(f"   ✅ Points d'attribut : {joueur.points_attribut}")
        print(f"   ✅ Royaume complété : Oui (téléportation débloquée)")
        print()
