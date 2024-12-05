dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'] #Los días de la semana en orden

n_em = int(input('Introduce el número de empleados'))
salario = float(input('Introduce el salario en €/hora: '))

horas = 0 #Estas son las horas que ha trabajado un empleado en toda la semana
for i in range(7): #Repetimos 7 veces...
    ans = input(f'Ha trabajado su empleado el {dias[i]}?: (S/N) ').lower() #Si el empleado ha trabajado ese mismo día...
    if ans == 's':
        h = int(input(f'Introduce el número de horas trabajadas el {dias[i]}: ')) #Le añadimos las horas que haya trabajado en el correspondiente día de la semana
        horas += h #Se lo sumamos al total de horas

t = salario * horas #La nómina semanal será el salario por las horas
    
print(f'Sueldo semanal del empleado: {t}')
print(f'Lo que pagará tu empresa por todos los empleados: {t*n_em}') #Lo que pagará la empresa por todos los empleados en una semana