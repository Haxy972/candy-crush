"""
Created on friday 24 08:53:00 2026

@author: Haxy

PROJET CANDY CRUSH
"""


from random import randint 
import utils.list_util as utl
import utils.detection as detec


###
# █▀ ▄▀▄ █▄ █ ▄▀▀ ▀█▀ █ ▄▀▄ █▄ █ ▄▀▀ 
# █▀ ▀▄▀ █ ▀█ ▀▄▄  █  █ ▀▄▀ █ ▀█ ▄█▀ 
###

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
    """
    peermet de déplacer le bonbon choisit dans une direction choisit
    
    Parameters
    ----------
    jeu : (list 2D) grille de bonbon
    point : (list) coordonnée x et y du bonbon choisit.
    direction : (chaine de caractère) 
    permet de choisir la direction dans laquel on veut déplacer le bonbon
    "z,q,s,d" les mêmes direction que pour les jeux vidéos. 
    "8,4,2,6" Les mêmes direction que pour les flèches du numpad.

    Returns
    -------
    jeu_rendu : TYPE
        DESCRIPTION.
    deplace : TYPE
        DESCRIPTION.

    """
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


def update_game(jeu):
    print()
    nouveau_jeu = utl.copie_l(jeu)
    nouveau_jeu = detec.erase_line(nouveau_jeu)
    utl.affiche_grille(nouveau_jeu)
    print()
    utl.fall_l(nouveau_jeu)
    utl.affiche_grille(nouveau_jeu)
    return nouveau_jeu

    
def fin_jeu(score):
    """
    en fonction du score nous permet de savoir si nous avons fini le jeu..
    
    Parameters
    ----------
    score : (int) valeur de nombres de lignes de 3 faits.

    Returns
    -------
    fin : (boolean) dit si on a fini.

    """
    fin = False
    if score >= 50:
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
            coord_x = int(input("Saisissez X : ")) - 1
            coord_y = len(grille) - int(input("Saisissez Y : "))

            
            if 0 <= coord_x < len(grille) and 0 <= coord_y < len(grille[0]):
                return coord_x, coord_y
            else:
                print("Coordonnées hors de la grille.")

        except ValueError:
            print("Veuillez saisir un nombre.")






#########################
#  █▀▄ █▀▄ ▄▀▄ ▄▀  
#  █▀  █▀▄ ▀▄▀ ▀▄█ 
#########################

#code du jeu niveau 2


jeu = None
while jeu == None:
    try:
        taille = int(input("taille de la grille: "))
        if taille < 3:
            print("Veuillez saisir un nombre supérieur ou égal à 3")
            continue
        
        jeu = init_jeu(taille)
    except ValueError:
        print("Veuillez saisir un nombre entier.")

utl.affiche_grille(jeu)
print()
print("Coordonnées en bas à gauche: (1, 1)")
print()
score = 0


est_fini = False
while est_fini == False:
    deplace = False
    while deplace == False:
        print()
        point_choisit = saisie_coord(jeu)
        print(point_choisit)
        print()
        print()
        jeu, deplace = deplacement(jeu, point_choisit, input("deplacement_vers: "))
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
    print()
    jeu = detec.erase_line(jeu)
    utl.affiche_grille(jeu)
    print()
    utl.fall_l(jeu)
    utl.affiche_grille(jeu)
    while detec.three_in_a_row(jeu) == True:
        score += count_point(jeu)
        jeu = update_game(jeu)
        print()
        print()
        print(f"+ {count_point(jeu)} points ")
        
    print()
    print(f"score: {score}")
    print()
    est_fini = fin_jeu(score)
    if detec.combinaison_possible(jeu) == True:
        print("Continue! Il reste des possibilitées!")
    elif detec.combinaison_possible(jeu) == False:
        est_fini = True
        print("Plus de possibilitées!")
        


print(f"Tu as gagné avec un score de  {score}")
utl.pause(1)
utl.anim_fin(jeu)
utl.pause(1) # 2 secondes avant la fermeture du jeu un fois fini.










