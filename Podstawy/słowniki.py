# IX. Słowniki ( dictionary)

klienci_wiek={
    "Kuba":20,
    "Michał":20,
    "Kuba":21,
    "Bartek":17,
    "Filip":9
}


#Wypisanie wszystkich kluczy w słowniku
for key in klienci_wiek:
    print(key)

#Wypisanie wszystkich wartorści w słowniku
print(klienci_wiek.values())


#Wyciąganie wartości elementu z słownika
print(klienci_wiek.get("Kuba","not Valid"))

#Dodawanie jakiegoś elementu do słownika
klienci_wiek["Marcin"]=59
print(klienci_wiek)

#Usuwanie jakiegoś elementu // Wszystkie elementy
klienci_wiek.pop("Kuba")
print(klienci_wiek)