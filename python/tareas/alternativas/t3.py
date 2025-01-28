#La verdad es que el ejercicio en sí es un poco raro, ya que no necesitas hacer todos estos pasos, solo elevar normalmente, pero de cualquier modo lo hacemos.
base = float(input('Introduce una base: '))
exponente = float(input('Introduce un exponente: '))
absexp = abs(exponente) #Convertimos el exponente en valor absoluto para elevarlo
res = base**absexp
if exponente > 0: #Si el exponente es positivo de por si...
    print(res) #Pues no le tenemos que hacer nada al resultado
elif exponente < 0: #De otro modo...
    print(1/res) #Es 1/res
else: #Y si el exponente es 0...
    print(1) #Cualquier cosa elevada a 0 es 1