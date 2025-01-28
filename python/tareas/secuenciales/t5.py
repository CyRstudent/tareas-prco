nombre = list(input('Introduce tu nombre: ')) #El usuario introduce el nombre, y el programa convierte su nombre en una lista que contiene cada letra de su nombre
apellidos = input('Introduce tus 2 apellidos separados por un espacio: ').split(' ') #El usuario introduce los apellidos, y los convierte en una lista
#En la lista hay 2 apellidos; El primero está en la posición 0, y el segundo en la posición 1
ap1 = list(apellidos[0]) #Hacemos lo mismo que con el nombre; Lo separamos letra a letra
ap2 = list(apellidos[1])

iniciales = nombre[0] + ap1[0] + ap2[0] #Cogemos la primera letra de cada nombre y apellido, y las concatenamos en una única cadena

print(f'Tus iniciales son {iniciales}')