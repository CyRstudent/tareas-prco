intentos = 0
def Login(usuario: str, contraseña: str):
    return ((usuario == 'usuario1') and (contraseña == 'asdasd'))

while intentos < 3:
    u = input('Introduce un usuario: ')
    c = input('Introduce una contraseña: ')
    res = Login(u, c)
    if res:
        break
    else:
        intentos += 1
        print('El usuario o la contraseña son incorrectos. Intentalo de nuevo')

if intentos == 3:
    print('Has gastado 3 intentos. No has conseeguido entrar')
else:
    print(f'¡Has conseguido entrar!')