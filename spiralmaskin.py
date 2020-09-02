#--------------------------------#
# uppgift från sida 84           #
# "spiralmaskin"                 #
#                                #
#--------------------------------#


import turtle
from itertools import cycle

färger = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def rita_cirkel(storlek, vinkel, vändning):
    turtle.pencolor(next(färger))
    turtle.circle(storlek)
    turtle.right(vinkel)
    turtle.forward(vändning)
    rita_cirkel(storlek + 5, vinkel + 1, vändning + 2)

turtle.hideturtle()
turtle.bgcolor('black')
turtle.speed('fastest')
turtle.pensize(10)

turtle.pencolor('red')
turtle.circle(1)
rita_cirkel(30, 0, 1)
