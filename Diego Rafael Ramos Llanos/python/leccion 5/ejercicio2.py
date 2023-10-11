# ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
numero = int(input("Digite un numero positivo: "))
factorial=1
while numero < 0:
    print("El número debe ser positivo.")
    numero = int(input("Digite un numero positivo: "))
if numero>0:
    for i in range (1,numero+1):
        factorial*=i

print(f"El factorial de {numero} es {factorial}")