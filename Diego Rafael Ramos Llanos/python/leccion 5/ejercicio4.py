# Ejercicio 7: juego adivina el numero
# realizar un juego para adivinar un numero. para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicando, "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli debe mostrar el numero de intentos.
import random
print("\t.:Juego Adivina el Numero:.")
aleat= random.randint(1,100)
contador=0
ver= False
while True:
    num = int(input("Digite un numero: "))
    contador+=1
    if num > aleat:
        print("El numero a adivinar es menor")
    elif num < aleat:
        print("El numero a adivinar es Mayor")
    else:
        print("FELICIDADES ADIVINASTE")
        break
print(f"Cntidad de veses intentadas {contador}")