# world/quetes.py
# Système de gestion des quêtes

from enum import Enum
from typing import List, Dict, Optional, Any


class TypeQuete(Enum):
    """
    Types de quêtes possibles.
    """
    PRINCIPALE = "principale"  # Quête de l'histoire principale
    ROYAUME = "royaume"  # Quête spécifique à un royaume
    SECONDAIRE = "secondaire"  # Quête secondaire optionnelle
    JOURNALIERE = "journaliere"  # Quête journalière (futur)


class StatutQuete(Enum):
    """
    Statut d'une quête.
    """
    DISPONIBLE = "disponible"  # Disponible mais pas encore acceptée
    EN_COURS = "en_cours"  # Acceptée et en cours
    COMPLETEE = "completee"  # Complétée
    ABANDONNEE = "abandonnee"  # Abandonnée


class TypeObjectif(Enum):
    """
    Types d'objectifs de quête.
    """
    TUER_ENNEMI = "tuer_ennemi"  # Tuer X ennemis d'un type donné
    COLLECTER_OBJET = "collecter_objet"  # Collecter X objets
    PARLER_PNJ = "parler_pnj"  # Parler à un PNJ
    EXPLORER_ZONE = "explorer_zone"  # Explorer une zone
    COMPLETER_DONJON = "completer_donjon"  # Compléter un donjon
    ATTEINDRE_NIVEAU = "atteindre_niveau"  # Atteindre un niveau


class ObjectifQuete:
    """
    Représente un objectif d'une quête.
    """

    def __init__(self, type_objectif: TypeObjectif, description: str,
                 cible: str, quantite_requise: int = 1, quantite_actuelle: int = 0):
        """
        :param type_objectif: Type d'objectif
        :param description: Description textuelle de l'objectif
        :param cible: Cible de l'objectif (nom ennemi, objet, zone, etc.)
        :param quantite_requise: Quantité requise pour compléter l'objectif
        :param quantite_actuelle: Quantité actuelle (progression)
        """
        self.type_objectif = type_objectif
        self.description = description
        self.cible = cible  # ID ou nom de la cible
        self.quantite_requise = quantite_requise
        self.quantite_actuelle = quantite_actuelle

    def est_complete(self) -> bool:
        """Vérifie si l'objectif est complété."""
        return self.quantite_actuelle >= self.quantite_requise

    def progresser(self, quantite: int = 1):
        """Fait progresser l'objectif."""
        self.quantite_actuelle = min(self.quantite_actuelle + quantite, self.quantite_requise)

    def __str__(self):
        return f"{self.description} ({self.quantite_actuelle}/{self.quantite_requise})"


class Quete:
    """
    Représente une quête dans le jeu.
    """

    def __init__(self, id_quete: str, nom: str, description: str, type_quete: TypeQuete,
                 royaume: Optional[str] = None, objectifs: List[ObjectifQuete] = None,
                 recompenses: Dict[str, Any] = None, prerequis: List[str] = None,
                 niveau_requis: int = 1):
        """
        :param id_quete: Identifiant unique de la quête
        :param nom: Nom de la quête
        :param description: Description de la quête
        :param type_quete: Type de quête (principale, royaume, secondaire)
        :param royaume: Nom du royaume associé (si quête de royaume)
        :param objectifs: Liste des objectifs de la quête
        :param recompenses: Dictionnaire des récompenses {"xp": int, "or": int, "objets": [str]}
        :param prerequis: Liste des IDs de quêtes requises pour débloquer cette quête
        :param niveau_requis: Niveau minimum requis pour accepter la quête
        """
        self.id_quete = id_quete
        self.nom = nom
        self.description = description
        self.type_quete = type_quete
        self.royaume = royaume
        self.objectifs = objectifs or []
        self.recompenses = recompenses or {}
        self.prerequis = prerequis or []
        self.niveau_requis = niveau_requis

        # État de la quête
        self.statut = StatutQuete.DISPONIBLE
        self.ordre_completion: Optional[int] = None  # Pour l'histoire principale (ordre de complétion des royaumes)

    def est_complete(self) -> bool:
        """Vérifie si tous les objectifs sont complétés."""
        if not self.objectifs:
            return False
        return all(obj.est_complete() for obj in self.objectifs)

    def peut_etre_acceptee(self, joueur, quetes_completees: List[str]) -> tuple[bool, str]:
        """
        Vérifie si la quête peut être acceptée.
        :param joueur: Le personnage joueur
        :param quetes_completees: Liste des IDs de quêtes complétées
        :return: (peut_etre_acceptee, message_erreur)
        """
        if self.statut != StatutQuete.DISPONIBLE:
            return False, "Cette quête n'est pas disponible."

        if joueur.niveau < self.niveau_requis:
            return False, f"Niveau requis : {self.niveau_requis} (votre niveau : {joueur.niveau})"

        # Vérifier les prérequis
        for prerequis_id in self.prerequis:
            if prerequis_id not in quetes_completees:
                return False, f"Prérequis manquant : {prerequis_id}"

        return True, ""

    def accepter(self):
        """Accepte la quête."""
        if self.statut == StatutQuete.DISPONIBLE:
            self.statut = StatutQuete.EN_COURS

    def abandonner(self):
        """Abandonne la quête."""
        if self.statut == StatutQuete.EN_COURS:
            self.statut = StatutQuete.ABANDONNEE

    def completer(self):
        """Marque la quête comme complétée."""
        if self.est_complete():
            self.statut = StatutQuete.COMPLETEE
            return True
        return False

    def afficher(self):
        """Affiche les informations de la quête."""
        from utils.affichage import COULEURS, afficher_titre_menu_avec_emoji, afficher_separateur, COULEUR_OR

        print()
        afficher_titre_menu_avec_emoji(f"QUÊTE : {self.nom}", "quetes")
        afficher_separateur(style="simple", couleur=COULEURS["GRIS"])
        print()
        if self.royaume:
            print(f"Royaume : {self.royaume}")
            print()
        print(f"Description :")
        print()
        print(f"{self.description}")
        print()

        if self.objectifs:
            print(f"Objectifs :")
            print()
            for i, obj in enumerate(self.objectifs, 1):
                etat = "✓" if obj.est_complete() else "○"
                couleur_etat = COULEURS["VERT"] if obj.est_complete() else COULEURS["GRIS"]
                print(f"  {couleur_etat}{etat}{COULEURS['RESET']} {i}. {obj}")
                print()

        if self.recompenses:
            print(f"Récompenses :")
            print()
            if "xp" in self.recompenses:
                print(f"  {COULEURS['VERT']}- XP : {self.recompenses['xp']}{COULEURS['RESET']}")
                print()
            if "or" in self.recompenses:
                print(f"  {COULEUR_OR}- Or : {self.recompenses['or']}{COULEURS['RESET']}")
                print()
            if "objets" in self.recompenses:
                for objet in self.recompenses['objets']:
                    print(f"  {COULEURS['CYAN']}- Objet : {objet}{COULEURS['RESET']}")
                    print()

        print(f"{COULEURS['CYAN']}{'='*60}{COULEURS['RESET']}\n")

    def __repr__(self):
        return f"Quete(id='{self.id_quete}', nom='{self.nom}', statut={self.statut.value})"


class SystemeQuetes:
    """
    Gère le système de quêtes du jeu.
    """

    def __init__(self):
        self.quetes: Dict[str, Quete] = {}  # Toutes les quêtes disponibles
        self.quetes_acceptees: List[str] = []  # IDs des quêtes acceptées
        self.quetes_completees: List[str] = []  # IDs des quêtes complétées
        self.ordre_completion_royaumes: List[str] = []  # Ordre de complétion des royaumes (pour histoire principale)

    def ajouter_quete(self, quete: Quete):
        """Ajoute une quête au système."""
        self.quetes[quete.id_quete] = quete

    def obtenir_quete(self, id_quete: str) -> Optional[Quete]:
        """Retourne une quête par son ID."""
        return self.quetes.get(id_quete)

    def obtenir_quetes_disponibles(self, joueur) -> List[Quete]:
        """Retourne les quêtes disponibles pour le joueur."""
        disponibles = []
        for quete in self.quetes.values():
            peut_accepter, _ = quete.peut_etre_acceptee(joueur, self.quetes_completees)
            if peut_accepter and quete.statut == StatutQuete.DISPONIBLE:
                disponibles.append(quete)
        return disponibles

    def obtenir_quetes_en_cours(self) -> List[Quete]:
        """Retourne les quêtes en cours."""
        return [self.quetes[qid] for qid in self.quetes_acceptees
                if qid in self.quetes and self.quetes[qid].statut == StatutQuete.EN_COURS]

    def obtenir_quetes_completees(self) -> List[Quete]:
        """Retourne les quêtes complétées."""
        return [self.quetes[qid] for qid in self.quetes_completees
                if qid in self.quetes]

    def accepter_quete(self, id_quete: str, joueur) -> tuple[bool, str]:
        """
        Accepte une quête.
        :return: (succes, message)
        """
        quete = self.obtenir_quete(id_quete)
        if not quete:
            return False, "Quête introuvable."

        peut_accepter, message = quete.peut_etre_acceptee(joueur, self.quetes_completees)
        if not peut_accepter:
            return False, message

        quete.accepter()
        if id_quete not in self.quetes_acceptees:
            self.quetes_acceptees.append(id_quete)

        return True, f"Quête '{quete.nom}' acceptée !"

    def abandonner_quete(self, id_quete: str) -> bool:
        """Abandonne une quête."""
        quete = self.obtenir_quete(id_quete)
        if not quete or quete.statut != StatutQuete.EN_COURS:
            return False

        quete.abandonner()
        if id_quete in self.quetes_acceptees:
            self.quetes_acceptees.remove(id_quete)

        return True

    def progresser_objectif(self, type_objectif: TypeObjectif, cible: str, quantite: int = 1):
        """
        Fait progresser un objectif de quête.
        :param type_objectif: Type d'objectif
        :param cible: Cible de l'objectif
        :param quantite: Quantité à ajouter
        """
        for quete_id in self.quetes_acceptees:
            quete = self.quetes.get(quete_id)
            if quete and quete.statut == StatutQuete.EN_COURS:
                for objectif in quete.objectifs:
                    if objectif.type_objectif == type_objectif and objectif.cible == cible:
                        objectif.progresser(quantite)
                        # Ne pas appeler completer_quete ici - laisser _verifier_et_completer_quetes s'en charger
                        # pour afficher le message et appliquer les récompenses correctement

    def completer_quete(self, id_quete: str) -> tuple[bool, Dict[str, Any]]:
        """
        Complète une quête et retourne les récompenses.
        :return: (succes, recompenses)
        """
        quete = self.obtenir_quete(id_quete)
        if not quete or not quete.est_complete():
            return False, {}

        quete.completer()

        # Retirer de quetes_acceptees et ajouter à quetes_completees
        if id_quete in self.quetes_acceptees:
            self.quetes_acceptees.remove(id_quete)
        if id_quete not in self.quetes_completees:
            self.quetes_completees.append(id_quete)

        # Enregistrer l'ordre de complétion pour les quêtes de royaume
        if quete.type_quete == TypeQuete.ROYAUME and quete.royaume:
            if quete.royaume not in self.ordre_completion_royaumes:
                self.ordre_completion_royaumes.append(quete.royaume)
                quete.ordre_completion = len(self.ordre_completion_royaumes)

        return True, quete.recompenses.copy()

    def obtenir_quete_principale_actuelle(self) -> Optional[Quete]:
        """Retourne la quête principale actuelle."""
        for quete in self.quetes.values():
            if quete.type_quete == TypeQuete.PRINCIPALE and quete.statut == StatutQuete.EN_COURS:
                return quete
        return None

    def obtenir_quetes_royaume(self, royaume: str) -> List[Quete]:
        """Retourne les quêtes d'un royaume."""
        return [q for q in self.quetes.values()
                if q.type_quete == TypeQuete.ROYAUME and q.royaume == royaume]

    def obtenir_quetes_secondaires(self, royaume: Optional[str] = None) -> List[Quete]:
        """Retourne les quêtes secondaires."""
        quetes = [q for q in self.quetes.values()
                  if q.type_quete == TypeQuete.SECONDAIRE]
        if royaume:
            quetes = [q for q in quetes if q.royaume == royaume]
        return quetes

    def to_dict(self) -> Dict[str, Any]:
        """
        Convertit le système de quêtes en dictionnaire pour la sauvegarde.
        """
        return {
            "quetes_acceptees": self.quetes_acceptees,
            "quetes_completees": self.quetes_completees,
            "ordre_completion_royaumes": self.ordre_completion_royaumes,
            "progression_objectifs": {
                quete_id: {
                    obj_idx: {
                        "quantite_actuelle": obj.quantite_actuelle,
                        "quantite_requise": obj.quantite_requise
                    }
                    for obj_idx, obj in enumerate(quete.objectifs)
                }
                for quete_id, quete in self.quetes.items()
                if quete_id in self.quetes_acceptees and quete.statut == StatutQuete.EN_COURS
            }
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SystemeQuetes':
        """
        Crée un système de quêtes à partir d'un dictionnaire (chargement).
        """
        from menus.quetes import initialiser_systeme_quetes

        systeme = initialiser_systeme_quetes()

        # Restaurer les quêtes acceptées et complétées
        systeme.quetes_acceptees = data.get("quetes_acceptees", [])
        systeme.quetes_completees = data.get("quetes_completees", [])
        systeme.ordre_completion_royaumes = data.get("ordre_completion_royaumes", [])

        # Restaurer les statuts des quêtes
        for quete_id in systeme.quetes_acceptees:
            quete = systeme.obtenir_quete(quete_id)
            if quete:
                quete.accepter()

        for quete_id in systeme.quetes_completees:
            quete = systeme.obtenir_quete(quete_id)
            if quete:
                quete.completer()

        # Restaurer la progression des objectifs
        progression = data.get("progression_objectifs", {})
        for quete_id, objectifs_data in progression.items():
            quete = systeme.obtenir_quete(quete_id)
            if quete:
                for obj_idx, obj_data in objectifs_data.items():
                    if 0 <= obj_idx < len(quete.objectifs):
                        quete.objectifs[obj_idx].quantite_actuelle = obj_data.get("quantite_actuelle", 0)
                        quete.objectifs[obj_idx].quantite_requise = obj_data.get("quantite_requise", 1)

        return systeme
