# Zadanie 4 - Dominika Maciąg
# Dynamiczny charakter języka Python nie pozwala na bezpośrednie przeładowywanie funkcji o tych samych
# nazwach, ale różnych argumentach. Z pomocą dekoratorów pojawiają się w język techniki emulujące takie
# zachowania. W ramach zadania proszę przestudiować materiał na temat singledispatch oraz
# singledispatchmethod z modułu functools oraz napisać dowolny kod ilustrujący te przypadki 

from functools import singledispatch, singledispatchmethod

@singledispatch
def multiply(a, b):
    raise NotImplementedError('Unsupported type')

@multiply.register(int)
def _(a,b):
    print(a*b)

@multiply.register(float)
def _(a,b):
    print(a*b)

@multiply.register(str)
def _(a,b):
    print(a,"*",b)

class Sum:
    @singledispatchmethod
    def add(self, a, b):
        raise NotImplementedError('Unsupported type')

    @add.register(int)
    def _(self, a, b):
        print(a+b)

    @add.register(float)
    def _(self, a, b):
        print(a+b)


if __name__ == '__main__':
    multiply(2,7)
    multiply(2.0,7.0)
    multiply("2","7")

    s = Sum()
    s.add(2, 2)
    s.add(2.0, 2.0)