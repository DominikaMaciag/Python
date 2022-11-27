from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda licznik, mianownik: licznik*mianownik, fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)