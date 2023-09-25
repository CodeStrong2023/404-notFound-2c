import random

print(".:Juego Adivina el Número:.")

aleatorio = random.randint(1, 100)
contador = 0
while True:
    numero = int(input("Ingrese un numero: "))
    contador += 1
    if numero > aleatorio:
        print("No es el número, ingrese un número menor!")
    elif numero < aleatorio:
        print("No es el número, ingrese un número mayor!")
    else:
        print(f"Felicitaciones, acabas de adivinar el número {aleatorio}")
        break

print(f"Juego finalizado, números de intentos realizados: {contador}")