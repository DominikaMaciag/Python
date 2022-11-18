# Zadanie 5 - Dominika Maciąg
# W tym zadaniu przyjrzymy się zewnętrznemu modułowi multipledispatch 

from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    # zdefiniuj __init__ i argumenty x, y
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    # __init__ i jeden argument x, wołanie __init__ bazowego
    def __init__(self,x):
        self.x = x

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
# zdefiniuj pole, zwróć x*y z instancji
def pole(instance: Prostokat):
    return instance.x*instance.y

@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni
def pole(instance: Prostokat,x,y):
    pole = x * y
    return pole

@dispatch(Kwadrat)
# funkcja pole
def pole(isinstance: Kwadrat):
    return isinstance.x*isinstance.x

@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku
def pole(isinstance: Figura, x):
    pole = x * x 
    return pole

# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime

polaPowierzchni([a,b,c])