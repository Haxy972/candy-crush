# -*- coding: utf-8 -*-


def copie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c