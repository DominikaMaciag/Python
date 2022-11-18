# Zadanie 3 - Dominika Maciąg

# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self,x):
        print(f"wykonanie foo({self}, {x})")

    @classmethod
    def class_foo(cls,x):
        print(f"class_foo({cls}, {x})")
    
    @staticmethod
    def static_foo(x):
        print(f"wykonanie static_foo({x})")

a = A()
print(a.foo(123)) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
print(A.foo(a,123)) # ditto
print(a.class_foo(123)) # class_foo(<class '__main__.A'>, 123)
print(A.class_foo(123)) # ditto
print(a.static_foo(123)) # wykonanie static_foo(123)
print(A.static_foo(123)) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod
class Baza(ABC):         
    @abstractmethod
    def my_abstract_method(self):
        print("message from Baza class!")

class Sister(Baza):
    def my_abstract_method(self): # nadpisujemy metodę abstrakcyjną
        print("hello from Sister class")

class Brother(Baza):
    def my_abstract_method(self): # napisujemy metodę abstrakcyjną
        super().my_abstract_method()
        print("hello from Brother class")

x = Sister()
x.my_abstract_method()
y = Brother()
y.my_abstract_method()


# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu
class Sample:
    def __init__(self):
        self.__name =''
    
    @property
    # getter
    def nazwa(self):
        print("Nazwa to: ")
        return self.__name

    # setter
    @nazwa.setter
    def nazwa(self,name):
        if len(name) <=0:
            raise ValueError("Nie podano nazwy")
        print("Podano nazwę.")
        self.__name = name

# tworzymy obiekt klasy Sample 
samp = Sample()
# ustalamy nazwę 
samp.nazwa = "Przykładowa Nazwa"
# wypiszmy nazwę:
print(samp.nazwa)
