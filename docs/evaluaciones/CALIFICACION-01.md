# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Laura Posada Taborda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-24 23:59 · **Versión revisada:** commit `e878c98`

Muy buen trabajo: su informe y su código están completos y bien sustentados con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 23 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (23 / 25)
**Lo que hizo bien:**
- Distingue bien entre corrección y eficiencia y nombra la restricción que se incumple (la ventana de cuatro horas).
- Explica por qué duplicar la velocidad del servidor solo reduce el tiempo a la mitad y no cambia el crecimiento cuadrático.
- Su segundo ejemplo (segmentación de imágenes de cámara web) trae datos concretos y una restricción clara (33 ms por fotograma).
- Calcula el consumo de energía diario y anual, e identifica dos perjuicios con quién asume el costo en cada uno.
- Discute que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- En la Parte 1 llama "exponencial" al crecimiento cuadrático; son cosas distintas.
- El cálculo de energía supone que el servidor trabaja las cuatro horas completas al 100 %; conviene decir que es un supuesto.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio indicando sobre qué entradas se toma cada uno, y justifica que usaría el peor caso por la ventana estricta.
- Deja escrita la predicción antes del experimento y la contrasta después.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando la condición del caso 2.
- Hace la tabla línea a línea de insertion sort para el peor y el mejor caso, y entrega la tabla de complejidades.

**Lo que puede mejorar:**
- En las tablas de insertion sort falta sumar explícitamente los costos para llegar a la expresión final; solo se afirma que es cuadrática (o lineal).
- No se justifica el caso promedio de insertion sort; solo aparece en la tabla.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, trabajan sobre una copia y cuentan solo comparaciones entre elementos. No usan `sorted()` ni `list.sort()`.
- `merge_sort` tiene su propia mezcla recursiva.
- Los generadores producen lotes con valores distintos y semilla; el escenario B queda con el 98 % ordenado y el 2 % al final.
- Código con type hints y docstrings en todas las funciones, y sin problemas de estilo.

**Lo que puede mejorar:**
- Los generadores llaman a `random.seed` sobre el generador global; es mejor usar un generador propio (`random.Random(semilla)`).

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes y leyenda, y las cifras del informe coinciden con ellas.
- Identifica con evidencia el peor caso (inverso), el mejor (casi ordenado) y el promedio (aleatorio).
- Concluye con su gráfica que merge sort es mejor para Tamiza y lo relaciona con las complejidades calculadas.
- En el concepto técnico recomienda merge sort, extrapola a 1.200.000 registros declarándolo estimación y responde a la propuesta del servidor con un dato medido (1,18 s en n = 6400).

**Lo que puede mejorar:**
- Dice que para tamaños pequeños merge sort pierde por las llamadas recursivas, pero en su gráfica no se ve que pierda; debía describir lo que realmente se observa.
- Afirma que la memoria de merge sort es menor a 10 MB para 1.200.000 registros sin sustentarlo; en Python una lista de ese tamaño ocupa bastante más.
- No discute el riesgo de que el escenario B deje de ser casi ordenado; las demás consideraciones sí están.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, informe por partes, gráficas incrustadas que se ven y enlaces al código en las Partes 3 y 4.
- Hay más de cinco commits descriptivos que tocan el laboratorio.

**Lo que puede mejorar:**
- Las instrucciones para reproducir quedaron incompletas: solo muestran cómo activar el entorno, el bloque de código no se cierra y faltan los comandos para ejecutar cada parte.
- Las instrucciones asumen Windows (`Scripts/activate`) y no indican cómo hacerlo en otros sistemas.

## ¿El código funciona?
Sí. Ambos algoritmos ordenan correctamente en mis pruebas con listas pequeñas y aleatorias, y los scripts de las Partes 3 y 4 generan las gráficas pedidas.

## Para el próximo laboratorio
- Complete las instrucciones de reproducción con el comando de cada parte y ciérrelas bien.
- Sume los costos de cada línea en el análisis para mostrar cómo se llega al resultado final.
- Describa lo que realmente muestra la gráfica en los tamaños pequeños, sin asumir lo esperado.
- Sustente con un cálculo las cifras de memoria que mencione.
- Use un generador aleatorio propio con semilla en lugar del global.
