mascotas = ["Pelusa", "Wolfgang", "Pulga",
            "Felipe", "Chanchito feliz", "Wolfgang"]

# print(mascotas.count("Wolfgang"))
# if "Wolfgang" in mascotas:
#     print(mascotas.index("Wolfgang"))

colores = ["Azul", "Verde", "Morado", "Gris", "Negro", "Verde", "Morado",]

# print(colores.count("Verde"))

while True:
    eleccion = input("Escribe un color o escribe 'salir' para terminar: \n")

    if eleccion.lower() == 'salir':
        print("Terminando el programa")
        break

    if eleccion in colores:
        print("Si, el color esta en la lista!")
    else:
        print("No, el color no esta en la lista")
