"Nombres"

import os
import random

racha_global_juego_1 = 0

victorias_juego_par_impar = 0
derrotas_juego_par_impar = 0

cant_mayor_menor = 0

cant_numero_secreto = 0
victorias_numero_secreto = 0
derrotas_numero_secreto = 0

numero_maximo_intentos_secreto = 6


def clear():
    if os.name == "nt":  # windows
        os.system("cls")
    elif os.name == "posix":  # unix
        os.system("clear")
    else:
        print("No se puede limpiar la pantalla")   

def ask_name(players: [str]) -> int:
    name = input("Cual es tu nombre? ")

    # we can not add one more player
    if players.len() == 10:
        return 1

    else:
        if name not in players:
            players.append(name)
        return 0


def mayor_menor(played: int, players: [str]):
    
    played += 1
    if ask_name(players) == 0:
        
     
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
                juego_terminado = True

        print(nombre, "tu racha fue de:", racha_juego)

        if racha_juego > racha_global_juego_1:
            racha_global_juego_1 = racha_juego

        input("Presione enter para continuar...")



def main():
    valid = ["a","b","c","d","e","f"]
    players = [""] * 10
    
    input("presione enter para jugar...")
    
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

            case "b":

                cant_numero_secreto += 1

                while not nombre_pedido or len(nombre) < 2:
                    nombre = input("Ingrese su nombre (2 o mas caracteres): ")
                    nombre_pedido = True

                secreto = random.randint(1, 100)

                numero_intento = 0
                victoria = False

                while numero_intento < numero_maximo_intentos_secreto and not victoria:

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

                        print(
                            "Intentos restantes:",
                            numero_maximo_intentos_secreto - numero_intento,
                        )

                if victoria:

                    victorias_numero_secreto += 1
                    print("Ganaste!")

                else:

                    derrotas_numero_secreto += 1
                    print("Perdiste")
                    print("El numero era:", secreto)

                input("Presione enter para continuar...")

            case "c":

                print("BlackJack en desarrollo")
                input("Presione enter para continuar...")

            case "d":

                while not nombre_pedido or len(nombre) < 2:
                    nombre = input("Ingrese su nombre (2 o mas caracteres): ")
                    nombre_pedido = True

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

                if gano:

                    print(nombre, "ganaste")
                    victorias_juego_par_impar += 1

                else:

                    print(nombre, "perdiste")
                    derrotas_juego_par_impar += 1

                input("Presione enter para continuar...")

            case "e":

                print("\n===== REPORTE =====")

                print("Jugador:", nombre)

                print("\n[*] Mayor o menor")
                print("Partidas jugadas:", cant_mayor_menor)
                print("Mayor racha:", racha_global_juego_1)

                print("\n[*] Numero secreto")
                print("Partidas jugadas:", cant_numero_secreto)
                print("Victorias:", victorias_numero_secreto)
                print("Derrotas:", derrotas_numero_secreto)

                print("\n[*] Par o impar")
                print(
                    "Partidas jugadas:",
                    victorias_juego_par_impar + derrotas_juego_par_impar,
                )
                print("Victorias:", victorias_juego_par_impar)
                print("Derrotas:", derrotas_juego_par_impar)

                input("\nPresione enter para continuar...")

            case "f":

                print("Gracias por jugar")
                print("No apueste. Juegue por diversion")           

            

if __name__ == '__main__':
    main()
