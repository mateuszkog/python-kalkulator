print("oto program który mówi jakim rodzajem czipsów jesteś")
print("żeby z niego skorzystać musić spełnić moje wymagania")
print("       ")

pytanie = input("Najpierw płatki czy mleko?")

if pytanie == 'płatki':
    print("(debil)")
    print("niestety nie spełniasz moich wymagań i nie możesz skorzystać z kodu")
    print("radzę też przemyśleć swoje decyzje życiowe")


if pytanie == 'mleko':
    print("dobra sigmo na spokojnie możesz skorzystać z kodu")
    print("tak btw odpowiadaj tylko tak albo nie")
    print("          ")
    a = input("Czy grasz w Clash Royale?")

    b = input("Czy twój najlepszy przyjaciel ma siostrę?")

    c = input("Czy uważasz żę 2+2=5?")

    d = input("Czy słuchasz eminema?")

    e = input("Czy tak znaczy nie?")

    f = input("Czy wiesz jak działa czas?")

    g = input("Czy twoja średnia z matmy jest większa niż 3,14?")

    wynik = 0 
    if a == 'tak':
        wynik += 1
    
    if b == 'tak':
        wynik += 1

    if c == 'tak':
        wynik += 1

    if d == 'tak':
        wynik += 1

    if e == 'tak':
        wynik += 1

    if f == 'tak':
        wynik += 1

    if g == 'tak':
        wynik += 1

    if wynik == 7:
        print("jesteś czipsami paprykowymi")  

    if wynik == 6:
        print("jesteś czipsami o smaku kebaba")
        
        print("KJEBAB ")

    if wynik == 5:
        print("jesteś czipsami o smaku kebaba")
        
        print("KJEBAB ")

    if wynik == 1:
        print("jesteś czipsami fromage")

    if wynik == 2:
        print("jesteś czipsami fromage")

    if wynik == 3:
        print("jesteś zwykłymi solonymi")

    if wynik == 4:
        print("jesteś czipsami z chili i limonką")
