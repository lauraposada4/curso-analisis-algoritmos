"""Script de medicion de tiempos y generacion de graficas"""

import os
import random
import time

import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def medir_rendimiento() -> None:
    """Mide el tiempo de ejecucion de fuerza bruta y divide y venceras

    para tamanos de entrada desde 10 hasta 8000 elementos
    """
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    tiempos_fb = []
    tiempos_dyv = []

    random.seed(42)

    print("Iniciando mediciones de rendimiento (Laboratorio 2)...")

    for n in tamanos:
        valores = [random.uniform(-100, 100) for _ in range(n)]

        # Medición Fuerza Bruta
        inicio = time.perf_counter()
        res_fb = subarreglo_fuerza_bruta(valores)
        fin = time.perf_counter()
        t_fb = fin - inicio
        tiempos_fb.append(t_fb)

        # Medición Divide y Vencerás
        inicio = time.perf_counter()
        res_dyv = subarreglo_maximo(valores, 0, len(valores) - 1)
        fin = time.perf_counter()
        t_dyv = fin - inicio
        tiempos_dyv.append(t_dyv)

        # Verificar integridad del resultado
        assert abs(res_fb[2] - res_dyv[2]) < 1e-5, f"Discrepancia en n={n}"

        print(f"  n = {n:5d} | Fuerza Bruta: {t_fb:.6f}s | Divide y Vencerás: {t_dyv:.6f}s")

    os.makedirs("graficas", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_fb, marker="o", color="tab:red", label="Fuerza Bruta Θ(n²)")
    plt.plot(tamanos, tiempos_dyv, marker="s", color="tab:blue", label="Divide y Vencerás Θ(n log n)")
    plt.title("Tiempo de Ejecución vs. Tamaño de Entrada (Subarreglo Máximo)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_n.png")
    plt.close()

    print("Medición finalizada. Gráfica guardada en 'graficas/tiempo_vs_n.png'.")


if __name__ == "__main__":
    medir_rendimiento()