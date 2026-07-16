"""
TP 2
Grande Valentino, Gibbons Francisco, Figueroa Casas Felipe, Girardi Miqueas.

jugadores: [str]
rachas_mayor_menor: [int]
mayor_menor_jugadas: [int]
secreto_jugadas: [int]
secreto_ganadas: [int]
secreto_perdidas: [int]
blackjack_jugadas: [int]
blackjack_ganadas: [int]
parimpar_jugadas: [int]
parimpar_aciertos: [int]
creditos: [int]
numero_maximo_intentos_secreto: int
RED: str
DARK_RED: str
BOLD: str
RESET: str
WHITE: str
texto: str
"""

import os
import random

# lista de jugadores, maximo 10, compartida por todos los juegos
jugadores = []

# datos de cada jugador, mismo indice que en la lista jugadores
rachas_mayor_menor = []
mayor_menor_jugadas = []

secreto_jugadas = []
secreto_ganadas = []
secreto_perdidas = []

blackjack_jugadas = []
blackjack_ganadas = []

parimpar_jugadas = []
parimpar_aciertos = []
creditos = []

numero_maximo_intentos_secreto = 6

RED = "\033[91m"
DARK_RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"
WHITE = "\033[97m"

texto = f"""
{RED}{BOLD}
+==============================================================+
|  ██╗    ██╗ █████╗ ██████╗ ███╗  ██╗██╗███╗  ██╗ ██████╗    |
|  ██║    ██║██╔══██╗██╔══██╗████╗ ██║██║████╗ ██║██╔════╝    |
|  ██║ █╗ ██║███████║██████╔╝██╔██╗██║██║██╔██╗██║██║  ███╗   |
|  ██║███╗██║██╔══██║██╔══██╗██║╚████║██║██║╚████║██║   ██║   |
|  ╚███╔███╔╝██║  ██║██║  ██║██║ ╚███║██║██║ ╚███║╚██████╔╝   |
|   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝╚═╝  ╚══╝ ╚═════╝    |
+==============================================================+
{RESET}

{DARK_RED}{BOLD}
+==============================================================+
|   ⚠   LOS JUEGOS DE APUESTA ESTAN PROHIBIDOS               |
|        PARA LOS MENORES DE EDAD   ⚠                         |
+--------------------------------------------------------------+
|        ⚠   PERJUDICIAL PARA LA SALUD   ⚠                    |
+--------------------------------------------------------------+
|  [!] Genera adiccion y dependencia psicologica              |
|  [!] Provoca perdidas economicas graves                     |
|  [!] Destruye vinculos familiares y sociales                |
|  [!] Causa ansiedad, depresion y estres cronico             |
|  [!] Riesgo de endeudamiento y ruina financiera             |
+==============================================================+
{RESET}

{WHITE}{BOLD}
>>> LINEA 800 - JUEGO RESPONSABLE <<<
{RESET}
"""


def clear():
    if os.name == "nt":  # windows
        os.system("cls")
    elif os.name == "posix":  # unix
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")


def pedir_jugador() -> int:
    nombre = input("Ingrese su nombre (2 o mas caracteres): ")

    while len(nombre) < 2:
        nombre = input("Ingrese su nombre (2 o mas caracteres): ")

    if nombre in jugadores:
        # es un jugador que ya entro antes
        indice = jugadores.index(nombre)
        print("Bienvenido de nuevo", nombre)

    else:
        # we can not add one more player
        if len(jugadores) == 10:
            print("No hay cupos para un nuevo jugador")
            indice = -1

        else:
            jugadores.append(nombre)
            rachas_mayor_menor.append(0)
            mayor_menor_jugadas.append(0)
            secreto_jugadas.append(0)
            secreto_ganadas.append(0)
            secreto_perdidas.append(0)
            blackjack_jugadas.append(0)
            blackjack_ganadas.append(0)
            parimpar_jugadas.append(0)
            parimpar_aciertos.append(0)
            creditos.append(1000)
            indice = len(jugadores) - 1

    return indice


def mayor_menor():

    indice = pedir_jugador()

    if indice == -1:
        input("Presione enter para continuar...")
        return

    nombre = jugadores[indice]
    mayor_menor_jugadas[indice] += 1

    racha_juego = 0
    juego_terminado = False

    numero = random.randint(1, 1000)

    while not juego_terminado:

        siguiente_numero = random.randint(1, 1000)

        while siguiente_numero == numero:
            siguiente_numero = random.randint(1, 1000)

        print("Numero actual:", numero)

        opcion = input("El siguiente numero sera mayor o menor?: ").lower()

        while opcion != "mayor" and opcion != "menor":
            opcion = input("Ingrese mayor o menor: ").lower()

        acerto = (opcion == "menor" and siguiente_numero < numero) or (
            opcion == "mayor" and siguiente_numero > numero
        )

        if acerto:

            print("Correcto! El numero era:", siguiente_numero)

            racha_juego += 1
            numero = siguiente_numero

        else:
            print("El juego esta terminado. El numero era:", siguiente_numero)
            juego_terminado = True

    print(nombre, "tu racha fue de:", racha_juego)

    if racha_juego > rachas_mayor_menor[indice]:
        rachas_mayor_menor[indice] = racha_juego

    input("Presione enter para continuar...")


def numero_secreto():

    indice = pedir_jugador()

    if indice == -1:
        input("Presione enter para continuar...")
        return

    secreto_jugadas[indice] += 1

    secreto = random.randint(1, 100)

    numero_intento = 0
    victoria = False

    while numero_intento < numero_maximo_intentos_secreto and not victoria:

        print(
            "Intentos restantes:",
            numero_maximo_intentos_secreto - numero_intento,
        )

        valido = False
        intento = 0

        while not valido:

            try:

                intento = int(input("Ingrese un numero entre 1 y 100: "))

                if intento < 1 or intento > 100:
                    print("El numero debe estar entre 1 y 100")

                else:
                    valido = True

            except ValueError:
                print("Ingrese un entero valido")

        numero_intento += 1

        if intento == secreto:

            victoria = True

        else:

            if intento < secreto:
                print("El numero secreto es mayor")

            else:
                print("El numero secreto es menor")

    if victoria:

        secreto_ganadas[indice] += 1
        print("Ganaste! Te llevo", numero_intento, "intentos")

    else:

        secreto_perdidas[indice] += 1
        print("Perdiste")
        print("El numero era:", secreto)

    input("Presione enter para continuar...")


def armar_mazo() -> [str]:
    # un solo mazo de 52 cartas, 4 palos y 13 cartas por palo
    palos = ["corazones", "diamantes", "picas", "treboles"]
    numeros = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    mazo = []

    for palo in palos:
        for numero in numeros:
            mazo.append(numero + " de " + palo)

    return mazo


def sacar_carta(mazo: [str]) -> str:
    # se saca la carta del mazo asi no puede salir repetida
    indice_carta = random.randint(0, len(mazo) - 1)
    carta = mazo[indice_carta]
    mazo.pop(indice_carta)
    return carta


def sumar_puntos(cartas: [str]) -> int:
    total = 0
    ases = 0

    for carta in cartas:
        numero = carta.split(" ")[0]

        if numero == "J" or numero == "Q" or numero == "K":
            total += 10

        elif numero == "A":
            total += 11
            ases += 1

        else:
            total += int(numero)

    # el As deja de valer 11 y pasa a valer 1 si nos pasamos de 21
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


def blackjack():

    indice = pedir_jugador()

    if indice == -1:
        input("Presione enter para continuar...")
        return

    nombre = jugadores[indice]

    jugar_otra = True

    while jugar_otra:

        mazo = armar_mazo()

        cartas_jugador = [sacar_carta(mazo), sacar_carta(mazo)]
        cartas_banca = [sacar_carta(mazo), sacar_carta(mazo)]

        blackjack_jugadas[indice] += 1

        puntos_jugador = sumar_puntos(cartas_jugador)
        puntos_banca = sumar_puntos(cartas_banca)

        print("\nCartas de la banca:", cartas_banca[0], "y", cartas_banca[1])
        print("Tus cartas:", cartas_jugador[0], "y", cartas_jugador[1])
        print("Tus puntos:", puntos_jugador)

        se_paso = False
        turno_jugador = puntos_jugador < 21

        while turno_jugador:

            opcion = input("Queres pedir o plantarte? (pedir/plantarse): ").lower()

            while opcion != "pedir" and opcion != "plantarse":
                opcion = input("Ingrese pedir o plantarse: ").lower()

            if opcion == "pedir":

                carta = sacar_carta(mazo)
                cartas_jugador.append(carta)
                puntos_jugador = sumar_puntos(cartas_jugador)

                print("Sacaste:", carta)
                print("Tus puntos:", puntos_jugador)

                if puntos_jugador > 21:
                    se_paso = True
                    turno_jugador = False

                elif puntos_jugador == 21:
                    turno_jugador = False

            else:
                turno_jugador = False

        if se_paso:
            print("Te pasaste de 21. Gana la banca")

        else:

            # la banca pide con 16 o menos y se planta con 17 o mas
            while puntos_banca <= 16:
                carta = sacar_carta(mazo)
                cartas_banca.append(carta)
                puntos_banca = sumar_puntos(cartas_banca)
                print("La banca saco:", carta)

            print("Puntos de la banca:", puntos_banca)
            print("Tus puntos:", puntos_jugador)

            if puntos_banca > 21:
                print("La banca se paso de 21. Ganaste", nombre)
                blackjack_ganadas[indice] += 1

            elif puntos_jugador > puntos_banca:
                print("Ganaste", nombre)
                blackjack_ganadas[indice] += 1

            elif puntos_banca > puntos_jugador:
                print("Gana la banca")

            else:
                print("Empate")

        respuesta = input("Queres jugar otra partida? (si/no): ").lower()

        while respuesta != "si" and respuesta != "no":
            respuesta = input("Ingrese si o no: ").lower()

        jugar_otra = respuesta == "si"


def par_impar():

    indice = pedir_jugador()

    if indice == -1:
        input("Presione enter para continuar...")
        return

    nombre = jugadores[indice]

    if creditos[indice] == 0:
        print(nombre, "te quedaste sin credito, ya no podes jugar")
        input("Presione enter para continuar...")
        return

    print("Tu credito es de: $", creditos[indice])

    apuesta_valida = False
    apuesta = 0

    while not apuesta_valida:

        try:

            apuesta = int(input("Cuanto queres apostar?: "))

            if apuesta < 1:
                print("La apuesta debe ser mayor a 0")

            elif apuesta > creditos[indice]:
                print("No podes apostar mas de lo que tenes")

            else:
                apuesta_valida = True

        except ValueError:
            print("Ingrese un entero valido")

    numero1 = random.randint(1, 6)
    numero2 = random.randint(1, 6)

    opcion = input("Par o impar?: ").lower()

    while opcion != "par" and opcion != "impar":
        opcion = input("Ingrese par o impar: ").lower()

    suma = numero1 + numero2

    print("Los numeros fueron:", numero1, "y", numero2)
    print("La suma es:", suma)

    suma_es_par = suma % 2 == 0
    gano = (opcion == "par" and suma_es_par) or (
        opcion == "impar" and not suma_es_par
    )

    parimpar_jugadas[indice] += 1

    if gano:

        print(nombre, "ganaste")
        parimpar_aciertos[indice] += 1
        creditos[indice] += apuesta

    else:

        print(nombre, "perdiste")
        creditos[indice] -= apuesta

    print("Tu credito ahora es: $", creditos[indice])

    input("Presione enter para continuar...")


def ordenar_y_mostrar(nombres: [str], valores: [int], descendente: bool):

    if len(nombres) == 0:
        print("Todavia no hay jugadores")

    n = len(valores)

    # metodo del falso burbuja, ordenamos las dos listas a la vez
    # para creciente o decreciente solo cambia el signo de la comparacion
    for i in range(n - 1):
        for j in range(i + 1, n):

            hay_que_cambiar = False

            if descendente:
                if valores[i] < valores[j]:
                    hay_que_cambiar = True
            else:
                if valores[i] > valores[j]:
                    hay_que_cambiar = True

            if hay_que_cambiar:
                aux = valores[i]
                valores[i] = valores[j]
                valores[j] = aux

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

    for i in range(len(nombres)):
        print(i + 1, "-", nombres[i], ":", valores[i])


def reporte():

    valid = ["a", "b", "c", "d", "e"]
    opcion = ""

    while opcion != "e":

        clear()

        print("""
    ===== REPORTE =====

    [*] A. Ranking de victorias por juego
    [*] B. Juegos jugados por un jugador
    [*] C. Jugadores de par o impar segun su credito
    [*] D. Racha de un jugador en mayor o menor
    [*] E. Volver al menu principal
    """)

        opcion = input("Ingrese una opcion: ").lower()

        while opcion not in valid:
            opcion = input("Ingrese una opcion: ").lower()

        if opcion == "a":

            # ordenados de mayor a menor por victorias, excepto mayor/menor
            print("\n[*] Numero secreto")
            ordenar_y_mostrar(jugadores.copy(), secreto_ganadas.copy(), True)

            print("\n[*] BlackJack")
            ordenar_y_mostrar(jugadores.copy(), blackjack_ganadas.copy(), True)

            print("\n[*] Par o impar")
            ordenar_y_mostrar(jugadores.copy(), parimpar_aciertos.copy(), True)

            input("\nPresione enter para continuar...")

        elif opcion == "b":

            nombre = input("Ingrese el nombre del jugador: ")

            if nombre not in jugadores:
                print("Ese jugador no existe")

            else:

                indice = jugadores.index(nombre)
                jugo_algo = False

                print("\nJuegos jugados por", nombre)

                if mayor_menor_jugadas[indice] > 0:
                    jugo_algo = True
                    print("\n[*] Mayor o menor")
                    print("Partidas:", mayor_menor_jugadas[indice])
                    print("Mejor racha:", rachas_mayor_menor[indice])

                if secreto_jugadas[indice] > 0:
                    jugo_algo = True
                    print("\n[*] Numero secreto")
                    print("Partidas:", secreto_jugadas[indice])
                    print("Ganadas:", secreto_ganadas[indice])
                    print("Perdidas:", secreto_perdidas[indice])

                if blackjack_jugadas[indice] > 0:
                    jugo_algo = True
                    print("\n[*] BlackJack")
                    print("Partidas:", blackjack_jugadas[indice])
                    print("Ganadas:", blackjack_ganadas[indice])

                if parimpar_jugadas[indice] > 0:
                    jugo_algo = True
                    print("\n[*] Par o impar")
                    print("Partidas:", parimpar_jugadas[indice])
                    print("Aciertos:", parimpar_aciertos[indice])
                    print("Credito: $", creditos[indice])

                if not jugo_algo:
                    print(nombre, "todavia no jugo a ningun juego")

            input("\nPresione enter para continuar...")

        elif opcion == "c":

            # solo los que jugaron al par o impar, de menor a mayor credito
            nombres_parimpar = []
            creditos_parimpar = []

            for i in range(len(jugadores)):
                if parimpar_jugadas[i] > 0:
                    nombres_parimpar.append(jugadores[i])
                    creditos_parimpar.append(creditos[i])

            print("\n[*] Jugadores de par o impar segun su credito")

            if len(nombres_parimpar) == 0:
                print("Todavia nadie jugo al par o impar")
            else:
                ordenar_y_mostrar(nombres_parimpar, creditos_parimpar, False)

            input("\nPresione enter para continuar...")

        elif opcion == "d":

            nombre = input("Ingrese el nombre del jugador: ")

            if nombre not in jugadores:
                print("Ese jugador no existe")

            else:
                indice = jugadores.index(nombre)

                if mayor_menor_jugadas[indice] ==0:
                    print(nombre, "todavia no jugo al mayor o menor")
                else:
                    print("La racha de", nombre, "en mayor o menor es:", rachas_mayor_menor[indice])

            input("\nPresione enter para continuar...")


def main():
    valid = ["a","b","c","d","e","f"]

    clear()

    print(texto)

    input("Presione enter para jugar...")

    option = ""

    while option != "f":
        clear()

        print("""
    [*] A. Juego de mayor o menor
    [*] B. Adivinar el numero secreto
    [*] C. BlackJack
    [*] D. Par o impar
    [*] E. Reporte
    [*] F. Salir
    """)

        option = input("Ingrese una opcion: ").lower()

        while option not in valid:
            option = input("Ingrese una opcion: ").lower()

        match option:

            case "a": mayor_menor()

            case "b": numero_secreto()

            case "c": blackjack()

            case "d": par_impar()

            case "e": reporte()

            case "f":

                clear()

                print("""
+==============================================================+
|                                                              |
|   Gracias por jugar, no apueste, juega por diversion         |
|                                                              |
+==============================================================+
    """)

                input("Presione enter para salir...")



if __name__ == '__main__':
    main()
