# Garbiñe Boned -P4E2-
# Pedir 5 numeros y decir si estan en orden decreciente, creciente o desordenados
num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introduce el tercer numero: '))
num4 = int(input('Introduce el cuarto numero: '))
num5 = int(input('Introduce el quinto numero: '))
if num1 > num2 > num3 > num4 > num5:
    print('Los numeros:', num1, num2, num3, num4, num5, 'estan en orden decreciente')
elif num1 < num2 < num3 < num4 < num5:
    print('Los numeros:', num1, num2, num3, num4, num5, 'estan en orden creciente')
else:
    print('Los numeros:', num1, num2, num3, num4, num5, 'estan desordenados')