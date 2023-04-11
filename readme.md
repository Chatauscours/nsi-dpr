# Projet Résolution Figure en Divisant et Régnant

### Auteurs
Projet réalisé par Mathieu Manganelli et Kirill Biryukov

### Principe de fonctionnement
Ce code permet de tracer une grille carrée de coté 2**n, composée de figures sous forme de L, ainsi que d'un carré manquant. Le but de ce code est d'automatiser le placement des figures L dans la grille pour tout carré manquant. Ceci est fait à l'aide d'une fonction récursive qui divise la grille en quatre quarts égaux à chaque récursion et simplifie ainsi pour elle même la résolution.
L'entièreté des paramètres de la figure tracée sont configurables par l'utilisateur à travers une interface console.

### Notice d'utilisation
Les librairies suivantes sont nécéssaires pour l'exécution du programme: `random`, `turtle`
Pour tester le programme, veuillez lancer le fichier `main.py`

Afin de rendre les figures obtenues personnalisables, le programme va demander à l'utilisateur des données à utiliser. Si la question est suivie par un "Y/N", veuillez répondre par un "Y" ou par un "N".