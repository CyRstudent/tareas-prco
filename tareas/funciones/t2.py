def EsMultiplo(n1: int, n2: int):
    return ((n1%n2 == 0) or (n2%n1 == 0))

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número'))
if EsMultiplo(num1, num2):
    print('El número es múltiplo del otro')
else:
    print('El número no es múltiplo del otro')