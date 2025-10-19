import datetime

a = int(input("Wybierz numer odpowiadający obecnej pogodzie za oknem:" \
" (1 - słonecznie" 
" 2 - burzowo" 
" 3 - deszczowo" 
" 4 - pochmurnie): "))

if a == 1:
    pogoda = 'słonecznie'

elif a == 2:
    pogoda = 'burzowo'

elif a == 3:
    pogoda = 'deszczowo'

elif a == 4:
    pogoda = 'pochmurnie'

else:
    print("error")
    quit()

godzina = datetime.datetime.now().hour

czy_mozna_wyjsc_na_dwor = False

if pogoda == "pochmurnie" and godzina >= 9 and godzina <= 15:
    czy_mozna_wyjsc_na_dwor = True

elif pogoda == "słonecznie" and godzina >= 9 and godzina <= 19:
    czy_mozna_wyjsc_na_dwor = True

print("Czy możesz wyjść na dwór: ", czy_mozna_wyjsc_na_dwor)