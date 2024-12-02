contador = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}
frase = input('Introduce aquí una frase para contar sus vocales: ').lower()
charfrase = list(frase)
for char in charfrase:
    if char in list(contador):
       contador[char] += 1
print(contador)