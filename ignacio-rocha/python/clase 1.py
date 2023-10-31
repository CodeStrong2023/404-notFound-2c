"""
#lista= ariel, liliana, natalia, osvaldo

nombres=["naty","osvaldo","lily","ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])


print(nombres[0:7]) #solo muestra el indice 0, 1 pero
#el indicice 2 del iniicio de la lista al indice (sin incluirlo)
print(nombres[:3])# indices a mostrar 0,1,2
#desde el indice indicado hasta el final
print(nombres[1:])
#modificamos un valor
nombres[3]="liliana"
nombres[0]="Natalia"
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")


#preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

#agregamos un elemento
nombres.append("marcelo")
print(nombres)

#insertar un elemento en un indice especifico
nombres.insert(1,"alberto")
print(nombres)
nombres.insert(3,"debora")
print(nombres)

#eliminamos un elemento
nombres.remove("alberto")
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[2] #del significa delete(eliminar)
print(nombres)

#eliminar , borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista
#del nombres
#print(nombres)

#ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2,
#en lugar de 1 en 1. ejemplo: 3 5 7 9
#ejercicio 1: iterar un rango de 0 a 10 e imprimir numeros divisibles entre
#3: ejemplo: 0,3,6,9

#ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
#ejemplo: 2,3,4,5,6


print("ejercicio 1: ")
di1 = []

for num in range(0, 11):
    if num % 3 == 0:
        di1.append(num)

for num in di1:
    print(num)

print("ejercicio 2: ")
di2 = []

for num in range(2, 7):
   di2.append(num)

for num in di2:
    print(num)

print("ejercicio 3:")
di3=[]

for num in range(3,11,2):
    di3.append(num)

for num in di3:
    print(num)
"""
#definimos una tupla
cocina=("cuchara","cuchillo","tenedor")
print(cocina)
print(len(cocina))

#acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

#mostrar de manera inversa
print(cocina[-1])

#acceder a un rango
print(cocina[0:1])
#ejemplo
verduras=("papa",) #una tupla necesita aunque sea un elemento la coma

#de lo contrario solo seria un tipo str cadena

#recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar,end=' ') #print esta usando \n para saltos de linea
#usamos end= para eliminar los saltos de linea

cocina=[0]="plato"
print(cocina)
