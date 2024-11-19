n = int(input('Introduce un número: ')) #Ni voy a explicar esto
arr = [] #Esta es la lista que contendrá todos los números
while n != 0: #Mientras que n sea distinto de cero
    arr.append(n) #Introducimos el número en la lista...
    n = int(input('Introduce otro número: ')) #Y preguntamos por otro

sum = 0 #Este número será la sumatoria de la lista

for num in arr: #Por cada número introducido en la lista...
    sum += num #Se lo sumamos a la variable de la sumatoria

print(f'La sumatoria de todos los números es {sum}')
med = sum/len(arr) #La media es la sumatoria de los números dividido entre la longitud de esta
print(f'La media de los números introducidos es {med}')