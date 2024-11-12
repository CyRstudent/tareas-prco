import random
incognita = random.randint(1, 100)
ans = int(input('Introduce el número a adivinar: '))
x = 1
while x <= 10 and ans != incognita:
    strk = 'No has adivinado el número. El número que has introducido es '
    if ans > incognita:
        print(f'{strk}menor')
    else:
        print(f'{strk}mayor')
    ans = int(input('Introduce otro número a adivinar: '))
    x+=1

if ans != incognita:
    print(f'Has perdido. El número era {incognita}')
else:
    print(f'Has ganado. Has adivinado el número {incognita} con {x} intentos')