nran = int(input('Introduce la cantidad de números a introducir'))
n_arr = [] #La lista de números
for j in range(nran): #Iteramos el número de veces que se nos ha pedido
    n_intr = float(input(f'Introduce el número {j+1}: ')) #Pongo j+1 porque se empieza a contar desde 0
    n_arr.append(n_intr) #Lo metemos en la lista

may = 0 #Números mayores de 0
men = 0 #Números menores de 0
igual = 0 #Números que son 0
for n in n_arr: #Por cada número que haya introducido el usuario, comprobamos qué tipo es
    if n > 0:
        may += 1
    elif n < 0:
        men += 1
    else:
        igual += 1
print(f'Números mayores que 0: {may}')
print(f'Números menores que 0: {men}')
print(f'Números iguales que 0: {igual}')