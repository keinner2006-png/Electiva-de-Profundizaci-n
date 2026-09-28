import pygame
import sys

# ============================================================
# INICIAR PYGAME
# ============================================================

pygame.init()


# ============================================================
# CONFIGURACIÓN DEL MAPA
# ============================================================

# Cada cuadrado tendrá 50 píxeles
TAMANO_CUADRADO = 50

# Nuestro mapa tiene:
# 13 columnas
# 8 filas
COLUMNAS = 13
FILAS = 8

# Calculamos automáticamente el tamaño de la ventana
ANCHO = COLUMNAS * TAMANO_CUADRADO
ALTO = FILAS * TAMANO_CUADRADO


# ============================================================
# CREAR VENTANA
# ============================================================

pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Bomberman - Mapa 1")

reloj = pygame.time.Clock()


# ============================================================
# COLORES
# ============================================================

VERDE = (40, 180, 50)
VERDE_BORDE = (25, 120, 30)

GRIS = (150, 150, 150)
GRIS_BORDE = (30, 30, 30)

NEGRO = (0, 0, 0)


# ============================================================
# MAPA
# ============================================================

# 0 = CAMINO VERDE
# 1 = PARED GRIS

mapa = [

    # 0
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    # 1
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],

    # 2
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],

    # 3
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],

    # 4
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],

    # 5
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],

    # 6
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],

    # 7
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# ============================================================
# FUNCIÓN PARA DIBUJAR EL MAPA
# ============================================================

def dibujar_mapa():

    # Recorremos cada fila
    for fila in range(FILAS):

        # Recorremos cada columna
        for columna in range(COLUMNAS):

            # Calculamos la posición del cuadrado
            x = columna * TAMANO_CUADRADO
            y = fila * TAMANO_CUADRADO

            # ------------------------------------------------
            # SI ES UNA PARED
            # ------------------------------------------------

            if mapa[fila][columna] == 1:

                # Dibujamos el cuadrado gris
                pygame.draw.rect(
                    pantalla,
                    GRIS,
                    (
                        x,
                        y,
                        TAMANO_CUADRADO,
                        TAMANO_CUADRADO
                    )
                )

                # Dibujamos el borde
                pygame.draw.rect(
                    pantalla,
                    GRIS_BORDE,
                    (
                        x,
                        y,
                        TAMANO_CUADRADO,
                        TAMANO_CUADRADO
                    ),
                    2
                )

            # ------------------------------------------------
            # SI ES CAMINO
            # ------------------------------------------------

            else:

                # Dibujamos el cuadrado verde
                pygame.draw.rect(
                    pantalla,
                    VERDE,
                    (
                        x,
                        y,
                        TAMANO_CUADRADO,
                        TAMANO_CUADRADO
                    )
                )

                # Dibujamos una línea verde oscura
                pygame.draw.rect(
                    pantalla,
                    VERDE_BORDE,
                    (
                        x,
                        y,
                        TAMANO_CUADRADO,
                        TAMANO_CUADRADO
                    ),
                    1
                )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

while True:

    # Revisar eventos
    for evento in pygame.event.get():

        # Cerrar la ventana
        if evento.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


    # --------------------------------------------------------
    # FONDO
    # --------------------------------------------------------

    pantalla.fill(VERDE)


    # --------------------------------------------------------
    # DIBUJAR MAPA
    # --------------------------------------------------------

    dibujar_mapa()


    # --------------------------------------------------------
    # ACTUALIZAR PANTALLA
    # --------------------------------------------------------

    pygame.display.flip()


    # Mantener 60 FPS
    reloj.tick(60)