# En esta clase veremos la sentencia if/else
condicion = "Hola"
if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion sin especificar")

num = int(input("Ingrese un numero entre el 1 y 3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f"El numero ingresado es {num} - {numTexto}")

# Operador Ternario
# Este operador solo se utiliza cuando es un codigo corto
condicion = True
print("La condicion es verdadera") if condicion else print("La condicion es falsa")