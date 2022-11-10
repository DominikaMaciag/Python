# 2. Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, a następnie każdą
# rozkłada na czynniki pierwsze 

import sys # importujemy modul
argv = sys.argv[1:] # argv to lista, a 1: robi selekcje bez pierwszego argumentu – nazwy programu

#obliczanie 
def primeFactorization(num):
    k=2
    licznik = 0 
    while num > 1:        
        if num%k == 0:
            licznik+=1
            num/=k

        if num%k!=0:
            if licznik>0 and licznik !=1:
                print(str(k), "^", str(licznik), "* " , end="")
                licznik = 0
            k+=1
            if licznik==1:
                licznik = 0
                if num==1:
                    print(str(k-1), end="")
                else:
                    print(str(k-1), "* ", end="")
                
                    
for i in range(1,len(sys.argv)):
    print("rozkład liczby ", str(sys.argv[i]), " wynosi: ")
    primeFactorization(int(sys.argv[i]))
    print("")
