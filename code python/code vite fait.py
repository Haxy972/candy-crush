# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:17:53 2026

@author: Mecdo

PROJET CANDY CRUSH
"""

def detecte_coordonnees_combinaison (griLle, i, j):
"""
Renvoie une l i s t e con tenan t l e s coordonn é e s de to u s l e s bonbons
appa r tenan t à l a combinai son du bonbon ( i , j ) .
"""

def copuie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c