char = input('Introduce un caracter: ').lower() #A prueba de tontos, le pedimos al usuario un caracter y lo convertimos en minuscula
vocales = ['a', 'e', 'i', 'o', 'u'] #Lista de las vocales
while True: #Por siempre...
    if char == ' ': #Si no introduce un caracter...
        exit() #Salimos del programa
    elif char in vocales: #Si introduce un caracter que pertenezca a la lista de las vocales...
        print('VOCAL') #Vocal
    else: #Y ya si no cumple ninguna de estas condiciones, por defecto, es una consonante
        print('NO VOCAL')
    char = input('Introduce otro caracter: ').lower() #Finalment, pedimos que introduzca otro caracter, dandole sentido al loop