# Ciclo While (Mientras, durante)
'''
contador = 0
while contador < 5:
    print("Ejecutamos nuestro ciclo while", contador)
    contador += 1
else:
    print("Fin del ciclo while")


#Imprimir numeros del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
'''

# Imprimir numeros de 5 al 0 con el ciclo while
'''minimo = 0
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
'''
# Ciclo for (Hasta con paso Hacer)
'''cadena = "Hello"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")
'''
#Palabra reservada break (se utiliza para romper los ciclos una vez que se encuentra lo que se buscaba)
'''for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break # si agregamos o quitamos esta palabra vemos la diferencia
else:
    print("Fin del ciclo for")
'''
# Palabra reservada continue
'''for i in range(6): #la palabra range significa rango
    if i % 2 == 0:
        print(f"valor :{i}")

for i in range(6):
    if i % 2 != 0: # la indicacion != significa diferente
        continue # aqui lo que haces es esta palabra es saltar todos los numeros impares
    print(f"valor: {i}")

# Ejercicio año bisiesto

def es_anio_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
while True:
    anio = int(input("Ingrese un año: (0 para salir) "))
    if anio == 0:
        break
    if es_anio_bisiesto(anio):
        print(anio, "Es año bisiesto")
    else:
        print(anio, "No es año bisiesto")

# Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
positivos = 0
negativos = 0
neutros = 0

for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1
print("Ud a ingresado",positivos,"numeros positivos,",negativos,"numeros negativos y",neutros,"numeros neutros")
'''
# Calcular la suma de N primeros numeros
numero = int(input("Ingrese un numero: "))
sumaDigitos = 0
while numero != 0:
    digito = numero % 10
    sumaDigitos += digito
    numero = numero // 10
print("La suma de los digitos es: ",sumaDigitos)



