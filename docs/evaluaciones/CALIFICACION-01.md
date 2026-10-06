# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Laura Posada Taborda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `c717c25`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 14 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **76 / 100** |
| **Nota (0–5)** | **3.80** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica que duplicar la velocidad del servidor no resuelve el problema, porque el trabajo crece al cuadrado con los datos.
- En la Parte 2 relaciona el tiempo de ejecución con el consumo de energía acumulado durante años, y señala dos perjuicios (el paciente y el centro de contacto) diciendo quién asume el costo.
- Discute con claridad la obligación ética de que el orden de la lista sea correcto.

**Lo que puede mejorar:**
- El segundo ejemplo (segmentación de imágenes) no dice cuántos datos se procesan; sin esa cifra no se ve del todo por qué es inviable.
- En la parte ambiental faltó precisar mejor cómo pasa de horas de CPU a energía consumida.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio indicando sobre qué se toma cada uno, y justifica que usaría el peor caso por la ventana estricta.
- Deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando la condición del caso 2.
- Calcula insertion sort línea a línea y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- El análisis de insertion sort solo cubre el peor caso; faltó mostrar brevemente el conteo del mejor caso, que es el que justifica el `O(n)` de la tabla.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista original, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`. La mezcla de `merge_sort` es propia y recursiva.
- Los tres generadores dan listas del tamaño pedido, sin repetidos, y los aleatorios usan semilla.

**Lo que puede mejorar:**
- No cumple del todo PEP 8: faltan líneas en blanco entre funciones y hay una línea demasiado larga.
- Las funciones internas de `merge_sort` no tienen docstring ni la mayoría de funciones internas tienen explicación al estilo Google.
- La función de `parte3_casos.py` tiene un docstring que no sigue el formato pedido.

## 4. Calidad del análisis de las gráficas (14 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con nombre, leyenda y las curvas pedidas en los mismos ejes.
- En la Parte 4.2 describe lo que hace cada curva, concluye que merge sort es mejor y lo contrasta con lo calculado en 4.1, explicando el efecto de los tamaños pequeños.
- En 4.3 recomienda merge sort, responde a la propuesta del servidor con un dato medido (1,18 s con n = 6400), extrapola a 1.200.000 registros declarándolo estimación y menciona memoria y estabilidad.

**Lo que puede mejorar:**
- En la Parte 3.2 solo incrustó las gráficas. Falta el texto que diga, con los datos de las gráficas, cuál escenario fue el peor caso, cuál el mejor y cuál se parece al promedio.
- Tampoco contrasta el resultado con la predicción que hizo en 3.1.
- No explica cómo midió los tiempos (una sola corrida por tamaño) ni que esos tiempos pueden variar entre ejecuciones.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos siguen la estructura pedida y las imágenes se ven en el informe.
- Hay seis commits sobre el laboratorio con mensajes claros.
- En la Parte 4 enlaza `parte4_complejidad.py` y `algoritmos.py`.

**Lo que puede mejorar:**
- El informe no trae su nombre completo.
- No hay instrucciones para reproducir los experimentos (cómo activar el entorno y qué comando correr en cada parte).
- La Parte 3 no enlaza su código (`parte3_casos.py` y `datos.py`).

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente y los dos programas de medición corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Agregue siempre su nombre y los comandos para reproducir cada parte al inicio del informe.
- Enlace el código de cada parte práctica donde se menciona por primera vez.
- Después de incrustar las gráficas, escriba qué muestran y compárelo con lo que predijo.
- Corra una herramienta de estilo (PEP 8) antes de subir y agregue docstrings a todas las funciones, también las internas.
- Dé cifras concretas en los ejemplos propios (cuántos datos, qué límite).
