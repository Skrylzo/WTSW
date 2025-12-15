# combat/selection.py
# Fonctions de sélection (cible, capacité)

from classes.base_combatant import Personnage
from classes.capacite import Capacite
from utils.affichage import COULEURS

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
        print(f"{COULEURS['ROUGE']}❌ {personnage.nom} n'a aucune capacité apprise ou disponible à votre niveau à utiliser.{COULEURS['RESET']}")
        return None

    print(f"\n{COULEURS['MAGENTA']}✨ {personnage.nom}, choisissez une capacité :{COULEURS['RESET']}\n")
    for i, cap in enumerate(capacites_disponibles_au_niveau):
        # Déterminer la couleur selon le type de ressource
        couleur_ressource = COULEURS["CYAN"]
        emoji_ressource = "💫"
        cost_info = ""

        if personnage.specialisation.type_ressource == "Mana" and cap.cout_mana > 0:
            couleur_ressource = COULEURS["BLEU"]
            emoji_ressource = "🔵"
            cost_info = f"{couleur_ressource}(Coût: {cap.cout_mana} Mana){COULEURS['RESET']}"
            # Vérifier si assez de ressources
            if personnage.mana < cap.cout_mana:
                couleur_ressource = COULEURS["ROUGE"]
        elif personnage.specialisation.type_ressource == "Energie" and cap.cout_energie > 0:
            couleur_ressource = COULEURS["JAUNE"]
            emoji_ressource = "⚡"
            cost_info = f"{couleur_ressource}(Coût: {cap.cout_energie} Énergie){COULEURS['RESET']}"
            if personnage.energie < cap.cout_energie:
                couleur_ressource = COULEURS["ROUGE"]
        elif personnage.specialisation.type_ressource == "Rage" and cap.cout_rage > 0:
            couleur_ressource = COULEURS["ROUGE"]
            emoji_ressource = "🔥"
            cost_info = f"{couleur_ressource}(Coût: {cap.cout_rage} Rage){COULEURS['RESET']}"
            if personnage.rage < cap.cout_rage:
                couleur_ressource = COULEURS["ROUGE"]

        # Emoji selon le type de capacité
        emoji_capacite = "✨"
        if cap.type_cible == "ennemi" or cap.type_cible == "unique":
            emoji_capacite = "⚔️"
        elif cap.type_cible == "soi":
            emoji_capacite = "🛡️"
        elif cap.type_cible == "allies":
            emoji_capacite = "💚"
        elif cap.type_cible == "tous_ennemis":
            emoji_capacite = "💥"

        # Afficher avec formatage amélioré
        nom_couleur = COULEURS["MAGENTA"] if personnage.mana >= cap.cout_mana or personnage.energie >= cap.cout_energie or personnage.rage >= cap.cout_rage else COULEURS["GRIS"]
        print(f"{COULEURS['CYAN']}{i+1}.{COULEURS['RESET']} {emoji_capacite} {nom_couleur}{cap.nom}{COULEURS['RESET']} {cost_info}")
        print(f"   {COULEURS['GRIS']}{cap.description}{COULEURS['RESET']}\n")

    while True:
        try:
            choix = input(f"{COULEURS['MAGENTA']}Entrez le numéro de la capacité (ou 'a' pour annuler) : {COULEURS['RESET']}")
            if choix.lower() == 'a':
                return None

            choix = int(choix) - 1
            if 0 <= choix < len(capacites_disponibles_au_niveau):
                capacite_choisie = capacites_disponibles_au_niveau[choix]
                if (capacite_choisie.cout_mana > 0 and personnage.mana < capacite_choisie.cout_mana) or \
                   (capacite_choisie.cout_energie > 0 and personnage.energie < capacite_choisie.cout_energie) or \
                   (capacite_choisie.cout_rage > 0 and personnage.rage < capacite_choisie.cout_rage):
                    print(f"{COULEURS['ROUGE']}❌ Pas assez de ressource pour {capacite_choisie.nom}!{COULEURS['RESET']}")
                    continue
                return capacite_choisie
            else:
                print(f"{COULEURS['ROUGE']}❌ Capacité invalide. Veuillez réessayer.{COULEURS['RESET']}")
        except ValueError:
            print(f"{COULEURS['ROUGE']}❌ Entrée invalide. Veuillez entrer un numéro.{COULEURS['RESET']}")
