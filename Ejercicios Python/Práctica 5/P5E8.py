# Garbiñe Boned -P5E8-
# Pedir anchura de triangulo y dibujarlo con asteriscos
anchura = int(input('Introduce anchura del triangulo: '))
dibujo = '*'
for i in range(1, anchura + 1):
    print(i * dibujo)
for i in range(anchura -1, 0, -1):
    print(i * dibujo)
