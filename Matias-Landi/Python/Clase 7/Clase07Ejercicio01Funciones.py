# Ejercicio 1: Función con * args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasadaos como argumentos

#Definimos la función para multiplicar

def multiplicar_valores(*numeros): # El mas utilizado es *args
    resultado = 1 # El cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

#Llamamos la función
print(multiplicar_valores(3, 5, 15, 3)) # Le pasamos los argumentos