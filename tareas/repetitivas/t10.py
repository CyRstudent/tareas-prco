dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

n_em = int(input('Introduce el número de empleados'))
salario = float(input('Introduce el salario en €/hora: '))

horas = 0
for i in range(7):
    ans = input(f'Ha trabajado su empleado el {dias[i]}?: (S/N) ').lower()
    if ans == 's':
        h = int(input(f'Introduce el número de horas trabajadas el {dias[i]}: '))
        horas += h

t = salario * horas
    
print(f'Sueldo semanal del empleado: {t}')
print(f'Lo que pagará tu empresa por todos los empleados: {t*n_em}')