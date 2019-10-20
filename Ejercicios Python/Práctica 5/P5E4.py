# Garbiñe Boned -P5E4-
# Programa que pida numero y calcule factorial
num = int(input('Introduce un numero para calcular factorial: '))
factorial = 1
for i in range(1, num +1):
    factorial = factorial * i
print(f'El factorial del numero {num} es {factorial}')