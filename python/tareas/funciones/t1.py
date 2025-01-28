def tempmed(min: float, max: float): #Definimos la función temperatura media donde ambas temperaturas introducidas son un número decimal
    res = (max + min)/2 #La media
    return res #Se la devolvemos

n = int(input('Introduce el número de dias: '))
for i in range(n): #Repetimos el número de días que nos ha introducido el usuario
    print(f'Calculando la temperatura media del día {i+1}...')
    min = float(input('Introduce la temperatura mínima del día: '))
    max = float(input('Introduce la temperatura máxima del día: '))
    res = tempmed(min, max) #Cogemos la función que nos dará la temperatura media
    print(f'Temperatura media del día {i+1}: {res}')
