import random #Importamos el módulo "random"
incognita = random.randint(1, 100) #Escogemos una incógnita que está entre el 1 y el 100
ans = int(input('Introduce el número a adivinar: ')) #Le preguntamos el número a adivinar
x = 1 #El número de intentos (De por sí ya gastó uno)
while x <= 10 and ans != incognita: #Mientras que el número de intentos sea menor o igual que 10 O el intento no se corresponda con la incognita...
    strk = 'No has adivinado el número. El número que has introducido es '
    if ans > incognita:
        print(f'{strk}menor') #El número intento es menor que la incógnita
    else:
        print(f'{strk}mayor') #Duh
    ans = int(input('Introduce otro número a adivinar: ')) #Hacemos que introduzca otro número...
    x+=1 #Le contabilizamos un intento más

if ans != incognita: #Si de por sí ha agotado los 10 intentos, y el último ya ni era el número a adivinar, se lo decimos
    print(f'Has perdido. El número era {incognita}')
else: #Si no, ha ganado
    print(f'Has ganado. Has adivinado el número {incognita} con {x} intentos')