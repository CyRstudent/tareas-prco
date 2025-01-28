# Empezemos por definir una función que nos permita saber si un número es primo o no.
# Un número es primo si y solo si tiene 2 divisores: El 1, y el mismo número
# Para comprobar el número de divisores, usaremos la función matemática de módulo:
def check_primo(n: int): #n es de tipo int (número entero)
    test = 0 #El número de divisores que tiene el número
    for j in range(n): #Iteramos sobre el número
        if (n%(j+1)) == 0: #Si el resto de n entre j+1 (porque empezamos a contar desde 0) es 0...
            test += 1 #Es un divisor de n
    return (test==2) #Devolvemos si el número es primo o no (True o False)

n = int(input('Introduce un número para comprobar si es primo: ')) #Le pedimos el número
res = check_primo(n) #Comprobamos si es primo
if res: #Si es primo...
    print(f'El número {n} es primo')
else: #Si no..
    print(f'El número {n} no es primo')