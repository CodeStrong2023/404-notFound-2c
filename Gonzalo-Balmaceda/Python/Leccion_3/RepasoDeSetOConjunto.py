# Repaso del tipo set o conjunto.
conjunto1 = set() # Con el set y los parentesis el conjunto se puede iniciar vacio.
conjunto2 = {"bye",} # Cundo queremos inicializar un conjunto con las llaves debe contener minimo un elemento

conjunto1.add(7)
conjunto1.add("Hola")
print(conjunto1)

conjunto2.add("hola")
print(conjunto2)

# Preguntamos si el 3 no esta en el conjunto1.
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos.
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un valor booleano.

# Operaciones en conjunto.
conjunto3 = conjunto1 | conjunto2 # Con la linea entre los conjuntos hace que los dos se unan.
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Guardara en el conjunto3 el elemento que tengan en común el conjunto1 y 2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2.
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferente entre ambos.
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Preguntamos si un conjunto es subconjunto dentro de otro.
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto1)) # conjunto3 es un super conjunto del conjunto1 porque contiene todos sus elementos.
print(conjunto3.issuperset(conjunto2))
print(conjunto1.issuperset(conjunto3))

# Preguntamos si ambos conjuntos son disconexos, esto si no comparten elementos en comun.
print(conjunto1.isdisjoint(conjunto2)) # true = no hay elementos en comun.

# Convertir un conjunto totalmente en inmutable.
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable.
# No se puede agregar, modificar ni eliminar elementos del conjunto.