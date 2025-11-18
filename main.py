# Importar archivos
from variables import *
from funciones import *
from clases import *
import numpy as np
import random

# ==============================
# PROGRAMA PRINCIPAL
# ==============================
while True:
    print("=== ¡Bienvenido a Hundir la Flota! ===")
    print("Reglas básicas:")
    print("- Tablero de 10x10.")
    print("- Dispara introduciendo fila y columna (0–9).")
    print("- Si aciertas, vuelves a disparar. Si fallas, dispara la máquina.\n")
    nombre = input("Introduce tu nombre: ")

    # Crear tableros: Ya definidas en variables:
    tablero_jugador = crear_tablero()
    tablero_rival = crear_tablero()
    tablero_rival_visible = crear_tablero()


    # Colocar barcos (solo inputs del jugador)
    print(f"\nHola {nombre}, coloca tus barcos en el tablero.")
    print("Tienes:")
    print("- 4 barcos de 1 posición")
    print("- 3 barcos de 2 posiciones")
    print("- 2 barcos de 3 posiciones")
    print("- 1 barco de 4 posiciones")

    barcos = {1: 4, 2: 3, 3: 2, 4: 1}

    for tamaño, cantidad in barcos.items():
        for n in range(cantidad):
            print(f"\nBarco {n+1} de tamaño {tamaño}")

            orientacion = "H"
            if tamaño > 1:
                orientacion = input("Orientación (H horizontal / V vertical): ").upper()

            try:
                fila, col = map(int, input("Introduce la posición inicial (fila,col): ").split(","))
            except:
                print("Formato incorrecto, usa 'fila,col' (ejemplo: 3,5).")
                continue

            try:
                colocar_barco(tablero_jugador, fila, col, tamaño, orientacion)
                print(f"→ Colocado barco de tamaño {tamaño} en ({fila}, {col}) orientado {orientacion}")
                print(tablero_jugador)
            except ValueError as e:
                print(f"❌ {e}")
                print("Intenta colocar de nuevo este barco.")
                continue


    # ---- COLOCAR FLOTA DEL JUGADOR ----
    flota_jugador = []

    # 4 barcos de 1 casilla
    for i in range(4):
        coords = colocar_barco_jugador(tablero_jugador, 1, "barco pequeño", "P")
        flota_jugador.append(coords)

    # 3 barcos de 2 casillas
    for i in range(3):
        coords = colocar_barco_jugador(tablero_jugador, 2, "barco mediano", "M")
        flota_jugador.append(coords)

    # 2 barcos de 3 casillas
    for i in range(2):
        coords = colocar_barco_jugador(tablero_jugador, 3, "barco grande", "G")
        flota_jugador.append(coords)

    # 1 barco de 4 casillas
    coords = colocar_barco_jugador(tablero_jugador, 4, "barco gigante", "E")
    flota_jugador.append(coords)

    # Mostrar flota
    mostrar_flota(flota_jugador)

    print("\n🛳️ Tu tablero queda así:\n")
    mostrar_tablero(tablero_jugador)





 #   for tamaño, cantidad in barcos.items():
 #       for n in range(cantidad):
  #          print(f"\nBarco {n+1} de tamaño {tamaño}")
 #           orientacion = "H"
  #          if tamaño > 1:
  #              orientacion = input("Orientación (H horizontal / V vertical): ").upper()
 #           try:
  #              fila, col = map(int, input("Introduce la posición inicial (fila,col): ").split(","))
  #          except:
  #              print("Formato incorrecto, usa 'fila,col' (ejemplo: 3,5).")
  #              continue
  #          print(f"→ Guardado: Barco de tamaño {tamaño}, orientación {orientacion}, en ({fila}, {col})")

    print("\nColocando barcos del rival aleatoriamente...")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    flota_peq,tablero_rival = flota_peq_aleatorio(tablero_rival)
    flota_med,tablero_rival = flota_med_aleatoria(tablero_rival, flota_peq)
    flota_grand,tablero_rival = flota_grand_aleatoria(tablero_rival, flota_peq,flota_med)
    flota_gigante, tablero_rival =  flota_enorme_aleatoria(tablero_rival, flota_peq,flota_med,flota_grand)
=======
=======
>>>>>>> Stashed changes
    flota_peq, tablero_rival = flota_peq_aleatorio()
    flota_med, tablero_rival = flota_med_aleatoria(tablero_rival, flota_peq)
    flota_grand, tablero_rival = flota_grand_aleatoria(tablero_rival, flota_peq,flota_med)
    flota_gig, tablero_rival = flota_enorme_aleatoria(tablero_rival, flota_peq,flota_med,flota_grand)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    turno_jugador = True

    # ==============================
    # BUCLE DE PARTIDAp
    # ==============================
    while True:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        print(tablero_jugador,'\n', tablero_rival)
=======
        print(tablero_jugador,'/n', tablero_rival_visible)
>>>>>>> Stashed changes
=======
        print(tablero_jugador,'/n', tablero_rival_visible)
>>>>>>> Stashed changes

        if turno_jugador:
            print(f"\nTurno de {nombre}:")
            try:
                fila, col = map(int, input("Introduce las coordenadas para disparar (fila,col): ").split(","))
            except:
                print("Formato incorrecto. Usa el formato fila,col (ejemplo: 3,5).")
                continue

            resultado = disparar(tablero_rival, tablero_rival_visible, fila, col)

            if resultado is True:
                print("🎯 ¡Has acertado! Vuelves a disparar.")
            elif resultado is False:
                print("🌊 Has fallado. Le toca a la máquina.")
                turno_jugador = False
            else:
                print("⚠️ Esa posición ya fue atacada, el turno pasa igualmente.")
                turno_jugador = False

            if comprobar_derrota(tablero_rival):
                print(f"🎉 ¡{nombre} ha ganado! Todos los barcos enemigos han sido hundidos.")
                break

        else:
            print("\nTurno de la máquina:")
            resultado = disparo_rival(tablero_jugador)

            if resultado:
                print("💥 La máquina ha acertado y repite turno.")
                turno_jugador = False
            else:
                print("💧 La máquina ha fallado. Te toca a ti.")
                turno_jugador = True

            if comprobar_derrota(tablero_jugador):
                print("💀 ¡La máquina ha ganado! Todos tus barcos han sido hundidos.")
                break

    # ==============================
    # FIN DE PARTIDA / REINICIO
    # ==============================
    print("\nPartida terminada.")
    calcular_estadisticas(tablero_jugador)
    calcular_estadisticas(tablero_rival)
    
    opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if opcion != "s":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nReiniciando partida...\n")
