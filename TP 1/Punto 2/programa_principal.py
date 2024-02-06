""" Hacer un programa en Python que le consulte al usuario a través de un menú de
opciones si desea obtener la información de un rectángulo, un triángulo o un
círculo. Ejemplo:
1. Rectangulo
2. Triangulo
3. Circulo
Cualquier otra opción debe dar “opción incorrecta”.
- Si ingresa Rectangulo, debe pedir la base y la altura. Luego informar el área y
el perímetro.
- Si ingresa Triangulo, también debe solicitar al usuario que ingrese la base y la
altura, pero solo informa el área.
- Si ingresa Circulo, debe pedirle el radio y la información será el área y el
perímetro.
Definir funciones para cada cálculo que deben estar en un módulo aparte.
Además, definir funciones para el menú y para el main.
Puntos: 10 (diez)
"""

import calculos_geometricos

def mostrar_menu():
    #Postcondiciones: Muestra el menu de opciones para el usuario

    print("\nSeleccione una Opción\n")
    print("1. Rectangulo")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Salir")

def main():
    #Precondiciones: El usuario ingresa numeros reales validos cuando se solicite la base, la altura o el radio, la opción seleccionada debe ser un numero entero entre 1 y 4.
    
    #Postcondiciones: El programa realiza calculos geometricos segun la opción seleccionada por el usuario y muestra los resultados.

    print("\nBienvenidos a Calculadora Geometrica ")

    ingresar_opcion = 0
    
    while ingresar_opcion!=4:
        mostrar_menu()
        ingresar_opcion = int(input("Ingrese una Opción: "))


        if ingresar_opcion == 1:

            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            area = calculos_geometricos.calcular_area_rectangulo(base,altura)
            perimetro = calculos_geometricos.calcular_perimetro_rectangulo(base,altura)
            print(f"\nArea del rectangulo: {area}")
            print(f"Perimetro del rectangulo: {perimetro}")

        elif ingresar_opcion == 2:

            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            area = calculos_geometricos.calcular_area_triangulo(base,altura)
            print(f"\nArea del Triangulo: {area}")

        elif ingresar_opcion == 3:

            radio = float(input("Ingrese el radio del circulo: "))
            area = calculos_geometricos.calcular_area_circulo(radio)
            perimetro = calculos_geometricos.calcular_perimetro_circulo(radio)
            print(f"\nArea del circulo: {area}")
            print(f"Perimetro del circulo: {perimetro}")

        elif ingresar_opcion == 4:

            print("\nSaliendo del Programa...\n")

        else:

            print("\nOpción incorrecta")


if __name__ == "__main__":
    main()               










