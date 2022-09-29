def nwd_algorytm_euklidesa(liczba1,liczba2):
    przechowanie=0
    while liczba2!=0:
        przechowanie=liczba2
        liczba2=liczba1%liczba2
        liczba1=przechowanie
    return liczba1

print(nwd_algorytm_euklidesa(12,18))