def zad_1():
    with open("slowa.txt","r") as plik:
        plik=plik.read()
        plik=plik.split("\n")
        with open("Wynik5.txt", "w") as odp:
            odp.write("zadanie1)\n")
        for i in range(1,13):
            slowa_n_literowe = 0
            for j in range(0,len(plik)):
                if i==len(plik[j]):
                    slowa_n_literowe+=1
            with open("Wynik5.txt","a") as odp:
                odp.write(f"{i} {slowa_n_literowe}\n")

def anagram(slowo):
    return slowo[::-1]

def zad_2():
    with open("nowe.txt","r") as nowyPlik:
        nowyPlik = nowyPlik.read()
        nowyPlik = nowyPlik.split("\n")
        nowyPlik.pop()
    with open("slowa.txt","r")as plik:
        plik = plik.read()
        plik = plik.split("\n")
    with open("wynik5.txt","a") as odp:
        odp.write("\nzadanie2)")
        for i in range(0,len(nowyPlik)):
            liczba_wystapien=0
            liczba_anagramow=0
            for j in range(0,len(plik)):
                if nowyPlik[i]==plik[j]:
                    liczba_wystapien+=1
                if anagram(plik[j])==nowyPlik[i]:
                    liczba_anagramow+=1

            odp.write(f"\n{nowyPlik[i]} {liczba_wystapien}, {liczba_anagramow} ")

zad_1()
zad_2()