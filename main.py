import matplotlib.pyplot as plt
import networkx as nx


from noeud import Noeud

# On crée l'expression exp(2 + y)
racine = Noeud("exp")       # Racine de l'arbre
somme = Noeud("+")          # Noeud enfant (l'opération +)
somme.ajouter_enfant(Noeud(2))   # Premier enfant = 2
somme.ajouter_enfant(Noeud("y")) # Deuxième enfant = y
racine.ajouter_enfant(somme)     # On relie somme à exp

# Affichage de l'expression en notation polonaise
print(racine.afficher())

