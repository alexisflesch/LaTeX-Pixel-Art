#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from itertools import product
import string
import sys

nom_image = sys.argv[1]

a = Image.open(nom_image)
z = list(a.getdata())

#Liste contenant les couleurs (sous forme de tuples) présentes dans l'image
couleurs = []
#Chaîne de caractères contenant les macros définissant les couleurs
macrocouleurs = ""
#Chaîne de caractères contenant les macros définissant les pixels
macropixels = ""

#Chaîne de caractères contenant la macro définissant le dessin
macro =  r"\newcommand{\dessin" + nom_image[:-4] + r"}{%" + "\n"
macro += r"  \setlength{\unitlength}{\dimension}%" + "\n"
macro += r"  \begin{picture}(" + str(a.size[0]) + "," + str(a.size[1]) +r")%" + "\n"


#Liste de mots de moins de trois lettres pour "numéroter" les couleurs
alphabet = list(''.join(string.letters))
num = []
for r in range(1, 4):
    for i in product(alphabet, repeat=r):
        num.append(''.join(i))


#Coordonnees des pixels qu'on recopie
i,j = 0, a.size[1]

for p in range(len(z)):
        if z[p][3] != 0:  #pixel non transparent
            pixelij = z[p][:3]
            try:
                k = couleurs.index(pixelij)
            except:
                couleurs.append(pixelij)
                k = len(couleurs) - 1
                macrocouleurs += r"\definecolor{couleur" + num[k] + r"}{RGB}{" + str(pixelij)[1:-1] + r"}" + "\n"
                macropixels += r"\newcommand{\pixel" +num[k] + r"}{\pixel{couleur" + num[k] + r"}{\dimension}}" + "\n"
            macro += r"    \put (" + str(i) +"," + str(j) + \
                        r") {\pixel" + num[k] + r"}%" + "\n"
        i += 1
        if i == a.size[0]:
            i = 0
            j = j - 1


macro += r"  \end{picture}%" + "\n"
macro += r"}"

pre = r"%Macro pour faire un pixel et dimension" + "\n"
pre += r"\newcommand{\dimension}{1pt}" + "\n"
pre +=  r"\newcommand{\pixel}[2]{\textcolor{#1}{\rule{#2}{#2}}}" + "\n\n\n"


sortie = open(nom_image[:-4]+".txt","w")
sortie.write(pre)
sortie.write(r"%Couleurs" + "\n")
sortie.write(macrocouleurs)
sortie.write("\n\n" + r"%Pixels de couleurs" +"\n")
sortie.write(macropixels)
sortie.write("\n\n" + r"%Macro pour dessiner l'image" +"\n")
sortie.write(macro)
sortie.close()
