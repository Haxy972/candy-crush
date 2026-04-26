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






def three_in_a_row(jeu):
    """
    verifie si il y a trois ensemble dans le jeu

    Parameters
    ----------
    jeu : (liste)  le jeu de candy crush

    Returns
    -------
    row :(bool) 
    """
    row = False
    count = 0
    for i in range(len(jeu)):
        for j in range(1, len(jeu)-1):
            if three_in_a_line(jeu, i, j) == True:
                count += 1
    for i in range(1, len(jeu)-1):
        for j in range(len(jeu)):
            if three_in_a_column(jeu, i, j) == True:
                count += 1       
    if count > 0 :
        row = True
    return row







def three_in_a_line(jeu, y, x):
    """
    détècte si les points autour sont égaux au point choisit

    Parameters
    ----------
    jeu : (liste) le jeu de candy crush
    y : (int) la ligne sur laquelle on est. Correspond a la variable i.
    x : (int) la collone sur laquelle on est. Correspond a la variable j.

    Returns
    -------
    line : (bool) savoir si il y a une ligne de trois autour du point.
    """
    line = False
    if jeu[y][x] == jeu[y][x-1] == jeu[y][x+1]:
        line = True
    return line
 
    
 
    
 
    
def three_in_a_column(jeu, y, x):
    """
    détècte si les points autour sont égaux au point choisit

    Parameters
    ----------
    jeu : (liste) le jeu de candy crush
    y : (int) la ligne sur laquelle on est. Correspond a la variable i.
    x : (int) la collone sur laquelle on est. Correspond a la variable j.

    Returns
    -------
    col : (bool) savoir si il y a une colone de trois autour du point.

    """
    col = False
    if jeu[y][x] == jeu[y-1][x] == jeu[y+1][x]:
        col = True
    return col
 




   
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
            
            

          
          
          
          
          
          
          
          
          
          
          
          
          
          