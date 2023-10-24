# Ejercicio 5: Función recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones rescursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de
# 5 debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el númro 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada.

numero = int(input("Ingrese un número: "))
def imprimirNumeroRecursivos(numero):
    if numero >= 1:
        print(numero)
        imprimirNumeroRecursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("El valor ingresado es incorrecto")

imprimirNumeroRecursivos(numero)