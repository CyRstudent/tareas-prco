sueldo = float(input('Introduce el salario en €/hora: ')) #El salario es de tipo decimal
horas_dias = [] #Esta lista contiene las horas que trabaja cada día
for i in range(6): #Iteramos sobre los 6 dias de la semana
    h = float(input(f'Introduce el nº de horas que ha trabajado el empleado el día nº {i+1} de la semana: ')) #Duh
    horas_dias.append(h) #Añadimos las horas a la lista

sum = 0 #La suma de todas las horas de la semana
for dia in horas_dias: #Por las horas de cada día...
    sum += dia #Se las sumamos al total

paga = sum * sueldo #La paga es el nº de horas trabajadas por el sueldo

print(f'Su empleado ha trabajado durante {sum} horas en total, siendo así su paga de {paga}€')