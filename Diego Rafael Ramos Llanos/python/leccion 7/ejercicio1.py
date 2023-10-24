# ejercicio 2: funcion con * args para multiplicar
# crear una funcion para multiplicar los valores
# recibidos de tipo numerico, utilizando argumentos
# variables *args como parametro de la funcion y
# regresar como resultado la multiplicacion
# de todos los valores pasados como argumento

def mi_func(*args):
    resultado = 1
    for numero in args:
        if isinstance(numero, (int, float)):
            resultado *= numero
        else:
            print(f"Ignorando valor no numérico: {numero}")
    return resultado
resultado = mi_func(3,5,15)
print("La multiplicacion es:", resultado)
