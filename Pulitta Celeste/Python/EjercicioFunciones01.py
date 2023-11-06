# Ejercicio 01: Crear una función para sumar los valors recibidos de tipo
# númericos, utilizando argumentos variables *args como parametro del la
#función y agregar como resultado la suma de todos los valores pasados
# como argumentos.
# Definimos una función
def sumar_valor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado
print(sumar_valor(3, 5, 9))
