import math

numero = (int(input("Digite un número positivo: ")))

while numero < 0:
    print("Error, Ingrese un número positivo!")
    numero = (int(input("Digite un número positivo: ")))

print(f"La raiz cuadrad del número ingresado es {math.sqrt(numero):.2f}")