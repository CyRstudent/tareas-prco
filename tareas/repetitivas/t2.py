n = int(input('Introduce el número al cual quieres hacerle el factorial: '))
res = 1
while n != 1:
    res *= n
    n -= 1
print(f'El resultado del factorial es: {res}')