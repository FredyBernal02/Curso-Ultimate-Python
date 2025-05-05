animal = "chanchITO feliz"
print(animal.upper())
print(animal.lower())  # Pasar cualquier mayuscula a minuscula
# Dejar mayusacula la primer letra de la primera palabra
print(animal.strip().capitalize())
print(animal.title())  # Dejar mayusculas las primeras letras de cada palabra
print(animal.strip())  # Remover espacios
print(animal.lstrip())  # Quitar espacios de la izquierda
print(animal.rstrip())  # Quitar espacios de la derecha
print(animal.find("ITO"))  # Busca la cadena de caracteres
print(animal.replace("nch", "j"))
# Te devulve un boolean para saber si se encuentra dentro del string
print("nch" in animal)
# Te devuelve un boolean para saber si no se encuentra en el string
print("nch" not in animal)
