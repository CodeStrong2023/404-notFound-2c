# ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
guardavalor=0
lista =[]
num = int(input("Digite la tablade de multiplicar deseada: "))
for i in range (1,11,1):
    guardavalor=i*num
    lista.append(guardavalor)
print(lista)
for indice,i in enumerate(lista):
    print(f"{num} x {i} = {lista[indice]}")
#Tengo dudas con terpecto a este ejercicio, por que la tabla si sale, sin embargo asi esta en el video del profesor