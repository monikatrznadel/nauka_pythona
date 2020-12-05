print('Zadanie 8')
owoce = ['jablko', 'banan', 'malina', 'truskawka']
print(owoce[0])
print(owoce[1])
print(owoce[2])
print(owoce[3])

for w in owoce:
    print('Iteruje wszystko',w)

print('Trzeci owoc na liscie to',owoce[2])

for  idx in range(len(owoce)):
    print("idx: " + str(idx) + " : " + owoce[idx])
