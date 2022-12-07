# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
final = { 0 }
tmp = set()

K, M = map(int, input().split())

for i in range(K):
    s = input().split()
    
    for j in final:
        for k in range(1,len(s)):
            tmp.add((pow(int(s[k]),2)+j)%M)
    final = tmp
    tmp = set()
    
print(max(final))