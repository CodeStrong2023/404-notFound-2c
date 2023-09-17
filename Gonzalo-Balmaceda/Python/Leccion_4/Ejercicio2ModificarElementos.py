lista = list(range(1, 11))

print("Lista original")
for i in lista:
    print(i, end="-")

num = int(input("\nDigite un valor a multiplicar: "))

# Multiplicamos por el número ingresado.
for indice, i in enumerate(lista):
    lista[indice] *= num

print(f"Lista final con los elementos multiplicados por {num}")
for i in  lista:
    print(i, end="-")