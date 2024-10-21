nota = float(input('Introduce una nota: '))
edad = int(input('Introduce una edad: '))
sexo = input('Introduce tu sexo (F o M): ').upper()

if nota>=5 and edad>=18:
    if sexo=='F':
        print('ACEPTADA')
    else:
        print('POSIBLE')
else:
    print('NO ACEPTADA')