# Ejercicio 2: Funcion con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# La multiplicacion de todos los valores pasados como argumentos

#Definimos la funcion para multiplicar
def multiplicar_valores(*args):
    resultado = 1 # El cero no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado

#Llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3))# Le pasamos los argumentos