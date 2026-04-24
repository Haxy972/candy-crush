# -*- coding: utf-8 -*-
"""
Created on friday 24 08:53:00 2026

@author: Mecdo

PROJET CANDY CRUSH
"""
import numpy as np
#import matplotlib.pyplot as plt
#from random import uniform  # génération nb aléatoire sous numpy
np.set_printoptions(precision=2)  # limiter le nb de chiffres significatifs print

def grille_vide(taille):
    """
    Parameters
    ----------
    taille : (int) la taille de la matrice carrée.

    Returns
    -------
    grille_np : matrice numpy de la grille vide
    """
    
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        grille.append(ligne)
    grille_vide_np = np.array(grille)
    
    return grille_vide_np
    
   
    
def copie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c