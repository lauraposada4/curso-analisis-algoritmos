"""Experimento de la Parte 4: Comparacion entre Insertion Sort y Merge Sort."""

import os
import time

import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento_comparativo() -> None:
    """Compara el tiempo de ejecucion de Insertion Sort y Merge Sort.

    Mide sobre el Escenario A (Aleatorio) para 7 tamanos de entrada
    y genera la grafica comparativa de tiempos de ejecucion.

    Returns:
        None
    """
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    print("Iniciando experimento comparativo de la Parte 4...")

    for n in tamanos:
        lote = generar_aleatorio(n)

        inicio = time.perf_counter()
        insertion_sort(lote)
        fin = time.perf_counter()
        tiempos_insertion.append(fin - inicio)

        inicio = time.perf_counter()
        merge_sort(lote)
        fin = time.perf_counter()
        tiempos_merge.append(fin - inicio)

        print(f"  Evaluado n = {n}")

    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        color="tab:red",
        label="Insertion Sort O(n²)",
    )
    plt.plot(
        tamanos,
        tiempos_merge,
        marker="s",
        color="tab:blue",
        label="Merge Sort O(n log n)",
    )
    plt.title("Tiempo de Ejecución vs. Tamaño de Entrada (Escenario A)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()

    print("Experimento comparativo finalizado. Gráfica guardada.")


if __name__ == "__main__":
    ejecutar_experimento_comparativo()