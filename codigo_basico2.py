"""Impresión y Entrada de Datos:

Pide al usuario que ingrese su nombre y luego imprime un mensaje de saludo personalizado.
Solicita al usuario que ingrese dos números enteros y luego muestra la suma, la resta, la multiplicación y la división de estos números en un formato legible.
Pide al usuario que ingrese una temperatura en grados Celsius y luego imprime la temperatura en grados Fahrenheit junto con un mensaje explicativo.
Crea un programa que solicite al usuario su nombre y su edad. Luego, imprime un mensaje que indique cuántos años le faltan para llegar a los 100 años."""

ingresar_nombre = input("Ingrese su Nombre: ")

print(f"Bienvenido {ingresar_nombre}")

ingresar_primer_numero = int(input("Ingrese el primer numero: "))
ingresar_segundo_numero = int(input("Ingrese el segundo numero: "))

suma = ingresar_primer_numero + ingresar_segundo_numero
resta = ingresar_primer_numero - ingresar_segundo_numero
multiplicacion = ingresar_primer_numero * ingresar_segundo_numero
division = ingresar_primer_numero / ingresar_segundo_numero

print(f"La suma es {suma} y la resta es {resta} y la multiplicacion es {multiplicacion} y la division es {division}")

grados_celcius = float(input("Ingrese el valor a convertir de celsius a fahrenheit: "))

fahrenheit = (grados_celcius * 9/5) + 32

print(f"El grado de Fahrenheit es {fahrenheit} °F")

ingresar_nombre2 = input("Ingrese su nombre: ")
ingresar_edad = int(input("Ingrese su edad: "))

calcular_anios = 100 - ingresar_edad

print(f"Bienvenido {ingresar_nombre2}, usted tiene {ingresar_edad} años y a usted le faltan {calcular_anios} años para llegar a los 100 años")
