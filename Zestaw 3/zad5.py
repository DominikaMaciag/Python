# Zadanie 5 - Dominika Maciąg

class Bug(object):
    """
    documentation:
    Klasa Bug zawiera w sobie:
    1) konstruktor __init__ który po utworzeniu instancji klasy Bug zwiększy licznik o jeden
    2) destruktor __del__ który po wywołaniu del object pomniejszy licznik o jeden
    3) metodę __str__ która zwraca wartość licznika oraz bieżące id

    """
    licznik = 0 
    def __init__(self):
        # print("A init called")
        Bug.licznik = Bug.licznik+1
        self.id = Bug.licznik
    def __del__(self):
        # print('Destructor called')
        Bug.licznik= Bug.licznik-1
        print('koniec', Bug.licznik, self.id)
    def  __str__(self):
        return 'Bug(licznik='+ str(Bug.licznik) + ', id= ' + str(self.id) + ')'

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])

# Moje testy: 
# obj = Bug()
# obj2 = Bug()
# obj3 = Bug()
# print(obj) # wypiszemy licznik
# del obj
# print(obj2)