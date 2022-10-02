def szyfrowanie(znak,k):
    liczba=0
    szyfrowanyNapis=""
    liczba=ord(znak)+k
    if liczba>90:
        liczba=64+liczba-90
    szyfrowanyNapis=chr(liczba)+szyfrowanyNapis
    return szyfrowanyNapis

def zad6_1():
    with open("dane_6_1.txt","r") as plik:
        zaszyfrowaneNapisy=[]
        plik=plik.read()
        plik=plik.split("\n")
        for i in range(0,len(plik)):
            napis=""
            for j in range(0,len(plik[i])):
                napis+=szyfrowanie(plik[i][j],107%26)
            zaszyfrowaneNapisy.append(napis)

        with open("wynik_dane_6_1.txt","w") as odp:
            odp.write("6.1\n")
            for napis in zaszyfrowaneNapisy:
                odp.write(f"{napis}\n")


def odszyfrowanie(napis,k):
    kodAscii=0
    odszyfrowanyNapis=""
    if k=="":
        k=0
    else:
        k=int(k)%26
    if len(napis)<2:
        kodAscii = ord(napis) - k
        if kodAscii < 65:
            kodAscii += 26
        return ord(kodAscii)
    for litera in napis:
        kodAscii=ord(litera)-k
        if kodAscii<65:
            kodAscii+=26
        odszyfrowanyNapis+=chr(kodAscii)

    return odszyfrowanyNapis
def zad6_2():
    with open("dane_6_2.txt", "r") as plik:
        odszyfrowaneNapisy = []
        plik = plik.read()
        plik = plik.split("\n")
        plik.pop()
        with open("wynik_dane_6_2.txt","w") as odp:
            for i in range(0,len(plik)):
                plik[i]=plik[i].split(" ")
            for j in range(0,len(plik)):
                napis=odszyfrowanie(plik[j][0],plik[j][1])
                odp.write(f"{napis}\n")

def zad6_3():
    with open("dane_6_3.txt", "r") as plik:
        plik = plik.read()
        plik = plik.split("\n")
        plik.pop()
        for i in range(0, len(plik)):
            plik[i] = plik[i].split(" ")
            stary_klucz=abs(ord(plik[i][0][0])-ord(plik[i][1][0]))
            for j in range(0,len(plik[i][1])):
                nowy_klucz=abs(ord(plik[i][0][j])-ord(plik[i][1][j]))
                if stary_klucz!=nowy_klucz and stary_klucz!=26-nowy_klucz:
                    with open("wynik_dane_6_3.txt","a") as odp:
                        odp.write(f"{plik[i][0]}\n")
                    break

zad6_1()
zad6_2()
zad6_3()