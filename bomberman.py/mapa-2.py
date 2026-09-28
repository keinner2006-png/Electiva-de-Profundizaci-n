import pygame
import sys

# ============================================================
# INICIAR PYGAME
# ============================================================

pygame.init()


# ============================================================
# CONFIGURACIÓN
# ============================================================

TAMANO_CUADRADO = 50

COLUMNAS = 13
FILAS = 8

ANCHO = COLUMNAS * TAMANO_CUADRADO
ALTO = FILAS * TAMANO_CUADRADO

pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Bomberman - Mapa 2")

reloj = pygame.time.Clock()


# ============================================================
# COLORES
# ============================================================

VERDE = (40, 180, 50)
VERDE_BORDE = (25, 120, 30)

GRIS = (150, 150, 150)
GRIS_BORDE = (30, 30, 30)


# ============================================================
# MAPA 2
# ============================================================
#
# 0 = CAMINO VERDE
# 1 = PARED GRIS
#
# ============================================================

mapa = [

    # FILA 0
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    # FILA 1
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],

    # FILA 2
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],

    # FILA 3
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],

    # FILA 4
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],

    # FILA 5
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],

    # FILA 6
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],

    # FILA 7
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# ============================================================
# FUNCIÓN PARA DIBUJAR EL MAPA
# ============================================================

def dibujar_mapa():

    for fila in range(FILAS):

        for columna in range(COLUMNAS):

            # Posición del cuadrado
            x = columna * TAMANO_CUADRADO
            y = fila * TAMANO_CUADRADO

            # ------------------------------------------------
            # PARED
            # ------------------------------------------------

            if mapa[fila][columna] == 1:

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

                # Borde negro/gris oscuro
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
            # CAMINO
            # ------------------------------------------------

            else:

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

                # Línea del cuadrado
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

        if evento.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    # Fondo
    pantalla.fill(VERDE)

    # Dibujar mapa
    dibujar_mapa()

    # Mostrar en pantalla
    pygame.display.flip()

    # 60 FPS
    reloj.tick(60)