lim_inf = float(input('Itroduce el límite inferior de un intervalo: '))
lim_sup = float(input('Introduce el límite superior de un intervalo: '))
while lim_inf > lim_sup: #Si el límite inferior es mayor que el superior, literalmente no tiene sentido
    lim_inf = float(input('El límite inferior de un intervalo no puede ser mayor que el mayor de este. Introduce uno válido: '))
n_arr = [] #Esta es la lista que contendrá los números
def preg_n(): #Definimos esta función que básicamente nos devuelve los números que introduzca el usuario. No es necesaria hacerla, yo la hice por pereza a tener que estár repitiendola
    tr = float(input('Introduce un número (0 si quieres terminar la operación): '))
    return tr
n = preg_n()
fuera = 0 #La cantidad de números que están fuera del intervalo
borde = 0 #La cantidad de números que son los bordes del intervalo
while n != 0: #Mientras que el usuario no introduzca 0...
    if (n > lim_inf) and (n < lim_sup): #Si el número está dentro del intervalo...
        n_arr.append(n) #Pos lo añadimos
    elif n == lim_inf or n == lim_sup: #O si no, si concide con los bordes...
        borde += 1 #Lo contamos
    else: #Y ya, si no cumple ninguna de estas condiciones (es decir,  el número no pertenece al intervalo)...
        fuera += 1 #Lo contamos
    n = preg_n() #Para darle sentido al bucle, pedimos el número de nuevo
sum = 0 #La suma de todos los números introducidos en la lista
for nir in n_arr: #Por cada número en la lista...
    sum += nir #Lo sumamos a la suma total

print(f'La suma de los números que has introducido pertenecientes al intervalo es {sum}')
print(f'Has introducido {fuera} números no pertenecientes al intervalo')
if borde > 0:
    print(f'Has introducido {borde} números que coinciden con los extremos del intervalo')