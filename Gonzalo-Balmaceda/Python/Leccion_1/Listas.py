
nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0:2]) # Solo muestra del indice 0 al 1 pero no el 2.

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Solo mostramos el indice 0, 1, 2

# Desde el indice indicado hasta el final.
print(nombres[1: ])

# Modificamos un valor.
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)

# Iterar una lista.
for i in nombres:
    print(i)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elemetos tiene.
print(len(nombres)) # A len() le pasa como parametro la lista.

# Agregamos un nombre a la lista.
nombres.append("Marcelo") # Con el .append() le ingresamos como parametro el nuevo nombre que queramos agregar.
print(nombres)

# Insertar un elemento en un indice especifico.
nombres.insert(1, "Alberto")
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento.
nombres.remove("Alberto")
print(nombres)

# Eliminamos el ultimo elemento.
nombres.pop() # Elimina el ultimo elemento de la lista.
print(nombres)

# Eliminamos un indice en especifico.
del nombres[2] # del = delete
print(nombres)

# Eliminamos todos los elementos de la lista.
nombres.clear()
print(nombres)

# Eliminamos la lista.
del nombres
print(nombres)