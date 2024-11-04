#Introducimos los datos con decimales
peso = float(input('Introduce tu peso en kilos: '))
estatura = float(input('Introduce tu estatura en metros: '))
imc = peso / (estatura**2)
imc = round(imc, 2) #Redondeamos el indice de masa corporal a 2 dígitos decimales
print(f'Tu índice de masa corporal es {imc}')