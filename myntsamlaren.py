import pgzrun
from random import randint

BREDD = 400
HOJD = 400
summa = 0
spelet_slut = False

rav = Actor("fox")
rav.pos = 100, 100

mynt = Actor("coin")
mynt.pos = 200, 200

def draw():
    screen.fill("green")
    rav.draw()
    mynt.draw()
    screen.draw.text("Summa: " + str (summa), color="black", topleft=(10, 10))

    if spelet_slut:
        screen.fill("pink")
        screen.draw.text("Slutsumma: " + str(summa), topleft=(10, 10), fontsize=60)

def placera_mynt():
    mynt.x = randint(20, (BREDD - 20))
    mynt.x = randint(20, (HOJD - 20))

def tiden_slut():
    global spelet_slut
    spelet_slut = True

def update():
    global summa

    if keyboard.left:
        rav.x = rav.x - 2
    elif keyboard.right:
        rav.x = rav.x + 2
    elif keyboard.up:
        rav.y = rav.y - 2
    elif keyboard.down:
        rav.y = rav.y + 2

        insamlade_mynt = rav.colliderect(mynt)

        if insamlade_mynt:
            summa = summa + 10
            placera_mynt()

clock.schedule(tiden_slut, 7.0)
placera_mynt()

pgzrun.go()