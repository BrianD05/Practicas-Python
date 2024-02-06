def calcular_area_rectangulo(base, altura):
    #Precondiciones: La base y la altura deben ser numeros reales positivos.
    #Postcondiciones: La función devuelve el area del rectangulo calculado correctamente, que es el producto de la base y la altura.
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    #Precondiciones: La base y la altura deben ser numeros reales positivos.
    #Postcondiciones: La función devuelve el perimetro del rectangulo correctamente calculado, que es el doble de la suma de la base y la altura.
    return 2 * (base + altura)

def calcular_area_triangulo(base, altura):
    #Precondiciones: La base y la altura deben ser numeros reales positivos.
    #Postcondiciones: La función devuelve el area del triangulo correctamente calculado, que es la mitad del producto de la base y la altura.
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    #Precondiciones: El radio debe ser un numero real positivo.
    #Postcondiciones: La función devuelve el area del circulo correctamente calculado, que es el producto de (PI) y el radio al cuadrado.
    return 3.1416 * radio**2

def calcular_perimetro_circulo(radio):
    #Precondiciones: El radio debe ser un numero real positivo.
    #Postcondiciones: La función devuelve el perimetro del circulo correctamente calculado, que es el doble del producto de (PI) y el radio.
    return 2 * 3.1416 * radio
