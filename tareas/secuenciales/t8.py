nombre = input('Introduce tu nombre: ')
minus = nombre.lower() #Devuelve el nombre completo en minusculas
mayus = nombre.upper() #Devuelve el nombre completo en mayusculas
nomaps = nombre.split(' ') #Separamos el nombre completo en nombre y apellidos
resfin = [] #Esta es la lista que contendrá el nombre y apellido escritos con la primera letra en mayuscula y las otras en minuscula
for nom in nomaps: #Por cada nombre que está en la lista de nombre y apellidos...
    nom = nom.title() #Será igual al nombre, pero con la primera letra en mayuscula y las otras en minusculas
    resfin.append(nom) #Y finalmente, lo metemos en la lista del resultado final
res = ' '.join(resfin) #El resultado será el nombre y los dos apellidos separados por comas en una sola cadena
print(f'Tu nombre en minúsculas: {minus}\nTu nombre en mayúsculas: {mayus}\nTu nombre con las iniciales en mayusculas: {res}')