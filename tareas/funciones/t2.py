def EsMultiplo(n1: int, n2: int): #Definimos una función que nos devuelve si un número es múltiplo del otro y viceversa
    return ((n1%n2 == 0) or (n2%n1 == 0)) #Mirar definición de módulo

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número'))
if EsMultiplo(num1, num2): #Si la función nos devuelve True...
    print('El número es múltiplo del otro')
else:
    print('El número no es múltiplo del otro')