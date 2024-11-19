sueldo = float(input('Introduce el salario en €/hora: '))
horas_dias = []
for i in range(6):
    h = float(input(f'Introduce el nº de horas que ha trabajado el empleado el día nº {i+1} de la semana: '))
    horas_dias.append(h)

sum = 0
for dia in horas_dias:
    sum += dia

paga = sum * sueldo

print(f'Su empleado ha trabajado durante {sum} horas en total, siendo así su paga de {paga}€')