# classes/armure.py

class Armure:
    def __init__(self, nom, sous_type, bonus_defense=0, bonus_force=0, bonus_agilite=0, bonus_intelligence=0, bonus_vitalite=0, bonus_mana=0, bonus_energie=0, bonus_rage=0, rarete=None):
        """
        Classe représentant une armure équipable.

        :param nom: Nom de l'armure
        :param sous_type: Type d'armure ('torse', 'casque', 'bottes')
        :param bonus_defense: Bonus de défense
        :param bonus_force: Bonus de force
        :param bonus_agilite: Bonus d'agilité
        :param bonus_intelligence: Bonus d'intelligence
        :param bonus_vitalite: Bonus de vitalité
        :param bonus_mana: Bonus de mana max
        :param bonus_energie: Bonus d'énergie max
        :param bonus_rage: Bonus de rage max
        :param rarete: Rareté de l'armure (pour l'affichage)
        """
        self.nom = nom
        self.sous_type = sous_type  # 'torse', 'casque', 'bottes'
        self.bonus_defense = bonus_defense
        self.bonus_force = bonus_force
        self.bonus_agilite = bonus_agilite
        self.bonus_intelligence = bonus_intelligence
        self.bonus_vitalite = bonus_vitalite
        self.bonus_mana = bonus_mana
        self.bonus_energie = bonus_energie
        self.bonus_rage = bonus_rage
        self.rarete = rarete  # Rareté de l'armure (pour l'affichage)

    def __str__(self):
        return self.nom
