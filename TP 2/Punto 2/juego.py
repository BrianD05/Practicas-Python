import time
import os
import palabras
import random

def limpiar_pantalla(tiempo_espera=1.2):
    """ 
    PRE:

    POST: Borra la pantalla despues de un tiempo de espera
    """

    time.sleep(tiempo_espera)
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_estado_juego(palabra, letras_arriesgadas, fallos):
    """
    PRE: Requiere una palabra, una lista de letras arriesgadas y un conteo de fallos.

    POST: Muestra el estado actual del juego en la pantalla.
    """

    tablero = ""
    for letra in palabra:
        if encontrar_letra(letra, letras_arriesgadas):
            tablero += letra + " "
        else:
            tablero += "_ "
    
    letras_arriesgadas_mostradas = ""
    for letra_arriesgada in letras_arriesgadas:
        letras_arriesgadas_mostradas += letra_arriesgada + " "
    
    print(f"{tablero}letras arriesgadas: {letras_arriesgadas_mostradas}fallos: {fallos}")

def encontrar_letra(letra, letras_arriesgadas):
    """
    PRE: letra es una cadena de longitud 1 y letras_arriesgadas es una lista no vacia de cadenas de longitud 1.
    
    POST: Devuelve True si la letra se encuentra en letras_arriesgadas, False en caso contrario.
    """
    encontrado = False
    i = 0
    while not encontrado and i < len(letras_arriesgadas):
        if letras_arriesgadas[i] == letra:
            encontrado = True
        i += 1
    return encontrado

def jugar_partida():
    """
    PRE: Necesita una lista de palabras no vacía.

    POST: Facilita una partida del juego de adivinar palabras y devuelve los puntos obtenidos al finalizar la partida.
    """
    palabra = obtener_palabra_aleatoria()
    letras_arriesgadas = []
    fallos = 0
    acertada = False
    
    print("\nComencemos!!")

    mostrar_estado_juego(palabra, letras_arriesgadas, fallos)
    
    while fallos < 6 and not acertada:
        intento = input("\nIngrese una letra o la palabra completa: ").upper()

        limpiar_pantalla()

        while not intento.isalpha():
            print("Error: Solo se pueden ingresar letras. Intentalo de nuevo.")

            limpiar_pantalla()

            intento = input("\nIngrese una letra o la palabra completa: ").upper()

        if len(intento) == 1:  
            if encontrar_letra(intento, letras_arriesgadas):
                print("\nYa has intentado esta letra.")

            elif encontrar_letra(intento, palabra):
                print(f"\nLa letra '{intento}' está en la palabra.")

                letras_arriesgadas.append(intento)
            else:
                print(f"\nLa letra '{intento}' no está en la palabra.")

                fallos += 1

                letras_arriesgadas.append(intento)
        else:  
            if intento == palabra:
                print("\nHas adivinado la palabra.")

                acertada = True
            else:
                print("\nLo siento, la palabra ingresada no es correcta.")

                fallos += 1

        mostrar_estado_juego(palabra, letras_arriesgadas, fallos)

    if fallos == 6:
        print("\nLo siento, has perdido. La palabra era:", palabra)

        puntos = -5
    else:
        puntos = 10

    return puntos

def obtener_palabra_aleatoria():
    return random.choice(palabras.PALABRAS)

