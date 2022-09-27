def czyPierwsza(liczba):
    i=2
    if liczba<2:
        return False
    while(liczba>=(i*i)):
        if(liczba%i==0):
            return False
        i+=1
    return True

def a():
    with open("NAPIS.TXT","r") as plik:
        dane=plik.read()
        dane=dane.rstrip()
        dane=dane.split("\n")
        suma=0
        lp=0
        for napis in dane:
            for i in range(0,len(napis)):
                suma+=ord(napis[i])

            if czyPierwsza(suma)==True:
                lp+=1
            suma=0
        print(lp)
        with open("ZADANIE5.txt","w") as odp:
            odp.write("Zadanie a)\n")
            odp.write(f"Ilosc pierwszych w pliku: {lp}")


def b():
    with open("NAPIS.TXT","r") as plik:
        dane=plik.read()
        dane=dane.rstrip()
        dane=dane.split("\n")
        with open("ZADANIE5.txt", "a") as odp:
            odp.write("\n\nZadanie b)\nNapisy Rosnace:\n")
        rosnacy=True
        for napis in dane:
            rosnacy = True
            for i in range(1,len(napis)):
                if rosnacy==False:
                    break
                if(ord(napis[i])<=ord(napis[i-1])):
                    rosnacy=False
            if rosnacy is True:
                with open("ZADANIE5.txt","a") as odp:
                    odp.write(f"{napis}\n")

def c():
    with open("NAPIS.TXT", "r") as plik:
        dane = plik.read()
        dane = dane.rstrip()
        dane = dane.split("\n")
        with open("ZADANIE5.txt", "a") as odp:
            odp.write("\nZadanie c)\nNapisy wystepujace wiecej niz jeden raz:\n")
        i=0
        for i in range(i,len(dane)):
            for j in range(i,len(dane)):
                if i==j:
                    continue
                if dane[i]==dane[j]:
                    with open("ZADANIE5.txt", "a") as odp:
                        odp.write(f"{dane[i]}\n")
            i+=1

a()
b()
c()