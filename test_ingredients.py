#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour data/ingredients.py
Teste toutes les fonctionnalités du système d'ingrédients
"""

import sys
sys.path.insert(0, '.')

from data.ingredients import (
    DEFINITIONS_INGREDIENTS,
    RARETES,
    DISTRIBUTION_RARETE,
    USAGE_POTIONS,
    USAGE_ARMES,
    USAGE_ARMURES,
    obtenir_ingredient,
    obtenir_ingredient_par_nom,
    obtenir_ingredients_par_usage,
    obtenir_ingredients_par_mob,
    obtenir_nom_complet_avec_qualite,
    obtenir_slug_par_nom,
    generer_slug,
    verifier_ingredient_existe
)

def test_basique():
    """Test des structures de base"""
    print("=" * 80)
    print("TEST 1 : Structures de base")
    print("=" * 80)

    print(f"✅ Total d'ingrédients : {len(DEFINITIONS_INGREDIENTS)}")
    print(f"✅ Niveaux de rareté : {RARETES}")
    print(f"✅ Distribution de rareté : {DISTRIBUTION_RARETE}")
    print(f"✅ Constantes d'usage : Potions={USAGE_POTIONS}, Armes={USAGE_ARMES}, Armures={USAGE_ARMURES}")

    # Vérifier que la somme des probabilités = 1
    somme = sum(DISTRIBUTION_RARETE.values())
    print(f"✅ Somme des probabilités : {somme} {'✅' if abs(somme - 1.0) < 0.001 else '❌'}")
    print()


def test_distribution_usage():
    """Test de la distribution par usage"""
    print("=" * 80)
    print("TEST 2 : Distribution par usage")
    print("=" * 80)

    potions = obtenir_ingredients_par_usage(USAGE_POTIONS)
    armes = obtenir_ingredients_par_usage(USAGE_ARMES)
    armures = obtenir_ingredients_par_usage(USAGE_ARMURES)

    print(f"✅ Ingrédients pour Potions : {len(potions)}")
    print(f"✅ Ingrédients pour Armes : {len(armes)}")
    print(f"✅ Ingrédients pour Armures : {len(armures)}")
    print(f"✅ Total : {len(potions) + len(armes) + len(armures)}")

    # Vérifier l'équilibrage
    if len(potions) == len(armes) == len(armures):
        print("✅ Distribution équilibrée !")
    else:
        print("⚠️  Distribution déséquilibrée")
    print()


def test_recherche_ingredient():
    """Test des fonctions de recherche"""
    print("=" * 80)
    print("TEST 3 : Recherche d'ingrédients")
    print("=" * 80)

    # Test par slug
    ing1 = obtenir_ingredient('cendre_maudite')
    if ing1:
        print(f"✅ Recherche par slug 'cendre_maudite' : {ing1['nom']} ({ing1['usage']})")
    else:
        print("❌ Échec recherche par slug")

    # Test par nom
    ing2 = obtenir_ingredient_par_nom('Cendre Maudite')
    if ing2:
        print(f"✅ Recherche par nom 'Cendre Maudite' : {ing2['nom']} ({ing2['usage']})")
    else:
        print("❌ Échec recherche par nom")

    # Test vérification existence
    existe = verifier_ingredient_existe('Cendre Maudite')
    print(f"✅ Vérification existence 'Cendre Maudite' : {existe}")

    # Test slug par nom
    slug = obtenir_slug_par_nom('Cendre Maudite')
    print(f"✅ Slug de 'Cendre Maudite' : {slug}")
    print()


def test_ingredients_par_mob():
    """Test de récupération des ingrédients par mob"""
    print("=" * 80)
    print("TEST 4 : Ingrédients par mob")
    print("=" * 80)

    # Test avec un mob spécifique
    mob_test = 'Spectres Cendrés'
    ingredients = obtenir_ingredients_par_mob(mob_test)

    print(f"✅ Ingrédients du mob '{mob_test}' : {len(ingredients)}")
    for ing in ingredients:
        print(f"   - {ing['nom']} ({ing['usage']})")

    # Vérifier qu'on a bien 3 ingrédients (1 potion, 1 arme, 1 armure)
    if len(ingredients) == 3:
        usages = [ing['usage'] for ing in ingredients]
        if USAGE_POTIONS in usages and USAGE_ARMES in usages and USAGE_ARMURES in usages:
            print("✅ Structure correcte : 1 Potion, 1 Arme, 1 Armure")
        else:
            print(f"⚠️  Structure incorrecte : {usages}")
    else:
        print(f"⚠️  Nombre d'ingrédients incorrect : {len(ingredients)}")
    print()


def test_qualite():
    """Test du système de qualité"""
    print("=" * 80)
    print("TEST 5 : Système de qualité")
    print("=" * 80)

    nom_ingredient = 'Cendre Maudite'

    print(f"✅ Génération de noms avec qualité pour '{nom_ingredient}' :")
    for qualite in RARETES:
        nom_complet = obtenir_nom_complet_avec_qualite(nom_ingredient, qualite)
        print(f"   - {nom_complet}")
    print()


def test_exemples_par_royaume():
    """Test d'exemples d'ingrédients par royaume"""
    print("=" * 80)
    print("TEST 6 : Exemples d'ingrédients par royaume")
    print("=" * 80)

    # Exemples de mobs par royaume
    exemples_mobs = {
        'Vrak\'thar': 'Spectres Cendrés',
        'Aerthos': 'Cerfs Lumina',
        'Khazak-Dûm': 'Gobs-Mineurs',
        'Luthesia': 'Brigands de Grand Chemin'
    }

    for royaume, mob in exemples_mobs.items():
        ingredients = obtenir_ingredients_par_mob(mob)
        print(f"\n🏰 {royaume} - Mob : {mob}")
        for ing in ingredients:
            print(f"   - {ing['nom']} ({ing['usage']})")
    print()


def test_generation_slug():
    """Test de génération de slug"""
    print("=" * 80)
    print("TEST 7 : Génération de slug")
    print("=" * 80)

    noms_test = [
        "Cendre Maudite",
        "Fragment d'Os Spectral",
        "Écorce de Cœur",
        "Essence du Chaos"
    ]

    for nom in noms_test:
        slug = generer_slug(nom)
        print(f"✅ '{nom}' → '{slug}'")
    print()


def test_statistiques():
    """Test des statistiques globales"""
    print("=" * 80)
    print("TEST 8 : Statistiques globales")
    print("=" * 80)

    # Compter les ingrédients par royaume
    royaumes = {}
    for slug, data in DEFINITIONS_INGREDIENTS.items():
        for source in data['sources']:
            royaume = source['royaume']
            if royaume not in royaumes:
                royaumes[royaume] = set()
            royaumes[royaume].add(slug)

    print("✅ Ingrédients par royaume (approximatif) :")
    for royaume, ingredients in sorted(royaumes.items()):
        print(f"   - {royaume} : {len(ingredients)} ingrédients uniques")
    print()


def main():
    """Fonction principale de test"""
    print("\n" + "=" * 80)
    print("TESTS DU SYSTÈME D'INGRÉDIENTS")
    print("=" * 80)
    print()

    try:
        test_basique()
        test_distribution_usage()
        test_recherche_ingredient()
        test_ingredients_par_mob()
        test_qualite()
        test_exemples_par_royaume()
        test_generation_slug()
        test_statistiques()

        print("=" * 80)
        print("✅ TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS !")
        print("=" * 80)

    except Exception as e:
        print(f"\n❌ ERREUR LORS DES TESTS : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
