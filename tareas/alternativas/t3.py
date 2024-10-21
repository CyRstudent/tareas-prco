base = float(input('Introduce una base: '))
exponente = abs(float(input('Introduce un exponente: ')))
res = base**exponente
if exponente > 0:
    print(res)
elif exponente < 0:
    print(1/res)
else:
    print(1)