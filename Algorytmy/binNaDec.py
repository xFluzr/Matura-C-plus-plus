# Sposób I
# def zamiana_na_dziesietne(liczba):
#    return int(liczba,2)

#TO samo ale jako nie funkcja
# liczbaBin="1101"
# liczbaDziesietna=int(liczbaBin,2)
# print(liczbaDziesietna)


# Sposób II
def zamiana_na_dziesietne(liczbaBin):
    liczbaDziesietna=1
    potega=1
    i=len(liczbaBin)-1
    while(i>0):
        if liczbaBin[i]=="0":
            potega = potega * 2
        if liczbaBin[i]=="1":
            potega = potega * 2
            liczbaDziesietna = liczbaDziesietna + potega
        i=i-1
    return liczbaDziesietna