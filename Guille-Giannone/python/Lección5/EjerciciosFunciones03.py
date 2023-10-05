# Ejercicio 3: Funcion Recursiva
# Imprimir nuemro de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positivo, por ejemplo,
# si pasamos el valor de 5, debe imprimir
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir
# 3
# 2
# 1
# si se ingresan numeros negativos no debe imprimir nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # casi base
        print(numero)
        imprimir_numeros_recursivos(numero - 1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto ...")
numeroUsuario = int(input("Digite un numero: "))
imprimir_numeros_recursivos(numeroUsuario)