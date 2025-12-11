# world/__init__.py
# Module de gestion du monde de Valdoria

from .royaumes import (
    Royaume,
    obtenir_royaume_par_race,
    obtenir_tous_royaumes,
    attacher_capitales_aux_royaumes,
    initialiser_royaumes_avec_hubs,
    obtenir_royaume_du_joueur,
    obtenir_hub_du_joueur,
    obtenir_royaume_par_nom,
    TOUS_LES_ROYAUMES,
)
from .biomes import Biome, Zone
from .story import HistoireGlobale, HistoireRoyaume
from .quetes import (
    SystemeQuetes, Quete, ObjectifQuete, TypeQuete, TypeObjectif, StatutQuete
)
from .gameplay import SystemeGameplay, TypeGameplay, ModeProgression
from .chapitres import Chapitre, ChoixNarratif, SystemeChapitres, TypeChapitre
from .farming import SystemeFarming, SYSTEME_FARMING
from .joueur_hub import (
    obtenir_capitale_joueur,
    teleporter_joueur_vers_capitale,
    afficher_services_capitale_joueur,
)
from .hubs import (
    HubCapital,
    HubFeature,
    FeatureType,
    CAPITALES_HUBS,
    initialiser_capitales_hubs,
)
from .data_loader import attacher_biomes_depuis_valdoria

# Charger automatiquement les biomes de Valdoria
attacher_biomes_depuis_valdoria()

__all__ = [
    'Royaume',
    'Biome',
    'Zone',
    'HistoireGlobale',
    'HistoireRoyaume',
    'SystemeQuetes',
    'Quete',
    'ObjectifQuete',
    'TypeQuete',
    'TypeObjectif',
    'StatutQuete',
    'SystemeGameplay',
    'TypeGameplay',
    'ModeProgression',
    'HubCapital',
    'HubFeature',
    'FeatureType',
    'CAPITALES_HUBS',
    'initialiser_capitales_hubs',
    'Chapitre',
    'ChoixNarratif',
    'SystemeChapitres',
    'TypeChapitre',
    'SystemeFarming',
    'SYSTEME_FARMING',
    'obtenir_capitale_joueur',
    'teleporter_joueur_vers_capitale',
    'afficher_services_capitale_joueur',
    'obtenir_royaume_par_race',
    'obtenir_tous_royaumes',
    'attacher_capitales_aux_royaumes',
    'initialiser_royaumes_avec_hubs',
    'obtenir_royaume_du_joueur',
    'obtenir_hub_du_joueur',
    'obtenir_royaume_par_nom',
    'TOUS_LES_ROYAUMES',
    'attacher_biomes_depuis_valdoria',
]
