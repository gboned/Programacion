# Garbiñe Boned -P4E1-
# Precio de un producto y nombre del producto y mostrar mensaje con el precio del IVA (21%)
nombre_producto = input('Introduce el nombre del producto: ')
precio_producto = float(input('Introduce el precio del producto: '))
iva_producto = (precio_producto * 0.21) + precio_producto
print(f'Tu {nombre_producto} cuesta {precio_producto} euros y con el 21% de IVA se queda en {iva_producto} euros en total')