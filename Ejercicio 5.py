import random,sys
respuestas=['Es seguro que sí','Las chances son buenas','Puedes contar con ello','Pregúntame de nuevo más tarde','Concéntrate y pregunta de nuevo','No veo con claridad, intenta de nuevo','Mi respuesta es no','Mis fuentes me dicen que no']
while True:
    seleccion=random.randint (0,7)
    print("--------------")
    print("Soy una bola 8 magica")
    entrada=input("Ingrese una pregunta o [Salir] para salir: ")

    if entrada=="Salir":
        sys.exit()
    else:
        print(respuestas[seleccion])