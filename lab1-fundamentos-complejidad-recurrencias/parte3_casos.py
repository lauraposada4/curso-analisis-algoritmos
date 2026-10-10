"""Experimento de la Parte 3: Evaluación de escenarios para Insertion Sort."""

import os
import time

import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento() -> None:
    """Ejecuta Insertion Sort sobre los escenarios A, B y C.

    Evalua 7 tamanos de entrada, mide el tiempo de ejecucion y cuenta
    las comparaciones para generar las graficas comparativas.

    Returns:
        None
    """
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_a, comps_a = [], []
    tiempos_b, comps_b = [], []
    tiempos_c, comps_c = [], []

    print("Iniciando experimento de la Parte 3...")

    for n in tamanos:
        lote_a = generar_aleatorio(n)
        lote_b = generar_casi_ordenado(n)
        lote_c = generar_inverso(n)

        # Escenario A: Aleatorio
        inicio = time.perf_counter()
        _, c_a = insertion_sort(lote_a)
        fin = time.perf_counter()
        tiempos_a.append(fin - inicio)
        comps_a.append(c_a)

        # Escenario B: Casi Ordenado
        inicio = time.perf_counter()
        _, c_b = insertion_sort(lote_b)
        fin = time.perf_counter()
        tiempos_b.append(fin - inicio)
        comps_b.append(c_b)

        # Escenario C: Inverso
        inicio = time.perf_counter()
        _, c_c = insertion_sort(lote_c)
        fin = time.perf_counter()
        tiempos_c.append(fin - inicio)
        comps_c.append(c_c)

        print(f"  Evaluado n = {n}")

    os.makedirs("graficas", exist_ok=True)

    # Gráfica de comparaciones
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, comps_a, marker="o", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, comps_b, marker="s", label="Escenario B (Casi Ordenado)")
    plt.plot(tamanos, comps_c, marker="^", label="Escenario C (Inverso)")
    plt.title("Comparaciones vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número total de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica de tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_a, marker="o", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, tiempos_b, marker="s", label="Escenario B (Casi Ordenado)")
    plt.plot(tamanos, tiempos_c, marker="^", label="Escenario C (Inverso)")
    plt.title("Tiempo de Ejecución vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()

    print("Experimento finalizado. Gráficas guardadas en 'graficas/'.")


if __name__ == "__main__":
    ejecutar_experimento()