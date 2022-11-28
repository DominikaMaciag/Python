# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())

list = []

for i in range(K):
    list.append(input())    
# print(list)

for i in range(K):
    print("---",i)
    print(list[i])
    print(max(list[i]))
    
#column out of 2d array
# def column(matrix, i):
#     return [row[i] for row in matrix]

# for i in range(K):
#     print(column(input(),i))
