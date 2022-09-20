def anagramLiczbowy(liczba):
    if(liczba[0]==liczba[-1]):
        return True
    else:
        return False

with open("liczby.txt","r") as plik:
    iloscAnagramow=0
    odczytany_plik=plik.read()
    podzielony_plik=odczytany_plik.split("\n")
    podzielony_plik.pop()
    i=0
    for i in range(len(podzielony_plik)):
        if (anagramLiczbowy(podzielony_plik[i])):
            iloscAnagramow+=1
        i+=1
    with open("Odpowiedz4.1.txt","w") as odp:
        odp.write(f"Ilosc liczb ktore tak samo sie zaczynaja i koncza: {iloscAnagramow}")


