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
                    with open("wyniki4.txt", "w+") as odp:
                        odp.write("Zadanie 4.1\n")
                        odp.write(f"Pierwsza liczba w pliku:{podzielony_plik[i]}\n")
                        pierwszaLiczba=2
                iloscAnagramow+=1
            i+=1

    with open("wyniki4.txt","a") as odp:
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

    with open("wyniki4.txt", "a") as odp:
        odp.write(f"\nZadanie4.2\nLiczba ktora ma najwiecej czynnikow pierwszych:{maksLiczba}\n")
        odp.write(f"Liczba tych czynnikow:{dlugoscCzynnikow}")
        odp.write(f"\nLiczba ktora ma maks roznych czynnikow:{liczbaKtoraMaMaksRCzynnikow}")
        odp.write(f"\nMaks czynnikow roznych:{maksRoznychCzynnikow}")



def ile_dobrych_3(wiersze):
    trojki=[]
    for i in range(0,len(wiersze)):
        liczba_1=int(wiersze[i])
        for j in range(0,len(wiersze)):
            if i==j:
                continue
            liczba_2=int(wiersze[j])
            if liczba_2 % liczba_1==0:
                for k in range(0,len(wiersze)):
                    if i==k or j==k:
                        continue

                    liczba_3=int(wiersze[k])
                    if liczba_3 % liczba_2==0:
                        trojki.append([liczba_1,liczba_2,liczba_3])
    return trojki

def ile_dobrych_5(wiersze):
    piatki=[]
    for i in range(0,len(wiersze)):
        liczba_1=int(wiersze[i])
        for j in range(0,len(wiersze)):
            if i==j:
                continue
            liczba_2=int(wiersze[j])
            if liczba_2%liczba_1==0:
                for k in range(0,len(wiersze)):
                    if k==j or i==k:
                        continue
                    liczba_3 = int(wiersze[k])
                    if liczba_3%liczba_2==0:
                        for m in range(0,len(wiersze)):
                            if m==k or m==j or m==i:
                                continue
                            liczba_4=int(wiersze[m])
                            if liczba_4%liczba_3==0:
                                for n in range(0,len(wiersze)):
                                    if m == k or m == j or m == i or m==n:
                                        continue
                                    liczba_5=int(wiersze[n])
                                    if liczba_5%liczba_4==0:
                                        piatki.append([liczba_1,liczba_2,liczba_3,liczba_4,liczba_5])

    return piatki

def zad4_3():
    with open("liczby.txt","r") as plik:
        odczytany_plik = plik.read()
        podzielony_plik = odczytany_plik.split("\n")
        podzielony_plik.pop()

        liczba_trojek=ile_dobrych_3(podzielony_plik)
        liczba_piatek=ile_dobrych_5(podzielony_plik)

        print(f"Ilosc trojek:{len(liczba_trojek)}")
        print(f"ILosc piatek{len(liczba_piatek)}")

        with open("trojki.txt","w")as odp:
            for i in range(0,len(liczba_trojek)):
                for j in range(0,len(liczba_trojek[i])):
                    odp.write(f"{liczba_trojek[i][j]} ")
                odp.write('\n')


        print(len(liczba_trojek))
        print(len(liczba_piatek))


zad4_1()
zad4_2()
zad4_3()
