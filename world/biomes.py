# world/biomes.py
# Définition des biomes (zones naturelles) dans les royaumes

class Biome:
    """
    Représente un biome dans un royaume.
    Un biome contient des mobs, peut-être un donjon et un boss.
    """

    def __init__(self, nom, description="", mobs_ids=None, donjon_nom="", boss_id="", difficulte=1):
        """
        :param nom: Nom du biome (ex: "La Forêt de Lumière Argentée")
        :param description: Description du biome
        :param mobs_ids: Liste des IDs d'ennemis qui spawnent dans ce biome
        :param donjon_nom: Nom du donjon de ce biome (optionnel)
        :param boss_id: ID du boss du donjon (optionnel)
        :param difficulte: Niveau de difficulté (1-10, pour gérer la progression)
        """
        self.nom = nom
        self.description = description
        self.mobs_ids = mobs_ids or []  # Liste des IDs d'ennemis disponibles dans ce biome
        self.donjon_nom = donjon_nom  # Nom du donjon (peut être vide)
        self.boss_id = boss_id  # ID du boss final du donjon (peut être vide)
        self.difficulte = difficulte  # Niveau de difficulté du biome
        self.est_debloque = False  # Pour la progression
        self.boss_vaincu = False  # Si le boss a été vaincu (peut être re-combattu)

        # IMPORTANT : Les mobs et boss peuvent être re-farmés
        # Vaincre le boss ne verrouille pas la zone, elle reste accessible

    def obtenir_mobs_aleatoires(self, nombre=1):
        """
        Retourne une liste aléatoire de mobs de ce biome.
        :param nombre: Nombre de mobs à retourner
        :return: Liste d'IDs d'ennemis
        """
        import random
        if not self.mobs_ids:
            return []
        # Retourne une liste de mobs aléatoires (avec répétitions possibles)
        return random.choices(self.mobs_ids, k=nombre)

    def __repr__(self):
        return f"Biome(nom='{self.nom}', difficulte={self.difficulte})"


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
