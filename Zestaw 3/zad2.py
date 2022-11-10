# Zadanie 2 - Dominika Maciąg
# Napisać program konwertujący liczby zapisane w systemie rzymskim (wielkimi literami I, V, X, L, C, D, M) na
# liczby arabskie w zakresie liczb 1-3999, i odwrotnie.
# Sprawdź poprawność danych wejściowych w formacie rzymskim!
# Algorytmy do zamiany zostały znalezione na stronie tutorialspoint

l_wejsciowa = input("podaj liczbe do zamiany: ") 

def romanToDecimal(number):
    dict = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V': 5, 'I': 1, 
    'IV': 4,'IX': 9,'XL': 40,'XC': 90,'CD': 400,'CM': 900}
    result = 0
    i = 0

    while i < len(number):
        if i+1 < len(number) and number[i:i+2] in dict:
            result += dict[number[i:i+2]]
            i+=2
        else:
            result += dict[number[i]]
            i+=1
    return result

def decimalToRoman(number):
    array = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),
    (90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I"),]
    result = "" 

    for decimal, roman in array:
        decimal_floor,rom_floor = divmod(int(number),decimal)
        result += roman * decimal_floor
        number = rom_floor
    return result

def checkCorectnessOfRoman(number):
    import re
    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",number))

def checkCorectnessOfDecimal(number):
    if int(number)>=1 and int(number)<=3999:
        return True
    else: 
        return False

if(checkCorectnessOfRoman(l_wejsciowa) == True):
    print(romanToDecimal(l_wejsciowa))

elif(checkCorectnessOfDecimal(l_wejsciowa) == True):
    print(decimalToRoman(l_wejsciowa))

else:
    print("niepawidlowy numer")
    

