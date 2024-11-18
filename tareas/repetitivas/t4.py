char = input('Introduce un caracter: ').lower()
vocales = ['a', 'e', 'i', 'o', 'u']
while True:
    if char == '':
        exit()
    elif char in vocales:
        print('VOCAL')
    else:
        print('NO VOCAL')
    char = input('Introduce otro caracter: ').lower()