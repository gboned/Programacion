# Garbiñe Boned -P4E3-
# Pedir si quiere calcular area de triangulo o cuadrado, pedir datos segun caso y mostrar resultado
print('Para calcular area de triangulo, escribe T'+'\n' + 'Para calcular area del cuadrado, escribe C')
calcular_area = str(input('Introduce una opción: '))
if calcular_area == 'T':
    base = float(input('Introduce la base del triangulo: '))
    altura = float(input('Introduce la altura del triangulo: '))
    area_triangulo = (base*altura)/2
    print(area_triangulo)
elif calcular_area == 'C':
    lado = float(input('Introduce el lado del cuadrado: '))
    area_cuadrado = lado**2
    print(area_cuadrado)
else:
    print('La letra', calcular_area, 'no es correcta, escribe T o C, respetando las mayusculas')