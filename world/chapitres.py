# world/chapitres.py
# Système de chapitres avec exploration libre et branches narratives conditionnelles

from enum import Enum

class TypeChapitre(Enum):
    """
    Types de chapitres possibles.
    """
    LINEAIRE = "linéaire"  # Progression strictement linéaire
    EXPLORATION_LIBRE = "exploration_libre"  # Plusieurs zones accessibles librement
    CHOIX_NARRATIF = "choix_narratif"  # Chapitre avec choix qui affecte la suite
    FINAL = "final"  # Chapitre final (différent selon les choix précédents)


class ChoixNarratif:
    """
    Représente un choix narratif dans un chapitre.
    """

    def __init__(self, id_choix, texte, description="", consequences=None):
        """
        :param id_choix: Identifiant unique du choix
        :param texte: Texte affiché pour le choix
        :param description: Description plus détaillée du choix
        :param consequences: Dictionnaire des conséquences {cle: valeur}
        """
        self.id_choix = id_choix
        self.texte = texte
        self.description = description
        self.consequences = consequences or {}  # Conséquences de ce choix

    def __repr__(self):
        return f"ChoixNarratif(id='{self.id_choix}', texte='{self.texte}')"


class Chapitre:
    """
    Représente un chapitre de l'histoire globale.
    Un chapitre peut être linéaire, avec exploration libre, ou avec choix narratifs.
    """

    def __init__(self, numero, titre, type_chapitre, description="", zones_accessibles=None,
                 choix_narratifs=None, objectifs=None, chapitre_suivant=None,
                 conditions_deblocage=None):
        """
        :param numero: Numéro du chapitre (1, 2, 3, etc.)
        :param titre: Titre du chapitre
        :param type_chapitre: TypeChapitre (LINÉAIRE, EXPLORATION_LIBRE, CHOIX_NARRATIF, FINAL)
        :param description: Description du chapitre (histoire)
        :param zones_accessibles: Liste des IDs de zones/biomes accessibles dans ce chapitre
        :param choix_narratifs: Liste de ChoixNarratif (si type_chapitre == CHOIX_NARRATIF)
        :param objectifs: Liste des objectifs à compléter pour débloquer le chapitre suivant
        :param chapitre_suivant: ID du chapitre suivant (ou dict {choix_id: chapitre_id} pour branches)
        :param conditions_deblocage: Conditions pour débloquer ce chapitre
        """
        self.numero = numero
        self.titre = titre
        self.type_chapitre = type_chapitre
        self.description = description
        self.zones_accessibles = zones_accessibles or []  # Liste des noms/IDs de zones
        self.choix_narratifs = choix_narratifs or []  # Liste de ChoixNarratif
        self.objectifs = objectifs or []  # Liste des objectifs
        self.chapitre_suivant = chapitre_suivant  # ID du chapitre suivant ou dict de branches
        self.conditions_deblocage = conditions_deblocage or {}  # Conditions pour débloquer

        # État du chapitre
        self.est_debloque = False
        self.est_complete = False
        self.choix_fait = None  # ChoixNarratif sélectionné (si applicable)
        self.zones_completees = []  # Liste des zones complétées dans ce chapitre

        # IMPORTANT : Les zones complétées restent accessibles pour farming/exploration
        # Compléter une zone ne la verrouille pas, elle reste dans zones_accessibles

    def ajouter_zone(self, zone_id):
        """Ajoute une zone accessible dans ce chapitre."""
        if zone_id not in self.zones_accessibles:
            self.zones_accessibles.append(zone_id)

    def completer_zone(self, zone_id):
        """
        Marque une zone comme complétée (objectif atteint).
        IMPORTANT : La zone reste accessible pour farming/re-exploration.
        """
        if zone_id not in self.zones_completees:
            self.zones_completees.append(zone_id)
        # Note : La zone reste dans zones_accessibles pour permettre le re-farming

    def verifier_objectifs(self):
        """
        Vérifie si tous les objectifs sont complétés.
        :return: True si tous les objectifs sont complétés
        """
        if not self.objectifs:
            return True

        # Vérifier si toutes les zones nécessaires sont complétées
        zones_requises = [obj for obj in self.objectifs if isinstance(obj, str)]
        if zones_requises:
            for zone in zones_requises:
                if zone not in self.zones_completees:
                    return False

        # Autres types d'objectifs peuvent être ajoutés ici

        return True

    def obtenir_chapitre_suivant(self):
        """
        Retourne l'ID du chapitre suivant selon les choix faits.
        :return: ID du chapitre suivant (int ou None)
        """
        if isinstance(self.chapitre_suivant, dict) and self.choix_fait:
            # Si chapitre suivant dépend d'un choix
            return self.chapitre_suivant.get(self.choix_fait.id_choix, self.chapitre_suivant.get('default'))
        elif isinstance(self.chapitre_suivant, int):
            return self.chapitre_suivant
        return None

    def afficher_info(self):
        """Affiche les informations du chapitre."""
        print(f"\n{'='*50}")
        print(f"CHAPITRE {self.numero} : {self.titre}")
        print(f"{'='*50}")
        if self.description:
            print(self.description)
        print(f"\nType : {self.type_chapitre.value}")
        if self.zones_accessibles:
            print(f"\nZones accessibles ({len(self.zones_accessibles)}) :")
            for i, zone in enumerate(self.zones_accessibles, 1):
                etat = "✓" if zone in self.zones_completees else "○"
                print(f"  {etat} {i}. {zone}")
        if self.choix_narratifs:
            print(f"\nChoix narratifs disponibles ({len(self.choix_narratifs)}) :")
            for i, choix in enumerate(self.choix_narratifs, 1):
                print(f"  {i}. {choix.texte}")
                if choix.description:
                    print(f"     {choix.description}")
        if self.objectifs:
            print(f"\nObjectifs :")
            for obj in self.objectifs:
                print(f"  - {obj}")
        print(f"{'='*50}\n")

    def __repr__(self):
        return f"Chapitre({self.numero}, '{self.titre}', type={self.type_chapitre.value})"


class SystemeChapitres:
    """
    Gère le système de chapitres avec branches narratives.
    """

    def __init__(self):
        self.chapitres = {}  # Dict {numero: Chapitre}
        self.chapitre_actuel_numero = 1
        self.histoire_choix = {}  # Dictionnaire des choix faits {chapitre_numero: choix_id}

    def ajouter_chapitre(self, chapitre):
        """Ajoute un chapitre au système."""
        self.chapitres[chapitre.numero] = chapitre

    def obtenir_chapitre_actuel(self):
        """Retourne le chapitre actuel."""
        return self.chapitres.get(self.chapitre_actuel_numero)

    def debloquer_chapitre(self, numero):
        """Débloque un chapitre."""
        if numero in self.chapitres:
            self.chapitres[numero].est_debloque = True

    def passer_au_chapitre_suivant(self):
        """
        Passe au chapitre suivant selon la progression et les choix.
        :return: True si un chapitre suivant existe, False sinon
        """
        chapitre_actuel = self.obtenir_chapitre_actuel()
        if not chapitre_actuel:
            return False

        # Vérifier que le chapitre est complété
        if not chapitre_actuel.verifier_objectifs():
            return False

        chapitre_actuel.est_complete = True

        # Obtenir le chapitre suivant
        chapitre_suivant_id = chapitre_actuel.obtenir_chapitre_suivant()
        if chapitre_suivant_id and chapitre_suivant_id in self.chapitres:
            self.chapitre_actuel_numero = chapitre_suivant_id
            self.debloquer_chapitre(chapitre_suivant_id)
            return True

        return False

    def faire_choix_narratif(self, chapitre_numero, choix_id):
        """
        Enregistre un choix narratif fait par le joueur.
        :param chapitre_numero: Numéro du chapitre
        :param choix_id: ID du choix
        """
        if chapitre_numero in self.chapitres:
            chapitre = self.chapitres[chapitre_numero]
            for choix in chapitre.choix_narratifs:
                if choix.id_choix == choix_id:
                    chapitre.choix_fait = choix
                    self.histoire_choix[chapitre_numero] = choix_id
                    return True
        return False

    def obtenir_zones_accessibles_actuelles(self):
        """
        Retourne la liste des zones accessibles dans le chapitre actuel.
        Inclut toutes les zones débloquées (même complétées) pour permettre le farming.
        :return: Liste des IDs de zones
        """
        chapitre_actuel = self.obtenir_chapitre_actuel()
        if chapitre_actuel:
            return chapitre_actuel.zones_accessibles
        return []

    def obtenir_toutes_zones_debloquees(self):
        """
        Retourne toutes les zones débloquées depuis le début du jeu.
        Permet au joueur de revenir dans n'importe quelle zone précédente.
        :return: Liste des IDs de zones débloquées
        """
        toutes_zones = []
        for chapitre_num, chapitre in self.chapitres.items():
            # Ajouter toutes les zones des chapitres débloqués
            if chapitre.est_debloque:
                for zone in chapitre.zones_accessibles:
                    if zone not in toutes_zones:
                        toutes_zones.append(zone)
        return toutes_zones

    def royaume_est_complete(self):
        """
        Vérifie si le royaume est complété.
        Un royaume est complété si :
        - Le chapitre actuel est complété ET
        - Il n'y a pas de chapitre suivant (ou le chapitre actuel est de type FINAL)
        :return: True si le royaume est complété, False sinon
        """
        chapitre_actuel = self.obtenir_chapitre_actuel()
        if not chapitre_actuel:
            return False

        # Vérifier que le chapitre actuel est complété
        if not chapitre_actuel.est_complete:
            return False

        # Vérifier s'il y a un chapitre suivant
        chapitre_suivant_id = chapitre_actuel.obtenir_chapitre_suivant()

        # Si le chapitre actuel est de type FINAL et complété, le royaume est complété
        if chapitre_actuel.type_chapitre == TypeChapitre.FINAL:
            return True

        # Si il n'y a pas de chapitre suivant, le royaume est complété
        if chapitre_suivant_id is None or chapitre_suivant_id not in self.chapitres:
            return True

        return False
