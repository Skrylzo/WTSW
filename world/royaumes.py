# world/royaumes.py
# Définition des royaumes de Valdoria et leurs associations avec les races

from typing import Optional, Dict

from .hubs import HubCapital, CAPITALES_HUBS


class Royaume:
    """
    Représente un royaume dans le monde de Valdoria.
    Chaque royaume est associé à une race et contient plusieurs biomes/zones.
    """

    def __init__(self, nom, race_associee, description="", capitale="", histoire=""):
        """
        :param nom: Nom du royaume (ex: "Aerthos", "Khazak-Dûm")
        :param race_associee: Race associée à ce royaume (ex: "Elfe", "Nain")
        :param description: Description générale du royaume
        :param capitale: Nom de la capitale
        :param histoire: Histoire spécifique du royaume
        """
        self.nom = nom
        self.race_associee = race_associee
        self.description = description
        self.capitale = capitale
        self.histoire = histoire
        self.biomes = []  # Liste des biomes de ce royaume (sera remplie plus tard)
        self.roi_ou_leader = None  # Informations sur le dirigeant
        self.npcs_importants = []  # Liste des NPCs importants (gardiens, conseillers, etc.)
        self.est_debloque = False  # Pour la progression du jeu
        self.hub_capital: Optional[HubCapital] = None  # Hub (capitale) associé

    def ajouter_biome(self, biome):
        """Ajoute un biome à ce royaume."""
        if biome not in self.biomes:
            self.biomes.append(biome)

    def obtenir_mobs_par_biome(self):
        """Retourne un dictionnaire {nom_biome: [liste_ids_mobs]}."""
        return {biome.nom: biome.mobs_ids for biome in self.biomes}

    def obtenir_donjons(self):
        """Retourne la liste des donjons de ce royaume."""
        donjons = []
        for biome in self.biomes:
            if biome.donjon_nom:
                donjons.append({
                    "nom": biome.donjon_nom,
                    "biome": biome.nom,
                    "boss_id": biome.boss_id
                })
        return donjons

    def attacher_hub_capital(self, hub: HubCapital):
        """Associe un hub (capitale) à ce royaume."""
        self.hub_capital = hub

    def obtenir_services_capitale(self) -> Dict[str, list]:
        """Retourne le résumé des services disponibles dans la capitale."""
        if self.hub_capital:
            return self.hub_capital.lister_services()
        return {}

    def __repr__(self):
        return f"Royaume(nom='{self.nom}', race='{self.race_associee}')"


# Mapping race → royaume (les démons spawnent dans leur royaume, etc.)
MAPPING_RACE_ROYAUME = {
    "Elfe": "Aerthos",
    "Nain": "Khazak-Dûm",
    "Humain": "Luthesia",
    "Démon": "Vrak'thar"
}


def obtenir_royaume_par_race(race):
    """
    Retourne le nom du royaume associé à une race.
    :param race: Nom de la race (ex: "Elfe", "Démon")
    :return: Nom du royaume associé, ou None si non trouvé
    """
    return MAPPING_RACE_ROYAUME.get(race)


def obtenir_tous_royaumes():
    """
    Retourne la liste de tous les royaumes disponibles.
    :return: Liste des noms de royaumes
    """
    return list(MAPPING_RACE_ROYAUME.values())


# Dictionnaire global contenant tous les royaumes instanciés
# Sera rempli par le data_loader ou manuellement
TOUS_LES_ROYAUMES = {}


def initialiser_royaumes_avec_hubs():
    """
    Initialise tous les royaumes de base avec leurs hubs attachés.
    Cette fonction doit être appelée une fois au démarrage du jeu.
    :return: Dict des royaumes initialisés {nom_royaume: Royaume}
    """
    if TOUS_LES_ROYAUMES:
        # Déjà initialisé, retourner les royaumes existants
        return TOUS_LES_ROYAUMES

    # Définitions de base des royaumes (sera enrichi plus tard avec les fichiers Valdoria)
    definitions_royaumes = {
        "Aerthos": {
            "nom": "Aerthos",
            "race_associee": "Elfe",
            "description": "Royaume elfique de beauté et de sagesse ancestrale",
            "capitale": "Lunara",
            "histoire": "Aerthos est une terre d'une beauté à couper le souffle..."
        },
        "Khazak-Dûm": {
            "nom": "Khazak-Dûm",
            "race_associee": "Nain",
            "description": "Royaume des Nains, forteresse souterraine et forge éternelle",
            "capitale": "Karahisar",
            "histoire": "Khazak-Dûm est le royaume souterrain des Nains..."
        },
        "Luthesia": {
            "nom": "Luthesia",
            "race_associee": "Humain",
            "description": "Royaume humain prospère et puissant",
            "capitale": "Massalia",
            "histoire": "Luthesia est le grand royaume humain de Valdoria..."
        },
        "Vrak'thar": {
            "nom": "Vrak'thar",
            "race_associee": "Démon",
            "description": "Royaume démoniaque, terre de puissance brute et de corruption",
            "capitale": "Erebus",
            "histoire": "Vrak'thar est le continent démoniaque où règnent la force et la terreur..."
        }
    }

    # Créer les instances de royaumes
    for royaume_nom, data in definitions_royaumes.items():
        royaume = Royaume(
            nom=data["nom"],
            race_associee=data["race_associee"],
            description=data["description"],
            capitale=data["capitale"],
            histoire=data["histoire"]
        )
        TOUS_LES_ROYAUMES[royaume_nom] = royaume

    # Attacher les hubs aux royaumes
    attacher_capitales_aux_royaumes(TOUS_LES_ROYAUMES)

    return TOUS_LES_ROYAUMES


def attacher_capitales_aux_royaumes(royaumes_dict=None):
    """
    Associe automatiquement les hubs de capitales aux royaumes instanciés.
    :param royaumes_dict: Dictionnaire {nom_royaume: Royaume} (utilise TOUS_LES_ROYAUMES si None)
    """
    royaumes_dict = royaumes_dict or TOUS_LES_ROYAUMES
    for royaume_nom, royaume in royaumes_dict.items():
        hub = CAPITALES_HUBS.get(royaume_nom)
        if hub:
            royaume.attacher_hub_capital(hub)


def obtenir_royaume_du_joueur(race_joueur: str) -> Optional[Royaume]:
    """
    Obtient le royaume associé à la race d'un joueur.
    Initialise les royaumes si nécessaire.
    :param race_joueur: Race du joueur (ex: "Elfe", "Démon")
    :return: Instance de Royaume associé, ou None si non trouvé
    """
    # S'assurer que les royaumes sont initialisés
    if not TOUS_LES_ROYAUMES:
        initialiser_royaumes_avec_hubs()

    royaume_nom = obtenir_royaume_par_race(race_joueur)
    if royaume_nom:
        return TOUS_LES_ROYAUMES.get(royaume_nom)
    return None


def obtenir_hub_du_joueur(race_joueur: str) -> Optional[HubCapital]:
    """
    Obtient le hub (capitale) associé à la race d'un joueur.
    Initialise les royaumes si nécessaire.
    :param race_joueur: Race du joueur (ex: "Elfe", "Démon")
    :return: Instance de HubCapital associé, ou None si non trouvé
    """
    royaume = obtenir_royaume_du_joueur(race_joueur)
    if royaume and royaume.hub_capital:
        return royaume.hub_capital
    return None


def obtenir_royaume_par_nom(nom_royaume: str) -> Optional[Royaume]:
    """
    Obtient un royaume par son nom.
    Initialise les royaumes si nécessaire.
    :param nom_royaume: Nom du royaume (ex: "Aerthos")
    :return: Instance de Royaume, ou None si non trouvé
    """
    # S'assurer que les royaumes sont initialisés
    if not TOUS_LES_ROYAUMES:
        initialiser_royaumes_avec_hubs()

    return TOUS_LES_ROYAUMES.get(nom_royaume)


# Initialisation automatique à l'import
initialiser_royaumes_avec_hubs()
