buscar = 10
for numero in range(5):  # range es un iterador(listas, tuplas, etc..)
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado")

for char in "Ultimate Python":
    print(char)
