numstr = input('Introduce 3 números separados por comas (Ej. 33, 72, 88): ').split(', ')
lnum = []
for i in numstr:
    n = float(i)
    lnum.append(n)

lnum = sorted(lnum)[::-1]
nstr = []
for i in lnum:
    n = str(i)
    nstr.append(n)
nstr = " ".join(nstr)
print(f'Los números introducidos de mayor a menor son: {nstr}')