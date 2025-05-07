# nombre_curso = "Ultimate Python"
# nombre1 = "Hola"
# NOMBRE_CURSO = "Mundo"
# NoMbRe_CuRsO = "Chanchito"
# NombreCurso = "Feliz"
# print(nombre_curso, nombre1, NOMBRE_CURSO)
# alumnos = 5000
# puntaje = 9.9
# publicado = True

# Casting de tipos y concatenación
# edad = int(input("Edad: "))
# print("El doble de tu edad es " + str(edad * 2))

# Ejercicio 1: Doble de la edad:
# edad = input("¿Cuantos años tienes?:\n")
# edad_entero = int(edad)
# doble = edad_entero * 2
# # print("El doble de tu edad es: " + str(doble))

# Ejercicio 2: Suma de números reales
# n1 = float(input("Ingresa el primer número decumal: "))
# n2 = float(input("Ingresa el segundo número decimal: "))
# suma = n1 + n2
# print(f"la suma de {n1} y {n2} es: {suma}")

# Ejercicio 3: Tipo de cada dato
# texto = "Hola"
# numero = 42
# decimal = 3.14
# booleano = True
# none_type = None

# print("Tipo de dato texto:", type(texto))
# print("Tipo de número:", type(numero))
# print("Tipo de decimal:", type(decimal))
# print("Tipo de booleano:", type(booleano))
# print("El tipo None:", type(none_type))

# # Ejercicio 4: Convertir string a número y operar
# numero_str = "100"
# print("Texto:", numero_str)
# print("Suma como texto:", numero_str + "5")  # Concatenación

# numero_int = int(numero_str)
# print("Suma como número:", numero_int + 5)

# Ejercicio 5: Operaciones combinadas
# a = input("Ingresa un número entero: ")
# b = input("Ingresa un número decimal: ")

# a = int(a)
# b = float(b)

# resultado = a + b
# print(f"La suma de {a} (int) y {b} (float) es: {resultado}")
# print("El tipo de resultado es:", type(resultado))

# Ejercicio: Haz un programa que pida la edad y muestre el doble
while True:
    entrada = input(
        "¿Cuantos años tienes? (o escribe 'salir' para terminar): ").lower()

    if entrada == "salir":
        break  # rompe el bucle

    try:
        edad = int(entrada)
        doble = edad * 2
        print(f"El doble de tus {edad} años es: {doble}")
    except ValueError:
        print("Por favor, ingresa un número entero valido.")
