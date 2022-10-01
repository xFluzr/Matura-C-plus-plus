#sposób I
# def zamiana_na_bin(liczbaDziesietna):
#     return bin(liczbaDziesietna)[2:]


#Sposób II
# def zamiana_na_bin(liczbaDziesietna):
#     liczbaBin=""
#     while liczbaDziesietna>0:
#         liczbaBin=f"{liczbaDziesietna%2}"+liczbaBin
#         liczbaDziesietna=liczbaDziesietna//2
#     return liczbaBin

#Sposób III (rekurencja)
# def zamiana_na_bin_rek(liczbaDziesietna):
#     if liczbaDziesietna>1:
#         zamiana_na_bin_rek(liczbaDziesietna//2)
#     print(liczbaDziesietna % 2,end ='')
#
# zamiana_na_bin_rek(10)
# print()