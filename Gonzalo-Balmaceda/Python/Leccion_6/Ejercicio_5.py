# Ejercicio 5: Sistemas de calificaciones

calif = int(input("Ingrese su calificacion entre 0 y 10: "))

if 9 <= calif <= 10:
    print( "Su nota es una A")
elif 8 <= calif < 9:
    print("Su nota es una B")
elif 7 <= calif < 8:
    print("Su nota es una C")
elif 6 <= calif < 7:
    print("Su nota es una D")
elif 0 <= calif < 6:
    print("Su nota es una F")
else:
    print("Valor incorrecto")