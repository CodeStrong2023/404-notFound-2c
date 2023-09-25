numero = (int(input("Ingrese un numero: ")))
lista = []

for i in range(1, 11):
    lista.append(numero * i)

print(f"La lista que guarda la tabla de multiplicar del número {numero} es {lista}")