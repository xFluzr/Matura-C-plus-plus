def rozklad_na_czynniki(liczba):
    czynniki=[]
    k=2
    while liczba>1:
        while liczba%k==0:
            czynniki.append(k)
            liczba=liczba/k
        k+=1
    return czynniki

print(rozklad_na_czynniki(10))