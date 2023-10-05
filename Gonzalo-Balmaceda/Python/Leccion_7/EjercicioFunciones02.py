# Definimos la función para multiplicar
def multiplicarValores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero

    return resultado

print(multiplicarValores(3, 5, 15))