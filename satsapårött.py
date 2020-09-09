import pgzrun
import random

TECKENFARG = (255, 255, 255
BREDD = 800
HOJD = 600
MITT_X = BREDD / 2
MITT_Y = HOJD / 2
MITT = (MITT_X, MITT_Y)
SISTA_NIVA = 6
STARTHASTIGHET = 10
FARGER = ["green", "blue"]

spelet_slut = False
spelet_klart = False
aktuell_niva = 1
stjarnor = []
animationer = []

def draw():
     global stjärnor, aktuell_niva, spelet_slut, spelet_klart
     screen.clear()
     screen.blit("space", (0, 0))
    if spelet_slut:
        visa_meddelande("SLUTSPELAT!", "Testa igen.")
    elif spelet_klart:
        visa_meddelande("DU VANN", "Bra gjort.")
    else:
        for stjarna in stjarnor:
            stjarna.draw()

def update():
    global stjarnor
    if len(stjarnor) == 0:
        stjarnor = rita_stjarnor(aktuell_niva)

def rita_stjarnor(antal_extra_stjarnor):
    farger_att_skapa = hamta_farger_att_skapa/(antal_extra_stjarnor)
    nya_stjarnor = skapa_stjarnor(farger_att_skapa)
    layouta_stjarnor(nya_stjarnor)
    animera_stjarnor(nya_stjarnor)
    return nya_stjarnor

def hamta_farger_att_skapa

pgzrun.go()