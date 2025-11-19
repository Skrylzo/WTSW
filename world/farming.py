# world/farming.py
# Système de farming et réapparition des ennemis

class SystemeFarming:
    """
    Gère le système de farming et de réapparition des ennemis.
    Permet au joueur de re-combattre les mobs et boss autant de fois qu'il veut.
    """

    def __init__(self):
        self.enregistrements_boss = {}  # Dict {biome_id: {boss_vaincu: bool, nb_defaites: int}}
        self.enregistrements_zones = {}  # Dict {zone_id: {nb_visites: int, dernier_combat: timestamp}}

    def peut_re_combattre_mob(self, zone_id):
        """
        Vérifie si le joueur peut re-combattre les mobs d'une zone.
        Réponse : Toujours True (farming illimité).
        :param zone_id: ID de la zone
        :return: True (toujours)
        """
        return True  # Les mobs réapparaissent toujours

    def peut_re_combattre_boss(self, biome_id):
        """
        Vérifie si le joueur peut re-combattre le boss d'un biome.
        Réponse : Toujours True (farming illimité).
        :param biome_id: ID du biome
        :return: True (toujours)
        """
        return True  # Les boss peuvent être re-combattus

    def enregistrer_victoire_boss(self, biome_id):
        """
        Enregistre une victoire contre le boss d'un biome.
        :param biome_id: ID du biome
        """
        if biome_id not in self.enregistrements_boss:
            self.enregistrements_boss[biome_id] = {
                "boss_vaincu": True,
                "nb_defaites": 0
            }
        self.enregistrements_boss[biome_id]["boss_vaincu"] = True
        self.enregistrements_boss[biome_id]["nb_defaites"] += 1

    def enregistrer_exploration(self, zone_id):
        """
        Enregistre une exploration de zone.
        :param zone_id: ID de la zone
        """
        if zone_id not in self.enregistrements_zones:
            self.enregistrements_zones[zone_id] = {
                "nb_visites": 0
            }
        self.enregistrements_zones[zone_id]["nb_visites"] += 1

    def obtenir_statistiques_boss(self, biome_id):
        """
        Retourne les statistiques de combat contre le boss d'un biome.
        :param biome_id: ID du biome
        :return: Dict avec statistiques ou None
        """
        return self.enregistrements_boss.get(biome_id)

    def obtenir_statistiques_zone(self, zone_id):
        """
        Retourne les statistiques d'exploration d'une zone.
        :param zone_id: ID de la zone
        :return: Dict avec statistiques ou None
        """
        return self.enregistrements_zones.get(zone_id)


# Instance globale du système de farming
SYSTEME_FARMING = SystemeFarming()
