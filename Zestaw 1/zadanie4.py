#4. Napisać program rysujący prostokąt zbudowany z małych kratek.

print("Podaj wysokosc: ")
wysokosc = input()

print("Podaj szerokosc: ")
szerokosc = input()

string = ""
for i in range (int(wysokosc)):
    for j in range(int(szerokosc)):
        string += "+---"
    string+="+"
    string = string + "\n"
    for j in range(int(szerokosc)):
        string = string + "|   " 
    string+="|"
    string=string+"\n"

for j in range(int(szerokosc)):    
    string+= "+---"
string+="+"
print(string)
