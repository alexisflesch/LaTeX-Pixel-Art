# LaTeX-Pixel-Art

Pixel art in LaTeX


## First steps

There has to be a numerous different ways to do pixel art using LATEX. To keep things fast, I've chosen to use simple basics macros. A pixel is represented using a rule. One can then create a pixel command that takes a color and a length as arguments:

```latex
\newcommand{\pixel}[2]{\textcolor{#1}{\rule{#2}{#2}}}
```  

It's now just a matter of using the picture environment ! You can learn how to use it here if you want to. An example of what you can achieve:

![mario](/files/mario.png)

And the corresponding code:

```latex
% Macro pixel et dimension
\newcommand{\dimension}{10pt}
\newcommand{\pixel}[2]{\textcolor{#1}{\rule{#2}{#2}}}

% Couleurs
\definecolor{rouge}{RGB}{255,0,0}
\definecolor{rose}{RGB}{255,200,168}
\definecolor{bleu}{RGB}{0,0,255}
\definecolor{jaune}{RGB}{255,255,0}
\definecolor{noir}{RGB}{0,0,0}

% Pixels de couleur
\newcommand{\rp}{\pixel{rouge}{\dimension}}
\newcommand{\pp}{\pixel{rose}{\dimension}}
\newcommand{\bp}{\pixel{bleu}{\dimension}}
\newcommand{\yp}{\pixel{jaune}{\dimension}}
\newcommand{\hp}{\pixel{noir}{\dimension}}
\newcommand{\ep}{\pixel{noir}{\dimension}}
\newcommand{\cp}{\pixel{rouge}{\dimension}}
\newcommand{\ssp}{\pixel{noir}{\dimension}}
\newcommand{\wwp}{\pixel{white}{\dimension}}

% Mario
\newcommand{\mario}{%
 \setlength{\unitlength}{\dimension}%
 \begin{picture}(0,0)%
 \multiput(0,0)(1,0){4}{\ssp}%
 \multiput(8,0)(1,0){4}{\ssp}%
 %
 \multiput(1,1)(1,0){3}{\ssp}%
 \multiput(8,1)(1,0){3}{\ssp}%
 %
 \multiput(2,2)(1,0){3}{\rp}%
 \multiput(7,2)(1,0){3}{\rp}%
 %
 \multiput(0,3)(1,0){2}{\pp}%
 \multiput(2,3)(1,0){3}{\rp}%
 \multiput(7,3)(1,0){3}{\rp}%
 \multiput(10,3)(1,0){2}{\pp}%
 %
 \multiput(0,4)(1,0){3}{\pp}%
 \multiput(3,4)(1,0){6}{\rp}%
 \multiput(9,4)(1,0){3}{\pp}%
 %
 \multiput(0,5)(1,0){2}{\pp}%
 \put(2,5){\bp}%
 \put(3,5){\rp}%
 \put(4,5){\yp}%
 \multiput(5,5)(1,0){2}{\rp}%
 \put(7,5){\yp}%
 \put(8,5){\rp}%
 \put(9,5){\bp}%
 \multiput(10,5)(1,0){2}{\pp}%
 %
 \multiput(0,6)(1,0){4}{\bp}%
 \multiput(4,6)(1,0){4}{\rp}%
 \multiput(8,6)(1,0){4}{\bp}%
 %
 \multiput(1,7)(1,0){3}{\bp}%
 \put(4,7){\rp}%
 \multiput(5,7)(1,0){2}{\bp}%
 \put(7,7){\rp}%
 \multiput(8,7)(1,0){3}{\bp}%
 %
 \multiput(2,8)(1,0){2}{\bp}%
 \put(4,8){\rp}%
 \multiput(5,8)(1,0){3}{\bp}%
 %
 \multiput(3,9)(1,0){7}{\pp}%
 %
 \multiput(1,10)(1,0){2}{\hp}%
 \multiput(3,10)(1,0){4}{\pp}%
 \multiput(7,10)(1,0){4}{\hp}%
 %
 \put(1,11){\hp}%
 \put(2,11){\pp}%
 \multiput(3,11)(1,0){2}{\hp}%
 \multiput(5,11)(1,0){3}{\pp}%
 \put(8,11){\hp}%
 \multiput(9,11)(1,0){3}{\pp}%
 %
 \put(1,12){\hp}%
 \put(2,12){\pp}%
 \put(3,12){\hp}%
 \multiput(4,12)(1,0){3}{\pp}%
 \put(7,12){\ep}%
 \multiput(8,12)(1,0){3}{\pp}%
 %
 \multiput(2,13)(1,0){3}{\hp}%
 \multiput(5,13)(1,0){2}{\pp}%
 \put(7,13){\ep}%
 \put(8,13){\pp}%
 %
 \multiput(2,14)(1,0){9}{\cp}%
 %
 \multiput(3,15)(1,0){5}{\cp}%
\end{picture}%
}
```


## A python script

### Why ?
Using the picture environment to copy an image "by hand" and program the corresponding macro takes a lot of time. You have to define the colors, and create the pixels one at a time (even though the multiput might come in handy).

In this repository, you will find a python script (**pixel.py**) that will save you a lot of time ! It takes a png file as an argument and creates a text file in which you will find everything you need to use this image in your document. One of the advantages of the png format is that it handles transparency: transparent pixels won't be copied in the tex macro.

### Example
Imagine you want to use this image (mushroom.png) in your document:
![mushroom](/files/mushroom.png)


You then just need to copy the script **pixel.py** in the same folder as the one where mushroom.png is located. You then open a terminal, hop to the right directory and:

```bash 
$ python   pixel.py   mushroom.png
```

The script will then create a file **mushroom.txt** in the same folder with everything you need (comments are in French but everything should be self-explanatory).

### Limitations

LaTeX doesn't allow one to use numbers in macro names. It would be too easy to use names like `\color1`, `\color2`, etc... The workaround is to use letters instead of numbers. This means that you are limited to 143364 colors with this script (this limit can be changed but shouldn't be a problem for pixel art).

### The script
It uses the "PIL" library (for Python Imaging Library). It just reads the image, one pixel at a time and writes the corresponding commands as it goes through the image. It ignores transparent pixels and define new colors each time it encounters one.


## Mario in your footer

Now that we know how to do pixel art in LaTeX, what can we do ? In this repository, you will a find a style file (**mario.sty**). It will print a little mario that runs through your footer from left to right, using pipes to go from the even pages to the odd ones. It should be used with two-sided documents. Some parameters should be tweaked depending on the number of pages in your document. Click on the image below to have an idea of what you can expect from it:

![footer](/files/mario_foot.png)

If you want to see it in action in a pdf (watch in in "facing pages" mode), then look at mario.pdf under the directory files.
