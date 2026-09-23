"""Experimento Parte 4: Comparación de tiempo de ejecución entre Insertion Sort y Merge Sort."""

import os
import time

import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento_comparativo() -> None:
    """Mide el tiempo de ejecución de Insertion Sort y Merge Sort sobre el Escenario A

    (Aleatorio) para 7 tamaños de entrada y genera la gráfica comparativa.
    """
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    print("Iniciando experimento comparativo (Parte 4)...")

    for n in tamanos:
        # Generar lote Escenario A (Aleatorio)
        lote = generar_aleatorio(n)

        # Medir tiempo para Insertion Sort
        inicio = time.perf_counter()
        insertion_sort(lote)
        fin = time.perf_counter()
        tiempos_insertion.append(fin - inicio)

        # Medir tiempo para Merge Sort
        inicio = time.perf_counter()
        merge_sort(lote)
        fin = time.perf_counter()
        tiempos_merge.append(fin - inicio)

        print(f"  Evaluado n = {n}")

    os.makedirs("graficas", exist_ok=True)

    # Gráfica comparativa de tiempos de ejecución
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

    print("Experimento finalizado con éxito.")
    print("Gráfica guardada en 'graficas/parte4_tiempo.png'.")


if __name__ == "__main__":
    ejecutar_experimento_comparativo()