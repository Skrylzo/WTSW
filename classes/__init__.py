# classes/__init__.py
# Exporte toutes les classes pour faciliter les imports

from .effet import Effet
from .specialisation import Specialisation
from .capacite import Capacite
from .objet import Objet
from .arme import Arme
from .base_combatant import BaseCombatant, Personnage, Ennemi

__all__ = [
    'Effet',
    'Specialisation',
    'Capacite',
    'Objet',
    'Arme',
    'BaseCombatant',
    'Personnage',
    'Ennemi'
]
