# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

# loop

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# loop infinito

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
