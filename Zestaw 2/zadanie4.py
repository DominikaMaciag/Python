# 4.  Wypisz listę wszystkich możliwych współrzędnych (i, j, k) na trójwymiarowej siatce, 
# gdzie i+j+k nie jest równe n.

x = input("podaj x:")
y = input("podaj y:")
z = input("podaj z:")
n = input("podaj n:")

list = []

for i in range(int(x)+1):
    for j in range(int(y)+1):
        for k in range(int(z)+1):
            if int(i)+int(j)+int(k)!=int(n):
                list += [[i,j,k]]
print(str(list)) 