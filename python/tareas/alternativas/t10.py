pssw = input('Introduce una contraseña: ') #Introducimos la contraseña
pssw = list(pssw) #Convertimos la contraseña en una lista conteniendo cada caracter
#Este es el recuento de tipo de carácteres
espacios = 0
let_min = 0 #Letras minusculas
let_may = 0 #Letras mayusculas
num = 0 #Números
def check_char(char: str): #Definimos la función check_char (comprobar caracter), que tendrá un parametro cuyo tipo es una string
    global let_min, let_may, espacios, num #Con la palabra global, podremos acceder a las variables de afuera de la función
    if char.islower(): #Si el caracter es minuscula...
        let_min += 1
    elif char.isupper():
        let_may += 1
    elif char.isspace():
        espacios += 1
    elif char.isnumeric():
        num += 1

for char in pssw: #Una vez terminada de definir la función, cogemos cada elemento de la lista pssw, que contiene cada carácter de la contraseña
    check_char(char) #Pasamos la función por cada caracter

errores = [] #Esta son la lista de errores, así nos ahorramos más código
if len(pssw) < 8: #Si la longitud de la contraseña es menor que 8...
    errores.append(f'Tu contraseña tiene {len(pssw)} carácteres, mientras que el mínimo son 8 carácteres')
if let_may == 0: #Si no hay mayusculas...
    errores.append(f'Tu contraseña no tiene mayusculas, y debes de poner al menos una')
if let_min == 0: #Si no hay minusculas...
    errores.append(f'Tu contraseña no tiene minusculas, y debes de poner al menos una')
if espacios > 0: #Si hay espacios...
    errores.append(f'Tu contraseña tiene {espacios} espacios, mientras que no debe de tener ninguno')
if num == 0: #Si no hay números...
    errores.append(f'Tu contraseña no tiene números, y debes de poner al menos uno')

if len(errores) == 0: #Si no hay errores...
    print('¡Bien hecho! Tu contraseña no tiene error alguno')
else: #Si hay errores...
    print('Tu contraseña presenta los siguientes errores: ')
    for error in errores: #Por cada error...
        print(f'\t•{error}') #Lo imprimimos en una linea distinta con un espacio
    print('Por favor, corrige tu contraseña') #Y finalmente, le decimos al usuario que la corrija
