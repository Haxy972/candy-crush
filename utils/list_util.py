# -*- coding: utf-8 -*-
"""
Created on friday 24 08:53:00 2026

@author: Mecdo

PROJET CANDY CRUSH
"""

# couleurs personnalisées
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Circle
from random import randint  # génération nb aléatoire sous numpy

# Variables globales
fig = None
ax = None
circles = []

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
    """
    Permet de copier la liste à l'identique.
    Est utile pour éviter la muabilité des listes
    
    Parameters
    ----------
    liste : (list) La liste que l'on veut copier

    Returns
    -------
    liste_c :(list) Liste copiée
    """
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c

def anim_fin(liste: list) -> None:
    reverse = False
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if reverse:
                liste[i][len(liste[i]) -1 -j] = 0
            else:
                liste[i][j] = 0
            pause(0.1)
            affiche_grille_graphique(liste)
            reverse = not reverse

    change_all_colors(liste, 1)
    change_all_colors(liste, 0)
    change_all_colors(liste, 1)
    change_all_colors(liste, 0)
    
    
    
def change_all_colors(liste, color):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j] = color
    affiche_grille_graphique(liste)
    pause(0.2)
    


def pause(time: float) -> None:
    """
    Permet de mettre sur pause le graphique pendant quelques secondes
    
    Parameters
    ----------
    liste (numpy.ndarray): Liste de jeu
    Returns
    -------
    None. 
    """
    plt.pause(time)
    

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
    pause(0.2) # pause pour visualiser les changements
    while zero_line(liste) == True:
        for i in range(size - 2, -1, -1): # size = 3 -> 0 , pas -1
            for j in range(size): # 0 -> size = 3
                row = i
                column = j
                _new_candy(liste) # génère les bonbons en haut de la grille
                while _fall_elem(liste, row, column):
                    row += 1
                    _new_candy(liste) # génère quand ça tombe
                    affiche_grille_graphique(liste)
                    pause(0.1) # pause pour visualiser le mouvement
                
            
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
    
def _new_candy(jeu: list):
    """
    Création d'un nouveau bonbon en haut de la grille partout où il n'y a pas de bonbon
    Parameters
    ----------
    jeu (numpy.ndarray): Liste de jeu
    """
    
    for j in range(len(jeu)):
        if is_zero(jeu, 0, j) == True:
            jeu[0][j] = randint(1, 4)             

def affiche_grille_graphique(jeu: list) -> None:
    """
    Affiche la grille de jeu graphiquement à l'aide de matplotlib.
    Parameters
    # Doc: https://matplotlib.org/stable/index.html
    ----------
    jeu : liste numpy du jeu.
    Returns -> None
    -------
    """
    global fig, ax, circles
    dict_colors = {0: 'black', 1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'}
    n = len(jeu)
    
    if fig is None:
        plt.ion() # Empêche le blocage du programme lors de l'affichage
        fig, ax = plt.subplots()

        circles = []

        # Pour chaque combinaison de jeu (i, j), on crée un cercle de la couleur
        for i in range(n):
            line = []
            for j in range(n):
                circle = Circle(
                    (j + 1, n - i), # inversé pour que le 0,0 soit en bas à gauche
                    0.4, # rayon
                    color=dict_colors[jeu[i][j]]
                )
                ax.add_patch(circle)
                line.append(circle)

            circles.append(line)

        # Axes
        ax.set_xlim(0.5, n + 0.5)
        ax.set_ylim(0.5, n + 0.5)
        ax.set_xticks(range(1, n + 1)) # Grad X
        ax.set_yticks(range(1, n + 1)) # Grad Y

        ax.grid(True)

        ax.set_aspect('equal') # Orthonormé

        plt.show()

    # MAJ: couleurs des cercles
    else:
        for i in range(n):
            for j in range(n):
                circles[i][j].set_color(
                    dict_colors[jeu[i][j]]
                )

    # MAJ: affichage
    fig.canvas.draw()
    fig.canvas.flush_events()

    
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
    affiche_grille_graphique(jeu)
            
def is_zero(jeu, i, j):
    """
    

    Parameters
    ----------
    jeu : TYPE
        DESCRIPTION.
    i : TYPE
        DESCRIPTION.
    j : TYPE
        DESCRIPTION.

    Returns
    -------
    zero : TYPE
        DESCRIPTION.

    """
    zero = False
    if jeu[i][j] == 0:
        zero = True
    return zero      
          
def zero_line(jeu):
    """
    

    Parameters
    ----------
    jeu : (liste 2D) grille de bonbon 

    Returns
    -------
    zero_on_line : (b) 

    """
    zero_on_line = False
    count = 0
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if is_zero(jeu, i, j) == True:
                count += 1      
    if count > 0 :
        zero_on_line = True
    return zero_on_line
          
          
def replace_zero(jeu):
    """
    

    Parameters
    ----------
    jeu : (liste 2D) grille de bonbon

    Returns
    -------
    new_game : (liste 2D) grille de bonbon aprés mise a jour

    """
    new_game = copie_l(jeu)        
    while zero_line(jeu) == True:
            for j in range(len(jeu)):
                if is_zero(jeu, 0, j) == True:
                    new_game[0][j] = randint(1, 4)                       
    return new_game
          
          
          
          
          
          
          