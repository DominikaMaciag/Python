from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    # zdefiniuj __init__ i argumenty x, y
    pass

class Kwadrat(Prostokat):
    # __init__ i jeden argument x, wołanie __init__ bazowego
    pass

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
# zdefiniuj pole, zwróć x*y z instancji

@dispatch(Prostokat, int, int)
# funkcja pole, najpierw przypisz argumenty do x, y instancji, potem policz pole powierzchni

@dispatch(Kwadrat)
# funkcja pole

@dispatch(Kwadrat, int)
# funkcja pole z podanym argumentem boku

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