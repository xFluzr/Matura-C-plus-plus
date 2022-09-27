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
        max=1
        chwilowyMax=1
        chwilowaInstr=""
        maxInstr=""
        for line in plik:
            line=line.strip()
            dane=line.split(" ")
            instrukcje.append(dane[0])
        for i in range(0,len(instrukcje)):
            if i>0:
                if instrukcje[i]==instrukcje[i-1] or instrukcje[i]:
                    chwilowyMax+=1
                    chwilowaInstr = instrukcje[i]
                    maxInstr=instrukcje[i]
                    max = chwilowyMax
                else:
                    chwilowyMax=0
                    chwilowaInstr=""
            else:
                chwilowyMax=1
                chwilowaInstr=instrukcje[i]
                continue


        print(maxInstr,max)






zad4_1()
zad4_2()