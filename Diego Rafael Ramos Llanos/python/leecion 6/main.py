# Comenzamos con Funciones
# mi_funcion #No se puede llamar antes de definir una función
# Definimos una funciónde

def mi_funcion():  # Para identificar a la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura!")
mi_funcion()  # Estamos llamando a la función.
mi_funcion()
mi_funcion()  # Se puede llamar a una función N cantidad de veces

def show(name, lastName):
    print(name + " " + lastName)
person = ["Diego", "Rafael"]
show(person[0], person[1])
show(*person)

# Desempaquetamos a traves de una tupla.
tupla = ("Osvaldo", "Giordanini")
show(*tupla)

# Desempaquetamos un diccionario.
persona3 = {"lastName": "Lucero", "name": "Natalia"}
show(**persona3)

numeros = [1, 2, 3, 4, 5]

for i in numeros:
    print(i)
    if ( i == 3):
        break
else:
    print("Esto se terminó")