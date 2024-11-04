nombre = input('Introduce tu nombre: ')
minus = nombre.lower()
mayus = nombre.upper()
nomaps = nombre.split(' ')
resfin = []
for nom in nomaps:
    nom = nom.title()
    resfin.append(nom)
res = ' '.join(resfin)
print(f'Tu nombre en minúsculas: {minus}\nTu nombre en mayúsculas: {mayus}\nTu nombre con las iniciales en mayusculas: {res}')