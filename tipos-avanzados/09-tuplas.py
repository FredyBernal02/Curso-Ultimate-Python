# La tupla es lo mismo que una lista con la
# diferencia que no se puede agregar elementos,
# eliminar elementos o modificar elementos.

numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)
for n in numeros:
    print(n)

# Si se quiere modificar una tupla, se debe crear una nueva lista con una nueva variable
# pero no se modifico la tupla, se modifico la lista.
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)
