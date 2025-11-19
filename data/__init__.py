# data/__init__.py
# Exporte toutes les données pour faciliter les imports

from .races_classes import DEFINITIONS_RACES_CLASSES
from .capacites import TOUTES_LES_CAPACITES_DATA
from .ennemis import DEFINITIONS_ENNEMIS
from .armes import DEFINITIONS_ARMES
from .objets import DEFINITIONS_OBJETS, RECETTES_CRAFTING

__all__ = [
    'DEFINITIONS_RACES_CLASSES',
    'TOUTES_LES_CAPACITES_DATA',
    'DEFINITIONS_ENNEMIS',
    'DEFINITIONS_ARMES',
    'DEFINITIONS_OBJETS',
    'RECETTES_CRAFTING'
]
