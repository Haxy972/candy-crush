# Candy Crush — Mini-projet Python

Jeu type "Candy Crush" développé en Python pour l'exploration d'algorithmes de grille et d'animations simples.

## Description

Ce projet propose une implémentation d'un jeu "Candy Crush" :
- génération aléatoire d'une grille de bonbons
- détection et suppression d'alignements de 3
- chute des bonbons et génération de nouveaux éléments
- affichage console et graphique via matplotlib

Le jeu est conçu pour être simple et dans une but scolaire, il a permis d'apprendre la manipulation de listes 2D, la détection de motifs et l'usage basique de matplotlib.

## Prérequis

- Python 3.8+ (testé sous Windows)
- package `matplotlib`

Installer la dépendance :

```bash
pip install matplotlib
```

## Lancer le jeu

Depuis la racine du dépôt :

```bash
python main.py
```

Le programme demande la taille de la grille puis propose des invites pour choisir une case et une direction (`z/q/s/d` ou `8/4/2/6` au numpad).

## Structure du projet

- `main.py` : logique principale du jeu et boucle de jeu.
- `utils/list_util.py` : fonctions utilitaires pour la grille, affichage graphique et animations.
- `utils/detection.py` : fonctions de détection d'alignements et combinaisons possibles.

## Contribution

Issues et pull requests bienvenues

## Auteurs

Léo, Anthony et Diego

---
Pour toute question ou amélioration souhaitée, dites-moi ce que vous voulez ajouter (modes, scores persistants, tests automatisés, etc.).
Conformément à la licence MIT, la notice de copyright et la licence doivent être conservées dans les redistributions du logiciel.
