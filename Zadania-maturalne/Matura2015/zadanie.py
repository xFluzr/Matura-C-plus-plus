def a():
    with open("liczby.txt", "r") as plik:
        zera=0
        jedynki=0
        wiekszoscZer=0
        plik=plik.read()
        plik=plik.split("\n")
        for i in range(0,len(plik)):
            for cyfra in plik[i]:
                if cyfra=="1":
                    jedynki+=1
                if cyfra=="0":
                    zera+=1
            if zera>jedynki:
                wiekszoscZer+=1
            jedynki=0
            zera=0
        with open("wynik4.txt", "w") as odp:
            odp.write("a)\n")
            odp.write(f"Ilosc wiekszosci z zerem:{wiekszoscZer}")

def b():
    with open("liczby.txt", "r") as plik:
        podzielnychPrzez2=0
        podzielnychPrzez8=0
        podzielnaPrzez8=True
        plik=plik.read()
        plik=plik.split("\n")
        for i in range(0, len(plik)):
            ostatniBit=plik[i][-1]
            if(ostatniBit=="0"):
                podzielnychPrzez2+=1
            else:
                continue
            for j in range(1,4):
                ostatniBit=plik[i][-j]
                if ostatniBit!="0":
                    podzielnaPrzez8=False
            if podzielnaPrzez8==True:
                podzielnychPrzez8+=1
            podzielnaPrzez8=True
        with open("wynik4.txt", "a") as odp:
            odp.write("\n\nb)\n")
            odp.write(f"Podzielnych przez 2:{podzielnychPrzez2}, Podzielnych przez 8: {podzielnychPrzez8}")


# Sposób I
# def zamiana_na_dziesietne(liczba):
#    return int(liczba,2)

# Sposób II
def zamiana_na_dziesietne(liczba):
    liczbaDziesietna=1
    potega=1
    i=len(liczba)-1
    while(i>0):
        if liczba[i]=="0":
            potega = potega * 2
        if liczba[i]=="1":
            potega = potega * 2
            liczbaDziesietna = liczbaDziesietna + potega
        i=i-1
    return liczbaDziesietna

def c():
    with open("liczby.txt", "r") as plik:
        plik=plik.read()
        plik=plik.split("\n")
        najw=0
        najm=zamiana_na_dziesietne(plik[0])
        for i in range(0, len(plik)):
            plik[i]=zamiana_na_dziesietne(plik[i])
            if najm>plik[i]:
                najm=plik[i]
                indeksNajm=i
            if najw<plik[i]:
                najw=plik[i]
                indeksNajw = i
        with open("wynik4.txt","a") as odp:
            odp.write("\nc)")
            odp.write(f"\nIndeks liczby najwiekszej: {indeksNajw+1}")
            odp.write(f"\nIndeks liczby najmniejszej: {indeksNajm+1}")




a()
b()
c()