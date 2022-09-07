# V. DEKLARACJA LISTY // Da się je modyfikować
friends = ["Kuba", "Kuba", "Bartek", "Michał", "Filip", 2137, False]
lucky_numbers = [7, 69, 420, 2137]

# Można brać elementy z listy od początku
# print(friends[1])

# Albo też od końca
# print(friends[-1])

# Wszystkie elementy od jakiegoś indeksa
# print(friends[1:])

# Branie elementów z danego range'a
# Weźmie 1,2 element bez 3
# print(friends[1:3])

# Update elementu
# friends[1]="Mariusz"
# print(friends)

# Łączenie list
# print(friends+lucky_numbers)
#lub
# friends.extend(lucky_numbers)
# print(friends)

# Dodawanie jednego elementu na koniec
# friends.append("Tadeusz")
# print(friends)

#Wstawianie elementu w dane miejsce
# friends.insert(5,"UPDATE DANYCH")
# print(friends)

#Usuwanie elementu
# friends.remove("Kuba")
# print(friends)

#Usuwanie ostatniego elementu
# friends.pop()
# print(friends)

#Wypisuje index danego elementu
# print(friends.index("Michał"))

#Wypisuje ile dany element się powtarza
# print(friends.count("Kuba"))

#SORTOWANIE ELEMENTÓW LISTY !!!!
# lucky_numbers.sort()
# print(lucky_numbers)

#Odwórcone sortowanie
# lucky_numbers.reverse()
# print(lucky_numbers)

#Kopiowanie listy
# friends2=friends.copy()

#Tworzenie listy z krotek
# cordinatesList=[(4,5),(5,6),(69,20)]
# print(cordinatesList)