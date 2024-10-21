compstr = input('Introduce tu lista de la compra separado por una coma (Ej. patata, aceite, verdura): ')
comp = compstr.split(', ')
for i in comp:
    print(i)
