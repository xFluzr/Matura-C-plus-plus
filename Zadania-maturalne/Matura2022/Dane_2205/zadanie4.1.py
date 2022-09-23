import math


def anagramLiczbowy(liczba):
    if(liczba[0]==liczba[-1]):
        return True
    else:
        return False
def zad4_1():
    with open("liczby.txt","r") as plik:
        iloscAnagramow=0
        pierwszaLiczba=1
        odczytany_plik=plik.read()
        podzielony_plik=odczytany_plik.split("\n")
        podzielony_plik.pop()
        i=0
        for i in range(len(podzielony_plik)):
            if anagramLiczbowy(podzielony_plik[i])==True:
                if pierwszaLiczba == 1:
                    with open("Odpowiedz4.1.txt", "w+") as odp:
                        odp.write("Zadanie 4.1\n")
                        odp.write(f"Pierwsza liczba w pliku:{podzielony_plik[i]}\n")
                        pierwszaLiczba=2
                iloscAnagramow+=1
            i+=1

        with open("Odpowiedz4.1.txt","a") as odp:
            odp.write(f"Ilosc liczb ktore tak samo sie zaczynaja i koncza: {iloscAnagramow}\n")


def rozkladNaPiewsze(liczba):
    czynniki = []
    k = 2
    while liczba != 1:
        while liczba % k == 0:
            liczba //= k
            czynniki.append(k)
        k += 1
    return czynniki

def rozneCzynniki(czynniki):
    iloscRoznychCzynnikow=0
    for czynnik in czynniki:
        if(czynniki.count(czynnik)>1):
            continue
        else:
            iloscRoznychCzynnikow+=1
    return iloscRoznychCzynnikow
def zad4_2():
    maksLiczba=0
    dlugoscCzynnikow=0
    maksRoznychCzynnikow=0
    with open("liczby.txt", "r") as plik:
        odczytany_plik = plik.read()
        podzielony_plik = odczytany_plik.split("\n")
        podzielony_plik.pop()
        for cyfra in podzielony_plik:
            cyfra=int(cyfra)
            if (maksRoznychCzynnikow < rozneCzynniki(rozkladNaPiewsze(cyfra))):
                maksRoznychCzynnikow = rozneCzynniki(rozkladNaPiewsze(cyfra))
                liczbaKtoraMaMaksRCzynnikow=cyfra
            if (dlugoscCzynnikow<len(rozkladNaPiewsze(cyfra))):
                maksLiczba=cyfra
                dlugoscCzynnikow=len(rozkladNaPiewsze(cyfra))

        with open("Odpowiedz4.1.txt", "a") as odp:
            odp.write(f"\nZadanie4.2\nLiczba ktora ma najwiecej czynnikow pierwszych:{maksLiczba}\n")
            odp.write(f"Liczba tych czynnikow:{dlugoscCzynnikow}")
            odp.write(f"\nLiczba ktora ma maks roznych czynnikow:{liczbaKtoraMaMaksRCzynnikow}")
            odp.write(f"\nMaks czynnikow roznych:{maksRoznychCzynnikow}")




zad4_1()
zad4_2()