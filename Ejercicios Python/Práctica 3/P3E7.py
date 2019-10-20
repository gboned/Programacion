# Garbiñe Boned -P3E7-
# Pedir a un usuario tres numeros que seran dia, mes y año. Comprobar que la fecha introducida es valida
print('Introducir fecha en formato DD/MM/AAAA')
dia = int(input('Introducir dia: '))
mes = int(input('Introducir mes: '))
año = int(input('Introducir año: '))
if (mes == 0o4 or mes == 0o6 or mes == 9 or mes == 11) and dia > 30:
    print(f'La fecha introducida: {dia}/{mes}/{año} Es incorrecta')
elif mes == 0o2 and dia > 28:
    print(f'La fecha introducida: {dia}/{mes}/{año} Es incorrecta')
elif dia > 31 or dia < 0o1 or mes > 12 or mes < 0o1 or año < 1000:
     print(f'La fecha introducida: {dia}/{mes}/{año} Es incorrecta')
else:
    print(f'La fecha introducida: {dia}/{mes}/{año} Es correcta')
