#parte de santi
#algoritmo que pide un numero y muestra la tabla de multiplicar de ese numero

# Solicitar al usuario un número
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
# Mostrar la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
