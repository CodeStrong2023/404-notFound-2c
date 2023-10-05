numero = int(input("Ingrese un número: "))
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(numero)
print(f"El facotial del número 5 es {resultado}")