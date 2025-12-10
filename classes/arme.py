# classes/arme.py

class Arme:
    def __init__(self, nom, degats_base, bonus_force=0, bonus_agilite=0, bonus_intelligence=0, bonus_vitalite=0, bonus_mana=0, bonus_energie=0, bonus_rage=0, rarete=None):
        self.nom = nom
        self.degats_base = degats_base
        self.bonus_force = bonus_force
        self.bonus_agilite = bonus_agilite
        self.bonus_intelligence = bonus_intelligence
        self.bonus_vitalite = bonus_vitalite
        self.bonus_mana = bonus_mana
        self.bonus_energie = bonus_energie
        self.bonus_rage = bonus_rage
        self.rarete = rarete  # Rareté de l'arme (pour l'affichage)

    def __str__(self):
        return self.nom
