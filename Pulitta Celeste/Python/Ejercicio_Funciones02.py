# Ejercicio 2: Función con * args para multiplicar
# Crea una aplicación para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables * args
# como párametro de la función y regresar el resultado
# la multiplicaión de todos los valores pasados por argumentos

def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado
print(multiplicar_valores(7,9,3))
