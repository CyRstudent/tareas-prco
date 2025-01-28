intentos = 0 #El número de intentos
def Login(usuario: str, contraseña: str): #Definimos los 2 parámetros como cadenas
    return ((usuario == 'usuario1') and (contraseña == 'asdasd')) #Devolvemos el valor booleano que comprueba si los 2 valores son correctos

while intentos < 3: #Mientras que el usuario haya hecho menos de 3 intentos...
    u = input('Introduce un usuario: ') #u de usuario
    c = input('Introduce una contraseña: ') #c de contraseña
    res = Login(u, c) #El resultado es un valor booleano
    if res: #Si las credenciales son correctas...
        break #Salimos del bucle automáticamente
    else:
        intentos += 1 #Si no, le añadimos un intento más
        print('El usuario o la contraseña son incorrectos. Intentalo de nuevo')
#Cuando ya haya terminado el bucle...
if intentos == 3: #Si el bucle terminó porque ya se usaron los 3 intentos..
    print('Has gastado 3 intentos. No has conseeguido entrar')
else: #Si no, es porque puso las credenciales correctas
    print('¡Has conseguido entrar!')