import subprocess
import os
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')
print("""
 /$$$$$$$$                                                               /$$                           /$$                          
|__  $$__/                                                              | $$                          | $$                          
   | $$  /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$        /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
   | $$ |____  $$ /$$__  $$/$$__  $$ |____  $$ /$$_____//$$$$$$/$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
   | $$  /$$$$$$$| $$  \\__/ $$$$$$$$  /$$$$$$$|  $$$$$$|______/ $$      | $$  \\ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \\__/
   | $$ /$$__  $$| $$     | $$_____/ /$$__  $$ \\____  $$      | $$      | $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
   | $$|  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$ /$$$$$$$/      |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \\  $$|  $$$$$$$| $$      
   |__/ \\_______/|__/      \\_______/ \\_______/|_______/        \\_______/|__/  |__/ \\_______/ \\_______/|__/  \\__/ \\_______/|__/      
""")
opt_text = '''Estas son las opciones que tienes:
    • 'opciones': Muestra este mismo texto
    • 'ayuda': Muestra como usar el programa
    • 'run': Ejecuta el programa
    • 'salir': Sal del programa
'''

def listopt(lmes: str ): #lmes: Last message - El mensaje que se pone abajo del todo
    toret = input(f'{opt_text}{lmes}: ').lower()
    return toret

opt = listopt('Introduce una opción')
while True:
    match opt:
        case 'opciones':
            opt = listopt('Si necesitas más información, usa el comando \'ayuda\'\nIntroduce una opción de nuevo: ')
            pass
        case 'ayuda':
            webbrowser.open('https://github.com/CyRstudent/tareas-prco?tab=readme-ov-file#check_tareaspy')
            pass
        case 'run':
            listdir = [] #La lista de carpetas que va introduciendo
            namecarp = input('Introduce la primera carpeta a escanear: ')
            while namecarp:
                listdir.append(namecarp)
                tolist = '/'.join(listdir)
                res = os.listdir(f'./{tolist}')
                for fil in res:
                    print(fil)
                namecarp = input('Si este es el directorio con los archivos de python, pulsa Enter. Si no, introduce la carpeta a escanear: ')
            updir = '/'.join(listdir)
            dir = os.listdir(f'./{updir}')
            testallopt = input('¿Quieres escanear TODOS los archivos sin parar? (S/N): ').upper()
            filerror = []
            for file in dir:
                if testallopt =='S':
                    print(f'Ejecutando el archivo: {file}...\n')
                    execf = subprocess.run(['python', f'./{updir}/{file}'])
                    if execf.returncode != 0:
                        filerror.append([file, execf.returncode])
                    else:
                        print('Código ejecutado con éxito')
                else:
                    runopt = input(f'El archivo que se va a ejecutar ahora es: {file}; ¿Deseas ejecutarlo? (S/N, o pulsa Enter si quieres ejecutarlo): ').upper()
                    if runopt != 'N':
                        print(f'Ejecutando el archivo: {file}...\n')
                        execf = subprocess.run(['python', f'./{updir}/{file}'])
                        if execf.returncode != 0:
                            filerror.append([file, execf.returncode])
                        else:
                            print('Código ejecutado con éxito')
                    else:
                        print(f'Archivo {file} omitido')
            if len(filerror) > 0:
                print('Has tenido errores con algun(os) archivos. Aquí tienes el nombre, y su código devuelto')
                for error in filerror:
                    print(f'\t•{error}')
            print('¡Ejecución de los códigos terminada!')
            pass
        case 'salir':
            print('¡Hasta luego!')
            exit()
    opt = listopt('Introduce una opción nuevamente: ')