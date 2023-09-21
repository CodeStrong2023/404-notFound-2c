#Ejercicio Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 =  lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1])
print(lista3)

print(lista3.index(5))

print(lista3.count(1))#Cuenta la cantidad de valores iguales en la lista

lista3.reverse()
print(lista3)

lista3 = lista3 * 2
print (lista3)

lista3.sort() #Ordena
print(lista3)
lista3.sort(reverse=True)
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print (4 in tupla) #Acción booleana, su respuesta es de tipo booleana