#Determinar el mayor entre dos numeros
a = int(input("inngrese el primer numero "))
b = int(input("ingrese el segundo numero "))

while a == b:
    print("Ingrese dos numeros de distinto valor")
    a = int(input("ingrese el primer numero "))
    b = int(input("ingrese el segundo numero "))
    
if a > b: 
    print('El primer numero es mayor')
else:
    print("el segundo numero es mayor")
