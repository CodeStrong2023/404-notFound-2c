"""ejercicio 3: Función Recursiva
imprimir números de 5 a 1 de manera descendente usando funciones recursivas
Puede ser valor positivo, por ejemplo, si pasamos el
valor de 5, debe imprimir:
5
4
3
2
1
En caso de ser el número 3 debe imprimir:
3
2
1
Si se ingggsan números negativos no imprime nada"""

def mi_funcion(valor):
    for i in range(valor,0,-1):
        if i == 0:
            break
        else:
            print(i)
valor=int(input("Digite un numero: "))
if valor < 0:
    print("Valor ingresado incorrecto")
else:
    mi_funcion(valor)


