import random
import turtle as t

def hämta_linjelängd():
    val = input('Ange linjelängd (lång, mellan, kort): ')
    if val == 'lång':
        linjelängd = 250
    elif val == 'mellan':
        linjelängd = 200
    else:
        linjelängd = 100
    return linjelängd

def hämta_linjebredd():
    val = input('Ange linjebredd (supertjock, tjock, tunn): ')
    if val == 'supertjock':
        linjebredd = 40
    elif val == 'tjock':
        linjebredd = 25
    else:
        linjebredd = 10
    return linjebredd

def inuti_fönster():
    vänster_gräns = (-t.window_width() / 2)+ 100
    höger_gräns = (t.window_width() / 2) + 100

linjelängd = hämta_linjelängd()
linjebredd = hämta_linjebredd()


t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(linjebredd)
