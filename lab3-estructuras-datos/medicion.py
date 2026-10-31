"""Script de medicion experimental y generacion de graficas para el Lab 3."""

import os
import random
import time

import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def obtener_primo_cercano(val: int) -> int:
    """Retorna un numero primo cercano (hacia arriba) para usar como m."""
    p = val
    while True:
        if p < 2:
            return 2
        primo = True
        i = 2
        while i * i <= p:
            if p % i == 0:
                primo = False
                break
            i += 1
        if primo:
            return p
        p += 1


def ejecutar_experimentos() -> None:
    """Ejecuta Experimento A (Lista vs Tabla) y Experimento B (Factor de carga)."""
    os.makedirs("graficas", exist_ok=True)
    random.seed(42)

    # -------------------------------------------------------------
    # EXPERIMENTO A: Lista enlazada vs Tabla Hash frente a n
    # -------------------------------------------------------------
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    print("Iniciando Experimento A: Lista Enlazada vs Tabla Hash...")

    for n in tamanos:
        # Generar n guías únicas de 10 dígitos
        existentes_set = set()
        while len(existentes_set) < n:
            existentes_set.add(random.randint(10**9, 10**10 - 1))

        # Poblar ListaEnlazada y TablaHash (m primo cercano a n / 2 para alfa ~ 2)
        lista = ListaEnlazada()
        m = obtener_primo_cercano(max(3, n // 2))
        tabla = TablaHash(m)

        for g in existentes_set:
            lista.insertar(g, "en bodega")
            tabla.insertar(g, "en bodega")

        # Generar 200 guías inexistentes
        inexistentes = generar_guias_inexistentes(existentes_set, 200)

        # Verificar integridad (muestras existentes)
        muestra_existentes = list(existentes_set)[:5]
        for g in muestra_existentes:
            assert lista.buscar(g) == tabla.buscar(g) == "en bodega"

        # Cronometrar búsquedas en ListaEnlazada (200 inexistentes)
        t0 = time.perf_counter()
        for g in inexistentes:
            lista.buscar(g)
        t1 = time.perf_counter()
        tiempo_medio_lista = (t1 - t0) / 200.0
        tiempos_lista.append(tiempo_medio_lista)

        # Cronometrar búsquedas en TablaHash (200 inexistentes)
        t0 = time.perf_counter()
        for g in inexistentes:
            tabla.buscar(g)
        t1 = time.perf_counter()
        tiempo_medio_tabla = (t1 - t0) / 200.0
        tiempos_tabla.append(tiempo_medio_tabla)

        print(
            f"  n = {n:5d} (m = {m:5d}) | Lista: {tiempo_medio_lista:.8f}s | Tabla: {tiempo_medio_tabla:.8f}s"
        )

    # Gráfica Experimento A
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_lista, marker="o", color="tab:red", label="Lista Enlazada Θ(n)")
    plt.plot(tamanos, tiempos_tabla, marker="s", color="tab:blue", label="Tabla Hash Θ(1 + α)")
    plt.title("Tiempo Medio de Búsqueda de Guías Inexistentes vs. n")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/lista_vs_tabla.png")
    plt.close()
    print("Gráfica guardada en 'graficas/lista_vs_tabla.png'.")

    # -------------------------------------------------------------
    # EXPERIMENTO B: Efecto del factor de carga (alfa) con n fijo
    # -------------------------------------------------------------
    n_fijo = 20000
    alfas_objetivo = [0.5, 1.0, 4.0, 10.0]
    valores_alfa_medidos = []
    tiempos_alfa = []

    print("\nIniciando Experimento B: Efecto del factor de carga (alfa)...")

    # Generar n_fijo guías base
    existentes_set_b = set()
    while len(existentes_set_b) < n_fijo:
        existentes_set_b.add(random.randint(10**9, 10**10 - 1))

    inexistentes_b = generar_guias_inexistentes(existentes_set_b, 200, semilla=99)

    for alfa_obj in alfas_objetivo:
        # m = n_fijo / alfa_obj
        m_calc = max(1, int(round(n_fijo / alfa_obj)))
        tabla_b = TablaHash(m_calc)

        for g in existentes_set_b:
            tabla_b.insertar(g, "en bodega")

        alfa_real = tabla_b.factor_carga()
        valores_alfa_medidos.append(alfa_real)

        t0 = time.perf_counter()
        for g in inexistentes_b:
            tabla_b.buscar(g)
        t1 = time.perf_counter()
        t_medio = (t1 - t0) / 200.0
        tiempos_alfa.append(t_medio)

        print(f"  Alfa objetivo: {alfa_obj:4.1f} (m = {m_calc:5d}, alfa real: {alfa_real:5.2f}) | Tiempo: {t_medio:.8f}s")

    # Gráfica Experimento B
    plt.figure(figsize=(10, 6))
    plt.plot(valores_alfa_medidos, tiempos_alfa, marker="o", color="tab:purple", label="Tabla Hash (Encadenamiento)")
    plt.title("Tiempo Medio de Búsqueda vs. Factor de Carga (α)")
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/tiempo_vs_alfa.png")
    plt.close()
    print("Gráfica guardada en 'graficas/tiempo_vs_alfa.png'.")
    print("Todos los experimentos finalizaron con éxito.")


if __name__ == "__main__":
    ejecutar_experimentos()