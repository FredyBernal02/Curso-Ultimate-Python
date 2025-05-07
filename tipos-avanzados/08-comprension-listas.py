usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]
# nombres = []

# for usuario in usuarios:
#     nombres.append(usuarios[0])
# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]

# Filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)
