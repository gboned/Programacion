# Garbiñe Boned -P4E4-
# Pedir tres numeros y un cuarto numero, y comprobar si el ultimo es divisor de los tres primeros numeros
num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introducir el tercer numero: '))
num4 = int(input('Introducir el cuarto numero: '))
if (num4 % num3) == 0:
    print('El numero', num4, 'es divisor de', num3)
else:
    print('El numero', num4, 'no es divisor de', num3)
if (num4 % num2) == 0:
    print('El numero', num4, 'es divisor de', num2)
else:
    print('El numero', num4, 'no es divisor de', num2)
if (num4 % num1) == 0:
    print('El numero', num4, 'es divisor de', num1)
else:
    print('El numero', num4, 'no es divisor de', num2)