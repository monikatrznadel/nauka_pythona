koszyk = [
{'nazwa':'mleko', 'ilosc':20, 'cena':4.0},
{'nazwa':'jajka','ilosc':5, 'cena':5.0},
{'nazwa':'majonez','ilosc':6, 'cena':6.0},
{'nazwa':'seler','ilosc':40, 'cena':7.0},
{'nazwa':'jablko','ilosc':30, 'cena':8.0}
]

# funkcja na sume koszyka
def suma_kosz(koszyk):
    suma=0
    for i in koszyk:
        suma = suma + (i['ilosc'] * i['cena'])
    return suma

if __name__ == '__main__':
    koszyk = [
    {'nazwa':'mleko', 'ilosc':20, 'cena':4.0},
    {'nazwa':'jajka','ilosc':5, 'cena':5.0},
    {'nazwa':'majonez','ilosc':6, 'cena':6.0},
    {'nazwa':'seler','ilosc':40, 'cena':7.0},
    {'nazwa':'jablko','ilosc':30, 'cena':8.0}
    ]
    suma = suma_kosz(koszyk)
    print(suma)
