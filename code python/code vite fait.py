# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:17:53 2026

@author: Mecdo

PROJET CANDY CRUSH
"""
import numpy as np
import matplotlib.pyplot as plt
from random import uniform  # génération nb aléatoire sous numpy
import tifffile as tiff   # importer des images .tif dans numpy
np.set_printoptions(precision=2)  # limiter le nb de chiffres significatifs print


np.array([[0, 0, 0,0,0],[0, 0, 0,0,0],[0, 0, 0,0,0],[0, 0, 0,0,0],[0, 0, 0,0,0]])




def detecte_coordonnees_combinaison (griLle, i, j):
"""
Renvoie une liste contenant les coordonnées de tous les bonbons
appartenant à la combinaison du bonbon ( i , j ) .
"""

def copie_l(liste):
    liste_c = []
    for i in range(len(liste)):
        ligne = []
        for j in range(len(liste)):
            ligne.append(liste[i][j])
        liste_c.append(ligne)
    return liste_c