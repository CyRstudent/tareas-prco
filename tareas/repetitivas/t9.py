cantidad = int(input('Introducir la cantidad de números que se van a introducir: ')) #La cantidad de números a introducir
n_arr = [] #Los números introducidos
iguales = 0 #El contador de números iguales
for j in range(cantidad): #No creo que haga falta explicar esto. Si hace falta, decidmelo
    if j == 0: #Si es el primer número que va a introducir...
        n = int(input('Introduce el número nº1: ')) #Le preguntamos el 1er número tal cual, y lo añadimos a la lista
        n_arr.append(n)
    else: #Si no es el primer número...
        b4_n = n_arr[j-1] #Cogemos el número que ha introducido antes
        n = int(input(f'Introduce el número nº{j+1}, distinto a {b4_n}: ')) #Self-explanatory
        n_arr.append(n) #Lo añadimos a la lista
        if n == b4_n: #Si el número de antes es igual al que ha introducido ahora...
            iguales += 1 #Lo contamos...
            print(f'¡{n} es igual que {b4_n}!') #Y le decimos que es igual

if iguales > 0: #Si ha introducido algún número igual...
    print(f'Has repetido número {iguales} veces') #Pos se lo decimos
else:
    print('No has repetido número en ninguna ocasión') #Si no, se lo decimos también
