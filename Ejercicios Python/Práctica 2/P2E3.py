# Garbiñe Boned -P2E3-
# Si un número es par, o no
numero = int(input('Introduce un número: '))
resto = numero % 2 == 0
if resto:
    print(f'El número {numero} es par.')
else:
    print(f'El número {numero} no es par.')