nombre = input('Introduce tu nombre: ')
minus = nombre.lower()
mayus = nombre.upper()
inip = nombre.split(' ')
ini = []
for i in inip:
    ini.append(list(i)[0])

inic = "".join(ini).upper()
print(f'Tu nombre en minúsculas: {minus}\nTu nombre en mayúsculas: {mayus}\nTus iniciales en mayusculas son: {inic}')