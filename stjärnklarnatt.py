import turtle as t
from random import randint, random

def rita_stjärna(uddar, storlek, färg, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    vinkel = 180 - (180 / uddar)
    t.color(färg)
    t.begin_fill()
    for i in range(uddar):
        t.forward(storlek)
        t.right(vinkel)
    t.end_fill()

# huvudkod
t.speed(0)
t.hideturtle()
t.Screen().bgcolor('dark blue')

while True:
    ranUddar = randint(2, 5) * 2 + 1
    ranStorlek = randint(10, 50)
    ranFärg = (random(),  random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)

    rita_stjärna(ranUddar, ranStorlek, ranFärg, ranX, ranY)
