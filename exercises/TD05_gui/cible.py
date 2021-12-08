import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600 , 600
fenetre = tk.Tk()
color = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']

canvas = tk.Canvas(fenetre, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black")
canvas.grid()
N=int(input('coisir un nombre de cercle'))
xM=CANVAS_WIDTH/2
yM=CANVAS_HEIGHT/2
for i in range(N):
    Pi=(xM*i/N, yM*i/N)
    Qi= (CANVAS_WIDTH - xM*i/N, CANVAS_HEIGHT - yM*i/N)
    canvas.create_oval(Pi,Qi,fill=color[i%len(color)])





fenetre.mainloop()