# Garbiñe Boned -P5E6-
# Programa que pida altura del triangulo y lo dibuje con asteriscos.
altura = int(input('Introduce la altura del triangulo: '))
dibujo = '*'
for i in range(altura, 0, -1):
    print(i * dibujo)