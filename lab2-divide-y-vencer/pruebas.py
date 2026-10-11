"""Script de pruebas unitarias con assert para el subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def ejecutar_pruebas() -> None:
    """Ejecuta las pruebas obligatorias y 20 listas aleatorias."""
    # 1. Serie de ocho días de la situación problema
    serie_problema = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie_problema)[2] == 17
    assert subarreglo_maximo(serie_problema, 0, len(serie_problema) - 1)[2] == 17

    # 2. Serie de un solo elemento
    serie_un_elemento = [42.5]
    assert subarreglo_fuerza_bruta(serie_un_elemento)[2] == 42.5
    assert subarreglo_maximo(serie_un_elemento, 0, 0)[2] == 42.5

    # 3. Serie con todos los valores negativos
    serie_negativa = [-5, -2, -9, -1]
    assert subarreglo_fuerza_bruta(serie_negativa)[2] == -1
    assert subarreglo_maximo(serie_negativa, 0, len(serie_negativa) - 1)[2] == -1

    # 4. Serie con todos los valores positivos
    serie_positiva = [2, 4, 6, 8]
    assert subarreglo_fuerza_bruta(serie_positiva)[2] == 20
    assert subarreglo_maximo(serie_positiva, 0, len(serie_positiva) - 1)[2] == 20

    # 5. Caso donde el mejor tramo cruza el punto medio
    serie_cruce = [-10, 10, 10, -10]
    assert subarreglo_fuerza_bruta(serie_cruce)[2] == 20
    assert subarreglo_maximo(serie_cruce, 0, len(serie_cruce) - 1)[2] == 20

    # 6. Al menos veinte listas aleatorias comparando ambas soluciones
    random.seed(42)
    for i in range(20):
        tam = random.randint(5, 40)
        lista_aleatoria = [random.uniform(-50, 50) for _ in range(tam)]
        res_fb = subarreglo_fuerza_bruta(lista_aleatoria)
        res_dyv = subarreglo_maximo(lista_aleatoria, 0, len(lista_aleatoria) - 1)
        assert abs(res_fb[2] - res_dyv[2]) < 1e-5, (
            f"Iteración {i} fallida: FB={res_fb[2]}, DyV={res_dyv[2]}"
        )

    print("¡Todas las pruebas con assert pasaron exitosamente!")


if __name__ == "__main__":
    ejecutar_pruebas()