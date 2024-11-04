pssw = input('Introduce una contraseña: ')
pssw = list(pssw)
espacios = 0
let_min = 0
let_may = 0
num = 0
def check_char(char: str):
    global let_min, let_may, espacios, num
    if char.islower():
        let_min += 1
    elif char.isupper():
        let_may += 1
    elif char.isspace():
        espacios += 1
    elif char.isnumeric():
        num += 1

for char in pssw:
    check_char(char)

errores = []
if len(pssw) < 8:
    errores.append(f'Tu contraseña tiene {len(pssw)} carácteres, mientras que el mínimo son 8 carácteres')
if let_may == 0:
    errores.append(f'Tu contraseña no tiene mayusculas, y debes de poner al menos una')
if let_min == 0:
    errores.append(f'Tu contraseña no tiene minusculas, y debes de poner al menos una')
if espacios > 0:
    errores.append(f'Tu contraseña tiene {espacios} espacios, mientras que no debe de tener ninguno')
if num == 0:
    errores.append(f'Tu contraseña no tiene números, y debes de poner al menos uno')

if len(errores) == 0:
    print('¡Bien hecho! Tu contraseña no tiene error alguno')
else:
    print('Tu contraseña presenta los siguientes errores: ')
    for error in errores:
        print(f'\t•{error}')
    print('Por favor, corrige tu contraseña')
