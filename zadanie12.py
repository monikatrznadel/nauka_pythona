kosz_cena=[100, 100, 90, 100, 100]
kosz_prod=['mleko','jajka','majonez','seler','jablko']

print('Wyjsciowa wartosc koszyka to: ')
suma = 0
for i in kosz_cena:
    suma=suma + i
print('Wartosc koszyka',suma)
## Dodatkowe 1
print('Dodatkowe 1: ')
if len(kosz_prod) > 3:
    suma_dot1 = suma*0.95
    print('cena kosza1 po znizce 5 % to ', suma_dot1)
elif suma>500:
    suma_dot1 = suma*0.9
    print ('cena kosza1 po znizce 10 % to', suma_dot1)
else:
    print('Brak znizek, cena koszyka1', suma)
## dodatkowe 2
print('Dodatkowe 2: ')
if suma>500:
    suma_dot1 = suma*0.9
    print ('cena kosza2 po znizce 10 % to', suma_dot1)
elif len(kosz_prod) > 3:
    suma_dot1 = suma*0.95
    print('cena kosza2 po znizce 5 % to ', suma_dot1)
else:
    print('Brak znizek, cena koszyka2', suma)

## dodatkowe3
print('Dodatkowe 3: ')
min=kosz_cena[0]
for i in kosz_cena:
    if i<min:
        min=i
suma_d3 = suma - min
print('Suma koszyka gdzie najtanszy produkt jest gratis to ',suma_d3)

##dodatkowe 4
print('Dodatkowe 4: ')
suma_d4 = 0
for idx in range(len(kosz_cena)):
    if (idx+1) % 3 != 0:
        suma_d4=suma_d4+kosz_cena[idx]
print('Suma gdy co trzeci produkt gratis ',suma_d4)
