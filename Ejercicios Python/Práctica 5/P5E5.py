# Garbiñe Boned -P5E5-
# Pedir altura y anchura de un rectangulo, y dibujarlo con asteriscos
ancho = int(input('Introduce anchura del rectangulo: '))
alto = int(input('Introduce altura del rectangulo: '))
dibujo = '*'
if ancho != alto:
    for i in range(alto):
        print(dibujo * ancho)
else:
    print('La altura y anchura de un rectangulo NO pueden ser iguales')