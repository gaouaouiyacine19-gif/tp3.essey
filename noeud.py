class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

    def afficher(self):
        """Affiche l'expression en notation polonaise"""
        if not self.enfants:
            return str(self.valeur)
        else:
            return f"{self.valeur} " + " ".join(enfant.afficher() for enfant in self.enfants)

