def czyPierwsza(liczba):
    if liczba<2:
        return False
    k=2
    i=1
    while (liczba>=i*i):
        if liczba%k==0:
            return False
        i+=1
        k+=1
    return True

print(czyPierwsza(5))
