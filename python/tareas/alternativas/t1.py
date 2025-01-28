#Este ejercicio es el mismo que el 11 de las secuenciales
pal = input('Introduce la palabra a comprobar: ')
revpal = pal[::-1]
if pal == revpal:
    print(f'La palabra {pal} es un palindromo')
else:
    print(f'La palabra {pal} no es un palindromo, y su reverso es: {revpal}')