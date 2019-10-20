# Garbiñe Boned -P4E1-
# Pida 5 numeros y diga cual es el mayor y el menor
num1 = int(input(f'Introduce el primer numero: '))
num2 = int(input(f'Introduce el segundo numero: '))
num3 = int(input(f'Introduce el tercer numero: '))
num4 = int(input(f'Introduce el cuarto numero: '))
num5 = int(input(f'Introduce el quinto numero: '))
maximo = max(num1, num2, num3, num4, num5)
minimo = min(num1, num2, num3, num4, num5)
print(f'El mayor numero es el: {maximo}')
print(f'El menor numero es el: {minimo}')