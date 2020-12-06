password=input('Wprowadz haslo: ')

newpassword = ''

for i in range(len(password)):
    if i == 0 or i == (len(password)-1):
        newpassword = newpassword + password[i]
    else:
        newpassword = newpassword + '*'

print(newpassword)
