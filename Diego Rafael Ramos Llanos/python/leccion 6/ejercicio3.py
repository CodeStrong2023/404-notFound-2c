# ejercicio 1: crear una funcion para sunar los valores recibidos de tipo
# numericos utilizando argumentos variables *args como parametro
# de la funcion y agregar como resultado la suma de todos los valores
# pasados como argumentos
def suma_numeros(*args):
    resultado = 0
    for numero in args:
        if isinstance(numero, (int, float)):#isinstance que se agrego compara si  es de tipo entero o flotante
            resultado += numero
        else:
            print(f"Ignorando valor no numérico: {numero}")
    return resultado
resultado = suma_numeros(3,5,2,9,1)
print("La suma es:", resultado)