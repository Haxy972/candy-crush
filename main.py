"""
Created on friday 24 08:53:00 2026

@author: Haxy

PROJET CANDY CRUSH
"""

#import matplotlib.pyplot as plt
from random import randint 
import utils.list_util as utl
import utils.detection as detec




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
            
    while detec.three_in_a_row(jeu) == True:
        for i in range(len(jeu)):
            for j in range(1, len(jeu)-1):
                if detec.three_in_a_line(jeu, i, j) == True:
                    jeu[i][j] = randint(1, 4)
        for i in range(1, len(jeu)-1):
            for j in range(len(jeu)):
                if detec.three_in_a_column(jeu, i, j) == True:
                    jeu[i][j] = randint(1, 4)        
    return jeu




def count_point(jeu):
    """
    compte le nomnbre de point à un instant donnée
    Parameters
    ----------
    jeu : (liste) la grille candy crush

    Returns
    -------
    count : (int) le nombre de alignement de trois dans la grille

    """
    count = 0
    for i in range(len(jeu)):
        for j in range(1, len(jeu)-1):
            if detec.three_in_a_line(jeu, i, j) == True:
                count += 1
    for i in range(1, len(jeu)-1):
        for j in range(len(jeu)):
            if detec.three_in_a_column(jeu, i, j) == True:
                count += 1       
    return count


def deplacement(jeu, point, direction):
    deplace = False
    nouveau_jeu = utl.copie_l(jeu)
    if direction == "z" or direction == "8":
        nouveau_jeu[point[1]][point[0]] = jeu[point[1]-1][point[0]]
        nouveau_jeu[point[1]-1][point[0]] = jeu[point[1]][point[0]]
    elif direction == "s" or direction == "2" :
        nouveau_jeu[point[1]][point[0]] = jeu[point[1]+1][point[0]]
        nouveau_jeu[point[1]+1][point[0]] = jeu[point[1]][point[0]]
    elif direction == "q" or direction == "4":
        nouveau_jeu[point[1]][point[0]] = jeu[point[1]][point[0]-1]
        nouveau_jeu[point[1]][point[0]-1] = jeu[point[1]][point[0]]
    elif direction == "d" or direction == "6":
        nouveau_jeu[point[1]][point[0]] = jeu[point[1]][point[0]+1]
        nouveau_jeu[point[1]][point[0]+1] = jeu[point[1]][point[0]]
    if detec.three_in_a_row(nouveau_jeu) == True:
        deplace = True
        jeu_rendu = nouveau_jeu
    else:
        jeu_rendu = jeu
    return jeu_rendu, deplace


def fin_jeu(score):
    fin = False
    if score >= 100:
        fin = True
    return fin

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










#code du jeu niveau 2

jeu = init_jeu(int(input("taille de la grille: ")))
utl.affiche_grille(jeu)
print()
print("coordonée en bas à gauche: (1, 1)")
print()
score = 0

while fin_jeu(score) == False:
    deplace = False
    while deplace == False:
        print()
        point_choisit = (int(input("Saisissez X : "))-1, len(jeu) - int( input("Saisissez Y : "))  )
        print(point_choisit)
        print()
        print()
        jeu, deplace = deplacement(jeu, point_choisit, input("deplacemnt_vers: "))
        if deplace == True:
            print("bien joué!")
        else:
            print("try again")
    utl.affiche_grille(jeu)
    print()
    print()
    score += count_point(jeu)
    print(f"+ {count_point(jeu)} points ")
    print(f"score: {score}")
    utl.affiche_grille(jeu)
    print()
    jeu = detec.erase_line(jeu)
    utl.fall_l(jeu)
    utl.affiche_grille(jeu)















