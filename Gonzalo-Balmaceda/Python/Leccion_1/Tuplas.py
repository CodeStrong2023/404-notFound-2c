# Definimos una tupla.
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemento, para eso usamos corchetes no parentesis.
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango.
print(cocina[0:2])

# Ejemplo.
verduras = ("papa",) # Una tupla necesita minimo un elemento seguido de una coma.
# De lo contrario se consideraria una cadena de String.

# Recorremos los elementos de una tupla.
'''
for cubiertos in cocina:
    print(cubiertos, end=" ") '''

# Para agregar un elemento a la tupla necesitamos hacer una conversion de tupla a lista.
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print(cocina)

# del cocina (esto es para eliminar la tupla)