a = float(input('Introduce la longitud del primer cateto: '))
b = float(input('Introduce la longitud del segundo cateto: '))
c = float(input('Introduce la longitud de la hipotenusa: '))
if ((a**2)+(b**2))==(c**2):
    print('El triangulo es rectángulo, ya que cumple el teorema de pitagoras')
if a==b or b==c or a==c:
    if a==b==c:
        print('El triangulo es equilátero')
    else:
        print('El triangulo es isósceles')
else:
    print('El triangulo es escaleno')