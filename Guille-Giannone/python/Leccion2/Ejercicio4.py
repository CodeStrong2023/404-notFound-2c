edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 40:
    mensaje = "Comienza una nueva etapa, ser padre"
elif 40 <= edad < 50:
    mensaje = "Estas cargado de responsabilidades"
elif 50 <= edad < 60:
    mensaje = "Comienzas a ver la vida de otra forma, sin tantos compromisos"
elif 60 <= edad < 70:
    mensaje = "Llega la tan ansiada jubilacion, ahora a disfrutar de los nietos"
else:
    mensaje = "Etapa de la vida no reconocida"
print(f"Tu edad es: {edad}, {mensaje} ")