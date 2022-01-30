# Application d'étude musicale - TDLOG


[![forthebadge](https://img.shields.io/badge/Python-3.8-blue)](https://www.python.org/downloads/)  [![forthebadge](https://img.shields.io/badge/Numpy-1.18.5-brightgreen)](https://numpy.org) [![forthebadge](https://img.shields.io/badge/Librosa-0.8.1-brightgreen)](https://librosa.org/doc/main/index.html) [![forthebadge](https://img.shields.io/badge/TensorFlow-2.7.0-brightgreen)](https://www.tensorflow.org/?hl=fr)

L'objectif de notre application est de pouvoir faire un mélange entre de la reconnaissance musicale (Shazam) mais aussi de l'analyse musicale, de l'extraction de sample mais aussi de la detection de genre. 

## Pour commencer

Il est nécessaire d'avoir accès à une connexion internet si on souhaite faire une reconnaissance de la musique.

### Pré-requis

Il est nécéssaire d'avoir 

- Python 64 bit  
- [FFMPEG](https://www.ffmpeg.org)
- Librairies principales Python : Dash, Plotly, Numpy, Pandas, Librosa, Scipy, ShazamAPI, TensorFlow


### Installation

Il suffit juste de télécharger le code, puis run le fichier python "app.py"


## Démarrage

* Une fois le fichier éxécuté, l'application se trouve en local sur l'adresse suivante : http://127.0.0.1:8050
* L'utilisateur peut _drag and drop_ un fichier audio (mp3, wav) de son choix
* Appel automatique à ShazamAPI
* On peut calculer la _wave_ puis extraire une partie juste en selectionnant la partie intéressante sur le graphe
* Une fois la _wave_ calculée il est possible de faire appel au programme de Machine Learning qui détecte le genre 


## Fabriqué avec
Programmes utilisés, bibliographie

* [Dash](https://dash.plotly.com/introduction) - Framework Dash (front-end)
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - Editeur de textes




## Auteurs
* SAYAH Ramzi 
* PINSOLLE Henri
* PASCAL Thimothée
* PARENT Nil


