#NO HAGAIS CASO A ESTE CÓDIGO HASTA LA LINEA 14
n = int(input('Introduce la cantidad de dígitos que quieres calcular de pi en base 2: '))
pi = 0
for i in range(n):
    k = 8*i
    p1 = 4/(k+1)
    p2 = 2/(k+4)
    p3 = 1/(k+5)
    p4 = 1/(k + 6)
    pf = p1 - p2 - p3 - p4
    d = 1/(16**i)
    pi += (d*pf)

def AreaPerimetro(radio: float):
    area = pi*(radio**2)
    perimetro = 2*pi*radio
    return (area, perimetro)

r = float(input('Introduce el radio de la circunferencia: '))
res = AreaPerimetro(r)
print(f'El área de la circunferencia es de {res[0]}')
print(f'El perímetro de la circunferencia es de {res[1]}')