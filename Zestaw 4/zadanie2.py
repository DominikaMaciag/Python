# Zadanie 2 - Dominika Maciąg

from math import hypot, atan, sin, cos

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        abs = 'Zespolona(' + abs(self.r) + "+" + abs(self.i) + "j" + ')'
        return abs

    # __repr__ is used to show a string representation of the object
    def __repr__(self):
        return 'Zespolona (' + str(self.r) + ',' + str(self.i) + ')'

    # __str__ is used in to show a string representation of object to be read easily by others
    def __str__(self):
        if(self.i<0):
            string = '(' + str(self.r) + str(self.i) + "j" + ')'
        else:
            string = '(' + str(self.r) + '+' + str(self.i) + "j" + ')'
        return string

    def __add__(self, other):
        if isinstance(other,int):
            sum_r = (int)(self.r) + other
            return Zespolona(sum_r, (int)(self.i))
        elif isinstance(other, float):
            sum_r = float(self.r) + other
            return Zespolona(sum_r, (float)(self.i))
        else:
            sum_r = self.r + other.r 
            sum_i = self.i + other.i
        return Zespolona(sum_r,sum_i)

    def __sub__(self, other):
        if isinstance(other,int):
            sub_r = (int)(self.r) - other
            return Zespolona(-sub_r, -(int)(self.i))
        elif isinstance(other, float):
            sub_r = float(self.r) - other
            return Zespolona(-sub_r, -(float)(self.i))
        else:
            sub_r = self.r - other.r 
            sub_i = self.i - other.i
        return Zespolona(sub_r,sub_i)

    def __mul__(self, other):
        mul_r = self.r * other
        mul_i = self.i * other
        return Zespolona(mul_r,mul_i)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __ne__(self, other):
        return self.r != other.r and self.i != other.i

    def __pow__(self, other):
        y = complex(self.r,self.i)
        return y**other


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)

if __name__ == "__main__":
    main()

# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)