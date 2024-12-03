def tempmed(min: float, max: float):
    res = (max + min)/2
    return res

n = int(input('Introduce el número de dias: '))
for i in range(n):
    print(f'Calculando la temperatura media del día {i+1}...')
    min = float(input('Introduce la temperatura mínima del día: '))
    max = float(input('Introduce la temperatura máxima del día: '))
    res = tempmed(min, max)
    print(f'Temperatura media del día {i+1}: {res}')
