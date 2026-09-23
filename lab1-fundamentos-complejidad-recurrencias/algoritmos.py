"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada (de mayor a menor) y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arr = datos.copy()
    comparaciones = 0
    n = len(arr)
    
    # Se ordena de mayor a menor (descendente)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparaciones += 1  # Se va contando la comparación entre arr[j] y key
            if arr[j] < key:    # Si el actual es menor que la llave, se mueve
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
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arr = datos.copy()

    def _merge_sort_recursivo(sub_arr: list[int]) -> tuple[list[int], int]:
        if len(sub_arr) <= 1:
            return sub_arr, 0

        medio = len(sub_arr) // 2
        izq, comp_izq = _merge_sort_recursivo(sub_arr[:medio])
        der, comp_der = _merge_sort_recursivo(sub_arr[medio:])

        mezclado, comp_mezcla = _mezclar(izq, der)
        return mezclado, comp_izq + comp_der + comp_mezcla

    def _mezclar(izq: list[int], der: list[int]) -> tuple[list[int], int]:
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