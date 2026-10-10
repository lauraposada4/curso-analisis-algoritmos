"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla para reproducibilidad del experimento.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)
    datos = list(range(1, n + 1))
    random.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: Cantidad de registros del lote.
        semilla: Semilla para reproducibilidad del experimento.

    Returns:
        Lista de n indices de riesgo distintos, con el primer 98% en
        orden descendente y el 2% restante desordenado al final.
    """
    random.seed(semilla)
    datos = list(range(n, 0, -1))

    limite = int(n * 0.98)
    parte_ordenada = datos[:limite]
    parte_desordenada = datos[limite:]

    random.shuffle(parte_desordenada)
    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: Cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en orden
        ascendente (inverso al objetivo descendente de Tamiza).
    """
    return list(range(1, n + 1))