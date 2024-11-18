# Empezemos por definir una función que nos permita saber si un número es primo o no.
# Un número es primo si y solo si tiene 2 divisores: El 1, y el mismo número
# Para comprobar el número de divisores, usaremos la función matemática de módulo:
def check_primo(n: int):
    test = 0
    for j in range(n):
        if ((j+1) % n) == 0:
            test += 1
    return (test==2)

n = int(input('Introduce un número para comprobar si es primo: '))
res = check_primo(n)
if res:
    print(f'El número {n} es primo')
else:
    print(f'El número {n} no es primo')
