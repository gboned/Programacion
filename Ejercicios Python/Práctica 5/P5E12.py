# Garbiñe Boned -P5E12-
# Escribe un programa que pida un número y escriba si es primo o no
num = int(input('Introduce un numero: '))
num_primo = 0
if num > 1:
    for i in range(1, num + 1):
        if (num % i) == 0:
            num_primo += 1
    if num_primo == 2:
        print(f'El numero {num} es primo')
    else:
        print(f'El numero {num} no es primo')
else:
    print(f'El numero {num} no es primo')