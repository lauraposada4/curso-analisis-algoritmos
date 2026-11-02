# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Laura Posada Taborda · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `51b490a`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 17 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y usa el ejemplo de las guías 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con una ventaja y un costo de cada uno.
- Dice con claridad que la tabla hash no sirve para rangos y que el árbol degenerado tiene altura cercana a 400.000, frente a unos 18 niveles en uno equilibrado.
- Recomienda una combinación razonable (tabla hash más árbol equilibrado) y declara la estimación de la lista como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- No explica por qué hay colisiones aunque la tabla tenga más casillas que guías.
  → *Cómo corregirlo:* piense cuántas guías posibles hay (números de diez dígitos) frente al número de casillas, y escriba qué consecuencia tiene eso.
- Del árbol degenerado da la altura, pero no estima el número total de comparaciones al insertar las 400.000 guías, ni compara ese total con el del árbol equilibrado.
  → *Cómo corregirlo:* cuente cuántas comparaciones cuesta insertar la guía número k en cada caso y sume sobre todas las guías.
- Para la tabla hash con 5.000.000 de envíos solo repite el valor medido con 50.000 y dice que es "constante", sin explicar por qué la curva se mantiene plana ni qué α usaría.
  → *Cómo corregirlo:* indique qué m elegiría para 5.000.000 y use la forma Θ(1 + α) para justificar el tiempo estimado, apoyándose en sus datos del Experimento B.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Justifica el Θ(1 + α) separando el cálculo del índice y el recorrido de la sublista.
- Nombra el supuesto de hash uniforme simple y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista con costo Θ(n).

**Lo que puede mejorar (y cómo corregirlo):**
- Para la lista dice que "recorre cada nodo", pero no explica que una guía inexistente obliga a revisar los n nodos antes de poder concluir.
  → *Cómo corregirlo:* añada una frase que explique por qué una búsqueda infructuosa no puede detenerse antes del final.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` son correctas; la búsqueda usa un ciclo `while` y la tabla reutiliza la lista sin `dict`, `set` ni `hash()`.
- `pruebas.py` cubre búsquedas exitosas e infructuosas, la colisión forzada con m = 7, el factor de carga 3/7 y 20 colecciones aleatorias.
- Las clases tienen docstrings con `Args` y `Returns` y type hints.

**Lo que puede mejorar (y cómo corregirlo):**
- En `medicion.py`, la función `obtener_primo_cercano` tiene un docstring de una línea sin `Args` ni `Returns`, y `ejecutar_experimentos` tampoco sigue el formato completo.
  → *Cómo corregirlo:* complete el docstring estilo Google con las secciones `Args:` y `Returns:` en cada función.

## 4. Calidad del análisis de las gráficas (17 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n con ambas curvas en los mismos ejes y la segunda cuatro valores de α.
- Incluye una tabla con los valores medidos, lo que ayuda a leer la curva plana de la tabla.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 2 usa un valor de n = 10.000 "interpolado" que no fue medido, y no calcula cuántas veces se multiplicó el tiempo de cada estructura.
  → *Cómo corregirlo:* tome dos valores de n consecutivos que sí midió, divida los tiempos de cada estructura y compare ese cociente con lo que predice Θ(n) y Θ(1).
- Sobre la tabla dice que "se mantuvo sin cambiar" con 1,27 × 10⁻⁶ s en n = 50.000, pero en su propia tabla ese valor es el doble que en n = 20.000; no discute esa variación.
  → *Cómo corregirlo:* comente la variación de la tabla y si se explica por ruido de medición.
- Sobre el Experimento B dice que el tiempo aumenta "de manera controlada" desde α = 0,5, pero en la gráfica el valor en α = 0,5 es más alto que en α = 1. Tampoco cita valores leídos de la gráfica.
  → *Cómo corregirlo:* lea los valores de la gráfica en cada α, describa también ese punto que sube y proponga una explicación (por ejemplo, ruido) antes de concluir que es coherente con Θ(1 + α).
- El informe dice que cada valor es el promedio de 3 rondas, pero el código de `medicion.py` hace una sola medición por valor.
  → *Cómo corregirlo:* agregue un ciclo que repita la medición tres veces y promedie, o corrija la nota del informe para que diga lo que realmente hizo.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada (`lab3-estructuras-datos/`) con todos los archivos del entregable.
- El informe sigue el orden pedido, enlaza el código en cada parte y las gráficas se ven con ruta relativa.
- Hay tres commits con mensajes descriptivos.

**Lo que puede mejorar (y cómo corregirlo):**
- Las instrucciones de reproducción activan el entorno con `source ../venv/Scripts/activate`, una ruta de Windows que no coincide con el entorno de la raíz del repositorio.
  → *Cómo corregirlo:* escriba el comando de activación del entorno que realmente usa y haga que `matplotlib` quede en `requirements.txt` en vez de instalarlo a mano.
- La nota sobre repeticiones no coincide con el código (ver punto 4).
  → *Cómo corregirlo:* haga que el informe describa exactamente lo que hace el código.

## ¿El código funciona?
Sí. Las pruebas pasan y la medición corre completa y genera las dos gráficas. Las dos estructuras devuelven lo mismo en búsquedas exitosas e infructuosas.
