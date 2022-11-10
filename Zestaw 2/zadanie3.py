# 3. Dla dowolnego podanego łańcucha znakowego wypisać: ile jest w nim słów,
# ile liter, ile cyfr, oraz wypisać statystykę częstości występowania
# poszczególnych liter oraz cyfr

string = ":a1b3A,a2Z,as3v."

def numberOfLetters(string):
    liczba_liter = 0
    for i in range(len(string)):
        if string[i].isupper() == True or string[i].islower() == True:
            liczba_liter += 1
    print("Liczba liter wyniosla: ", liczba_liter)

def numberOfNumbers(string):
    liczba_cyfr = 0
    for i in range(len(string)):
        if string[i].isnumeric() == True:
            liczba_cyfr = liczba_cyfr +1
    print("Liczba cyfr wyniosla: ", liczba_cyfr)

def frequency(string):
    czestotliwos = {}
    for i in set(string):
        if i > chr(48) and i < chr(58) or i> chr(64) and i<chr(91) or i >chr(96) and i < chr(123):
            czestotliwos[i]=string.count(i)
    return czestotliwos

def numberOfWords(string):
    for i in range(len(string)):
        if string[i]<chr(48) or string[i]>chr(57) and string[i]<chr(65) or string[i]>chr(90) and string[i]<chr(97) and string[i]>chr(122):
            string = string.replace(str(string[i]), " ")
    #print("String zamieniony:", string)

    new_string = ""
    is_space = False
    for i in range(len(string)):
        if string[i] == " ":
            if (is_space == False):
                new_string+=string[i]
                is_space = True
        else:
            new_string+=string[i]
            is_space = False
    #print("Nowy string:", new_string)

    words_count = new_string.count(" ")+1
    if(string[0]==" "):
        words_count-=1
    if(string[len(string)-1]==" "):
        words_count-=1
    print("Ilosc slow wynosi: ", words_count)


numberOfNumbers(string)
numberOfLetters(string)
numberOfWords(string)
print("Czestosc wystepowania poszczegolnych znakow:")
print(frequency(string))

