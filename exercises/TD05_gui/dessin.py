from tkinter import *
import random as rd
import random
CANVAS_WIDTH, CANVAS_HEIGHT = 600 , 600

fenetre = Tk()

color = ["red", "green", "cyan", "yellow", "white"]
colors=random.choice(color)

canvas = Canvas(fenetre, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black")
canvas.grid(row=1, column=1, rowspan=3)


def change_color():
    global colors
    colors=random.choice(color)



    
bouton=Button(fenetre, text="choisir une couleur", command=change_color)
bouton.grid(row=0, column=1)

def cercle():
    x1=rd.randint(0, 500)
    y1=rd.randint(0, 500)
    x2=x1+100
    y2=y1+100
    canvas.create_oval(x1, y1, x2, y2, fill=colors)
bouton2=Button(fenetre, text="cercle", command=cercle)
bouton2.grid(row=1, column=0)

def carré():
    x3=rd.randint(0, 500)
    y3=rd.randint(0, 500)
    x4=x3+100
    y4=y3+100
    canvas.create_rectangle(x3, y3, x4, y4, fill=colors)
bouton3=Button(fenetre, text="carré", command=carré)
bouton3.grid(row=2, column=0)

def croix():
    x5=rd.randint(0, 500)
    y5=rd.randint(0, 500)
    x6=x5+100
    y6=y5+100
    canvas.create_rectangle(x5+100/3, y5, x5+2*(100/3), y6, fill=colors)
    canvas.create_rectangle(x5, y5+100/3,x6,  y5+(100*2/3), fill=colors)
bouton4=Button(fenetre, text="croix", command=croix)
bouton4.grid(row=3, column=0)



# Début de votre code

    
# Fin de votre code


fenetre.mainloop()

