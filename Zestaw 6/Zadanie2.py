# Enter your code here. Read input from STDIN. Print output to STDOUT

S = list(input())
# print(S)

# nowe tablice do ktorych wrzucimy posortowane znaki
upper = []
lower = []
odd = []
even = []

for i in range(len(S)):
    if S[i].isupper():
        upper.insert(i, S[i])
    elif S[i].islower():
        lower.insert(i, S[i])
    elif int(S[i])%2 == 0:
        even.insert(i,S[i])
    else:
        odd.insert(i,S[i])
    
# print("upper: ", upper)
# print("lower: ", lower)
# print("even: ", even)
# print("odd: ", odd)

lower.sort()
upper.sort()
odd.sort()
even.sort()

output = [lower, upper, odd, even]

for i in output:
    for j in i:
        print(j, end="")