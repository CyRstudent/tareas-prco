fnaci = input('Introduce tu fecha de nacimiento en el formato dd/mm/aaaa: ')
fnaci = fnaci.split('/') #Separamos cada cosa con la barra
print(f'Dia: {fnaci[0]}\nMes: {fnaci[1]}\nAño: {fnaci[2]}')