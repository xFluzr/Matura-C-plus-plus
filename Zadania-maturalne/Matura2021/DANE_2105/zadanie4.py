def obliczanie_dlugosci_neonu(instrukcja,dlugosc):
    if instrukcja=="DOPISZ":
        dlugosc+=1
    elif instrukcja=="USUN":
        dlugosc-=1
    return dlugosc
def zad4_1():
    with open("instrukcje.txt","r") as plik:
        dlugosc=0
        for line in plik:
            line=line.strip()
            dane=line.split(" ")
            dlugosc=obliczanie_dlugosci_neonu(dane[0],dlugosc)
        with open("wyniki4.txt","w") as odp:
            odp.write(f"Zad 4.1) \nDlugosc neonu:{dlugosc}")

def zad4_2():
    with open("przyklad.txt", "r") as plik:
        instrukcje=[]
        chiwlowaInstrukcja=""
        for line in plik:
            line=line.strip()
            dane=line.split(" ")
            instrukcje.append(dane[0])
        



zad4_1()
zad4_2()