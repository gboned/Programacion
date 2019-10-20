# Garbiñe Boned -P5E9-
# Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje
ancho = int(input('Introduce la anchura del rectangulo: '))
alto = int(input('Introduce la altura del rectangulo: '))
dibujo = '*'
espacio = ' '
if ancho != alto:
    for i in range(alto):
        if i == 0 or i == (alto - 1):
            print(dibujo * ancho)
        else:
            print(dibujo + espacio * (ancho -2) + dibujo)
else:
    print('La altura y anchura de un rectangulo NO pueden ser iguales')