base = float(input('Introduce una base: '))
exponente = float(input('Introduce un exponente: '))
absexp = abs(exponente)
res = base**absexp
if exponente > 0:
    print(res)
elif exponente < 0:
    print(1/res)
else:
    print(1)