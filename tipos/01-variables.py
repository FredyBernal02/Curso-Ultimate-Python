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
# while True:
#     entrada = input(
#         "¿Cuantos años tienes? (o escribe 'salir' para terminar): ").lower()

#     if entrada == "salir":
#         break  # rompe el bucle

#     try:
#         edad = int(entrada)
#         doble = edad * 2
#         print(f"El doble de tus {edad} años es: {doble}")
#     except ValueError:
#         print("Por favor, ingresa un número entero valido.")

#  Reto 1: Tu nombre y edad
# Crea un programa que:

# Pida al usuario que escriba su nombre y su edad usando input().

# Guarde esos valores en variables.

# Muestre un mensaje que diga:
# "Hola [nombre], tienes [edad] años."

# nombre = input("¿Cual es tu nombre?: ")
# edad = int(input("¿Cuantos años tienes?: "))

# print(f"Hola {nombre}, tienes {edad} años")
# print(f"El tipo de 'nombre' es: {type(nombre)}")
# print(f"El tipo de 'edad' es: {type(edad)}")

# 🧮 Reto 3: Calculadora de suma
# Crea un programa que:

# Pida al usuario dos números (pueden ser decimales).

# Convierta ambos a float.

# Sume los dos números.

# Muestre el resultado de la suma con un mensaje como:
# "La suma de [número1] + [número2] es: [resultado]"


# n1 = float(input("Escribe el primer numero: "))
# n2 = float(input("Escribe el segundo numero: "))

# resultado = n1 + n2

# print(f"La suma de {n1} y {n2} es: {resultado}")

# ➗ Reto 4: Calculadora completa
# Ahora, amplia tu calculadora para que haga más operaciones:

# Pide dos números(como antes).

# Convierte los números a float.

# Realiza las siguientes operaciones:

# Suma

# Resta

# Multiplicación

# División(asegurándote de no dividir por 0)

# Muestra los resultados de cada operación de manera clara y ordenada.

# numero1 = float(input("Escribe el primer numero: "))
# numero2 = float(input("Escribe el segundo numero: "))

# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2

# print(f"La suma entre {numero1} y {numero2} es: {suma}")
# print(f"La resta entre {numero1} y {numero2} es: {resta}")
# print(f"La multiplicacion entre {numero1} y {numero2} es: {multiplicacion}")

# if numero2 != 0:
#     division = numero1 / numero2
#     print(f"La division entre {numero1} y {numero2} es: {division}")
# else:
#     print("No se puede dividir por cero.")

# Reto 5: ¿Mayor de edad?
# Crea un programa que:

# Pida al usuario su edad.

# Convierte la entrada a int.

# Verifique si el usuario es mayor o menor de edad(mayor o igual a 18 años).

# Muestra un mensaje como:

# "Eres mayor de edad"

# "Eres menor de edad"

edad = int(input("Escribe tu edad: "))

if edad <= 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
