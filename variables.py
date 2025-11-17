# Donde están declaradas las constantes
# variables.py
import numpy as np
import random

# Barcos (nombre: eslora)
BARCOS = {
    "barco_1": 1,
    "barco_2": 1,
    "barco_3": 1,
    "barco_4": 1,
    "barco_5": 2,
    "barco_6": 2,
    "barco_7": 2,
    "barco_8": 3,
    "barco_9": 3,
    "barco_10": 4,
}

# Tableros
tablero_jugador = np.full((10, 10), " ")
tablero_rival = np.full((10, 10), " ")
tablero_rival_visible = np.full((10, 10), " ")

# Convención de códigos:
AGUA = "~"  # casilla sin disparar ni barco
BARCO = "B"  # casilla con barco intacto (solo en tablero propio)
IMPACTO = "X" # casilla con barco impactado
FALLO = "O"  # casilla donde se disparó y no había barco
