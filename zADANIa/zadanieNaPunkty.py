czy_a_to_max = False

czy_b_to_max = False

czy_c_to_max = False

a = float(input("wybierz losową liczbę: "))

b = float(input("jeszcze raz: "))

c = float(input("ostatni raz: "))

d = a, b, c

e = max(d)

if e == a:
    czy_a_to_max = True

elif e == b:
    czy_b_to_max = True

elif czy_a_to_max == False and czy_b_to_max == False:
    czy_c_to_max = True

print("czy 1 liczba jest największa: ", czy_a_to_max)
print("czy 2 liczba jest największa: ", czy_b_to_max)
print("czy 3 liczba jest największa: ", czy_c_to_max)




