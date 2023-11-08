"""Variables y Tipos de Datos:

1 Crea una variable llamada nombre y asígnale tu nombre. Luego imprime el valor de esta variable.
2 Declara tres variables: edad, altura y peso. Asigna valores numéricos que representen tu edad, altura en metros y peso en kilogramos. Calcula tu índice de masa corporal (IMC) usando la fórmula IMC = peso / (altura * altura) y almacena el resultado en una variable imc.
3 Crea una variable llamada mensaje que contenga una cadena de texto con información sobre ti, utilizando las variables nombre, edad, altura y peso.
4 Define una variable booleana llamada es_estudiante y asígnale True si eres estudiante o False si no lo eres."""

#1 Crea una variable llamada nombre y asígnale tu nombre. Luego imprime el valor de esta variable.

nombre = "Brian"

print(nombre)

#2 Declara tres variables: edad, altura y peso. Asigna valores numéricos que representen tu edad, altura en metros y peso en kilogramos. Calcula tu índice de masa corporal (IMC) usando la fórmula IMC = peso / (altura * altura) y almacena el resultado en una variable imc.

edad = 24
altura = 1.70
peso = 80 

imc = peso / (altura * altura)

print(imc)

#3 Crea una variable llamada mensaje que contenga una cadena de texto con información sobre ti, utilizando las variables nombre, edad, altura y peso.

mensaje = f"Mi nombre es {nombre} y tengo {edad} años, tengo una altura de {altura} cm y peso {peso} kg"

print(mensaje)

#def main():

    #es_estudiante = input("Eres estudiante? (si/no): ")

    #if es_estudiante == "si".lower():

        #return True
    
    #else:
        #return False
    
#print(main())    

"""Operadores y Expresiones:

1 Escribe un programa que calcule el área de un triángulo a partir de la base y la altura ingresadas por el usuario. Utiliza la fórmula: Área = (base * altura) / 2.
2 Solicita al usuario que ingrese dos números enteros y calcula su suma, resta, multiplicación y división. Imprime los resultados.
3 Dado un valor en grados Celsius ingresado por el usuario, conviértelo a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
4 Escribe un programa que calcule el área de un círculo a partir del radio ingresado por el usuario. Utiliza la fórmula: Área = π * radio^2. Puedes usar una aproximación de π = 3.14159."""

#1 Escribe un programa que calcule el área de un triángulo a partir de la base y la altura ingresadas por el usuario. Utiliza la fórmula: Área = (base * altura) / 2.

ingresar_base = int(input("Ingrese la Base: "))
ingresar_altura = int(input("Ingrese la Altura: "))

area = (ingresar_base * ingresar_altura) / 2

print(area)

#2 Solicita al usuario que ingrese dos números enteros y calcula su suma, resta, multiplicación y división. Imprime los resultados.    

ingresar_numero1 = int(input("Ingrese el Primer Numero: "))
ingresar_numero2 = int(input("Ingrese el Segundo Numero: "))

suma = ingresar_numero1 + ingresar_numero2

resta = ingresar_numero1 - ingresar_numero2

multiplicacion = ingresar_numero1 * ingresar_numero2

division = ingresar_numero1 / ingresar_numero2

print(f"La suma de los numeros ingresado es {suma} y la resta es {resta} y la multiplicacion es {multiplicacion} y la division es {division}")


#3 Dado un valor en grados Celsius ingresado por el usuario, conviértelo a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.

grados_celcius = float(input("Ingrese el valor a convertir de celsius a fahrenheit: "))

fahrenheit = (grados_celcius * 9/5) + 32

print(f"El grado de Fahrenheit es {fahrenheit}")

#4 Escribe un programa que calcule el área de un círculo a partir del radio ingresado por el usuario. Utiliza la fórmula: Área = π * radio^2. Puedes usar una aproximación de π = 3.14159."""

ingresar_radio = float(input("Ingrese el Radio: "))

area = 3.14159 * ingresar_radio**2

print(f"El area calculado es {area}")