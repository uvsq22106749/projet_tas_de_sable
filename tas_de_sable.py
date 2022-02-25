# groupe MIASHS 1
# Akram AMRAOUI
# Vlad CIRNEANU
# Paul ROUILLIER
# Hajar ZAAZOUA 
# https://github.com/uvsq22106749/projet_tas_de_sable

#CONFIGURATION#

L = [[0] * 4 for i in range(4)]
for i in range(4) :
    for j in range(4) :
        if i == j :
            L[i][j] = 0
        elif i < j :
            L[i][j] = 0
            
for i in L:
    print(' '.join([str(j) for j in i]))

#INTERFACE GRAPHIQUE#

import tkinter as tk

HEIGHT = 400
WIDTH = 500

racine = tk.Tk() # Création de la fenêtre racine

bouton1 = tk.Button(text="afficher config", font = ("Helvitica", "30"))
bouton1.grid(column = 0, row = 1)

canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH,)
canvas.grid(column = 0, row = 0)

racine.mainloop() # Lancement de la boucle principale

#FONCTION#
