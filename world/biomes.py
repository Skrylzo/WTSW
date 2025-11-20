# world/biomes.py
# Définition des biomes (zones naturelles) dans les royaumes

class Biome:
    """
    Représente un biome dans un royaume.
    Un biome contient des mobs, peut-être un donjon et un boss.
    """

    def __init__(self, nom, description="", mobs_ids=None, donjon_nom="", boss_id="", difficulte=1, niveau_min=None, niveau_max=None):
        """
        :param nom: Nom du biome (ex: "La Forêt de Lumière Argentée")
        :param description: Description du biome
        :param mobs_ids: Liste des IDs d'ennemis qui spawnent dans ce biome
        :param donjon_nom: Nom du donjon de ce biome (optionnel)
        :param boss_id: ID du boss du donjon (optionnel)
        :param difficulte: Niveau de difficulté (1-10, pour gérer la progression)
        :param niveau_min: Niveau minimum recommandé pour ce biome (optionnel, calculé depuis difficulte si None)
        :param niveau_max: Niveau maximum recommandé pour ce biome (optionnel, calculé depuis difficulte si None)
        """
        self.nom = nom
        self.description = description
        self.mobs_ids = mobs_ids or []  # Liste des IDs d'ennemis disponibles dans ce biome
        self.donjon_nom = donjon_nom  # Nom du donjon (peut être vide)
        self.boss_id = boss_id  # ID du boss final du donjon (peut être vide)
        self.difficulte = difficulte  # Niveau de difficulté du biome
        self.est_debloque = False  # Pour la progression
        self.boss_vaincu = False  # Si le boss a été vaincu (peut être re-combattu)

        # Calculer niveau_min et niveau_max si non fournis (progression par blocs de 5 niveaux)
        # Biome 1 (difficulte 1) : 1-5, Biome 2 : 5-10, Biome 3 : 10-15, etc.
        if niveau_min is None:
            # Progression avec chevauchement : (1-5), (5-10), (10-15), (15-20), etc.
            # Biome 1: 1, Biome 2: 5, Biome 3: 10, Biome 4: 15...
            self.niveau_min = (difficulte - 1) * 5 if difficulte > 1 else 1
        else:
            self.niveau_min = niveau_min

        if niveau_max is None:
            # Chaque biome couvre 5 niveaux consécutifs
            # Biome 1: 5, Biome 2: 10, Biome 3: 15, Biome 4: 20...
            self.niveau_max = difficulte * 5
        else:
            self.niveau_max = niveau_max

        # IMPORTANT : Les mobs et boss peuvent être re-farmés
        # Vaincre le boss ne verrouille pas la zone, elle reste accessible

    def obtenir_mobs_aleatoires(self, nombre=1):
        """
        Retourne une liste aléatoire de mobs de ce biome.
        :param nombre: Nombre de mobs à retourner
        :return: Liste d'IDs d'ennemis

        TODO FUTURE AMÉLIORATION :
        - Implémenter un système de poids/probabilité pour les mobs
        - Actuellement, tous les mobs ont la même probabilité (sélection uniforme)
        - Idée : Ajouter un système de poids (comme les loot tables) pour ajuster
          les probabilités de spawn de chaque mob (ex: mob commun 80%, rare 20%)
        """
        import random
        if not self.mobs_ids:
            return []
        # Retourne une liste de mobs aléatoires (avec répétitions possibles)
        # TODO: Système de poids pour différencier la probabilité des mobs
        return random.choices(self.mobs_ids, k=nombre)

    def afficher_niveau_recommande(self):
        """Retourne une string avec le niveau recommandé du biome."""
        if self.niveau_min == self.niveau_max:
            return f"Niveau {self.niveau_min}"
        return f"Niveau {self.niveau_min}-{self.niveau_max}"

    def __repr__(self):
        return f"Biome(nom='{self.nom}', difficulte={self.difficulte}, niveau={self.niveau_min}-{self.niveau_max})"


class Zone:
    """
    Représente une zone spécifique dans un biome (plus granulaire).
    Pour l'instant, c'est un alias/concept pour les futures zones d'exploration.
    """

    def __init__(self, nom, biome_parent, description=""):
        """
        :param nom: Nom de la zone
        :param biome_parent: Biome auquel cette zone appartient
        :param description: Description de la zone
        """
        self.nom = nom
        self.biome_parent = biome_parent
        self.description = description
        self.mobs_ids = biome_parent.mobs_ids  # Hérite des mobs du biome par défaut
