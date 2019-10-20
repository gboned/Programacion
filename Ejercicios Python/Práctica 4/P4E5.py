# Garbiñe Boned -P4E5-
# Pedir un importe en euros y decir si el cajero le puede dar ese importe usando el mismo billete y el más grande
# Billetes disponibles 5, 10, 20, 50, 100, 200, 500
# numero_billetes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
euros = int(input('¿Cuánto dinero quieres retirar del cajero? (Hasta 500 euros): '))
if euros % 500 == 0:
    num_billetes = euros / 500
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 200 == 0:
    num_billetes = euros / 200
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 100 == 0:
    num_billetes = euros / 100
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 50 == 0:
    num_billetes = euros / 50
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 20 == 0:
    num_billetes = euros / 20
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 10 == 0:
    num_billetes = euros / 10
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
elif euros % 5 == 0:
    num_billetes = euros / 5
    print('El cajero te devuelve', num_billetes, 'billete(s) de', euros/num_billetes, 'euros')
else:
    print(f'No es posible que te devuelva esa cantidad')