"""
Created on friday 24 08:53:00 2026

@author: Anthony

PROJET CANDY CRUSH
"""

import utils.list_util as utl

def combinaison_possible(jeu: list) -> bool:
    """
    Verifie si il y a une combinaison possible dans le jeu
    Parameters
    ----------
    jeu : (liste) le jeu de candy crush
    Returns
    -------
    comb : (bool) vrai s'il y a une combinaison possible, faux sinon
    """
    comb = False
    count = 0
    for i in range(1, len(jeu)):
        for j in range(1, len(jeu)-1):
            if three_in_a_line_possible1(jeu, i, j) == True:
                count += 1
            elif three_in_a_line_possible3(jeu, i, j) == True:
                count += 1
            elif three_in_a_line_possible5(jeu, i, j) == True:
                count += 1
    for i in range( len(jeu)-1):
        for j in range(1, len(jeu)-1):
            if three_in_a_line_possible2(jeu, i, j) == True:
                count += 1
            elif three_in_a_line_possible4(jeu, i, j) == True:
                count += 1
            elif three_in_a_line_possible6(jeu, i, j) == True:
                count += 1
                           
    for i in range(1, len(jeu)-1):
        for j in range(len(jeu)-1):
            if three_in_a_column_possible1(jeu, i, j) == True:
                count += 1 
            elif three_in_a_column_possible3(jeu, i, j) == True:
                count += 1
            elif three_in_a_column_possible5(jeu, i, j) == True:
                count += 1
    for i in range(1, len(jeu)-1):
        for j in range(1, len(jeu)):
            if three_in_a_column_possible2(jeu, i, j) == True:
                count += 1 
            elif three_in_a_column_possible4(jeu, i, j) == True:
                count += 1
            elif three_in_a_column_possible6(jeu, i, j) == True:
                count += 1
                
    if count > 0 :
        comb = True
    return comb 




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


def erase_line(jeu):
    """
    Efface les lignes ou colonnes de trois ou plus dans le jeu et les remplace par des 0
    Parameters
    ----------
    jeu : (liste) le jeu de candy crush

    Returns
    -------
    nouveau_jeu : (liste) le jeu mis à jour
    """
    
    nouveau_jeu = utl.copie_l(jeu)
    for i in range(len(jeu)):
        for j in range(1, len(jeu)-1):
            if three_in_a_line(jeu, i, j) == True:
                nouveau_jeu[i][j] = nouveau_jeu[i][j-1] = nouveau_jeu[i][j+1] = 0
    for i in range(1, len(jeu)-1):
        for j in range(len(jeu)):
            if three_in_a_column(jeu, i, j) == True:
                nouveau_jeu[i][j] = nouveau_jeu[i-1][j] = nouveau_jeu[i+1][j] = 0     
   
    return nouveau_jeu



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
 
##-------------------------------------------------------##
## DETECTION DES COMBINAISONS POSSIBLES 12 CAS POSSIBLES ##
##-------------------------------------------------------##

# les possibilitées en lignes
def three_in_a_line_possible1(jeu, y, x):
    line = False
    if jeu[y][x-1] == jeu[y][x+1] == jeu[y-1][x]:
        line = True
    return line    
 
def three_in_a_line_possible2(jeu, y, x):
    line = False
    if jeu[y][x-1] == jeu[y][x+1] == jeu[y+1][x]:
        line = True
    return line


def three_in_a_line_possible3(jeu, y, x):
    line = False
    if jeu[y][x-1] == jeu[y][x] == jeu[y-1][x+1]:
        line = True
    return line    

def three_in_a_line_possible4(jeu, y, x):
    line = False
    if jeu[y][x-1] == jeu[y][x] == jeu[y+1][x+1]:
        line = True
    return line

def three_in_a_line_possible5(jeu, y, x):
    line = False
    if jeu[y-1][x-1] == jeu[y][x] == jeu[y][x+1]:
        line = True
    return line

def three_in_a_line_possible6(jeu, y, x):
    line = False
    if jeu[y+1][x-1] == jeu[y][x] == jeu[y][x+1]:
        line = True
    return line

# les possibilitées en colonnes
def three_in_a_column_possible1(jeu, y, x):
    col = False
    if jeu[y-1][x] == jeu[y+1][x] == jeu[y][x+1]:
        col = True
    return col

def three_in_a_column_possible2(jeu, y, x):
    col = False
    if jeu[y-1][x] == jeu[y+1][x] == jeu[y][x-1]:
        col = True
    return col

def three_in_a_column_possible3(jeu, y, x):
    col = False
    if jeu[y][x] == jeu[y+1][x] == jeu[y-1][x+1]:
        col = True
    return col

def three_in_a_column_possible4(jeu, y, x):
    col = False
    if jeu[y][x] == jeu[y+1][x] == jeu[y-1][x-1]:
        col = True
    return col

def three_in_a_column_possible5(jeu, y, x):
    col = False
    if jeu[y][x] == jeu[y-1][x] == jeu[y+1][x+1]:
        col = True
    return col

def three_in_a_column_possible6(jeu, y, x):
    col = False
    if jeu[y][x] == jeu[y-1][x] == jeu[y+1][x-1]:
        col = True
    return col