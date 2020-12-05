zakupy = [{'nazwa': 'jablko', 'cena': 10},
{'nazwa': 'banan', 'cena': 15},
{'nazwa': 'malina', 'cena': 22},
{'nazwa': 'truskawka', 'cena': 4}]

suma=0

for i in zakupy:
    suma+=i['cena']

print(suma)
