a = int(input("Ingrese desde donde va a comenzar a sumar: "))
b = int(input("Ingrese hasta donde quiere sumar: "))
suma = 0

for i in range(a,b+1):
    if (i % 2 == 0):
        suma += i

print(f"La suma de los numeros pares es = {suma}")
