"""Script de pruebas con assert para la ListaEnlazada y la TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash


def ejecutar_pruebas() -> None:
    """Ejecuta pruebas unitarias y de esfuerzo para las estructuras."""
    # 1. Búsqueda exitosa e infructuosa en ListaEnlazada
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(9999999999) is None

    # 2. Búsqueda exitosa e infructuosa en TablaHash
    tabla_prueba = TablaHash(10)
    tabla_prueba.insertar(1000000010, "en bodega")
    assert tabla_prueba.buscar(1000000010) == "en bodega"
    assert tabla_prueba.buscar(9999999999) is None

    # 3. Colisión forzada con m = 7 (guias 10, 24, 17 caen en casilla 3)
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(99) is None
    assert abs(tabla.factor_carga() - (3 / 7)) < 1e-5

    # Verificar que la casilla 3 tiene longitud 3 por el encadenamiento
    casilla_idx = tabla.hash(10)  # 10 % 7 = 3
    assert casilla_idx == 3
    assert tabla.casillas[3].tamano == 3

    # 4. Al menos veinte colecciones aleatorias comparando lista y tabla hash
    azar = random.Random(42)
    for _ in range(20):
        l = ListaEnlazada()
        t = TablaHash(13)

        guias_actuales = set()
        while len(guias_actuales) < 15:
            g = azar.randint(10**9, 10**10 - 1)
            guias_actuales.add(g)

        estados = ["en bodega", "en reparto", "entregado"]
        for g in guias_actuales:
            est = azar.choice(estados)
            l.insertar(g, est)
            t.insertar(g, est)

        # Verificar búsquedas de guías existentes
        for g in guias_actuales:
            assert l.buscar(g) == t.buscar(g), f"Discrepancia en guía existente {g}"

        # Verificar búsquedas de guías inexistentes
        for _ in range(5):
            inexistente = azar.randint(10**9, 10**10 - 1)
            if inexistente not in guias_actuales:
                assert l.buscar(inexistente) == t.buscar(inexistente) is None

    print("¡Todas las pruebas con assert pasaron exitosamente!")


if __name__ == "__main__":
    ejecutar_pruebas()