# Donde están declaradas las constantes
# variables.py
import numpy as np
import random

# Barcos (nombre: eslora)
barco_2 = [(0,1), (1,1)]
barco_4 = [(1,3), (1,4), (1,5), (1,6)]

# Tableros
tablero_jugador = np.full((10, 10), " ")
tablero_rival = np.full((10, 10), " ")
tablero_rival_visible = np.full((10, 10), " ")

# Convención de códigos:
AGUA = "~"  # casilla sin disparar ni barco
BARCO = "B"  # casilla con barco intacto (solo en tablero propio)
IMPACTO = "X" # casilla con barco impactado
FALLO = "O"  # casilla donde se disparó y no había barco
