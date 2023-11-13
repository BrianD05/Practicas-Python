"""Ejercicio 1: División segura
Escribe un programa que solicite al usuario dos números y realice la división. Maneja la excepción que ocurre si el usuario intenta dividir por cero."""

def division_segura():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = num1 / num2
        
        print("El resultado de la división es:", resultado)

    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Ingrese números válidos.")

division_segura()

"""Ejercicio 2: Archivo inexistente
Escribe un programa que intente abrir un archivo. Maneja la excepción que ocurre si el archivo no existe."""

def abrir_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

abrir_archivo()

"""Ejercicio 3: Índice fuera de rango
Crea una lista de números y pide al usuario que ingrese un índice. Intenta acceder al elemento en ese índice. Maneja la excepción que ocurre si el índice está fuera del rango de la lista."""

def indice_fuera_de_rango():
    numeros = [10, 20, 30, 40, 50]

    try:
        indice = int(input("Ingrese un índice para acceder a la lista: "))
        valor = numeros[indice]
        print(f"El valor en el índice {indice} es: {valor}")

    except IndexError:
        print("Error: Índice fuera de rango. Ingrese un índice válido.")
    except ValueError:
        print("Error: Ingrese un número entero como índice.")
    except Exception as e:
        print(f"Error inesperado: {e}")

indice_fuera_de_rango()        


def division_segura():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        resultado = num1 / num2
        
        print("El resultado de la división es:", resultado)

    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Ingrese números válidos.")

def abrir_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def indice_fuera_de_rango():
    numeros = [10, 20, 30, 40, 50]

    try:
        indice = int(input("Ingrese un índice para acceder a la lista: "))
        valor = numeros[indice]
        print(f"El valor en el índice {indice} es: {valor}")

    except IndexError:
        print("Error: Índice fuera de rango. Ingrese un índice válido.")
    except ValueError:
        print("Error: Ingrese un número entero como índice.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Llamadas a las funciones
division_segura()
abrir_archivo()
indice_fuera_de_rango()



def ejercicio_sintaxis():
    try:
        # Sintaxis incorrecta: falta un paréntesis
        print("Hola, mundo!")

    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")

# Llamada a la función
ejercicio_sintaxis()

def ejercicio_indentacion():
    try:
        # Indentación incorrecta: falta un nivel de indentación
        print("Hola, mundo!")

    except IndentationError as e:
        print(f"Error de indentación: {e}")

# Llamada a la función
ejercicio_indentacion()

def ejercicio_tipo_incorrecto():
    try:
        # Operación en tipo incorrecto de objeto
        resultado = "10" + 5

    except TypeError as e:
        print(f"Error de tipo: {e}")

# Llamada a la función
ejercicio_tipo_incorrecto()


def ejercicio_division_por_cero():
    try:
        # División por cero
        resultado = 10 / 0

    except ZeroDivisionError as e:
        print(f"Error de división por cero: {e}")

# Llamada a la función
ejercicio_division_por_cero()

def ejercicio_valor_incorrecto():
    try:
        # Valor incorrecto en función
        numero = int("abc")

    except ValueError as e:
        print(f"Error de valor: {e}")

# Llamada a la función
ejercicio_valor_incorrecto()


def ejercicio_indice_fuera_de_rango():
    try:
        # Índice fuera de rango
        lista = [1, 2, 3]
        elemento = lista[10]

    except IndexError as e:
        print(f"Error de índice: {e}")

# Llamada a la función
ejercicio_indice_fuera_de_rango()

def ejercicio_archivo_no_encontrado():
    try:
        # Archivo no encontrado
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()

    except FileNotFoundError as e:
        print(f"Error de archivo no encontrado: {e}")

# Llamada a la función
ejercicio_archivo_no_encontrado()

def ejercicio_clave_no_presente():
    try:
        # Clave no presente en diccionario
        diccionario = {"nombre": "Juan", "edad": 25}
        valor = diccionario["apellido"]

    except KeyError as e:
        print(f"Error de clave no presente: {e}")

# Llamada a la función
ejercicio_clave_no_presente()

