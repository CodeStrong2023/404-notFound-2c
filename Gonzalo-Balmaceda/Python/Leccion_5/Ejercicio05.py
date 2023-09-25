numero = int(input("Ingrese un número: "))

while (numero < 0):
    print("Error, Ingrese un número positivo!")
    numero = int(input("Ingrese un número: "))

factorial = 1
for i in range(1, numero+1):
    factorial *= i

print(f"El factorial de {numero} es = {factorial}")
