# world/gameplay.py
# Définition du système de gameplay (linéaire, tour par tour, exploration, etc.)

from enum import Enum

class TypeGameplay(Enum):
    """
    Types de gameplay possibles pour le jeu.
    """
    LINEAIRE = "linéaire"  # Histoire linéaire, progression séquentielle
    TOUR_PAR_TOUR = "tour_par_tour"  # Système de tours (déjà implémenté pour le combat)
    EXPLORATION_LIBRE = "exploration_libre"  # Le joueur choisit où aller librement
    HYBRIDE = "hybride"  # Mélange des approches ci-dessus


class ModeProgression(Enum):
    """
    Modes de progression dans le jeu.
    """
    PAR_NIVEAU = "par_niveau"  # Débloque les zones selon le niveau du joueur
    PAR_QUETE = "par_quete"  # Débloque les zones selon les quêtes complétées
    LIBRE = "libre"  # Toutes les zones sont disponibles dès le début
    PAR_HISTOIRE = "par_histoire"  # Débloque selon la progression de l'histoire globale


class SystemeGameplay:
    """
    Classe principale qui définit comment le jeu se joue.
    Cette classe sera utilisée pour gérer la logique de progression et de gameplay.
    """

    def __init__(self, type_gameplay=TypeGameplay.HYBRIDE, mode_progression=ModeProgression.PAR_HISTOIRE):
        """
        :param type_gameplay: Type de gameplay (linéaire, tour par tour, etc.)
        :param mode_progression: Mode de progression (par niveau, par quête, etc.)
        """
        self.type_gameplay = type_gameplay  # CHAPITRE-BASED (configuré comme HYBRIDE)
        self.mode_progression = mode_progression  # PAR_HISTOIRE
        self.zones_debloquees = []  # Liste des zones débloquées
        self.progression_globale = 0  # Progression globale (0-100)
        self.systeme_chapitres = None  # Sera initialisé avec SystemeChapitres

    def peut_acceder_zone(self, nom_zone, joueur):
        """
        Détermine si le joueur peut accéder à une zone donnée.
        :param nom_zone: Nom de la zone à vérifier
        :param joueur: Instance du personnage joueur
        :return: True si accessible, False sinon
        """
        # Si libre, toutes les zones sont accessibles
        if self.mode_progression == ModeProgression.LIBRE:
            return True

        # Si la zone est déjà débloquée
        if nom_zone in self.zones_debloquees:
            return True

        # Vérifications selon le mode de progression
        if self.mode_progression == ModeProgression.PAR_NIVEAU:
            # Vérifier le niveau requis (à implémenter selon les besoins)
            return False  # TODO: Implémenter la logique de niveau

        elif self.mode_progression == ModeProgression.PAR_QUETE:
            # Vérifier les quêtes complétées (à implémenter)
            return False  # TODO: Implémenter la logique de quêtes

        elif self.mode_progression == ModeProgression.PAR_HISTOIRE:
            # Vérifier la progression de l'histoire (à implémenter)
            return False  # TODO: Implémenter la logique d'histoire

        return False

    def debloquer_zone(self, nom_zone):
        """Débloque une zone pour le joueur."""
        if nom_zone not in self.zones_debloquees:
            self.zones_debloquees.append(nom_zone)
            return True
        return False

    def obtenir_prochaines_zones_disponibles(self, joueur):
        """
        Retourne la liste des prochaines zones accessibles au joueur.
        :param joueur: Instance du personnage joueur
        :return: Liste des noms de zones disponibles
        """
        # TODO: Implémenter selon le mode de progression
        return self.zones_debloquees


# Instance globale du système de gameplay
# Sera configurée selon les préférences du jeu
SYSTEME_GAMEPLAY = SystemeGameplay()
