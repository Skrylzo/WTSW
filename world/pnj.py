# world/pnj.py
# Système de base pour les PNJ (Personnages Non-Joueurs)

from typing import Dict, Optional, List


class PNJ:
    """
    Représente un Personnage Non-Joueur dans le jeu.
    """

    def __init__(self, id_pnj: str, nom: str, description: str = "", royaume: Optional[str] = None,
                 dialogue_par_defaut: str = "", quetes_liees: List[str] = None,
                 dialogues_quetes: Dict[str, str] = None):
        """
        :param id_pnj: Identifiant unique du PNJ
        :param nom: Nom du PNJ
        :param description: Description du PNJ
        :param royaume: Royaume où se trouve le PNJ
        :param dialogue_par_defaut: Dialogue par défaut du PNJ
        :param quetes_liees: Liste des IDs de quêtes liées à ce PNJ
        :param dialogues_quetes: Dictionnaire {id_quete: dialogue} pour dialogues contextuels selon les quêtes
        """
        self.id_pnj = id_pnj
        self.nom = nom
        self.description = description
        self.royaume = royaume
        self.dialogue_par_defaut = dialogue_par_defaut
        self.quetes_liees = quetes_liees or []
        self.dialogues_quetes = dialogues_quetes or {}  # {id_quete: dialogue}

    def parler(self, joueur) -> str:
        """
        Retourne le dialogue du PNJ selon le contexte des quêtes.
        Priorité : quête en cours > quête complétée > dialogue par défaut
        """
        if not hasattr(joueur, 'systeme_quetes'):
            return self.dialogue_par_defaut or f"{self.nom} vous regarde sans dire un mot."

        systeme_quetes = joueur.systeme_quetes

        # Vérifier d'abord les quêtes en cours
        for quete_id in self.quetes_liees:
            quete = systeme_quetes.obtenir_quete(quete_id)
            if quete and quete.statut.value == "en_cours":
                # Vérifier si ce PNJ a un dialogue spécifique pour cette quête
                if quete_id in self.dialogues_quetes:
                    return self.dialogues_quetes[quete_id]
                # Sinon, utiliser le dialogue par défaut mais avec un contexte
                return self.dialogue_par_defaut or f"{self.nom} vous regarde avec intérêt."

        # Vérifier les quêtes complétées récemment
        for quete_id in self.quetes_liees:
            quete = systeme_quetes.obtenir_quete(quete_id)
            if quete and quete.statut.value == "completee":
                # Si une quête liée est complétée, on peut avoir un dialogue de remerciement
                dialogue_complete = f"{quete_id}_complete"
                if dialogue_complete in self.dialogues_quetes:
                    return self.dialogues_quetes[dialogue_complete]

        # Dialogue par défaut
        return self.dialogue_par_defaut or f"{self.nom} vous regarde sans dire un mot."

    def __repr__(self):
        return f"PNJ(id='{self.id_pnj}', nom='{self.nom}')"


# Dictionnaire de tous les PNJ du jeu
PNJS: Dict[str, PNJ] = {}

def enregistrer_pnj(pnj: PNJ):
    """Enregistre un PNJ dans le système."""
    PNJS[pnj.id_pnj] = pnj

def obtenir_pnj(id_pnj: str) -> Optional[PNJ]:
    """Retourne un PNJ par son ID."""
    return PNJS.get(id_pnj)

def parler_a_pnj(joueur, id_pnj: str) -> bool:
    """
    Permet au joueur de parler à un PNJ.
    Fait progresser les quêtes si nécessaire.

    :param joueur: Le personnage joueur
    :param id_pnj: ID du PNJ
    :return: True si l'interaction a réussi
    """
    pnj = obtenir_pnj(id_pnj)
    if not pnj:
        print(f"PNJ '{id_pnj}' introuvable.")
        return False

    print(f"\n{'='*60}")
    print(f"--- {pnj.nom} ---")
    print(f"{'='*60}")
    if pnj.description:
        print(f"{pnj.description}\n")

    dialogue = pnj.parler(joueur)
    print(dialogue)
    print(f"{'='*60}\n")

    # Progresser les quêtes "Parler à un PNJ"
    if hasattr(joueur, 'systeme_quetes'):
        from world.progression_quetes import progresser_quetes_parler_pnj
        progresser_quetes_parler_pnj(joueur, id_pnj)

    return True
