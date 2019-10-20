# Garbiñe Boned -P5E3-
# Pedir dos numeros y escriba suma de enteros desde el primero hasta el ultimo
num1 = int(input('Escribe un numero: '))
num2 = int(input(f'Escribe un numero que sea mayor que {num1}: '))
suma = 0
if num1 < num2:
    for i in range(num1, num2 + 1):
        suma = suma + i
    print(f'La suma de los numeros entre el {num1} y el {num2} es de {suma}')
else:
    print(f'El segundo numero tiene que ser mayor que el primer numero')