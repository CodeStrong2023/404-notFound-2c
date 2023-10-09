# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

# Definimos una función
def sumar_valor(*args):  # Firma de nuestro método o función / Recibimos una cantidad de parámetros indefinidos.
    # pass   Se usa para no dejar la vacía la función. Cuando no queremos dar detalle de nuestra función se utiliza pass.
    resultado = 0
    # Iteramos elemento
    for valor in args:
        resultado += valor
    return resultado

# Llamamos a la función
print(sumar_valor(3, 5, 9, 2, 1))
