import random


szansa = random.randint(1, 10)

proba = 0

print("ziomuś znalezłeś się w grze zgadywania liczby!")
print("nagrodą są poczucie własnej wartości albo coś")
poziom = input("Wybierz poziom trudny czy łatwy: ")

if poziom == 'łatwy':
    liczba = random.randint(1, 20)
    print("dobra to od 1 do 20")
elif poziom == 'trudny':
    liczba = random.randint(1, 100)
    print("dobra to od 1 do 100")

if szansa == 2:
    print("T@ Llcźb@ ttO: ", liczba)

while True:

    a = int(input("Zgaduj: "))

    proba += 1

    if a == liczba:
        print("Wygrałeś GG")
        win = input("Dobra to wolisz poczucie własnej wartości czy coś: ")
        if win == 'poczucie własnej wartości':
            print("Właśnie czujesz własną wartość :D")
        elif win == 'coś':
            print("to coś to nic")
        quit()

        
       
    elif liczba - a == 4:
        print("4 wyżej")    
        
    else:
        print("nie ta")

#tu są podpowiedzi do poziomu trudnego (pod tym)

    if poziom == 'trudny':
        if (a == 1 and liczba == 100) or (a == 100 and liczba == 1):
            print("debilu frajerze komletnie nie tak")

        if a > 100 or a < 1:
            print("miała byc od 1 do 100")

        if proba == 12:
            print("widzę że się męczysz")
            checi = input("Chcesz rzucić monetą (jeśli wygrasz dam ci dobrą podpowiedź): ")
            if checi == 'tak':
                wynik = random.randint(1, 2)
                strona = input("orzeł czy reszka: ")
                liczbaOdlegla = liczba - a
                if strona == 'orzeł':
                    if wynik == 1:
                        print("Wygrałeś! oto podpowiedź: tyle jeszcze do właściwej liczby:  ", liczbaOdlegla)
                    elif wynik == 2:
                        print("Niestety przegrałeś")
                        print("męcz się dalej")
                elif strona == 'reszka':
                    if wynik == 2:
                        print("Wygrałeś! oto podpowiedź: tyle jeszcze do właściwej liczby:  ", liczbaOdlegla)
                    elif wynik == 1:
                        print("Niestety przegrałeś")
                        print("męcz się dalej")
                        
#tu są podpowiedzi do poziomu łatwego (pod tym)

    if poziom == 'łatwy':
        if a < 10 and liczba > 10:
            print("psst: 2 dziesiątka")

        elif a > 10 and liczba < 10:
            print("psst: 1 dziesiątka")

        if (a == 1 and liczba == 20) or (a == 20 and liczba == 1):
            print("debilu frajerze komletnie nie tak")

        if a > 20 or a < 1:
            print("miała być liczba od 1 do 20")