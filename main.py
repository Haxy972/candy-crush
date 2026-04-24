"""
Created on friday 24 08:53:00 2026

@author: Haxy

PROJET CANDY CRUSH
"""

#import matplotlib.pyplot as plt
import numpy as np
from random import randint 
import utils.list_util as utl

def init_jeu(taille):
    """
    Parameters
    ----------
    taille : (int) taille de la matrice 

    Returns
    -------
    jeu_np :liste 2D numpy.
    """

    grille_np = utl.grille_vide(taille)
    jeu = utl.copie_l(grille_np)
    for i in range(taille):
        for j in range(taille):
            jeu[i][j] = randint(1, 4)
    jeu_np = np.array(jeu)        
    return jeu_np


def detecte_coordonnees_combinaison (griLle, i, j):
  """
  Renvoie une liste contenant les coordonnées de tous les bonbons
  appartenant à la combinaison du bonbon ( i , j ) .
  """

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
