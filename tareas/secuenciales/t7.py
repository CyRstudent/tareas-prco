barrapandura = int(input('Introduce el número de barras vendidas que no son del día: '))
print('El coste de una barra de pan normal es de 3.49€ y se le hace un descuento del 60% por no ser fresca')
preciopanduro = 3.49 * 0.4 #Si queremos ver el precio cuyo descuento es del 60%, el precio será el (100-60)% del precio original
preciofinal = barrapandura * preciopanduro
print(f'El coste total por {barrapandura} barras no frescas es {preciofinal}€')