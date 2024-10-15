nombre = list(input('Introduce tu nombre: '))
apellidos = input('Introduce tus 2 apellidos separados por un espacio: ').split(' ')
ap1 = list(apellidos[0])
ap2 = list(apellidos[1])

iniciales = nombre[0] + ap1[0] + ap2[0]

print(f'Tus iniciales son {iniciales}')