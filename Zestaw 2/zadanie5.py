# 5. Napisz funkcję, która dla podanej liczby naturalnej N zwraca długość jej najdłuższej binarnej przerwy, albo 0

def fun(N):
    count = 0
    list = []
    binary = bin(N)
    for i in range(len(str(binary))):
        if str(binary)[i] == '1':
            for j in range(i+1,len(binary)):
                if str(binary)[j] == '0':
                    count += 1
                else:
                    break
            if str(binary)[j] == '1':
                list += [count]
            count = 0
    return max(list)

print(str(fun(529)))
