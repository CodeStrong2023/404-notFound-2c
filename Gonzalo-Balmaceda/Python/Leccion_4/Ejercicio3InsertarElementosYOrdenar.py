lista = []
salir = False

while not salir:
    num = int(input("Ingrese un número "))
    if(num == 0):
        salir = True
    else:
        lista.append(num)
lista.sort() # Ordena la lista.
print(f"Lista ordenada {lista}")