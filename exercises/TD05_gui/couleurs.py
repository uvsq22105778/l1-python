import tkinter as tk
import random
CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256
fenetre = tk.Tk()

canvas = tk.Canvas(fenetre, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black")
canvas.grid()

colors=['white', 'red', 'blue', 'green', 'black', 'yellow']



def draw_pixel(i, j, color):
    canvas.create_rectangle(i, j, i, j, outline=color,fill=color)

def draw_random():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            color = random.choice(colors)
            draw_pixel(i,j,color)


bouton=tk.Button(fenetre, text="Aléatoire", command=draw_random)
bouton.grid(row=1, column=0, rowspan=2)

'''draw_pixel(128,128,"white")'''

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def degrade_gris():
     for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            cdict2 = {'red':   [(0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)],
                   'green': [(0.0,  0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.75, 1.0, 1.0),
                   (1.0,  1.0, 1.0)],
                   'blue':  [(0.0,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (1.0,  1.0, 1.0)]} 
            canvas.config(bg=get_color(r, g, b))


'''def degrade_gris():
     for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            r = int(input("Teinte de rouge? "))
            v = int(input("Teinte de vert? "))
            b = int(input("Teinte de bleu? "))
            if 0 <= r <= 255 and 0 <= v <= 255 and 0 <= b <= 255:
                break
canvas.config(bg=get_color(r, v, b))'''

bouton2=tk.Button(fenetre, text='Dégradé gris', command=degrade_gris)
bouton2.grid(row=2, column=0, rowspan=2)


bouton3=tk.Button(fenetre, text='Dégradé 2D', command=quit)
bouton3.grid(row=3, column=0, rowspan=2)


canvas.grid(row=2, column=4, rowspan=2)
fenetre.mainloop()