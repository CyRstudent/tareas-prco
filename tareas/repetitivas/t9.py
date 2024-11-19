cantidad = int(input('Introducir la cantidad de números que se van a introducir: '))
n_arr = []
iguales = 0
for j in range(cantidad):
    if j == 0:
        n = int(input('Introduce el número nº1: '))
        n_arr.append(n)
    else:
        b4_n = n_arr[j-1]
        n = int(input(f'Introduce el número nº{j+1}, distinto a {b4_n}: '))
        n_arr.append(n)
        if n == b4_n:
            iguales += 1
            print(f'¡{n} es igual que {b4_n}!')

if iguales > 0:
    print(f'Has repetido número {iguales} veces')
else:
    print('No has repetido número en ninguna ocasión')
