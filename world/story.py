# world/story.py
# Gestion des histoires (globale et par royaume)

class HistoireGlobale:
    """
    Gère l'histoire globale de Valdoria.
    Cette classe contiendra la narration principale qui relie tous les royaumes.
    """

    def __init__(self, titre="", introduction="", chapitres=None):
        """
        :param titre: Titre de l'histoire globale
        :param introduction: Texte d'introduction de l'histoire globale
        :param chapitres: Liste des chapitres de l'histoire (pour progression linéaire)
        """
        self.titre = titre
        self.introduction = introduction
        self.chapitres = chapitres or []  # Liste des chapitres/étapes de l'histoire
        self.chapitre_actuel = 0  # Index du chapitre actuel (pour progression linéaire)

    def obtenir_chapitre_actuel(self):
        """Retourne le chapitre actuel de l'histoire."""
        if 0 <= self.chapitre_actuel < len(self.chapitres):
            return self.chapitres[self.chapitre_actuel]
        return None

    def passer_au_chapitre_suivant(self):
        """Passe au chapitre suivant de l'histoire."""
        if self.chapitre_actuel < len(self.chapitres) - 1:
            self.chapitre_actuel += 1
            return True
        return False

    def afficher_introduction(self):
        """Affiche l'introduction de l'histoire globale."""
        if self.introduction:
            print(f"\n{'='*50}")
            print(f"{self.titre}")
            print(f"{'='*50}")
            print(self.introduction)
            print(f"{'='*50}\n")


class HistoireRoyaume:
    """
    Gère l'histoire spécifique d'un royaume.
    Chaque royaume a sa propre histoire qui se déroule en parallèle ou en complément de l'histoire globale.
    """

    def __init__(self, royaume_nom, introduction="", quetes=None):
        """
        :param royaume_nom: Nom du royaume concerné
        :param introduction: Introduction de l'histoire du royaume
        :param quetes: Liste des quêtes spécifiques à ce royaume
        """
        self.royaume_nom = royaume_nom
        self.introduction = introduction
        self.quetes = quetes or []  # Liste des quêtes/étapes de l'histoire du royaume
        self.quete_actuelle = 0  # Index de la quête actuelle

    def obtenir_quete_actuelle(self):
        """Retourne la quête actuelle du royaume."""
        if 0 <= self.quete_actuelle < len(self.quetes):
            return self.quetes[self.quete_actuelle]
        return None

    def passer_quete_suivante(self):
        """Passe à la quête suivante."""
        if self.quete_actuelle < len(self.quetes) - 1:
            self.quete_actuelle += 1
            return True
        return False

    def afficher_introduction(self):
        """Affiche l'introduction de l'histoire du royaume."""
        if self.introduction:
            print(f"\n{'='*50}")
            print(f"Histoire de {self.royaume_nom}")
            print(f"{'='*50}")
            print(self.introduction)
            print(f"{'='*50}\n")
