notastr = input('Introduce las notas de tus 3 parciales y el examen final separados por comas (Ej. 10, 8, 3): ').split(', ')
notas = []
media = 0
for i in notastr:
    n = int(i)
    if (n<0) or (n>10):
        print('Introduce a la proxima notas validas')
        exit()
    else:
        notas.append(int(i))

for j in range(len(notas)):
    if j == (len(notas)-1):
        media += (0.4*notas[j])
    else:
        media += (0.2*notas[j])
msg = 'Tu nota está clasificada como '
media = round(media)
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