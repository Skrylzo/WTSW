# classes/objet.py

class Objet:
    """
    Classe représentant un objet dans l'inventaire.
    Préparée pour le système de crafting futur.
    """
    def __init__(self, nom, type_objet, quantite=1, description="", rarete=None, niveau_biome=None):
        """
        :param nom: Nom de l'objet
        :param type_objet: Type de l'objet ("matériau", "potion", "équipement", "consommable")
        :param quantite: Quantité de l'objet (défaut: 1)
        :param description: Description de l'objet (défaut: "")
        :param rarete: Rareté de l'objet (optionnel, ex: "commun", "rare", "épique", "légendaire")
        :param niveau_biome: Niveau minimum du biome d'origine (pour calculer les bonus de craft)
        """
        self.nom = nom
        self.type = type_objet
        self.quantite = quantite
        self.description = description
        self.rarete = rarete
        self.niveau_biome = niveau_biome  # Niveau minimum du biome d'origine

    def __str__(self):
        """Représentation textuelle de l'objet"""
        affichage = f"{self.nom}"
        if self.quantite > 1:
            affichage += f" x{self.quantite}"
        if self.rarete:
            affichage += f" [{self.rarete}]"
        if self.description:
            affichage += f" - {self.description}"
        return affichage

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour la sauvegarde"""
        return {
            "nom": self.nom,
            "type": self.type,
            "quantite": self.quantite,
            "description": self.description,
            "rarete": self.rarete,
            "niveau_biome": self.niveau_biome
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet à partir d'un dictionnaire (pour le chargement)"""
        return cls(
            nom=data.get("nom", ""),
            type_objet=data.get("type", "matériau"),
            quantite=data.get("quantite", 1),
            description=data.get("description", ""),
            rarete=data.get("rarete", None),
            niveau_biome=data.get("niveau_biome", None)
        )
