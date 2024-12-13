dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'] #Los días de la semana en orden

n_em = int(input('Introduce el número de empleados'))
salario = float(input('Introduce el salario en €/hora: '))
horas_trabajadores = []
for j in range(n_em):
    horas = 0 #Estas son las horas que ha trabajado un empleado en toda la semana
    for i in range(7): #Repetimos 7 veces...
        ans = input(f'Ha trabajado su empleado nº{j+1} el {dias[i]}?: (S/N) ').lower() #Si el empleado ha trabajado ese mismo día...
        if ans == 's':
            h = int(input(f'Introduce el número de horas trabajadas el {dias[i]}: ')) #Le añadimos las horas que haya trabajado en el correspondiente día de la semana
            horas += h #Se lo sumamos al total de horas
    horas_trabajadores.append(horas)
t = sum(horas_trabajadores)
for h in range(n_em):
    print(f'Sueldo del empleado nº{h+1}: {salario * horas_trabajadores[h]}')
print(f'Lo que pagará tu empresa por todos los empleados: {t*salario}') #Lo que pagará la empresa por todos los empleados en una semana