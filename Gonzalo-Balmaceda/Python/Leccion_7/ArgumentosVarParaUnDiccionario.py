def listarTerminos(**terminos):
    for key, value in terminos.items():
        print(f"{key} : {value}")

listarTerminos() # Si no recibe nada, no va a mostrar nada.
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primaruy Key")