"""Experimento de la Parte 3: Evaluación de peor, mejor y caso promedio para Insertion Sort."""

import os
import time

import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


def ejecutar_experimento() -> None:
    """Ejecuta insertion_sort sobre los tres escenarios para 7 tamaños de entrada

    y genera las gráficas comparativas de tiempo y comparaciones.
    """
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_A, comps_A = [], []
    tiempos_B, comps_B = [], []
    tiempos_C, comps_C = [], []

    print("Iniciando mediciones del experimento (Parte 3)...")

    for n in tamanos:
        lote_A = generar_aleatorio(n)
        lote_B = generar_casi_ordenado(n)
        lote_C = generar_inverso(n)

        # Escenario A: Aleatorio (Caso Promedio)
        inicio = time.perf_counter()
        _, c_A = insertion_sort(lote_A)
        fin = time.perf_counter()
        tiempos_A.append(fin - inicio)
        comps_A.append(c_A)

        # Escenario B: Casi Ordenado (Mejor Caso)
        inicio = time.perf_counter()
        _, c_B = insertion_sort(lote_B)
        fin = time.perf_counter()
        tiempos_B.append(fin - inicio)
        comps_B.append(c_B)

        # Escenario C: Inverso (Peor Caso)
        inicio = time.perf_counter()
        _, c_C = insertion_sort(lote_C)
        fin = time.perf_counter()
        tiempos_C.append(fin - inicio)
        comps_C.append(c_C)

        print(f"  Evaluado n = {n}")

    # Carpeta de gráficas
    os.makedirs("graficas", exist_ok=True)

    # Gráfica 1: Comparaciones vs Tamaño de entrada
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, comps_A, marker="o", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, comps_B, marker="s", label="Escenario B (Casi Ordenado)")
    plt.plot(tamanos, comps_C, marker="^", label="Escenario C (Inverso)")
    plt.title("Comparaciones vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número total de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()

    # Gráfica 2: Tiempo vs Tamaño de entrada
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_A, marker="o", label="Escenario A (Aleatorio)")
    plt.plot(tamanos, tiempos_B, marker="s", label="Escenario B (Casi Ordenado)")
    plt.plot(tamanos, tiempos_C, marker="^", label="Escenario C (Inverso)")
    plt.title("Tiempo de Ejecución vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()

    print("Experimento completado con éxito.")
    print("Gráficas guardadas en 'graficas/parte3_comparaciones.png' y 'graficas/parte3_tiempo.png'.")


if __name__ == "__main__":
    ejecutar_experimento()