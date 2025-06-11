#calcular promedio de 3 numeros
a = float(input("nota 1:"))
b = float(input("nota 2:"))
c = float(input("nota 3:"))
prom = (a+b+c) / 3
print ("promedio:",prom)

#determinar el mayor entre 2 numeros
a = int(input("numero 1: "))
b = int(input("numero 2: "))
if a>b:
    print("el mayor es", a)
elif b>a:
    print("el mayor es",b)
else:
    print ("son iguales")