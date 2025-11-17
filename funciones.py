# Aquí irán las funciones
import numpy as np
import random
tablero = np.zeros((10, 10), dtype=int) # Crear un tablero de 10x10 lleno de ceros

import numpy as np

# Convención de códigos:
AGUA = 0
BARCO = 1
IMPACTO = 2
FALLO = 3

def crear_tablero(filas=10, columnas=10):
  
    # Crea un tablero vacío usando NumPy.
    # Cada casilla empieza como AGUA (0).
 
    return np.full((filas, columnas), AGUA , dtype=int)

def colocar_barco(tablero, fila, columna, longitud, orientacion): 
   
    # Coloca un barco en el tablero NumPy.
    # Orientacion: 'H' (horizontal) o 'V' (vertical).
    # Lanza ValueError si se sale del tablero o pisa otro barco.
  
    filas, columnas = tablero.shape

    if orientacion == "H":
        if columna + longitud > columnas:
            raise ValueError("El barco se sale del tablero (horizontal).")

        zona = tablero[fila, columna:columna + longitud]
        if np.any(zona != AGUA):
            raise ValueError("Casilla ocupada al colocar el barco (horizontal).")

        tablero[fila, columna:columna + longitud] = BARCO

    elif orientacion == "V":
        if fila + longitud > filas:
            raise ValueError("El barco se sale del tablero (vertical).")

        zona = tablero[fila:fila + longitud, columna]
        if np.any(zona != AGUA):
            raise ValueError("Casilla ocupada al colocar el barco (vertical).")

        tablero[fila:fila + longitud, columna] = BARCO

    else:
        raise ValueError("La orientación debe ser 'H' o 'V'.")
    return tablero
def calcular_estadisticas(tablero):
   
    # Calcula estadísticas básicas del tablero:
        # - total_disparos
        # - impactos (IMPACTO)
        # - fallos (FALLO)
        # - precision (impactos / total_disparos)
        # - casillas_barco (total de celdas con BARCO o IMPACTO)
   
    impactos = np.count_nonzero(tablero == IMPACTO)
    fallos = np.count_nonzero(tablero == FALLO)
    total_disparos = impactos + fallos

    # Barcos aún enteros + barcos impactados
    casillas_barco = np.count_nonzero((tablero == BARCO) | (tablero == IMPACTO))

    precision = impactos / total_disparos if total_disparos > 0 else 0.0

    return {
        "total_disparos": total_disparos,
        "impactos": impactos,
        "fallos": fallos,
        "precision": precision,
        "casillas_barco_totales": casillas_barco,
    }

def mostrar_tablero(tablero, mostrar_barcos=True):
   
    # Muestra el tablero por consola.
    # Si mostrar_barcos es False, los BARCO se ven como agua (para ocultarlos al rival).
    
    simbolos = {
        AGUA: "~",
        BARCO: "B" if mostrar_barcos else "~",
        IMPACTO: "X",
        FALLO: "O",
    }

    filas, columnas = tablero.shape
    print("   " + " ".join(str(c) for c in range(1,columnas+1)))
    for f in range(filas):
        fila_str = " ".join(simbolos[val] for val in tablero[f])
        if f <= 8:
            print(f" {f+1} {fila_str}")
        elif f == 9:
            print(f"{f+1} {fila_str}")

def disparar(tablero_rival, tablero_rival_2, fila, col):
    # Devuelve True si acierta, False si falla, None si ya disparó ahí.
    if tablero_rival[fila, col] == "O":
        tablero_rival[fila, col] = "X"
        tablero_rival_2[fila, col] = "X"
        print(f"¡Impacto en ({fila}, {col})!")
        print(tablero_rival_2)
        return True
    elif tablero_rival[fila, col] == " ":
        tablero_rival[fila, col] = "-"
        tablero_rival_2[fila, col] = "-"
        print(f"Agua en ({fila}, {col}).")
        print(tablero_rival_2)
        return False
    else:
        print(f"Ya se disparó en ({fila}, {col}).")
        return None

def disparo_rival(tablero):
    filas, cols = tablero.shape
    while True:
        fila = random.randint(0, filas - 1)
        col = random.randint(0, cols - 1)

        if tablero[fila, col] in ["O", " "]:
            if tablero[fila, col] == "O":
                tablero[fila, col] = "X"
                print(f"¡Impacto en ({fila}, {col})!")
                print(tablero)
                return True
            else:
                tablero[fila, col] = "-"
                print(f"Agua en ({fila}, {col}).")
                print(tablero)
                return False
if __name__ == "__main__":
    # 1. Crear tablero vacío
    tablero = crear_tablero(10, 10)
    print("Tablero vacío:")
    mostrar_tablero(tablero)
    print()

    # 2. Colocar un barco horizontal
    print("Colocando barco horizontal en (fila=2, col=3) longitud 4...")
    colocar_barco(tablero, fila=2, columna=3, longitud=4, orientacion="H")
    mostrar_tablero(tablero)
    print()

    # 3. Colocar un barco vertical
    print("Colocando barco vertical en (fila=5, col=0) longitud 3...")
    colocar_barco(tablero, fila=5, columna=0, longitud=3, orientacion="V")
    mostrar_tablero(tablero)
    print()

    # 4. Intentar colocar un barco que se sale del tablero (debe dar error)
    print("Intentando colocar barco que se sale del tablero...")
    try:
        colocar_barco(tablero, fila=9, columna=8, longitud=4, orientacion="H")
    except ValueError as e:
        print("✅ Error controlado:", e)
    else:
        print("❌ No se ha producido error y debería haberse producido.")
    print()

    # 5. Intentar solapar barcos (debe dar error)
    print("Intentando solapar un barco sobre otro...")
    try:
        colocar_barco(tablero, fila=2, columna=4, longitud=3, orientacion="H")
    except ValueError as e:
        print("✅ Error controlado:", e)
    else:
        print("❌ No se ha producido error y debería haberse producido.")
    print()
