edad = int(input("Ingresa tu edad:\n"))

if edad > 65:
    print("Puedes ver la pelicula con super descuento")
elif edad > 54:
    print("Puedes ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar por tu edad")
