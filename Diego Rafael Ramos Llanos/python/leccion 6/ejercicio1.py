# ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, Luego
# meter los caracteres en una lista sin repetir caracteres
lista=[]
palabra = input("Digite la cadena: ")
for i in palabra:
    if i  not in lista:
        lista.append(i)
print(f"la lista sin repetir caracteres es: {lista}")


