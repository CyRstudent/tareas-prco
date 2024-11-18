lim_inf = float(input('Itroduce el límite inferior de un intervalo: '))
lim_sup = float(input('Introduce el límite superior de un intervalo: '))
while lim_inf > lim_sup:
    lim_inf = float(input('El límite inferior de un intervalo no puede ser mayor que el mayor de este. Introduce uno válido: '))
n_arr = []
def preg_n():
    tr = float(input('Introduce un número (0 si quieres terminar la operación): '))
    return tr
n = preg_n()
fuera = 0
borde = 0
while n != 0:
    if (n > lim_inf) and (n < lim_sup):
        n_arr.append(n)
    elif n == lim_inf or n == lim_sup:
        borde += 1
    else:
        fuera += 1
    n = preg_n()
sum = 0
for nir in n_arr:
    sum += nir

print(f'La suma de los números que has introducido pertenecientes al intervalo es {sum}')
print(f'Has introducido {fuera} números no pertenecientes al intervalo')
if borde > 0:
    print(f'Has introducido {borde} números que coinciden con los extremos del intervalo')