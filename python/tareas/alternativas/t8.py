tipo = input('Introduce qué tipo de cliente eres (Regular, Oro, Platino): ').lower() #A prueba de tontos
importe = float(input('Introduce el importe de tu compra en €: '))
match tipo:
    case 'regular':
        importe *= 0.95
    case 'oro':
        importe *= 0.9
    case 'platino':
        importe *= 0.85
    case _:
        print('Por favor, introduce un tipo de cliente válido')
        exit()
print(f'Su importe de compra con el descuento aplicado es {importe}€')