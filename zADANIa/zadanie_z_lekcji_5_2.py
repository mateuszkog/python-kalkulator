a = (input("jaki mamy miesiąc?: "))



if a == 'styczeń' or a == 'luty':
    cena = 150

elif a == 'marzec' or a == 'kwiecień':
    cena = 199

elif a == 'maj' or a == 'czerwiec':
    cena = 249

elif a == 'lipiec' or a == 'sierpień' or a == 'wrzesień':
    cena = 299

elif a == 'październik':
    cena = 249

elif a == 'listopad' or a == 'grudzień':
    cena = 199

else:
    print("nie ma takiego miesiąca albo zrobiłeś literówkę")

print("atrakcja turystyczna kosztuje:", cena, "$")