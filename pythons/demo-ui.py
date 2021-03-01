import random
import itertools
from math import *

# regarder https://www.youtube.com/watch?v=KAmZe5D3v5I

import PySimpleGUI as sg


largeur = 600
hauteur = 400


class Personne:
    def __init__(self, x, y, vitesse, direction):
        self.x = x
        self.y = y
        self.size = 4
        self.vitesse = vitesse
        self.direction = direction
        self.contact = False
    def move(self):
        self.x += self.vitesse * cos(self.direction)
        self.x = self.x % largeur
        self.y += self.vitesse * sin(self.direction)
        self.y = self.y % hauteur

    def contacts(self, m):
        if m.x - self.x > self.size:
            return False
        if self.x - m.x > self.size:
            return False
        if m.y - self.y > self.size:
            return False
        if self.y - m.y > self.size:
            return False
        return True


gens = []
for i in range(0,100):
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


def detectContact(gens):
    for a in gens:
        a.contact = False
    for a, b in itertools.combinations(gens, 2):
        if a.contacts(b):
            a.contact = True
            b.contact = True


    # for i in range(0, len(gens)):
    #     for j in range(0, i):
    #         a = gens[i]
    #         b = gens[j]
    #         if a == b:
    #             continue
    #         if a.contacts(b):
    #             a.contact = True
    #             b.contact = True

    # for a, b in zip(gens, gens[1:]):
    #     if a.contacts(b):
    #         a.contact = True
    #         b.contact = True




while True:             # Event Loop
    event, values = window.read(timeout=40)
    # print('step')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Go':
        window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
    #window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
    canvas.TKCanvas.delete("all")
    for p in gens:
        p.move()
    detectContact(gens)
    for p in gens:
        color =  'black' if p.contact else 'red'
        taille = 8 if p.contact else 5
        canvas.TKCanvas.create_oval(p.x, p.y, p.x + taille, p.y + taille, fill=color)
    #canvas.TKCanvas.create_oval(counter % largeur, counter/2 + 200 % hauteur, counter % largeur + 1 , hauteur/2 )
    counter += 1
window.close()