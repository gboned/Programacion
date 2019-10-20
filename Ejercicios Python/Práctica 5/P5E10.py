# Garbiñe Boned -P5E6-
# Programa que pida altura del triangulo y lo dibuje con asteriscos.
alto = int(input('Introduce la altura del triángulo: '))
dibujo = '*'
espacio = ' '
minima = 3

if not alto < minima:
    for i in range(alto):
        alto-=1
        print(espacio * (alto) + dibujo * (((i + 1) *2) -1))
else:
    print(f'La altura mímina permitida es {minima}')