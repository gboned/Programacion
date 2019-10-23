# Garbiñe Boned -P5E11-
# Escribe un programa que pida un número e imprima todos sus divisores.
num = int(input('Introduce un numero: '))
# Divisores: al dividir ese numero entre ellos, el resto tiene que dar 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i)