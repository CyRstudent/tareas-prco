compstr = input('Introduce tu lista de la compra separado por una coma (Ej. patata, aceite, verdura): ') #Le pedimos al usuario su lista de la compra
comp = compstr.split(', ') #Convertimos la lista de la compra en una lista
for i in comp: #Por cada elemento de la lista de la compra...
    print(i) #Lo imprimimos