# Tipo Set
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas) # Nos mostrara en consola los elementos en un orden aleatorio

# Revisar si un elemento existe dentro del set.
print("Marte" in planetas)

# Agregar un elemento.
planetas.add("Tierra")
planetas.add("Tierra") # En un set no se pueden agregar elementos duplicados.
print(planetas)

# Elinar un elemento-
planetas.remove("Jupiter") # El metodo .remove() si ingresamos mal el nombre del elemento o uno inexistente nos dara un error.
print(planetas)

planetas.discard("Tierra") # El metodo .discar() no nos dara ningun error al ingresar un elemento mal o que no exista.
print(planetas)

# Limpiar set.
planetas.clear()
print(planetas)

# Eliminar set.
del planetas
print(planetas)