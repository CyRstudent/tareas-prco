#Introducimos los datos
nota = float(input('Introduce una nota: '))
edad = int(input('Introduce una edad: '))
sexo = input('Introduce tu sexo (F o M): ').upper() #A prueba de niños; Hacemos que el sexo sea si o si mayúscula

if nota>=5 and edad>=18: #Si la nota es un aprobado o más, y es mayor de edad...
    if sexo=='F': #Y encima de todo, tiene sexo femenino...
        print('ACEPTADA')
    else: #Si tiene sexo masculino...
        print('POSIBLE')
else: #Y si está suspenso o no es mayor de edad...
    print('NO ACEPTADA')