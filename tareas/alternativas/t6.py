precio = float(input('Introduce el precio inicial del kilo de la uva en euros: '))
prec_original = precio
tipo = input('Introduce el tipo de uva (A o B): ')
tamaño = input('Introduce el tamaño de la uva (1 o 2): ')
kilos = float(input('Introduce los kilos de uva: '))

if tipo == 'A':
    if tamaño == '1':
        precio += 0.2
    elif tamaño == '2':
        precio += 0.3
elif tipo == 'B':
    if tamaño == '1':
        precio -= 0.3
    elif tamaño == '2':
        precio -= 0.5

ganancias = kilos*precio
base = kilos*prec_original
neto = ganancias - base
print(f'Las ganancias obtenidas son de {str(neto)}€')