# Zadanie 1 - Dominika Maciąg 

class Baza(object):
    def __new__(cls, *args):
        print("-> Baza __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- Baza __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> Baza __init__", x)
        super().__init__()
        print("-- Baza __init__")
        self.x = x
        print("<- Baza __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-Baza-")

class A(object): 
    def __new__(cls, *args):
        print("-> A __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- A __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> A __init__",x)
        super().__init__(x)
        print("-- A __init__")
        self.x = x
        print("<- A __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-A-")

"""
    SCENARIUSZ 1
    1) W przypadku:
    class B(Baza):
        pass
    Klasa B odziedziczy wszystkie metody oraz własności po klasie Baza

    2) Jeśli dodamy własne metody __new__, __init__, __str__ oraz id() 
    to klasa B nie będzie już dziedziczyła po swoim rodzicu powyższych metod.
    Dzieje się tak z powodu MRO (Method Resolution Order) - reguł wyszukiwania metod.
    Kolejność klas w MRO w tym przypadku będzie następująca:
    class B -> class Baza

    3) Aby klasa B nadal dziedziczyła daną metodę od swojego rodzica musimy użyć funkcji super():
    super().__init__(x)

"""
class B(Baza):
    def __new__(cls, *args):
        print("-> B __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- B __new__")
        return nowy_obiekt
    
    def __init__(self, x):
        print("-> B __init__", x)
        super().__init__(x)
        print("-- B __init__")
        self.x = x
        print("<- B __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-B-")

"""
    SCENARIUSZ 2
    Klasa C odziedziczy metodę __init__ od klasy B, 
    oraz z racji tego, że klasa B dziedziczy po klasie Baza
    Klasa C również odziedziczy metodę __init__ po klasie Baza
    Kolejność klas w MRO w tym przypadku będzie następująca:
    class C -> class B -> class Baza

"""
class C(B):
    def __new__(cls, *args):
        print("-> C __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- C __new__")
        return nowy_obiekt
    
    def __init__(self, x):
        print("-> C __init__", x)
        super().__init__(x)
        print("-- C __init__")
        self.x = x
        print("<- C __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-C-")

"""
    SCENARIUSZ 3
    W tym przypadku dziedziczymy od klasy A brakującą w klasie D metodę __new__
    Od każdej z pozostałych klas dziedziczymy ich metodę __init__ (z powodu użycia funkcji super())
    Kolejność klas w MRO w tym przypadku będzie następująca:
    class D -> class A -> class C -> class B -> class Baza

"""
class D(A, C, B, Baza):
    # tu nie definiować __new__
    def __init__(self, x):
        print("-> D __init__", x)
        super().__init__(x)
        print("-- D __init__")
        self.x = x
        print("<- D __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-D-")


### SCENARIUSZ 1: 
print(B.mro())
b = B(123)
print("------------")
b.id()
print("------------")
print(b)
print("---koniec scenariusza 1--\n")

### SCENARIUSZ 2: 
print(C.mro())
c = C(456)
print("------------")
c.id()
print("------------")
print(c)
print("---koniec scenariusza 2--\n")

### SCENARIUSZ 3: 
print(D.mro())
d = D(789)
print("------------")
d.id()
print("------------")
print(d)
print("---koniec scenariusza 3--\n")

### SCENARIUSZ 4: 
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d),id() albo B(d),id() itp.
# a = A(d)
# print("------------")
# a.id()
# print("------------")
# print("---koniec scenariusza a.id()--\n")

b = B(d)
print("------------")
b.id()
print("------------")
print(b)
print("---koniec scenariusza b.id()--\n")

c = C(d)
print("------------")
c.id()
print("------------")
print(c)
print("---koniec scenariusza c.id()--\n")