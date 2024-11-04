pal = input('Introduce la palabra a comprobar: ')
revpal = pal[::-1] #La palabra al reves
if pal == revpal: #Si son la misma...
    print(f'La palabra {pal} es un palindromo')
else:
    print(f'La palabra {pal} no es un palindromo, y su reverso es: {revpal}')