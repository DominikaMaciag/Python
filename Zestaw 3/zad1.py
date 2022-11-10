# Zadanie 1 - Dominika Maciąg
# Przepisz dane z jsona do słownika, gdzie kluczem jest nr. linii, 
# a wartością krotka zawierająca nazwy wszystkich przystanków danej linii.

import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
# print(data["linia"][0]["przystanek"][0]["name"])

dict = {}
dict_sup = {} # pomocniczy słownik
tuple = ()
liczba_przystankow = 0

for j in range (len(data["linia"])):
    if len(data["linia"][j]) == 2: 
        for i in range (len(data["linia"][j]["przystanek"])):
            tuple += (data["linia"][j]["przystanek"][i]["name"][:-3],)
        dict[data["linia"][j]["name"]] = tuple
        # print("linia nr.",data["linia"][j]["name"], "ma", len(tuple), "przystanków")
        dict_sup[data["linia"][j]["name"]] = len(tuple)
        tuple = () 

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(dict, file, ensure_ascii=False) # zapisujemy do nowego jsona 

# Wypisz numer linii oraz liczbę jego przystanków, posortowane po liczbie przystanków w kolejności malejącej
dict_sorted = sorted(dict_sup.items(), key=lambda x:x[1], reverse=True)

for i in dict_sorted:
    print("linia nr.",*i, "przystanków")

#  Wypisz liczbę wszystkich przystanków obsługiwanych przez tramwaje
odpowiedz = set()
for i in range (len(dict)):
    if len(data["linia"][i]) == 2: 
        odpowiedz = odpowiedz | set(dict[data["linia"][i]["name"]])
# print(odpowiedz)
print("liczba wszystkich przystanków wynosi: ", len(odpowiedz))

    