liczba1 = float(input("podaj 1 liczbę: "))
liczba2 = float(input("podaj 2 liczbę: "))
wybierz = int(input("wybierz działanie (1 = +) (2 = -) (3 = *) (4 = /) (5 = **): "))

if wybierz == 1:
    print(liczba1, "+", liczba2, "=", liczba1 + liczba2)

elif wybierz == 2:
    print(liczba1, "-", liczba2, "=", liczba1 - liczba2)

elif wybierz == 3:
    print(liczba1, "*", liczba2, "=", liczba1 * liczba2)

elif wybierz == 4:
    print(liczba1, "/", liczba2, "=", liczba1 / liczba2)

elif wybierz == 5:
    print(liczba1, "**", liczba2, "=", liczba1 ** liczba2)

else:
    print("miałeś wybrać w działaniu od 1 do 5 idioto")

print("teraz należą mi się 3 franki szwajcarskie")
print("możesz blikiem")
a = input("podaj kod blik: ")
print("dzięki, a jeśli podałeś fałszywy kod blik to umrzesz w przyszły czwartek")