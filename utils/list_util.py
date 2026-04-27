# -*- coding: utf-8 -*-
"""
Created on friday 24 08:53:00 2026

@author: Mecdo

PROJET CANDY CRUSH
"""
import numpy as np
#import matplotlib.pyplot as plt
#from random import uniform  # génération nb aléatoire sous numpy
 # limiter le nb de chiffres significatifs print

def grille_vide(taille):
    """
    Parameters
    ----------
    taille : (int) la taille de la matrice carrée.

    Returns
    -------
    grille_vide :(liste) matrice de la grille vide
    """
    grille_vide = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        grille_vide.append(ligne)
    return grille_vide
   
def copie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c


def fall_l(liste: list):
    """
    La fonction fait tomber les bonbons de la liste vers le bas
    
    Parameters
    ----------
    liste (numpy.ndarray): Liste de jeu
    Returns
    -------
    None. 
    """
    size = len(liste)
    
    for i in range(size - 2, -1, -1): # size = 3 -> 0 , pas -1
        for j in range(size): # 0 -> size = 3
            row = i
            column = j
            while _fall_elem(liste, row, column):
                row += 1
            
def _fall_elem(liste: list, i: int, j: int) -> bool:
    """
    Parameters
    ----------
    liste (numpy.ndarray): Liste de jeu
    i (int): Coordonnné x du bonbon
    j (int): Coordonnné y du bonbon

    Returns
    -------
    Bool. -> Retourne vrai si le bonbon tombe, faux si il est bloqué.
    """
    fell = False # 1 0
    if i < len(liste) - 1:
        below = liste[i+1][j]
        if below == 0 and liste[i][j] != 0:
            liste[i + 1][j] = liste[i][j]
            liste[i][j] = 0
            fell = True
    return fell
    
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
            
            

          
          
          
          
          
          
          
          
          
          
          
          
          
          