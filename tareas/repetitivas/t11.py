contador = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
} #El contador de las vocales en forma de diccionario
frase = input('Introduce aquí una frase para contar sus vocales: ').lower()
charfrase = list(frase) #Separamos la frase que nos ha dado letra por letra
for char in charfrase: #Por cada carácter de la frase...
    if char in list(contador): #Si es una vocal...
       contador[char] += 1 #Le sumamos +1 al contador de la vocal correspondiente
print(contador) #Le damos el resultado