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

    # Crear tableros
    tablero_jugador = crear_tablero(filas=10, columnas=10)    
    tablero_rival = crear_tablero(filas=10, columnas=10)
    tablero_rival_visible = crear_tablero(filas=10, columnas=10)

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
            print(f"→ Guardado: Barco de tamaño {tamaño}, orientación {orientacion}, en ({fila}, {col})")

    print("\nColocando barcos del rival aleatoriamente...")
    flota_peq_aleatorio()
    flota_med_aleatoria(tablero_rival, flota_peq)
    flota_grand_aleatoria(tablero_rival, flota_peq,flota_med)

    turno_jugador = True

    # ==============================
    # BUCLE DE PARTIDA
    # ==============================
    while True:
        print(tablero_jugador/n, tablero_rival_visible)

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
    calcular_estadisticas(tablero)
    calcular_estadisticas(tablero_rival)
    
    opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if opcion != "s":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nReiniciando partida...\n")
