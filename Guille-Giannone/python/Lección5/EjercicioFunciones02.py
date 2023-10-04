# Ejercicio 2: Funcion con * args para multiplicar
# Crear una funcione para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados por argumentos

# definimos la funcion para multiplicar
def multiplicar_valores(*args): # El mas utilizado es *args
    resultado = 1 # El 0 no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado
# Llamamos a la funcion
print(multiplicar_valores(3,5,15,3)) # Le pasamos los argumentos