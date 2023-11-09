"""Uso de operadores lógicos:

Escribe un programa que determine si un número ingresado por el usuario es divisible por 3 y 5 al mismo tiempo.

Crea un programa que solicite al usuario su edad y verifique si es mayor de edad (18 años o más) y si tiene permiso de conducir.

Desarrolla un programa que determine si un año ingresado por el usuario es un año bisiesto y al mismo tiempo es divisible por 10.

Escribe un programa que pida al usuario dos números y determine si al menos uno de ellos es positivo."""

numero = int(input("Ingrese un numero: "))

if numero %3 == 0 and numero %5==0:
    print(f"El numero {numero} es divisible por 3 y 5")

else:
    print(f"El numero {numero} no es divisible por 3 y 5")    


#Crea un programa que solicite al usuario su edad y verifique si es mayor de edad (18 años o más) y si tiene permiso de conducir.

edad = int(input("Ingrese su edad: "))
permiso_conducir = input("Tiene permiso de conducir?: ")

if edad > 18 and permiso_conducir == "si".lower():

    print("Tiene permiso de conducir")

else:
    print("No tiene permiso de conducir")

año = int(input("Ingrese un año: "))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0 and año % 10 == 0:
    print("El año {} es bisiesto y divisible por 10.".format(año))
else:
    print("El año {} no es bisiesto o no es divisible por 10.".format(año))

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 >=0 or numero2 >=0:

    print("Al menos uno de los numeros es positivo")

    
else:
    print("No es positivo")    