"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: Lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada (descendente) y el numero total
        de comparaciones entre elementos realizadas durante el proceso.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1
            if arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: Lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada (descendente) y el numero total
        de comparaciones entre elementos realizadas durante la mezcla.
    """
    arr = datos.copy()

    def _merge_sort_recursivo(sub_arr: list[int]) -> tuple[list[int], int]:
        """Divide recursivamente el arreglo y acumula comparaciones.

        Args:
            sub_arr: Sublista de enteros a dividir y ordenar.

        Returns:
            Tupla con la sublista ordenada y comparaciones acumuladas.
        """
        if len(sub_arr) <= 1:
            return sub_arr, 0

        medio = len(sub_arr) // 2
        izq, comp_izq = _merge_sort_recursivo(sub_arr[:medio])
        der, comp_der = _merge_sort_recursivo(sub_arr[medio:])

        mezclado, comp_mezcla = _mezclar(izq, der)
        return mezclado, comp_izq + comp_der + comp_mezcla

    def _mezclar(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        """Combina dos listas ordenadas en orden descendente.

        Args:
            izq: Primera sublista ordenada.
            der: Segunda sublista ordenada.

        Returns:
            Tupla con la lista unificada ordenada y sus comparaciones.
        """
        resultado = []
        i = j = comparaciones = 0

        while i < len(izq) and j < len(der):
            comparaciones += 1
            if izq[i] >= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado, comparaciones

    return _merge_sort_recursivo(arr)