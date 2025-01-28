#MIRAR LA DEFINICIÓN DE FACTORIAL
n = int(input('Introduce el número al cual quieres hacerle el factorial: '))
res = 1 #El resultado total
while n != 1: #Mientras que n sea distinto de 1...
    res *= n #Lo multiplicamos por el resultado
    n -= 1 #Y le restamos 1
print(f'El resultado del factorial es: {res}')