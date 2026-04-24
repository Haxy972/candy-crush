import matplotlib.pyplot as plt
from random import randint, choice

def init_grille(taille):
  grille = []
  return grille
  
def init_jeu(grille):
  return 

def detecte_coordonnees_combinaison (griLle, i, j):
  """
  Renvoie une liste contenant les coordonnées de tous les bonbons
  appartenant à la combinaison du bonbon ( i , j ) .
  """

def affiche_grille(jeu):
  for i in range(len(jeu)):
      print()
      for j in range(len(jeu[i])):
          print(jeu[i][j],end=" ")

def saisie_coord(grille):
    """ 
    Permet de saisir les coordoonées du bonbon que l'on voudra déplacer
    param : grille (liste 2D)
    return : coord_x(int), coord_y(int)
    """
    test = True 
    
    while test == True:
        try:
            coord_x = int(input("Saisissez X : "))
            coord_y = int(input("Saisissez Y : "))

            
            if 0 <= coord_x < len(grille) and 0 <= coord_y < len(grille[0]):
                return coord_x, coord_y
            else:
                print("Coordonnées hors de la grille.")

        except ValueError:
            print("Veuillez saisir un nombre.")


liste = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
print(saisie_coord(liste))