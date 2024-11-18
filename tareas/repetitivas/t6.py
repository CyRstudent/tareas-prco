nran = int(input('Introduce la cantidad de números a introducir'))
n_arr = []
for j in range(nran):
    n_intr = float(input(f'Introduce el número {j+1}: '))
    n_arr.append(n_intr)

may = 0
men = 0
igual = 0
for n in n_arr:
    if n > 0:
        may += 1
    elif n < 0:
        men += 1
    else:
        igual += 1
print(f'Números mayores que 0: {may}')
print(f'Números menores que 0: {men}')
print(f'Números iguales que 0: {igual}')