# VIII. Instrukcje warunkowe IF , ELIF, ELSE

#Budowa instrukcji warunkowej w pythonie

# czy_udalo_sie=False
#Wersja z nawiasami
# if(czy_udalo_sie):
#     print("Udało się")
# else:
#     print("Nie udało się")

#Wersja bez nawiasów
# if czy_udalo_sie:
#     print("Udało się")
# else:
#     print("Nie udało się")



#Porównania

# wiek_sprzedazy_alkoholu=18
# wiek_bartka=14
# wiek_kuby=19
# def czy_moze_kupic_piwo(wiek):
#     if(wiek<18):
#         return "Jesteś jeszcze za młody !"
#     elif(wiek==18):
#         return "Oj byczq twój szczęśliwy rok ;)"
#     else:
#         return "Chłopie ty się jeszcze pytasz, taki stare a jeszcze nie wie"
#
# print(czy_moze_kupic_piwo(wiek_bartka))


#AND oraz OR

# jest_wysoki=False
# jest_gruby=True
#
# if jest_wysoki and jest_gruby:
#     print("Jesteś gruby i brzydki")
# if jest_wysoki or jest_gruby:
#     print("Jesteś gruby lub wysoki")

#Negacja/zaprzeczanie

# jest_chudy=True
# print(not(jest_chudy))


#Większy lub równy od czegoś/ oraz Mniejszy lub równy od czegoś/

# liczba_wylosowana=50
# if(liczba_wylosowana<=40):
#     print("Mniejsza lub równa od 40")
# elif(liczba_wylosowana>=50):
#     print("liczba większa lub równa 50")