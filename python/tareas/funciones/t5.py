def mcd(n1: int, n2: int):
    nums = sorted((n1, n2))[::-1]
    div = []
    for i in range(1, nums[0]):
        if ((n1%i) == 0) and (n2%i == 0):
            div.append(i)
    div = div[::-1]
    if len(div) == 0:
        return 1
    else:
        return div[0]

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
res = mcd(num1, num2)
print(f'El máximo común divisor de los 2 números es: {res}')