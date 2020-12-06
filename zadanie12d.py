koszyk = [
{'nazwa':'mleko', 'ilosc':20, 'cena':4.0},
{'nazwa':'jajka','ilosc':5, 'cena':5.0},
{'nazwa':'majonez','ilosc':6, 'cena':6.0},
{'nazwa':'seler','ilosc':40, 'cena':7.0},
{'nazwa':'jablko','ilosc':30, 'cena':8.0}
]

print('Wyjsciowa wartosc koszyka bez znizki to: ')
suma = 0
for i in koszyk:
    suma=suma + (i['ilosc']*i['cena'])
print('Wartosc koszyka',suma)

## Dodatkowe 1
print('Dodatkowe 1: ')
if len(koszyk) > 3:
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
elif len(koszyk) > 3:
    suma_dot1 = suma*0.95
    print('cena kosza2 po znizce 5 % to ', suma_dot1)
else:
    print('Brak znizek, cena koszyka2', suma)
