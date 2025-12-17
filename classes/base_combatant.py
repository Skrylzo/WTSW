# classes/base_combatant.py
# Classe parent BaseCombatant avec ses enfants Personnage et Ennemi

from .effet import Effet
from .specialisation import Specialisation
from .capacite import Capacite
from .objet import Objet
from .arme import Arme
from .armure import Armure
# Importation des données du jeu
from data.races_classes import DEFINITIONS_RACES_CLASSES
from data.capacites import TOUTES_LES_CAPACITES_DATA
from data.ennemis import DEFINITIONS_ENNEMIS
from data.armes import DEFINITIONS_ARMES


class BaseCombatant:
    def __init__(self, nom, vie_max, vitesse, attaque, defense, chance_critique):
        self.nom = nom
        self.vie_max = vie_max
        self.vie = vie_max # La vie actuelle commence au maximum
        # Stocker les stats de base (utilisées pour calculer les stats finales avec effets)
        self.base_vitesse = vitesse
        self.base_attaque = attaque
        self.base_defense = defense
        self.base_chance_critique = chance_critique
        # Les stats finales sont calculées dynamiquement via obtenir_stat_modifiee()
        # mais on garde des attributs pour compatibilité avec le code existant
        self.est_vivant = True # Attribut pour l'état de vie
        self.effets_actifs = [] # Liste pour stocker les effets actifs

    def prendre_degats(self, degats):
        # Vérifier l'invulnérabilité
        if self.est_invulnerable():
            print(f"{self.nom} est invulnérable et ignore les dégâts !")
            return

        # Cette méthode prend les dégâts finaux après toutes les réductions.
        self.vie -= degats
        if self.vie <= 0:
            self.vie = 0
            self.est_vivant = False # Mise à jour de l'attribut est_vivant
        print(f"{self.nom} subit {degats:.1f} dégâts. Vie restante : {self.vie:.1f}/{self.vie_max:.1f}")
        print()

    def soigner(self, montant, afficher_message=True):
        vie_avant = self.vie
        self.vie += montant
        self.vie = min(self.vie, self.vie_max) # Ne pas dépasser la vie max
        vie_recuperee = self.vie - vie_avant
        if afficher_message and vie_recuperee > 0:
            from utils.affichage import COULEURS, COULEURS_STATS, formater_nombre
            vie_recuperee_int = int(vie_recuperee)
            print(f"{COULEURS_STATS['vie']}💚 {self.nom} récupère {formater_nombre(vie_recuperee_int)} points de vie. Vie actuelle : {int(self.vie)}/{int(self.vie_max)}{COULEURS['RESET']}")
        return vie_recuperee

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")
        print()
        return self.calculer_attaque_totale()


    def appliquer_effet(self, effet_data):
        # Vérifier si l'effet existe déjà et renouveler sa durée ou l'ajouter
        for effet_existant in self.effets_actifs:
            if effet_existant.nom == effet_data["nom"]:
                effet_existant.duree = effet_data.get("duree", 1) # Renouveler la durée totale
                effet_existant.duree_actuelle = effet_data.get("duree", 1) # Renouveler la durée actuelle
                effet_existant.deja_applique = False  # Réinitialiser pour afficher le message à nouveau
                print(f"{self.nom} : Durée de l'effet {effet_existant.nom} renouvelée.")
                return

        # Si l'effet n'existe pas, l'ajouter
        effet = Effet(effet_data)
        self.effets_actifs.append(effet)
        # Le message d'activation initial s'affiche une seule fois
        if not effet.deja_applique:
            print(f"{self.nom} est affecté par {effet.nom} ({effet.description}).")
            effet.deja_applique = True

    def retirer_effets_expires(self):
        # Décrémenter les effets avec condition "etourdi" et "invulnerable" à la fin du tour
        for effet in list(self.effets_actifs):
            if effet.condition == "etourdi" or effet.condition == "invulnerable":
                effet.duree_actuelle -= 1
                if effet.duree_actuelle <= 0:
                    print(f"{self.nom} n'est plus affecté par {effet.nom}.")
                    self.effets_actifs.remove(effet)

        # Retirer les autres effets expirés
        for effet in list(self.effets_actifs):
            if effet.duree_actuelle <= 0:
                self.effets_actifs.remove(effet)

    def est_etourdi(self):
        """
        Vérifie si le combatant est étourdi (ne peut pas agir ce tour).
        :return: True si étourdi, False sinon
        """
        for effet in self.effets_actifs:
            if effet.condition == "etourdi" and effet.duree_actuelle > 0:
                return True
        return False

    def est_invulnerable(self):
        """
        Vérifie si le combatant est invulnérable (ignore les dégâts).
        :return: True si invulnérable, False sinon
        """
        for effet in self.effets_actifs:
            if effet.condition == "invulnerable" and effet.duree_actuelle > 0:
                return True
        return False

    def appliquer_effets(self, phase):
        for effet in list(self.effets_actifs):
            # Vérifier si la condition de l'effet est remplie
            if not effet.verifier_condition(self, phase):
                continue

            # Appliquer les effets de stats (attaque, défense, vitesse, critique)
            # Ces effets sont appliqués via obtenir_stat_modifiee() dans les calculs

            # Appliquer les dégâts/soins et régénération pour les effets "tour"
            if effet.condition == "tour" or effet.condition is None:
                # Appliquer les dégâts ou soins de l'effet
                if effet.effet_vie:
                    # Si effet_vie est positif, c'est un soin. Si négatif, c'est des dégâts.
                    if effet.effet_vie < 0: # C'est des dégâts sur la durée
                        self.prendre_degats(-effet.effet_vie) # On prend la valeur absolue pour les dégâts
                    else: # C'est un soin sur la durée
                        self.soigner(effet.effet_vie)

                if hasattr(self, 'mana') and effet.effet_regen_mana:
                    self.mana = min(self.mana + effet.effet_regen_mana, self.mana_max)
                    print(f"{self.nom} régénère {effet.effet_regen_mana} Mana grâce à {effet.nom}.")
                if hasattr(self, 'energie') and effet.effet_regen_energie:
                    self.energie = min(self.energie + effet.effet_regen_energie, self.energie_max)
                    print(f"{self.nom} régénère {effet.effet_regen_energie} Énergie grâce à {effet.nom}.")

                # Décrémenter la durée après application de l'effet
                effet.duree_actuelle -= 1
                if effet.duree_actuelle <= 0:
                    print(f"{self.nom} n'est plus affecté par {effet.nom}.")
                    self.effets_actifs.remove(effet)
            elif effet.condition == "debut":
                # Les effets "debut" s'appliquent une fois au début du combat
                # Ils ne se décrémentent pas automatiquement
                pass
            elif effet.condition == "sous_30hp":
                # Effets qui s'activent quand la vie est sous 30%
                # Ces effets peuvent avoir des effets de stats qui sont appliqués via obtenir_stat_modifiee()
                pass
            elif effet.condition == "mort_imminente":
                # Effets qui s'activent à la mort (comme réincarnation)
                # Ces effets sont gérés spécialement dans le code de combat
                pass


    def obtenir_stat_modifiee(self, stat_nom):
        """
        Calcule la valeur d'une stat en prenant en compte les effets actifs.
        Utilise les stats de base (base_attaque, base_defense, etc.) comme point de départ.
        """
        # Obtenir la stat de base correspondante
        if stat_nom == "attaque":
            valeur = self.base_attaque
        elif stat_nom == "defense":
            valeur = self.base_defense
        elif stat_nom == "vitesse":
            valeur = self.base_vitesse
        elif stat_nom == "chance_critique":
            valeur = self.base_chance_critique
        else:
            # Pour les autres stats, utiliser la valeur actuelle
            valeur = getattr(self, stat_nom, 0)

        # Ajouter les bonus/malus des effets actifs
        for effet in self.effets_actifs:
            effet_attr = getattr(effet, f"effet_{stat_nom}", 0)
            valeur += effet_attr
        return valeur

    def calculer_attaque_totale(self):
        """Calcule l'attaque totale (base + effets)."""
        return self.obtenir_stat_modifiee("attaque")

    def calculer_defense_totale(self):
        """Calcule la défense totale (base + effets)."""
        return self.obtenir_stat_modifiee("defense")

    def calculer_vitesse_totale(self):
        """Calcule la vitesse totale (base + effets)."""
        return self.obtenir_stat_modifiee("vitesse")

    def calculer_chance_critique_totale(self):
        """Calcule la chance critique totale (base + effets)."""
        return self.obtenir_stat_modifiee("chance_critique")

    # Propriétés pour Personnage uniquement - calculent dynamiquement les stats avec effets
    @property
    def attaque(self):
        """Propriété pour obtenir l'attaque totale (base + effets)."""
        return self.calculer_attaque_totale()

    @property
    def defense(self):
        """Propriété pour obtenir la défense totale (base + effets)."""
        return self.calculer_defense_totale()

    @property
    def vitesse(self):
        """Propriété pour obtenir la vitesse totale (base + effets)."""
        return self.calculer_vitesse_totale()

    @property
    def chance_critique(self):
        """Propriété pour obtenir la chance critique totale (base + effets)."""
        return self.calculer_chance_critique_totale()


class Personnage(BaseCombatant):
    def __init__(self, nom, race, specialisation_nom, force, agilite, vitalite, intelligence, arme=None):
        self.race = race
        self.force = force
        self.agilite = agilite
        self.vitalite = vitalite
        self.intelligence = intelligence
        self.niveau = 1
        self.xp = 0
        self.xp_requise = 100
        self.points_attribut = 0

        spec_data = DEFINITIONS_RACES_CLASSES[race]["classes"][specialisation_nom]
        self.specialisation = Specialisation(
            nom=specialisation_nom,
            description=spec_data['description'],
            type_ressource=spec_data.get('type_ressource', 'Mana'),
            capacites_initiales=spec_data.get('capacites_ids', [])
        )

        super().__init__(nom, vie_max=1, vitesse=1, attaque=1, defense=1, chance_critique=1)

        self.mana = 0.0
        self.mana_max = 0.0
        self.energie = 0.0
        self.energie_max = 0.0
        self.rage = 0.0
        self.rage_max = 0.0

        self.arme = arme
        self.armure_torse = None
        self.armure_casque = None
        self.armure_bottes = None
        self.inventaire = {}  # Dictionnaire {nom_objet: Objet} pour gérer les quantités
        self.or_ = 100  # Or de départ pour le commerce

        self.capacites_apprises = []
        self._initialiser_capacites()
        self.mettre_a_jour_stats_apres_attributs()

        # S'assurer que la vie est à max après le calcul des stats
        self.vie = self.vie_max

        # Initialise les ressources à max après avoir calculé les max
        if self.specialisation.type_ressource == "Mana":
            self.mana = self.mana_max
        elif self.specialisation.type_ressource == "Energie":
            self.energie = self.energie_max
        elif self.specialisation.type_ressource == "Rage":
            self.rage = 0


    def _initialiser_capacites(self):
        # Seules les capacités de niveau 1 sont apprises au départ
        # Les autres doivent être apprises via le menu de formation
        for cap_id in self.specialisation.capacites_initiales:
            cap_data = TOUTES_LES_CAPACITES_DATA.get(cap_id)
            if cap_data:
                niveau_requis = cap_data.get("niveau_requis", 1)
                # Ne charger que les capacités de niveau 1 au départ
                if niveau_requis == 1:
                    capacite = Capacite(
                        id_cap=cap_id,
                        nom=cap_data["nom"],
                        description=cap_data["description"],
                        cout_mana=cap_data.get("cout_mana", 0),
                        cout_energie=cap_data.get("cout_energie", 0),
                        cout_rage=cap_data.get("cout_rage", 0),
                        degats_fixes=cap_data.get("degats_fixes", 0),
                        soin_fixe=cap_data.get("soin_fixe", 0),
                        effet_data=cap_data.get("effet_data"),
                        type_cible=cap_data.get("type_cible", "unique"),
                        niveau_requis=niveau_requis,
                        peut_critiquer=cap_data.get("peut_critiquer", False)
                    )
                    self.capacites_apprises.append(capacite)
            else:
                print(f"Avertissement: Capacité '{cap_id}' introuvable dans TOUTES_LES_CAPACITES_DATA.")

    def mettre_a_jour_stats_apres_attributs(self):
        """
        Recalcule les stats de base à partir des attributs.
        Ne modifie PAS les stats finales (attaque, defense, etc.) qui sont calculées dynamiquement
        via obtenir_stat_modifiee() pour prendre en compte les effets.
        """
        # Calculer les attributs totaux en incluant les bonus des armures
        force_totale = self.force
        agilite_totale = self.agilite
        vitalite_totale = self.vitalite
        intelligence_totale = self.intelligence

        # Ajouter les bonus d'attributs des armures
        armures_equipees = [self.armure_torse, self.armure_casque, self.armure_bottes]
        for armure in armures_equipees:
            if armure:
                force_totale += armure.bonus_force
                agilite_totale += armure.bonus_agilite
                vitalite_totale += armure.bonus_vitalite
                intelligence_totale += armure.bonus_intelligence

        # Calculer les stats de base avec les attributs totaux
        self.base_attaque = force_totale * 2
        self.base_defense = (force_totale * 0.5) + (vitalite_totale * 0.3)
        self.base_vitesse = agilite_totale * 1.2
        self.base_chance_critique = 5 + (agilite_totale * 0.3) + (intelligence_totale * 0.2)

        # Calculer les valeurs max avec les attributs totaux (incluant les bonus d'armures)
        self.vie_max = 50 + (vitalite_totale * 5) + (self.niveau - 1) * 5

        self.mana_max = 0.0
        self.energie_max = 0.0
        self.rage_max = 0.0

        if self.specialisation.type_ressource == "Mana":
            self.mana_max = 30 + (intelligence_totale * 3) + (self.niveau - 1) * 3
        elif self.specialisation.type_ressource == "Energie":
            self.energie_max = 100 + (agilite_totale * 2) + (force_totale * 2) + (self.niveau - 1) * 5
        elif self.specialisation.type_ressource == "Rage":
            self.rage_max = 100 + (vitalite_totale * 1) + (force_totale * 0.5)

        # Ajouter les bonus de l'arme
        if self.arme:
            self.base_attaque += self.arme.degats_base
            self.vie_max += self.arme.bonus_vitalite * 5
            self.mana_max += self.arme.bonus_mana
            self.energie_max += self.arme.bonus_energie
            self.rage_max += self.arme.bonus_rage

        # Ajouter les bonus directs des armures (défense, ressources)
        # Les bonus d'attributs sont déjà pris en compte dans le calcul ci-dessus
        for armure in armures_equipees:
            if armure:
                self.base_defense += armure.bonus_defense
                self.mana_max += armure.bonus_mana
                self.energie_max += armure.bonus_energie
                self.rage_max += armure.bonus_rage

        # NE PAS modifier directement self.attaque, self.defense, etc.
        # Ces valeurs sont calculées dynamiquement via obtenir_stat_modifiee()
        # pour prendre en compte les effets actifs.

        # Assurer que les valeurs actuelles ne dépassent pas les nouvelles max
        self.vie = min(self.vie, self.vie_max)
        self.mana = min(self.mana, self.mana_max)
        self.energie = min(self.energie, self.energie_max)
        self.rage = min(self.rage, self.rage_max)


    def calculer_reduction_degats_pourcentage(self):
        """
        Calcule le pourcentage de réduction des dégâts basé sur la défense totale.
        Utilise la défense totale (base + effets) pour le calcul.
        Une défense de 100 donnerait 50% de réduction. Une défense de 20 donnerait 16.6%
        Maximum de 90% de réduction pour éviter l'invulnérabilité totale.
        """
        defense_totale = self.calculer_defense_totale()
        return min(0.9, defense_totale / (defense_totale + 100))

    def depenser_points_attribut(self, attribut, montant):
        if montant <= 0:
            print("Le montant doit être supérieur à zéro.")
            return False
        if montant > self.points_attribut:
            print("Vous n'avez pas assez de points d'attribut.")
            return False

        if attribut == "force":
            self.force += montant
        elif attribut == "agilite":
            self.agilite += montant
        elif attribut == "vitalite":
            self.vitalite += montant
        elif attribut == "intelligence":
            self.intelligence += montant
        else:
            print("Attribut invalide.")
            return False
        self.points_attribut -= montant
        print(f"{montant} points dépensés en {attribut}. Points restants : {self.points_attribut}.")
        self.mettre_a_jour_stats_apres_attributs()
        return True

    def gagner_xp(self, montant):
        self.xp += montant
        print(f"{self.nom} gagne {montant} XP. Total : {self.xp}/{self.xp_requise}")
        while self.xp >= self.xp_requise:
            self.xp -= self.xp_requise
            self.xp_requise = int(self.xp_requise * 1.5)
            self.niveau_superieur()

    def niveau_superieur(self):
        self.niveau += 1
        self.points_attribut += 3

        print(f"\n{self.nom} atteint le Niveau {self.niveau}!")
        print(f"Vous avez {self.points_attribut} points d'attribut à dépenser.")

        self.mettre_a_jour_stats_apres_attributs()

        # Progresser les quêtes : niveau atteint
        if hasattr(self, 'systeme_quetes'):
            from world.progression_quetes import progresser_quetes_atteindre_niveau
            progresser_quetes_atteindre_niveau(self, self.niveau)

    def apprendre_capacite(self, capacite_id):
        # Vérification de l'ID de capacité
        if not capacite_id or not isinstance(capacite_id, str):
            print(f"ID de capacité invalide : {capacite_id}")
            return False

        # Vérifiez si la capacité n'est pas déjà apprise
        if any(cap.id == capacite_id for cap in self.capacites_apprises):
            print(f"{self.nom} connaît déjà la capacité {capacite_id}.")
            return False

        # Vérifier que la capacité existe dans les données
        if capacite_id not in TOUTES_LES_CAPACITES_DATA:
            print(f"Capacité {capacite_id} non trouvée dans les données du jeu.")
            return False

        cap_data = TOUTES_LES_CAPACITES_DATA[capacite_id]

        # Vérifier que les données essentielles sont présentes
        if not cap_data or "nom" not in cap_data:
            print(f"Données de capacité invalides pour {capacite_id}.")
            return False

        try:
            capacite = Capacite(
                id_cap=capacite_id,
                nom=cap_data["nom"],
                description=cap_data.get("description", ""),
                cout_mana=cap_data.get("cout_mana", 0),
                cout_energie=cap_data.get("cout_energie", 0),
                cout_rage=cap_data.get("cout_rage", 0),
                degats_fixes=cap_data.get("degats_fixes", 0),
                soin_fixe=cap_data.get("soin_fixe", 0),
                effet_data=cap_data.get("effet_data"),
                type_cible=cap_data.get("type_cible", "unique"),
                niveau_requis=cap_data.get("niveau_requis", 1),
                peut_critiquer=cap_data.get("peut_critiquer", False)
            )
            self.capacites_apprises.append(capacite)
            print(f"{self.nom} a appris la capacité {capacite.nom}.")
            return True
        except Exception as e:
            print(f"Erreur lors de l'apprentissage de la capacité {capacite_id} : {e}")
            return False

    def afficher_capacites(self):
        from utils.affichage import effacer_console, COULEURS
        effacer_console()

        if not self.capacites_apprises:
            print(f"{self.nom} n'a pas encore appris de capacités.")
            return

        print(f"\n--- Capacités de {COULEURS['CYAN']}{self.nom}{COULEURS['RESET']} ({self.specialisation.nom}) ---")
        print()
        for i, capacite in enumerate(self.capacites_apprises):
            # Pour l'affichage, on peut choisir de montrer toutes les capacités ou seulement celles débloquées.
            if self.niveau >= capacite.niveau_requis:
                # Couleur pour le coût selon le type de ressource (utiliser COULEURS_STATS pour cohérence)
                from utils.affichage import COULEURS_STATS
                cout_str = ""
                couleur_cout = COULEURS["CYAN"]
                if self.specialisation.type_ressource == "Mana" and capacite.cout_mana > 0:
                    couleur_cout = COULEURS_STATS["mana"]
                    cout_str = f"{couleur_cout}(Coût : {capacite.cout_mana} Mana){COULEURS['RESET']}"
                elif self.specialisation.type_ressource == "Energie" and capacite.cout_energie > 0:
                    couleur_cout = COULEURS_STATS["energie"]
                    cout_str = f"{couleur_cout}(Coût : {capacite.cout_energie} Énergie){COULEURS['RESET']}"
                elif self.specialisation.type_ressource == "Rage" and capacite.cout_rage > 0:
                    couleur_cout = COULEURS_STATS["rage"]
                    cout_str = f"{couleur_cout}(Coût : {capacite.cout_rage} Rage){COULEURS['RESET']}"

                print(f"{COULEURS['CYAN']}{i+1}. {COULEURS['MAGENTA']}{capacite.nom}{COULEURS['RESET']} {COULEURS['GRIS']}(Niveau requis: {capacite.niveau_requis}){COULEURS['RESET']}")
                print()
                print(f"   {COULEURS['GRIS']}Description: {capacite.description}{COULEURS['RESET']}")
                print()
                if cout_str:
                    print(f"   {cout_str}")
                    print()
                if capacite.degats_fixes > 0:
                    print(f"   {COULEURS['ROUGE']}Dégâts fixes: {capacite.degats_fixes}{COULEURS['RESET']}")
                    print()
                if capacite.soin_fixe > 0:
                    print(f"   {COULEURS['VERT']}Soin fixe: {capacite.soin_fixe}{COULEURS['RESET']}")
                    print()
                if capacite.effet_data:
                    print(f"   {COULEURS['MAGENTA']}Applique Effet: {capacite.effet_data['nom']} ({capacite.effet_data.get('duree',1)} tours){COULEURS['RESET']}")
                    print()
                print("-" * 20)
                print()
            else:
                pass # Ne rien afficher si la capacité n'est pas débloquée et qu'on ne veut pas la montrer.


    def afficher_stats(self):
        from utils.affichage import COULEURS

        # Codes ANSI pour le gras
        GRAS = "\033[1m"
        RESET = COULEURS["RESET"]

        print(f"\n--- Statistiques de {self.nom} (Niveau {self.niveau} {self.race} {self.specialisation.nom}) ---")

        # Vie avec couleur selon le pourcentage
        pourcentage_vie = (self.vie / self.vie_max) * 100 if self.vie_max > 0 else 0
        couleur_vie = COULEURS["VERT"] if pourcentage_vie > 60 else COULEURS["JAUNE"] if pourcentage_vie > 30 else COULEURS["ROUGE"]
        print(f"{couleur_vie}Vie : {self.vie:.1f}/{self.vie_max:.1f}{RESET}")

        # Ressource avec couleur (utiliser COULEURS_STATS pour cohérence)
        from utils.affichage import COULEURS_STATS
        if self.specialisation.type_ressource == "Mana":
            couleur_ressource = COULEURS_STATS["mana"]
            print(f"{couleur_ressource}Mana : {self.mana:.1f}/{self.mana_max:.1f}{RESET}")
        elif self.specialisation.type_ressource == "Energie":
            couleur_ressource = COULEURS_STATS["energie"]
            print(f"{couleur_ressource}Énergie : {self.energie:.1f}/{self.energie_max:.1f}{RESET}")
        elif self.specialisation.type_ressource == "Rage":
            couleur_ressource = COULEURS_STATS["rage"]
            print(f"{couleur_ressource}Rage : {self.rage:.1f}/{self.rage_max:.1f}{RESET}")

        # Identifier les meilleures et pires stats de combat
        stats_combat = {
            "Attaque": self.attaque,
            "Défense": self.defense,
            "Vitesse": self.vitesse,
            "Chance Critique": self.chance_critique
        }

        # Trouver les meilleures et pires stats
        stats_triees = sorted(stats_combat.items(), key=lambda x: x[1], reverse=True)
        meilleure_stat = stats_triees[0][0] if stats_triees else None
        pire_stat = stats_triees[-1][0] if stats_triees else None

        # Afficher les stats avec couleurs et gras
        def formater_stat(nom, valeur, suffixe=""):
            if nom == meilleure_stat:
                return f"{GRAS}{COULEURS['VERT']}{nom} : {valeur:.1f}{suffixe}{RESET}"
            elif nom == pire_stat and len(stats_triees) > 1 and stats_triees[0][1] != stats_triees[-1][1]:
                return f"{GRAS}{COULEURS['ROUGE']}{nom} : {valeur:.1f}{suffixe}{RESET}"
            else:
                return f"{COULEURS['CYAN']}{nom} : {valeur:.1f}{suffixe}{RESET}"

        print(formater_stat("Attaque", self.attaque))
        print(formater_stat("Défense", self.defense))
        print(formater_stat("Vitesse", self.vitesse))
        print(formater_stat("Chance Critique", self.chance_critique, "%"))

        print(f"{COULEURS['GRIS']}XP : {self.xp}/{self.xp_requise}{RESET}")
        print(f"{COULEURS['JAUNE']}Points d'Attribut : {self.points_attribut}{RESET}")

        from utils.affichage import COULEURS_RARETE

        # Afficher les équipements
        print("\n--- Équipements ---")

        # Arme équipée
        if self.arme:
            affichage_arme = f"Arme : {self.arme.nom} (Dégâts: {self.arme.degats_base})"
            if self.arme.rarete:
                rarete_lower = str(self.arme.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                affichage_arme += f" [{couleur}{self.arme.rarete.upper()}{COULEURS['RESET']}]"
            print(affichage_arme)
            bonus_arme = []
            if self.arme.bonus_force > 0: bonus_arme.append(f"Force: +{self.arme.bonus_force}")
            if self.arme.bonus_agilite > 0: bonus_arme.append(f"Agilité: +{self.arme.bonus_agilite}")
            if self.arme.bonus_intelligence > 0: bonus_arme.append(f"Intelligence: +{self.arme.bonus_intelligence}")
            if self.arme.bonus_vitalite > 0: bonus_arme.append(f"Vitalité: +{self.arme.bonus_vitalite}")
            if self.arme.bonus_mana > 0: bonus_arme.append(f"Mana: +{self.arme.bonus_mana}")
            if self.arme.bonus_energie > 0: bonus_arme.append(f"Énergie: +{self.arme.bonus_energie}")
            if self.arme.bonus_rage > 0: bonus_arme.append(f"Rage: +{self.arme.bonus_rage}")
            if bonus_arme:
                print(f"  Bonus : {', '.join(bonus_arme)}")
        else:
            print("Arme : Aucune")

        # Armure de torse
        if self.armure_torse:
            affichage_torse = f"Torse : {self.armure_torse.nom} (Défense: +{self.armure_torse.bonus_defense})"
            if self.armure_torse.rarete:
                rarete_lower = str(self.armure_torse.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                affichage_torse += f" [{couleur}{self.armure_torse.rarete.upper()}{COULEURS['RESET']}]"
            print(affichage_torse)
        else:
            print("Torse : Aucune")

        # Casque
        if self.armure_casque:
            affichage_casque = f"Casque : {self.armure_casque.nom} (Défense: +{self.armure_casque.bonus_defense})"
            if self.armure_casque.rarete:
                rarete_lower = str(self.armure_casque.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                affichage_casque += f" [{couleur}{self.armure_casque.rarete.upper()}{COULEURS['RESET']}]"
            print(affichage_casque)
        else:
            print("Casque : Aucun")

        # Bottes
        if self.armure_bottes:
            affichage_bottes = f"Bottes : {self.armure_bottes.nom} (Défense: +{self.armure_bottes.bonus_defense})"
            if self.armure_bottes.rarete:
                rarete_lower = str(self.armure_bottes.rarete).lower().strip()
                couleur = COULEURS_RARETE.get(rarete_lower, COULEURS["RESET"])
                affichage_bottes += f" [{couleur}{self.armure_bottes.rarete.upper()}{COULEURS['RESET']}]"
            print(affichage_bottes)
        else:
            print("Bottes : Aucunes")

        print("-----------------------------------")

        if self.effets_actifs:
            print("\n--- Effets Actifs ---")
            for effet in self.effets_actifs:
                print(f"- {effet}")
            print("---------------------")

    def appliquer_effets(self, phase):
        super().appliquer_effets(phase)

        # Régénération passive des ressources en fin de tour du joueur
        if self.specialisation.type_ressource == "Mana":
            regen_mana = (0.5 + (self.intelligence * 0.1)) # Petite régénération de base + bonus Intel
            mana_avant = self.mana
            self.mana += regen_mana
            self.mana = min(self.mana, self.mana_max)
            mana_recuperee = self.mana - mana_avant
            if mana_recuperee > 0:
                print(f"  {self.nom} régénère {mana_recuperee:.1f} Mana passivement. Mana actuelle : {self.mana:.1f}/{self.mana_max:.1f}")
        elif self.specialisation.type_ressource == "Energie":
            regen_energie = (5 + (self.agilite * 0.2) + (self.force * 0.1)) # Régénération plus rapide, basée Agi/Force
            energie_avant = self.energie
            self.energie += regen_energie
            self.energie = min(self.energie, self.energie_max)
            energie_recuperee = self.energie - energie_avant
            if energie_recuperee > 0:
                print(f"  {self.nom} régénère {energie_recuperee:.1f} Énergie passivement. Énergie actuelle : {self.energie:.1f}/{self.energie_max:.1f}")
        elif self.specialisation.type_ressource == "Rage":
            # La rage ne se régénère pas passivement, elle s'accumule en combat ou via capacités
            pass

        # Ne pas appeler mettre_a_jour_stats_apres_attributs() ici car cela pourrait
        # écraser des valeurs en plein tour. Les stats sont calculées dynamiquement
        # via les propriétés attaque, defense, vitesse, chance_critique.


    def equiper_arme(self, arme):
        """
        Équipe une arme. Si une arme est déjà équipée, elle retourne dans l'inventaire.
        :param arme: Instance de la classe Arme
        """
        # Si une arme est déjà équipée, la remettre dans l'inventaire
        if self.arme:
            # Créer un objet Objet à partir de l'arme équipée pour le remettre dans l'inventaire
            ancienne_arme_objet = Objet(
                nom=self.arme.nom,
                type_objet="équipement",
                quantite=1,
                description=f"Dégâts: {self.arme.degats_base}",
                rarete=self.arme.rarete
            )
            # Restaurer les stats de l'arme dans l'objet
            ancienne_arme_objet.stats = {
                "degats_base": self.arme.degats_base,
                "bonus_force": self.arme.bonus_force,
                "bonus_agilite": self.arme.bonus_agilite,
                "bonus_intelligence": self.arme.bonus_intelligence,
                "bonus_vitalite": self.arme.bonus_vitalite,
                "bonus_mana": self.arme.bonus_mana,
                "bonus_energie": self.arme.bonus_energie,
                "bonus_rage": self.arme.bonus_rage
            }
            # Déterminer le sous_type si possible (pour les armes craftées)
            if hasattr(self.arme, 'sous_type'):
                ancienne_arme_objet.sous_type = self.arme.sous_type
            self.ajouter_objet(ancienne_arme_objet)
            print(f"✓ {self.arme.nom} a été retirée et remise dans l'inventaire.")

        self.arme = arme
        print(f"✓ {self.nom} a équipé {arme.nom}.")
        self.mettre_a_jour_stats_apres_attributs()

    def equiper_armure(self, armure):
        """
        Équipe une armure selon son type (torse, casque, bottes).
        Si une armure est déjà équipée à cet emplacement, elle retourne dans l'inventaire.
        :param armure: Instance de la classe Armure
        """
        if armure.sous_type == "torse":
            ancienne = self.armure_torse
            self.armure_torse = armure
            type_nom = "armure de torse"
        elif armure.sous_type == "casque":
            ancienne = self.armure_casque
            self.armure_casque = armure
            type_nom = "casque"
        elif armure.sous_type == "bottes":
            ancienne = self.armure_bottes
            self.armure_bottes = armure
            type_nom = "bottes"
        else:
            print(f"❌ Type d'armure invalide : {armure.sous_type}")
            return

        # Si une armure est déjà équipée, la remettre dans l'inventaire
        if ancienne:
            # Créer un objet Objet à partir de l'armure équipée pour le remettre dans l'inventaire
            ancienne_armure_objet = Objet(
                nom=ancienne.nom,
                type_objet="équipement",
                quantite=1,
                description=f"Défense: +{ancienne.bonus_defense}",
                rarete=ancienne.rarete
            )
            # Restaurer les stats de l'armure dans l'objet
            ancienne_armure_objet.stats = {
                "bonus_defense": ancienne.bonus_defense,
                "bonus_force": ancienne.bonus_force,
                "bonus_agilite": ancienne.bonus_agilite,
                "bonus_intelligence": ancienne.bonus_intelligence,
                "bonus_vitalite": ancienne.bonus_vitalite,
                "bonus_mana": ancienne.bonus_mana,
                "bonus_energie": ancienne.bonus_energie,
                "bonus_rage": ancienne.bonus_rage
            }
            ancienne_armure_objet.sous_type = ancienne.sous_type
            self.ajouter_objet(ancienne_armure_objet)
            print(f"✓ {ancienne.nom} a été retirée et remise dans l'inventaire.")

        print(f"✓ {self.nom} a équipé {armure.nom} ({type_nom}).")
        self.mettre_a_jour_stats_apres_attributs()

    def ajouter_objet(self, objet):
        """
        Ajoute un objet à l'inventaire. Si l'objet existe déjà, incrémente la quantité.
        :param objet: Instance de la classe Objet
        """
        if objet.nom in self.inventaire:
            # Si l'objet existe déjà, incrémenter la quantité
            self.inventaire[objet.nom].quantite += objet.quantite
        else:
            # Sinon, ajouter l'objet
            self.inventaire[objet.nom] = objet

    def retirer_objet(self, nom_objet, quantite=1):
        """
        Retire une quantité d'un objet de l'inventaire.
        :param nom_objet: Nom de l'objet à retirer
        :param quantite: Quantité à retirer (défaut: 1)
        :return: True si l'objet a été retiré, False sinon
        """
        if nom_objet not in self.inventaire:
            return False

        objet = self.inventaire[nom_objet]
        if objet.quantite <= quantite:
            # Retirer complètement l'objet si la quantité est insuffisante ou égale
            del self.inventaire[nom_objet]
            return True
        else:
            # Réduire la quantité
            objet.quantite -= quantite
            return True

    def avoir_objet(self, nom_objet):
        """
        Vérifie si le joueur possède un objet dans son inventaire.
        :param nom_objet: Nom de l'objet à vérifier
        :return: L'objet si présent, None sinon
        """
        return self.inventaire.get(nom_objet)

    def compter_objet(self, nom_objet):
        """
        Retourne la quantité d'un objet dans l'inventaire.
        :param nom_objet: Nom de l'objet à compter
        :return: Quantité de l'objet (0 si absent)
        """
        objet = self.inventaire.get(nom_objet)
        return objet.quantite if objet else 0

    def sauvegarder_donnees(self):
        data = {
            "nom": self.nom,
            "race": self.race,
            "specialisation_nom": self.specialisation.nom,
            "force": self.force,
            "agilite": self.agilite,
            "vitalite": self.vitalite,
            "intelligence": self.intelligence,
            "niveau": self.niveau,
            "xp": self.xp,
            "xp_requise": self.xp_requise,
            "points_attribut": self.points_attribut,
            "vie": self.vie,
            "mana": self.mana,
            "energie": self.energie,
            "rage": self.rage,
            "arme": self.arme.nom if self.arme else None,
            "capacites_apprises": [
                {
                    "id": cap.id,
                    "niveau_amelioration": getattr(cap, 'niveau_amelioration', 1)
                }
                for cap in self.capacites_apprises
            ],
            "effets_actifs": [effet.__dict__ for effet in self.effets_actifs],
            "inventaire": [objet.to_dict() for objet in self.inventaire.values()],
            "or_": getattr(self, 'or_', 100),  # Sauvegarder l'or (100 par défaut si absent)
            "bonus_formation_achetes": getattr(self, 'bonus_formation_achetes', []),  # Sauvegarder les bonus de formation
            "systeme_quetes": getattr(self, 'systeme_quetes', None).to_dict() if hasattr(self, 'systeme_quetes') and self.systeme_quetes else None,  # Sauvegarder le système de quêtes
            "royaume_actuel": getattr(self, 'royaume_actuel', None),  # Sauvegarder le royaume actuel
            "temps_jeu_secondes": getattr(self, 'temps_jeu_secondes', 0)  # Sauvegarder le temps de jeu
        }
        return data

    @classmethod
    def from_dict(cls, data):
        # Charger l'arme avec les données complètes si disponible dans DEFINITIONS_ARMES
        arme_chargee = None
        arme_nom_ou_id = data.get("arme")

        if arme_nom_ou_id:
            # Essayer d'abord avec l'ID (ancien format)
            if arme_nom_ou_id in DEFINITIONS_ARMES:
                arme_data = DEFINITIONS_ARMES[arme_nom_ou_id]
                arme_chargee = Arme(
                    nom=arme_data["nom"],
                    degats_base=arme_data["degats_base"],
                    bonus_force=arme_data.get("bonus_force", 0),
                    bonus_agilite=arme_data.get("bonus_agilite", 0),
                    bonus_intelligence=arme_data.get("bonus_intelligence", 0),
                    bonus_vitalite=arme_data.get("bonus_vitalite", 0),
                    bonus_mana=arme_data.get("bonus_mana", 0),
                    bonus_energie=arme_data.get("bonus_energie", 0),
                    bonus_rage=arme_data.get("bonus_rage", 0),
                    rarete=arme_data.get("rarete", None)  # Rareté si disponible dans les définitions
                )
            else:
                # Si pas trouvé par ID, chercher par nom (nouveau format)
                arme_trouvee = None
                for arme_id, arme_data in DEFINITIONS_ARMES.items():
                    if arme_data.get("nom") == arme_nom_ou_id:
                        arme_trouvee = arme_data
                        break

                if arme_trouvee:
                    arme_chargee = Arme(
                        nom=arme_trouvee["nom"],
                        degats_base=arme_trouvee["degats_base"],
                        bonus_force=arme_trouvee.get("bonus_force", 0),
                        bonus_agilite=arme_trouvee.get("bonus_agilite", 0),
                        bonus_intelligence=arme_trouvee.get("bonus_intelligence", 0),
                        bonus_vitalite=arme_trouvee.get("bonus_vitalite", 0),
                        bonus_mana=arme_trouvee.get("bonus_mana", 0),
                        bonus_energie=arme_trouvee.get("bonus_energie", 0),
                        bonus_rage=arme_trouvee.get("bonus_rage", 0),
                        rarete=arme_trouvee.get("rarete", None)  # Rareté si disponible dans les définitions
                    )
                else:
                    # Arme non trouvée : créer une arme par défaut pour éviter les erreurs
                    print(f"Avertissement: Arme '{arme_nom_ou_id}' introuvable dans DEFINITIONS_ARMES lors du chargement.")
                    print(f"  → Création d'une arme par défaut. Vous pouvez rééquiper une arme depuis votre inventaire.")
                    arme_chargee = Arme(nom=arme_nom_ou_id, degats_base=0)


        perso = cls(
            nom=data["nom"],
            race=data["race"],
            specialisation_nom=data["specialisation_nom"],
            force=data["force"],
            agilite=data["agilite"],
            vitalite=data["vitalite"],
            intelligence=data["intelligence"],
            arme=arme_chargee # Passe l'arme chargée ici
        )

        perso.niveau = data["niveau"]
        perso.xp = data["xp"]
        perso.xp_requise = data["xp_requise"]
        perso.points_attribut = data["points_attribut"]
        perso.vie = data["vie"]
        perso.mana = data.get("mana", 0.0) # Gérer les anciennes sauvegardes sans mana
        perso.energie = data.get("energie", 0.0)
        perso.rage = data.get("rage", 0.0)
        perso.or_ = data.get("or_", 100)  # Charger l'or (100 par défaut pour anciennes sauvegardes)

        # Charger le temps de jeu (si disponible dans les métadonnées)
        metadonnees = data.get("metadonnees", {})
        if metadonnees.get("temps_jeu_secondes"):
            # Si on a le temps de jeu, on peut calculer le temps de début approximatif
            from datetime import datetime, timedelta
            temps_jeu_secondes = metadonnees["temps_jeu_secondes"]
            perso.temps_jeu_debut = datetime.now() - timedelta(seconds=temps_jeu_secondes)
        else:
            # Sinon, initialiser avec maintenant (nouveau personnage ou ancienne sauvegarde)
            from datetime import datetime
            perso.temps_jeu_debut = datetime.now()

        # Charger les bonus de formation achetés
        perso.bonus_formation_achetes = data.get("bonus_formation_achetes", [])

        # Charger le royaume actuel
        perso.royaume_actuel = data.get("royaume_actuel", None)

        # Charger le temps de jeu
        perso.temps_jeu_secondes = data.get("temps_jeu_secondes", 0)

        # Charger le système de quêtes
        systeme_quetes_data = data.get("systeme_quetes")
        if systeme_quetes_data:
            from world.quetes import SystemeQuetes
            perso.systeme_quetes = SystemeQuetes.from_dict(systeme_quetes_data)
        else:
            # Initialiser un nouveau système de quêtes si aucune sauvegarde
            from menus.quetes import initialiser_systeme_quetes
            perso.systeme_quetes = initialiser_systeme_quetes()
            # Accepter automatiquement la première quête principale si elle n'est pas déjà complétée
            premiere_quete_id = "decouverte_ordre"
            if premiere_quete_id in perso.systeme_quetes.quetes:
                if premiere_quete_id not in perso.systeme_quetes.quetes_completees:
                    perso.systeme_quetes.accepter_quete(premiere_quete_id, perso)

        # Appliquer les bonus de formation aux attributs
        # Note: Les bonus sont appliqués lors du chargement, mais les stats seront recalculées après
        # Pour éviter les dépendances circulaires, on applique les bonus directement ici
        if perso.bonus_formation_achetes:
            # Import différé pour éviter les dépendances circulaires
            try:
                from menus.formation import obtenir_bonus_formation_classe
                bonus_disponibles = obtenir_bonus_formation_classe(perso.specialisation.nom)
                for bonus_id in perso.bonus_formation_achetes:
                    bonus = next((b for b in bonus_disponibles if b['id'] == bonus_id), None)
                    if bonus:
                        if "force" in bonus['bonus']:
                            perso.force += bonus['bonus']['force']
                        if "agilite" in bonus['bonus']:
                            perso.agilite += bonus['bonus']['agilite']
                        if "vitalite" in bonus['bonus']:
                            perso.vitalite += bonus['bonus']['vitalite']
                        if "intelligence" in bonus['bonus']:
                            perso.intelligence += bonus['bonus']['intelligence']
            except ImportError:
                # Si l'import échoue (dépendance circulaire), on saute cette étape
                # Les bonus seront appliqués lors de la prochaine utilisation du menu de formation
                pass

        # Les capacités sont déjà initialisées dans __init__, il faut juste s'assurer que celles apprises sont les bonnes
        perso.capacites_apprises = [] # On vide celles par défaut

        # Gérer l'ancien format (liste d'IDs) et le nouveau format (liste de dicts avec niveau_amelioration)
        capacites_data = data.get("capacites_apprises", [])
        capacites_ids_ancien_format = data.get("capacites_apprises_ids", [])

        # Si on a l'ancien format, le convertir
        if capacites_ids_ancien_format and not capacites_data:
            capacites_data = [{"id": cap_id, "niveau_amelioration": 1} for cap_id in capacites_ids_ancien_format]

        for cap_info in capacites_data:
            # Gérer les deux formats : dict ou string
            if isinstance(cap_info, dict):
                cap_id = cap_info.get("id", cap_info)
                niveau_amelioration = cap_info.get("niveau_amelioration", 1)
            else:
                cap_id = cap_info
                niveau_amelioration = 1

            if cap_id in TOUTES_LES_CAPACITES_DATA:
                cap_data = TOUTES_LES_CAPACITES_DATA[cap_id]
                capacite = Capacite(
                    id_cap=cap_id,
                    nom=cap_data["nom"],
                    description=cap_data["description"],
                    cout_mana=cap_data.get("cout_mana", 0),
                    cout_energie=cap_data.get("cout_energie", 0),
                    cout_rage=cap_data.get("cout_rage", 0),
                    degats_fixes=cap_data.get("degats_fixes", 0),
                    soin_fixe=cap_data.get("soin_fixe", 0),
                    effet_data=cap_data.get("effet_data"),
                    type_cible=cap_data.get("type_cible", "unique"),
                    niveau_requis=cap_data.get("niveau_requis", 1),
                    peut_critiquer=cap_data.get("peut_critiquer", False),
                    niveau_amelioration=niveau_amelioration
                )

                # Appliquer les améliorations si nécessaire
                while capacite.niveau_amelioration < niveau_amelioration:
                    capacite.ameliorer()

                perso.capacites_apprises.append(capacite)
            else:
                print(f"Avertissement: Capacité '{cap_id}' non trouvée lors du chargement.")


        perso.effets_actifs = []
        if "effets_actifs" in data:
            for effet_dict in data["effets_actifs"]:
                perso.appliquer_effet(effet_dict) # Applique l'effet via la méthode qui gère l'ajout

        perso.mettre_a_jour_stats_apres_attributs() # Recalcule toutes les stats une fois tout chargé

        # S'assurer que la vie actuelle ne dépasse pas la vie maximale après chargement et calcul des stats
        perso.vie = min(perso.vie, perso.vie_max)
        perso.mana = min(perso.mana, perso.mana_max)
        perso.energie = min(perso.energie, perso.energie_max)
        perso.rage = min(perso.rage, perso.rage_max)

        # Charger l'inventaire
        inventaire_data = data.get("inventaire", [])
        perso.inventaire = {}

        if inventaire_data:
            # Migration : si l'inventaire est une liste simple de noms (ancienne sauvegarde)
            if isinstance(inventaire_data[0], str):
                # Ancien format : liste de noms -> convertir en objets
                for nom_objet in inventaire_data:
                    # Créer un objet par défaut (type matériau, quantité 1)
                    objet = Objet(nom=nom_objet, type_objet="matériau", quantite=1)
                    perso.ajouter_objet(objet)
            else:
                # Nouveau format : liste de dictionnaires d'objets
                for objet_dict in inventaire_data:
                    objet = Objet.from_dict(objet_dict)
                    perso.ajouter_objet(objet)

        return perso


class Ennemi(BaseCombatant):
    def __init__(self, id_ennemi, nom, vie_max, vitesse, attaque, defense, chance_critique, xp_a_donner, loot_table=None):
        super().__init__(nom, vie_max, vitesse, attaque, defense, chance_critique)
        self.id_ennemi = id_ennemi
        self.xp_a_donner = xp_a_donner
        # loot_table peut être :
        # - Liste de strings (100% de chance pour chaque objet)
        # - Liste de dicts {"nom": "...", "chance": 1-100} (probabilité personnalisée)
        # - Format mixte (strings et dicts)
        self.loot_table = loot_table if loot_table is not None else []

        # Les ennemis n'ont pas de ressources pour l'instant, mais c'est bien de les initialiser à 0
        self.mana = 0
        self.mana_max = 0
        self.energie = 0
        self.energie_max = 0
        self.rage = 0
        self.rage_max = 0


    def afficher_stats(self):
        print(f"--- Statistiques de {self.nom} ---")
        print(f"Vie : {self.vie:.1f}/{self.vie_max:.1f}")
        print(f"Attaque : {self.calculer_attaque_totale():.1f}")
        print(f"Défense : {self.calculer_defense_totale():.1f}")
        print(f"Vitesse : {self.calculer_vitesse_totale():.1f}")
        print(f"Chance Critique : {self.calculer_chance_critique_totale():.1f}%")
        if self.effets_actifs:
            print("\n--- Effets Actifs ---")
            for effet in self.effets_actifs:
                print(f"- {effet}")
            print("---------------------")
        print("--------------------------")

    def appliquer_effets(self, phase):
        super().appliquer_effets(phase)
        # Pour Ennemi, les stats sont calculées dynamiquement via calculer_*_totale()
        # Pas besoin de les mettre à jour manuellement


    @classmethod
    def from_data(cls, ennemi_id):
        data = DEFINITIONS_ENNEMIS.get(ennemi_id)
        if not data:
            print(f"Erreur: Définition de l'ennemi '{ennemi_id}' introuvable.")
            return None

        # Créer une nouvelle instance d'Ennemi à partir des données
        return cls(
            id_ennemi=ennemi_id,
            nom=data["nom"],
            vie_max=data["vie_max"],
            vitesse=data["vitesse"],
            attaque=data["attaque"],
            defense=data["defense"],
            chance_critique=data["chance_critique"],
            xp_a_donner=data["xp_a_donner"],
            loot_table=data.get("loot_table", [])
        )
