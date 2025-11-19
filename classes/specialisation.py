# classes/specialisation.py

class Specialisation:
    def __init__(self, nom, description, type_ressource, capacites_initiales):
        self.nom = nom
        self.description = description
        self.type_ressource = type_ressource
        self.capacites_initiales = capacites_initiales

    def __str__(self):
        return self.nom
