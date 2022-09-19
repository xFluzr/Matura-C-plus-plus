# XII. Działania na plikach (czytanie , pisanie)

#Żeby otworzyć plik przypisujemy plik do jakieś zmiennej. np. plik =open("dupa.txt","r")
#ZAWSZE TRZEBA PLIK ZAMKNĄĆ ! np. plik.close()


# DRUGI ARGUMENT W FUNKCJI OPEN MOŻE MIEĆ RÓZNE TRYBY
# r-read ( Default value. Opens a file for reading, error if the file does not exist)
# a-append ( Opens a file for appending, creates the file if it does not exist)
# w-write ( Opens a file for writing, creates the file if it does not exist)
# x-create (Creates the specified file, returns an error if the file exist)
# b-binary (Binary mode (e.g. images)
# t-text (Default value. Text mode)

#Pierwszy sposób(gorszy)
# f=open("test.txt","r")
# print(f.name)
# f.close()


#Drugi sposób(lepszy bo nie trzeba zamykać :) )
# with open("test.txt","r") as plik:


#Czytanie całego pliku
# with open("test.txt","r") as plik:
#     zawartosc_Pliku = plik.read()
#     print(zawartosc_Pliku)


#Czytanie JEDNEJ linii pliku
# with open("test.txt","r") as plik:
#     zawartosc_Pliku = plik.readline()
#     print(zawartosc_Pliku)


#Czytanie każdej linii pliku po kolei i złączenie jej w liste
# with open("test.txt","r") as plik:
#     zawartosc_Pliku = plik.readlines()
#     print(zawartosc_Pliku)


#Czytanie każdej linii pliku pętla
# with open("test.txt","r") as plik:
#     for line in plik:
#         print(line)


#Czytanie ile znaków chcemy przeczytać
# with open("test.txt","r") as plik:
#     plik_zawartosc=plik.read(100)
#     print(plik_zawartosc)


#Czytanie znaków do końca plików pętla while
# with open("test.txt","r") as plik:
#     ilosc_znakow=10
#     plik_zawartosc=plik.read(ilosc_znakow)

    # while len(plik_zawartosc)>0:
    #     print(plik_zawartosc,end="*")
    #     plik_zawartosc = plik.read(ilosc_znakow)


    # Zwraca na którym znaku obecnie jesteśmy w pliku
    # print(plik.tell())


    #Wraca do 0 znaku w pliku
    # plik.seek(0)


# PISANIE DO PLIKÓW
# with open("test2.txt","w") as plik:
    #plik.write("dupa")
    # plik.seek(0)           # Jeśli użyjemy seek'a nadpiszemy to co jest na początku pliku
    # plik.write("Piwo")


#Łączenie zapisywanie i czytania pliku
# with open("test.txt","r") as czytanie:
#     with open("kopia.txt", "w") as pisanie:
#         for line in czytanie:
#             pisanie.write(line)