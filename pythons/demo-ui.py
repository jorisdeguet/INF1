import random
from math import *

import PySimpleGUI as sg


largeur = 600
hauteur = 400


class Personne:
    def __init__(self, x, y, vitesse, direction):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.direction = direction
    def move(self):
        self.x += self.vitesse * cos(self.direction)
        self.x = self.x % largeur
        self.y += self.vitesse * sin(self.direction)
        self.y = self.y % hauteur


gens = []
for i in range(1,400):
    personne = Personne(
        random.randint(0, largeur),
        random.randint(0, hauteur),
        random.randint(1, 5),
        random.randint(0, 360)
    )
    gens.append(personne)


layout = [  [sg.Canvas(size=(largeur, hauteur), background_color='grey99', key= 'canvas'),
                sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(50,35))],
            [sg.Text('Demonstration of Multiline Element Printing')],
            [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,8))],
            [],
            [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, finalize=True)

canvas = window['canvas']
#cir = canvas.TKCanvas.create_oval(50, 50, 100, 100)


# Note, need to finalize the window above if want to do these prior to calling window.read()
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1, 2, 3, 4, end='', text_color='red', background_color='yellow')
window['-ML1-'+sg.WRITE_ONLY_KEY].print('\n', end='')
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1,2,3,4,text_color='white', background_color='green')
counter = 0

while True:             # Event Loop
    event, values = window.read(timeout=50)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Go':
        window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
    #window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
    canvas.TKCanvas.delete("all")
    for p in gens:
        p.move()
    for p in gens:
        canvas.TKCanvas.create_oval(p.x, p.y, p.x + 3, p.y + 3)
    #canvas.TKCanvas.create_oval(counter % largeur, counter/2 + 200 % hauteur, counter % largeur + 1 , hauteur/2 )
    counter += 1
window.close()