# Ejercicio 2: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

#Definimos una función

def sumar_Valor(*args): #Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado
# Llamamos a la función
print(sumar_Valor(3, 5, 9, 2, 1))