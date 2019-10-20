# Garbiñe Boned -P3E5-
# Que pida numero de maximo 3 cifras, si usuario introduce un numero de mas de 3 cifras, hay que dar mensaje de error
numero = int(input('Introduce un numero de maximo 3 cifras: '))
if numero > 999:
    print('ERROR, el numero', numero, 'tiene mas de 3 cifras')
else:
    print(numero)


