# Lista = Ariel, Liliana, Natalia, Osvaldo
# Mostramos los nombres de adelante para atras con numero positivo y de atras para adelante con numero negativo
nombres = ["Naty","Lily","Osvaldo","Ariel"]
'''print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])'''

print(nombres[0:2]) #Solo muestra el indice 0,1. Pero no muestra el indice 2
print(nombres[ :3]) # muestra desde el inicio de la lista hasta la posicion que le indicamos
print(nombres[1: ]) # muestra desde el indice indicado hasta el final de la lista

nombres[1] = "Liliana" # Modificamos el valor del indice
nombres[0] = "Natalia"
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es en plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# preguntamos cuantos elementos tiene la lista
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento a la lista
nombres.append("Marcelo")
print(nombres)

# Insertar un elemento en un indice especifico

nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

# Eliminar un elemto

nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)
# Eliminar un indice especifico
del nombres[2]
print(nombres)

#Eliminar, borrar o limpiar la lista
nombres.clear()
print(nombres)

# Eliminar la lista. Nos muestra error porque no esta definida, ya fue eliminada
del nombres
#print(nombres)

# definimos una Tupla
cocina = ("Cuchara","Cuchillo","Tenedor")
print(cocina)
print(len(cocina)) # nos dice cuantos elementos tiene

# Acceder a un elemento dentro de una Tupla, para esto utilizamos corchetes
print(cocina[0]) # nos indica el elemento de la primer posicion
print(cocina[-1]) # mostramos de mandera inversa

# Acceder a un rango
print(cocina[0:1])

# Ejemplo
verduras = ("papas",) # para que sea una tupla aunque tenga un solo elemento debe tener la coma
# de lo contrario seria una cadena de tipo str

# Recorremos los elementos de la tupla
for cocinar in cocina:
   #print(cocinar) # Print esta usando el \n para saltos de linea
    print(cocinar, end=" ") # usamos end=" " para eliminar los saltos de linea del print

# Esta es la unica forma de cambiar un elemento de una tupla, nunca se aconseja hacerlo
cocinaLista = list(cocina) # convertimos la tupla en lista
cocinaLista[0] = "Plato" # modificamos el elemento
cocina = tuple(cocinaLista) # volvemos la lista a tupla
print("\n", cocina)

#del cocina # esta es la forma de eliminar la tupla