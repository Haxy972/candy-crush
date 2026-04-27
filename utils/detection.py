import utils.list_util as utl

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
 
