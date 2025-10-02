liczba1 = float(input("podaj 1 liczbę: "))
liczba2 = float(input("podaj 2 liczbę: "))
wybierz = int(input("wybierz działanie (1 = +) (2 = -) (3 = *) (4 = /): "))

if wybierz == 1:
    print(liczba1, "+", liczba2, "=", liczba1 + liczba2)

elif wybierz == 2:
    print(liczba1, "-", liczba2, "=", liczba1 - liczba2)

elif wybierz == 3:
    print(liczba1, "*", liczba2, "=", liczba1 * liczba2)

elif wybierz == 4:
    print(liczba1, "/", liczba2, "=", liczba1 / liczba2)

else:
    print("nieobsugiwana funkcja")

