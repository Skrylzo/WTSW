# classes/effet.py

class Effet:
    def __init__(self, data):
        self.nom = data.get("nom", "Effet Inconnu")
        self.description = data.get("description", "")
        self.duree = data.get("duree", 1)  # Durée initiale (totale)
        self.duree_actuelle = data.get("duree", 1)  # Durée restante, pour l'affichage et la décrémentation
        self.condition = data.get("condition", "tour")
        self.deja_applique = data.get("deja_applique", False)  # Indique si l'effet a déjà été "activé" (pour le message initial)

        self.effet_attaque = data.get("effet_attaque", 0)
        self.effet_defense = data.get("effet_defense", 0)
        self.effet_vitesse = data.get("effet_vitesse", 0)
        self.effet_critique = data.get("effet_critique", 0)
        self.effet_vie = data.get("effet_vie", 0) # Dégâts si négatif, Soin si positif
        self.effet_regen_mana = data.get("effet_regen_mana", 0)
        self.effet_regen_energie = data.get("effet_regen_energie", 0)

    def verifier_condition(self, combatant, phase):
        """
        Vérifie si la condition de l'effet est remplie.
        :param combatant: Le combatant sur lequel l'effet est appliqué
        :param phase: La phase actuelle du combat ('tour', 'debut', etc.)
        :return: True si la condition est remplie, False sinon
        """
        if self.condition is None:
            return True
        if isinstance(self.condition, str):
            if self.condition == phase:
                # Conditions spéciales basées sur la phase
                if phase == 'sous_30hp':
                    return combatant.vie <= (combatant.vie_max * 0.3)
                elif phase == 'mort_imminente':
                    return combatant.vie <= 0 or not combatant.est_vivant
                return True
            return False
        return False

    def __str__(self):
        return f"{self.nom} ({self.duree_actuelle} tours restants)"
