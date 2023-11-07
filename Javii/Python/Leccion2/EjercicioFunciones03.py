# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos no imprime nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1: #Caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1)# Caso recursivo
    elif numero == 0:
        return
    elif numero<= 0:
        print("Valor ingrsado incorrecto...")

imprimir_numeros_recursivos(5)
