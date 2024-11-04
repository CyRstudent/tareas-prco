notastr = input('Introduce las notas de tus 3 parciales y el examen final separados por comas (Ej. 10, 8, 3): ').split(', ') #Separamos cada elemento por comas
notas = []
media = 0
for i in notastr: #Este loop sirve para convertir cada nota a un número decimal
    n = int(i)
    if (n<0) or (n>10): #Si la nota no está comprendida entre 0 y 10...
        print('Introduce a la proxima notas validas')
        exit()
    else:
        notas.append(int(i))

for j in range(len(notas)): #Cogemos el indice de cada elemento de la lista
    if j == (len(notas)-1): #Si es el último elemento de la lista (AKA el examen final...)
        media += (0.4*notas[j]) #Lo multiplicamos por 0.4
    else: #Es decir, si es un parcial...
        media += (0.2*notas[j]) #Lo multiplicamos por 0.2
msg = 'Tu nota está clasificada como '
media = round(media) #Redondeamos la media a un número entero
match media:
    case media if media >= 9:
        print(msg + 'Sobresaliente')
    case media if media in [7, 8]:
        print(msg + 'Notable')
    case media if media == 6:
        print(msg + 'Bien')
    case media if media == 5:
        print(msg + 'Suficiente')
    case _:
        print(msg + 'Suspenso')