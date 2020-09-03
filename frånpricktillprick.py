import pgzrun
from random import randint

BREDD = 400
HOJD = 400

prickar = []
linjer = []

kommande_prick = 0

for prick in range(0, 10):
    aktor = Actor("dot")
    aktor.pos = randint(20, BREDD - 20), \
    randint(20, HOJD - 20)
    prickar.append(aktor)

def draw():
    screen.fill("black")
    siffra =  1
    for prick in prickar:
        screen.draw.text(str(siffra), \
                         (prick.pos[0], prick.pos[1] + 12))
        prick.draw()
        siffra = siffra + 1
    for linje in linjer:
        screen.draw.line(linje[0], linje[1], (100, 0, 0))

def on_mouse_down(pos):
    global kommande_prick
    global linjer
    if prickar[kommande_prick].collidepoint(pos):
        if kommande_prick:
            linjer.append((prickar[kommande_prick - 1].pos, prickar[kommande_prick].pos))
        kommande_prick = kommande_prick + 1
    else:
        linjer = []
        kommande_prick = 0

pgzrun.go()