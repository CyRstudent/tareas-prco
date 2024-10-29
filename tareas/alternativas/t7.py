alm = int(input('Introduce el número de alumnos que van a ir al viaje: '))
precio = 0
match alm:
    case alm if alm >= 100:
        precio += 65*alm
    case alm if alm >= 50 and alm <= 99:
        precio += 70*alm
    case alm if alm >= 30 and alm <= 49:
        precio += 95*alm
    case alm if alm < 30:
        precio += 4000

print(f'El precio por alumno es de {precio/alm}€, dando un total de {precio}€')