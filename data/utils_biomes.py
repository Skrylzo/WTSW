# data/utils_biomes.py
# Utilitaires pour obtenir les informations de biome depuis un mob

from typing import Optional
from data.ingredients import DEFINITIONS_INGREDIENTS


def obtenir_niveau_biome_depuis_mob(nom_mob: str) -> Optional[int]:
    """
    Obtient le niveau minimum du biome d'origine d'un mob.

    :param nom_mob: Nom du mob
    :return: Niveau minimum du biome ou None si non trouvé
    """
    try:
        from world.biomes_valdoria import BIOMES_DATA

        # Chercher dans tous les royaumes et biomes
        for royaume, biomes in BIOMES_DATA.items():
            for biome in biomes:
                # Vérifier si le mob est dans ce biome
                mobs_ids = biome.mobs_ids
                mob_slug = _slugify_mob(nom_mob)

                if mob_slug in mobs_ids or nom_mob in [mob for mob in mobs_ids]:
                    return biome.niveau_min

        # Si pas trouvé dans les biomes, chercher dans les ingrédients
        for ing_id, ing_data in DEFINITIONS_INGREDIENTS.items():
            sources = ing_data.get('sources', [])
            for source in sources:
                if source.get('mob') == nom_mob:
                    # Trouver le biome correspondant
                    biome_nom = source.get('biome', '')
                    royaume = source.get('royaume', '')

                    if royaume in BIOMES_DATA:
                        for biome in BIOMES_DATA[royaume]:
                            if biome_nom in biome.nom or biome.nom in biome_nom:
                                return biome.niveau_min

        return None
    except ImportError:
        return None


def _slugify_mob(nom: str) -> str:
    """Crée un slug à partir du nom du mob (similaire à celui utilisé dans le système)"""
    import unicodedata
    import re

    nom = unicodedata.normalize('NFD', nom)
    nom = nom.lower()
    nom = re.sub(r'[^\w\s-]', '', nom)
    nom = re.sub(r'[-\s]+', '_', nom)
    return nom.strip('_')
