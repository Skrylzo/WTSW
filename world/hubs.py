# world/hubs.py
# Définition des capitales comme hubs principaux (commerce, craft, quêtes, téléportation, etc.)

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional


class FeatureType(Enum):
    """Types de fonctionnalités disponibles dans une capitale."""

    COMMERCE = "commerce"
    CRAFT = "craft"
    QUETE = "quete"
    TELEPORTATION = "teleportation"
    SOINS = "soins"
    FORMATION = "formation"
    TRANSPORT = "transport"


@dataclass
class HubFeature:
    """Représente une fonctionnalité disponible dans un hub (marché, forge, etc.)."""

    nom: str
    type_feature: FeatureType
    description: str
    services: List[str] = field(default_factory=list)
    conditions: Optional[str] = None


@dataclass
class HubCapital:
    """Hub principal (capitale) d'un royaume."""

    nom: str
    royaume_nom: str
    description: str
    lieux_cles: List[str]
    features: List[HubFeature]
    pnjs_importants: List[str]
    teleportations: List[str]
    respawn_message: str
    notes: Optional[str] = None

    def obtenir_features_par_type(self, type_feature: FeatureType) -> List[HubFeature]:
        """Retourne les fonctionnalités correspondant à un type donné."""
        return [feature for feature in self.features if feature.type_feature == type_feature]

    def lister_services(self) -> Dict[str, List[str]]:
        """Retourne un résumé des services disponibles par type."""
        resume = {}
        for feature in self.features:
            resume.setdefault(feature.type_feature.value, []).append(feature.nom)
        return resume


DEFINITIONS_CAPITALES: Dict[str, Dict] = {
    "Aerthos": {
        "nom": "Lunara",
        "description": (
            "Sanctuaire elfique sculpté dans des arbres-mondes et des cristaux vivants, "
            "où la lumière lunaire nourrit les jardins et les portails arcanes."
        ),
        "lieux_cles": [
            "Carrefour des Murmures Éthérés",
            "Jardins Lunaires Suspendus",
            "Portails de Sélénia",
            "Bibliothèque des Aurores",
        ],
        "features": [
            {
                "nom": "Marché de Lumière",
                "type": FeatureType.COMMERCE,
                "description": "Boutiques organiques vendant artefacts enchantés, herbes rares et soies lunaires.",
                "services": [
                    "Achat/Vente d'objets magiques",
                    "Échange de ressources naturelles",
                    "Contrats d'artisans spirituels",
                ],
            },
            {
                "nom": "Ateliers Arcaniques",
                "type": FeatureType.CRAFT,
                "description": "Ateliers suspendus pour imbu de magie les armes et armures.",
                "services": [
                    "Infusions lunaires",
                    "Gravure de runes sylvestres",
                    "Réparation accélérée par magie",
                ],
            },
            {
                "nom": "Conseil de Lumina",
                "type": FeatureType.QUETE,
                "description": "Lieu où les gardiens élèvent les quêtes principales d'Aerthos.",
                "services": [
                    "Quêtes scénarisées du royaume",
                    "Missions de protection des biomes",
                    "Accès aux archives (lore, indices)",
                ],
            },
            {
                "nom": "Portails Lunaires",
                "type": FeatureType.TELEPORTATION,
                "description": "Anneaux cristallins permettant de rejoindre les autres royaumes débloqués.",
                "services": [
                    "Téléportation vers capitales alliées",
                    "Retour instantané depuis les biomes",
                    "Synchronisation des chapitres",
                ],
                "conditions": "Débloqué après l'Alliance d'Aerthos (Chapitre 2).",
            },
            {
                "nom": "Sanctuaire de Sélène",
                "type": FeatureType.SOINS,
                "description": "Bassins d'énergie lunaire pour se soigner et récupérer ses ressources.",
                "services": [
                    "Soins gratuits après défaite",
                    "Restauration des ressources",
                    "Bénédictions temporaires",
                ],
            },
        ],
        "pnjs": [
            "Roi Aerion Luminael",
            "Lyraea Ombrefeuille",
            "Faelar Éternelbranche",
            "Seraphina Étoileprofonde",
            "Lorien Chantclair",
        ],
        "teleportations": [
            "Portails vers Khazak-Dûm, Luthesia, Vrak'thar (après alliances)",
            "Ancrages vers chaque biome elfique",
        ],
        "respawn_message": "Vous vous réveillez à Lunara, baigné par la lumière guérisseuse des Jardins Lunaires.",
        "notes": "Hub prioritaire pour les joueurs elfes ; accessible aux alliés après Chapitre 2.",
    },
    "Khazak-Dûm": {
        "nom": "Karahisar",
        "description": (
            "Citadelle creusée dans la montagne, illuminée par des forges éternelles et "
            "des rails de transport runiques."
        ),
        "lieux_cles": [
            "Le Marteau Rouge",
            "La Forge Éternelle",
            "Hall des Clans",
            "Portails Runés",
        ],
        "features": [
            {
                "nom": "Bazars du Marteau Rouge",
                "type": FeatureType.COMMERCE,
                "description": "Marchés troquant minerais rares, pièces mécaniques et schémas nains.",
                "services": [
                    "Achat de matériaux métalliques",
                    "Vente d'objets artisanaux",
                    "Contrats de mineurs",
                ],
            },
            {
                "nom": "Forge Éternelle",
                "type": FeatureType.CRAFT,
                "description": "Forge mythique alimentée par un cœur de magma.",
                "services": [
                    "Craft d'armes/armures lourdes",
                    "Insertion de gemmes runiques",
                    "Améliorations de boucliers",
                ],
            },
            {
                "nom": "Hall des Clans",
                "type": FeatureType.QUETE,
                "description": "Conseil des quatre chefs de clan, dispensant missions et réputations.",
                "services": [
                    "Quêtes de défense des mines",
                    "Contrats de récupération",
                    "Déblocage d'améliorations de clan",
                ],
            },
            {
                "nom": "Portails Runés",
                "type": FeatureType.TELEPORTATION,
                "description": "Cercles gravés permettant de voyager via les lignes telluriques.",
                "services": [
                    "Transport instantané vers les biomes nains",
                    "Ponts vers les capitales alliées",
                    "Retour automatique après mission",
                ],
                "conditions": "Activé après avoir réparé les relais runiques (Chapitre 2).",
            },
            {
                "nom": "Sanctuaire de Durin",
                "type": FeatureType.SOINS,
                "description": "Hall de repos supervisé par les matriarches guérisseuses.",
                "services": [
                    "Soins gratuits après défaite",
                    "Renforts défensifs temporaires",
                    "Banquets augmentant le moral",
                ],
            },
            {
                "nom": "Académie d'Ingénierie",
                "type": FeatureType.FORMATION,
                "description": "Lieu d'apprentissage des gadgets et automatons nains.",
                "services": [
                    "Déblocage de recettes technologiques",
                    "Tests de prototypes",
                    "Leçons de renforcement mécanique",
                ],
            },
        ],
        "pnjs": [
            "Roi Orhan Demirci",
            "Grom Starkov",
            "Borina Yer",
            "Zamir Oural",
            "Bayar Sözcü",
        ],
        "teleportations": [
            "Rails gravitationnels vers les mines",
            "Portails runiques vers Luthesia et Aerthos (après alliances)",
        ],
        "respawn_message": "Vous reprenez vos esprits dans Karahisar, entouré du grondement rassurant des forges.",
        "notes": "Hub par défaut des joueurs nains ; requis pour débloquer les craft avancés.",
    },
    "Luthesia": {
        "nom": "Massalia",
        "description": (
            "Capitale humaine bâtie autour de l'Esplanade de l'Unité, combinant forteresse, "
            "académie et marché continental."
        ),
        "lieux_cles": [
            "Esplanade de l'Unité",
            "Fort Solara",
            "Observatoire des Astres",
            "Basilique de la Lumière",
        ],
        "features": [
            {
                "nom": "Grand Marché de Massalia",
                "type": FeatureType.COMMERCE,
                "description": "Centre névralgique du commerce humain, reliant tous les fiefs.",
                "services": [
                    "Achat/Vente d'équipement polyvalent",
                    "Bourses aux contrats",
                    "Offres saisonnières",
                ],
            },
            {
                "nom": "Arsenal de Fort Solara",
                "type": FeatureType.CRAFT,
                "description": "Arsenal militaire permettant de forger des armes et armures disciplinées.",
                "services": [
                    "Forge d'armes chevaleresques",
                    "Renforcement de bannières",
                    "Production de consommables tactiques",
                ],
            },
            {
                "nom": "Chancellerie Royale",
                "type": FeatureType.QUETE,
                "description": "Quartier général des quêtes principales humaines et diplomatiques.",
                "services": [
                    "Quêtes politiques",
                    "Missions d'escorte et de siège",
                    "Accès aux archives impériales",
                ],
            },
            {
                "nom": "Observatoire des Astres",
                "type": FeatureType.TELEPORTATION,
                "description": "Tour offrant un réseau de miroirs arcaniques pour voyager.",
                "services": [
                    "Téléportation vers capitales alliées",
                    "Projecteurs tactiques vers les biomes",
                    "Observation des menaces en temps réel",
                ],
                "conditions": "Synchronisé après la signature du Pacte des Royaumes.",
            },
            {
                "nom": "Basilique de la Lumière",
                "type": FeatureType.SOINS,
                "description": "Sanctuaire de soins et bénédictions sacrées.",
                "services": [
                    "Soins gratuits après défaite",
                    "Bénédictions offensives",
                    "Purge des malédictions",
                ],
            },
            {
                "nom": "Académie de Commandement",
                "type": FeatureType.FORMATION,
                "description": "École stratégique pour perfectionner les tactiques de combat.",
                "services": [
                    "Entraînements (bonus temporaires)",
                    "Simulations",
                    "Déblocage d'emplacements tactiques",
                ],
            },
        ],
        "pnjs": [
            "Sire Erme de l'Épée d'Or",
            "Dame Seraphina Veritas",
            "Baron Silas de Monnaie",
            "Duchesse Aliénor de Valois",
        ],
        "teleportations": [
            "Miroirs vers Aerthos, Khazak-Dûm et Vrak'thar",
            "Balises vers les fiefs humains",
        ],
        "respawn_message": "Vous êtes ramené à Massalia, accueilli par la lumière rassurante de la Basilique.",
        "notes": "Hub par défaut des joueurs humains ; offre les meilleures options diplomatiques.",
    },
    "Vrak'thar": {
        "nom": "Erebus",
        "description": (
            "Cité démoniaque sculptée dans l'obsidienne et la chair, où les marchés noirs et les "
            "obélisques dimensionnels pulsent d'énergie."
        ),
        "lieux_cles": [
            "Carrefour des Abominations",
            "Château de la Déraison",
            "Obélisques de Xyl'ka",
            "Fosse de Régénération",
        ],
        "features": [
            {
                "nom": "Marché Noir d'Erebus",
                "type": FeatureType.COMMERCE,
                "description": "Marché où se négocient reliques corrompues et essences d'âmes.",
                "services": [
                    "Achat de composants démoniaques",
                    "Échanges d'essences",
                    "Contrats obscurs",
                ],
            },
            {
                "nom": "Forges de la Déraison",
                "type": FeatureType.CRAFT,
                "description": "Forges qui infusent le matériel avec l'énergie du chaos.",
                "services": [
                    "Fusion d'essences",
                    "Création d'armes corruptrices",
                    "Altération d'armures",
                ],
            },
            {
                "nom": "Citadelle du Roi Démon",
                "type": FeatureType.QUETE,
                "description": "Lieu où Vol'thrak et ses généraux assignent les quêtes.",
                "services": [
                    "Quêtes de domination",
                    "Missions d'infiltration des royaumes",
                    "Accès au lore démoniaque",
                ],
            },
            {
                "nom": "Obélisques de Pliage",
                "type": FeatureType.TELEPORTATION,
                "description": "Monolithes capables de déchirer le voile entre les royaumes.",
                "services": [
                    "Téléportation vers zones corrompues",
                    "Intrusions rapides dans les autres capitales",
                    "Retour instantané après défaite",
                ],
                "conditions": "Utilisable après avoir calmé les obélisques (Chapitre 3).",
            },
            {
                "nom": "Fosse de Régénération",
                "type": FeatureType.SOINS,
                "description": "Bassin de chair et d'ichor régénérant les forces des démons.",
                "services": [
                    "Soins rapides",
                    "Boost de rage",
                    "Restauration d'effets corrompus",
                ],
            },
            {
                "nom": "Puits des Légions",
                "type": FeatureType.FORMATION,
                "description": "Arènes d'entraînement pour affiner les capacités démoniaques.",
                "services": [
                    "Entraînements brutaux",
                    "Déblocage de transformations",
                    "Simulations d'assauts",
                ],
            },
        ],
        "pnjs": [
            "Roi Démon Vol'thrak",
            "A'skaran",
            "Mor'Gath",
            "Zar'eth",
            "Vyk'thal",
        ],
        "teleportations": [
            "Obélisques vers les biomes démoniaques",
            "Fissures vers les capitales ennemies (après Chapitre 4)",
        ],
        "respawn_message": "Vous rouvrez les yeux dans Erebus, immergé dans les fosses régénératrices.",
        "notes": "Hub par défaut des joueurs démons ; offre des options uniques de corruption.",
    },
}


CAPITALES_HUBS: Dict[str, HubCapital] = {}


def initialiser_capitales_hubs() -> Dict[str, HubCapital]:
    """Instancie les hubs des capitales à partir des définitions."""
    if CAPITALES_HUBS:
        return CAPITALES_HUBS

    for royaume_nom, data in DEFINITIONS_CAPITALES.items():
        features = [
            HubFeature(
                nom=feature_data["nom"],
                type_feature=feature_data["type"],
                description=feature_data["description"],
                services=feature_data.get("services", []),
                conditions=feature_data.get("conditions"),
            )
            for feature_data in data["features"]
        ]

        hub = HubCapital(
            nom=data["nom"],
            royaume_nom=royaume_nom,
            description=data["description"],
            lieux_cles=data["lieux_cles"],
            features=features,
            pnjs_importants=data["pnjs"],
            teleportations=data["teleportations"],
            respawn_message=data["respawn_message"],
            notes=data.get("notes"),
        )

        CAPITALES_HUBS[royaume_nom] = hub

    return CAPITALES_HUBS


# Initialisation à l'import pour rendre les hubs disponibles immédiatement
initialiser_capitales_hubs()
