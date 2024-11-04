precio = float(input('Introduce el precio inicial del kilo de la uva en euros: ')) #El usuario introduce el precio, y nosotros lo convertimos a un número decimal
prec_original = precio #Declaramos la variable prec_original, una copia de precio, pero que no va a variar
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

ganancias = kilos*precio #Estas son las ganancias con el precio variado
base = kilos*prec_original #Estas son las ganancias con el precio original
neto = ganancias - base #Esta es la diferencia de precio
print(f'Las ganancias obtenidas son de {str(neto)}€')