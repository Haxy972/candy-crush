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
    grille_vide_np = np.zeros([taille, taille])
    
    return grille_vide_np
    
   
    
def copie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c



def affiche_grille(jeu):
    """
    

    Parameters
    ----------
    jeu : liste numpy du jeu.

    Returns
    -------
    None.

    """
  for i in range(len(jeu)):
      print()
      for j in range(len(jeu[i])):
          print(jeu[i][j],end=" ")