barrapandura = int(input('Introduce el número de barras vendidas que no son del día: '))
print('El coste de una barra de pan normal es de 3.49€ y se le hace un descuento del 60% por no ser fresca')
preciopanduro = 3.49 * 0.4
preciofinal = barrapandura * preciopanduro
print(f'El coste total por {barrapandura} barras no frescas es {preciofinal}')