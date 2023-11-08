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

def main():

    es_estudiante = input("Eres estudiante? (si/no): ")

    if es_estudiante == "si".lower():

        return True
    
    else:
        return False
    
print(main())    

    