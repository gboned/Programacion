# Garbiñe Boned -P5E2-
# Escribir programa que pida 2 numeros y escriba que numeros entre esos son pares y cuales impares
num1 = int(input('Escribe un numero: '))
num2 = int(input(f'Escribe un numero que sea mayor que {num1}: '))
for i in range(num1, (num2+1)):
    if i % 2 == 0:
        print('El numero', i, 'es par')
    else :
        print('El numero', i, 'es impar')