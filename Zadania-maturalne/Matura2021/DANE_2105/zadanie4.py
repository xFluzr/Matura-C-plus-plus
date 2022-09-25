def obliczanie_neonu(instrukcja,literaBadzCyfra,iteracja,neon):
    iteracja=int(iteracja)
    if instrukcja=='DOPISZ':
        neon.append(literaBadzCyfra)
        iteracja+=1
    elif instrukcja=='ZMIEN':
        neon[iteracja]=literaBadzCyfra
    elif instrukcja=='USUN':
        neon.pop(iteracja)
        iteracja=iteracja-1
    elif instrukcja=="PRZESUN":
        for i in range(0,len(neon)):
           if literaBadzCyfra==neon[i]:
               neon[i]=ord(literaBadzCyfra)+1
               neon[i]=chr(neon[i])
    return neon


def zad4_1():
    neon = []
    with open("przyklad.txt","r") as plik:
        i=0
        for line in plik:
            line=line.strip()
            dane=line.split(" ")
            obliczanie_neonu(dane[0],dane[1],i,neon)
        print(neon)
        print(len(neon))



zad4_1()