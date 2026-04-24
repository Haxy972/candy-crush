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


