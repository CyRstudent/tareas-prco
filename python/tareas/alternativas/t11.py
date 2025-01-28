saldo = float(input('Introduce tu saldo inicial (Ej. 43.23): ')) #El usuario introduce el saldo inicial y nosotros lo convertimos a un número decimal
opt = input('Estas son las opciones disponibles:\n\t•\'retiro\': Retira una cantidad de saldo\n\t•\'deposito\': Deposita una cantidad de saldo\n\t•\'consulta\': Consulta tu saldo\n\t•\'salir\': Sal del programa\n\t•\'ayuda\': Vé de nuevo las opciones\nIntroduce aquí tu opción: ')
while True: #Hasta que no rompamos el loop...
    opt = opt.lower() #A prueba de tontos
    match opt: #Vemos a que opción se asemeja lo que puso el usuario
        case 'retiro':
            n = float(input('Introduce la cantidad de dinero a sacar: '))
            if n > saldo: #Si el usuario quiere sacar más dinero del que tiene...
                print(f'¡No puedes sacar más dinero del que tienes! Necesitas al menos {n-saldo}€ más para poder sacar esa cantidad de dinero')
            else:
                saldo = saldo - n
                print(f'¡Operación realizada con éxito! Has sacado {n}€, quedando tu saldo en {saldo}€')
            pass #Ejecuta la linea 32 del código
        case 'deposito':
            n = float(input('Introduce la cantidad de dinero a depositar: '))
            saldo = saldo + n
            print(f'¡Operación realizada con éxito! Has depositado {n}€, quedando tu saldo en {saldo}€')
            pass
        case 'consulta':
            print(f'Tu saldo total es de {saldo}€')
            pass
        case 'salir':
            print('¡Hasta luego!')
            exit() #Dejamos de ejecutar el código
            break
        case 'ayuda':
            print('"retiro" para retirar dinero, "deposito" para depositar dinero, "consulta" para consultar tu saldo, "salir" para salir del programa, "ayuda" para mostrar este mensaje de nuevo')
            pass
        case _: #Si no ha puesto ninguna opción valida...
            print('No has introducido una opción válida. Por favor, intentelo de nuevo')
            pass
    opt = input('Introduce una nueva opción, o introduce \'ayuda\' si necesitas verlas de nuevo: ')