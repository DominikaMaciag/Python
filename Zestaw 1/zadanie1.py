# 1. Narysować odwrócony pusty trójkąt z gwiazdek o zadanej długości nieparzystej, np. dla 11 

podstawa = input()
wysokosc = (int(podstawa)/2)+0.5
podstawaInt = int(podstawa)

for i in range(int(wysokosc)-1):
    for j in range(int(podstawa)):        
        if(i==0):
            print("*", end="")
            if(j==int(podstawa)-1):
                print("") 
        else:
            if(i==j):
                print("*", end="")
            if(j==podstawaInt-3):
                print("*", end="")
                podstawaInt=podstawaInt-1
            if(j==int(podstawa)-1):
                print("") 
            else:
                print(" ", end="")

for i in range(int(wysokosc)):
    if(i==int(wysokosc)-1):
        print("*", end="")
    else:
        print(" ", end="")