#3. Napisać program rysujący "miarkę" o zadanej długości.

import sys 
argv = sys.argv[1:] 

for i in range(1,len(argv)+1): 
    dlugosc = int(sys.argv[i])

for i in range(dlugosc-1):
    string="|...." * (i+2)
string=string+"|\n"

for i in range(dlugosc+1):
    if i==9:
        string=string+str(i)
        string=string+" "*3
    else:
        string=string+str(i)
        string=string+" "*(5-int(len(str(i))))
print(string)