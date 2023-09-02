# Un diccionario esta compuesto por dos elemento
# una LLAVE y un VALOR.
diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programacion Orientada a Objetos",
    "SABD": "Sistema de Administracion de Base de Datos"
}
print(diccionario)

# Verificar la cantidad de elementos de un diccionario.
print(len(diccionario))

# Acceder a un diccionario con la llave key.
print(diccionario["IDE"])

# Otra forma de acceder a un elemento.
print(diccionario.get("POO")) # get = obtener
print(diccionario.get("SABD"))

# Modificamos un elemento.
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Eliminamos el diccionario.
del diccionario
print(diccionario)