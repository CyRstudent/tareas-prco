n = int(input('Introduce un número: '))
arr = []
while n != 0:
    arr.append(n)
    n = int(input('Introduce otro número: '))

sum = 0

for num in arr:
    sum += num

print(f'La sumatoria de todos los números es {sum}')
med = sum/len(arr)
print(f'La media de los números introducidos es {med}')