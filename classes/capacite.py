# classes/capacite.py

import random

class Capacite:
    def __init__(self, id_cap, nom, description, cout_mana=0, cout_energie=0, cout_rage=0, degats_fixes=0, soin_fixe=0, effet_data=None, type_cible="unique", niveau_requis=1, peut_critiquer=False, niveau_amelioration=1):
        self.id = id_cap
        self.nom = nom
        self.description = description
        self.cout_mana = cout_mana
        self.cout_energie = cout_energie
        self.cout_rage = cout_rage
        self.degats_fixes = degats_fixes
        self.soin_fixe = soin_fixe
        self.effet_data = effet_data
        self.type_cible = type_cible
        self.niveau_requis = niveau_requis
        self.peut_critiquer = peut_critiquer
        self.niveau_amelioration = niveau_amelioration  # Niveau d'amélioration de la capacité (1 = base, 2+ = améliorée)
        self._degats_base = degats_fixes  # Valeur de base pour les calculs d'amélioration
        self._soin_base = soin_fixe  # Valeur de base pour les calculs d'amélioration
        self._effet_base = effet_data.copy() if effet_data else None  # Copie de l'effet de base

    def utiliser(self, lanceur, cible=None):
        # IMPORTER ICI, JUSTE AVANT L'UTILISATION POUR ÉVITER LES DÉPENDANCES CIRCULAIRES
        from combat.calculs import calculer_degats_finaux

        resource_type = lanceur.specialisation.type_ressource
        cost_value = 0
        current_resource_amount = 0
        resource_name = ""

        if resource_type == "Mana":
            cost_value = self.cout_mana
            current_resource_amount = lanceur.mana
            resource_name = "Mana"
        elif resource_type == "Energie":
            cost_value = self.cout_energie
            current_resource_amount = lanceur.energie
            resource_name = "Énergie"
        elif resource_type == "Rage":
            cost_value = self.cout_rage
            current_resource_amount = lanceur.rage
            resource_name = "Rage"
        else:
            print(f"Erreur: Type de ressource '{resource_type}' non géré pour la spécialisation {lanceur.specialisation.nom}.")
            return False

        # Vérification des ressources avant toute autre action
        if cost_value > 0 and current_resource_amount < cost_value:
            print(f"Vous n'avez pas assez de {resource_name} ({current_resource_amount:.1f}/{cost_value}) pour utiliser {self.nom}!")
            return False

        # Déduction du coût de la ressource
        if cost_value > 0:
            if resource_type == "Mana":
                lanceur.mana -= cost_value
            elif resource_type == "Energie":
                lanceur.energie -= cost_value
            elif resource_type == "Rage":
                lanceur.rage -= cost_value
            print(f"  {lanceur.nom} dépense {cost_value:.1f} {resource_name}. {resource_name} restante: {getattr(lanceur, resource_type.lower()):.1f}/{getattr(lanceur, resource_type.lower() + '_max'):.1f}")


        print(f"{lanceur.nom} utilise {self.nom}!")

        # Gérer les cibles de manière uniforme
        targets_to_affect = []
        if self.type_cible == "soi":
            targets_to_affect = [lanceur]
        elif isinstance(cible, list): # AOE ou aoe_mixte
            targets_to_affect = cible
        elif cible: # Cible unique
            targets_to_affect = [cible]

        for t in targets_to_affect:
            if t and t.est_vivant: # S'assurer que la cible existe et est vivante
                if self.degats_fixes > 0:
                    # Appliquer les dégâts fixes de la capacité en passant par calculer_degats_finaux
                    # Cela assure que la défense et les critiques sont correctement pris en compte.
                    degats_bruts = self.degats_fixes
                    if self.peut_critiquer and random.randint(1, 100) <= lanceur.calculer_chance_critique_totale():
                        degats_bruts *= 1.5
                        print("  Coup critique!")

                    degats_finaux = calculer_degats_finaux(lanceur, t, degats_bruts, est_capacite=True)
                    print(f"  {lanceur.nom} inflige {degats_finaux:.1f} points de dégâts à {t.nom}.")
                    t.prendre_degats(degats_finaux)
                if self.effet_data:
                    t.appliquer_effet(self.effet_data)

        # Le soin est appliqué au lanceur (pas à la cible) pour les capacités qui drainent la vie
        # Sauf si la capacité cible "soi" ou "aoe_amis" où le soin va aux alliés
        if self.soin_fixe > 0:
            if self.type_cible == "soi" or self.type_cible == "aoe_amis":
                # Pour les capacités de soin, soigner la/les cible(s)
                for t in targets_to_affect:
                    if t and t.est_vivant:
                        vie_recuperee = t.soigner(self.soin_fixe, afficher_message=False)
                        if vie_recuperee > 0:
                            from utils.affichage import COULEURS, formater_nombre
                            vie_recuperee_int = int(vie_recuperee)
                            print(f"  {COULEURS['VERT']}💚 {t.nom} récupère {formater_nombre(vie_recuperee_int)} points de vie grâce à {self.nom}. Vie actuelle : {int(t.vie)}/{int(t.vie_max)}{COULEURS['RESET']}")
            else:
                # Pour les capacités offensives avec drain de vie, soigner le lanceur
                vie_recuperee = lanceur.soigner(self.soin_fixe, afficher_message=False)
                if vie_recuperee > 0:
                    from utils.affichage import COULEURS, formater_nombre
                    vie_recuperee_int = int(vie_recuperee)
                    print(f"  {COULEURS['VERT']}💚 {lanceur.nom} récupère {formater_nombre(vie_recuperee_int)} points de vie grâce à {self.nom}. Vie actuelle : {int(lanceur.vie)}/{int(lanceur.vie_max)}{COULEURS['RESET']}")

        return True

    def ameliorer(self):
        """
        Améliore la capacité en augmentant ses stats.
        Chaque niveau d'amélioration augmente les dégâts/soins de 20% et les effets de 15%.
        """
        self.niveau_amelioration += 1

        # Améliorer les dégâts (20% par niveau)
        if self._degats_base > 0:
            bonus_degats = self._degats_base * 0.20 * (self.niveau_amelioration - 1)
            self.degats_fixes = int(self._degats_base + bonus_degats)

        # Améliorer le soin (20% par niveau)
        if self._soin_base > 0:
            bonus_soin = self._soin_base * 0.20 * (self.niveau_amelioration - 1)
            self.soin_fixe = int(self._soin_base + bonus_soin)

        # Améliorer les effets (15% par niveau)
        if self._effet_base:
            self.effet_data = self._effet_base.copy()
            # Améliorer les effets numériques
            if "effet_attaque" in self.effet_data:
                base_effet = abs(self._effet_base.get("effet_attaque", 0))
                bonus = base_effet * 0.15 * (self.niveau_amelioration - 1)
                if self._effet_base.get("effet_attaque", 0) < 0:
                    self.effet_data["effet_attaque"] = -(base_effet + bonus)
                else:
                    self.effet_data["effet_attaque"] = base_effet + bonus

            if "effet_defense" in self.effet_data:
                base_effet = self._effet_base.get("effet_defense", 0)
                bonus = base_effet * 0.15 * (self.niveau_amelioration - 1)
                self.effet_data["effet_defense"] = int(base_effet + bonus)

            if "effet_vie" in self.effet_data:
                base_effet = abs(self._effet_base.get("effet_vie", 0))
                bonus = base_effet * 0.15 * (self.niveau_amelioration - 1)
                if self._effet_base.get("effet_vie", 0) < 0:
                    self.effet_data["effet_vie"] = -(base_effet + bonus)
                else:
                    self.effet_data["effet_vie"] = base_effet + bonus

    def obtenir_nom_avec_niveau(self):
        """Retourne le nom de la capacité avec son niveau d'amélioration."""
        if self.niveau_amelioration > 1:
            return f"{self.nom} (Niveau {self.niveau_amelioration})"
        return self.nom
