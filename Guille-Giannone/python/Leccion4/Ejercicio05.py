# Ejercicio 5: Factorial de numero positivo
# Hacer un programa para calcular el factorial de numero positivo

numero = int(input("Digite un numero: "))
while numero < 0: # Esto por si se ingresa un numero negativo
    print("Error -> el numero tiene que ser positivo")
    numero = int(input("Digite un numero: "))
factorial = 1 # variable para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i
print(f"\nEl factorial del numero {numero} positivo ingresado es: {factorial}")