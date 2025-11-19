# combat/selection.py
# Fonctions de sélection (cible, capacité)

from classes.base_combatant import Personnage
from classes.capacite import Capacite

def choisir_cible(attaquant, cibles_potentielles):
    """Permet à l'attaquant de choisir une cible parmi une liste."""
    if not cibles_potentielles:
        print("Il n'y a pas de cibles disponibles.")
        return None

    print(f"\n{attaquant.nom}, choisissez votre cible:")
    for i, cible in enumerate(cibles_potentielles):
        if cible.est_vivant:
            print(f"{i+1}. {cible.nom} (Vie: {cible.vie:.1f}/{cible.vie_max:.1f})")
        else:
            print(f"{i+1}. {cible.nom} (Vaincu)")

    while True:
        try:
            choix = input("Entrez le numéro de la cible (ou 'a' pour annuler) : ")
            if choix.lower() == 'a':
                return None

            choix = int(choix) - 1
            if 0 <= choix < len(cibles_potentielles) and cibles_potentielles[choix].est_vivant:
                return cibles_potentielles[choix]
            else:
                print("Cible invalide ou déjà vaincue. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")

def choisir_capacite(personnage):
    """Permet au personnage de choisir une capacité à utiliser."""
    capacites_disponibles_au_niveau = [cap for cap in personnage.capacites_apprises if personnage.niveau >= cap.niveau_requis]

    if not capacites_disponibles_au_niveau:
        print(f"{personnage.nom} n'a aucune capacité apprise ou disponible à votre niveau à utiliser.")
        return None

    print(f"\n{personnage.nom}, choisissez une capacité:")
    for i, cap in enumerate(capacites_disponibles_au_niveau):
        cost_info = ""
        if personnage.specialisation.type_ressource == "Mana" and cap.cout_mana > 0:
            cost_info = f" (Coût: {cap.cout_mana} Mana)"
        elif personnage.specialisation.type_ressource == "Energie" and cap.cout_energie > 0:
            cost_info = f" (Coût: {cap.cout_energie} Énergie)"
        elif personnage.specialisation.type_ressource == "Rage" and cap.cout_rage > 0:
            cost_info = f" (Coût: {cap.cout_rage} Rage)"

        print(f"{i+1}. {cap.nom}{cost_info}: {cap.description}")

    while True:
        try:
            choix = input("Entrez le numéro de la capacité (ou 'a' pour annuler) : ")
            if choix.lower() == 'a':
                return None

            choix = int(choix) - 1
            if 0 <= choix < len(capacites_disponibles_au_niveau):
                capacite_choisie = capacites_disponibles_au_niveau[choix]
                if (capacite_choisie.cout_mana > 0 and personnage.mana < capacite_choisie.cout_mana) or \
                   (capacite_choisie.cout_energie > 0 and personnage.energie < capacite_choisie.cout_energie) or \
                   (capacite_choisie.cout_rage > 0 and personnage.rage < capacite_choisie.cout_rage):
                    print(f"Pas assez de ressource pour {capacite_choisie.nom}!")
                    continue
                return capacite_choisie
            else:
                print("Capacité invalide. Veuillez réessayer.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
