# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Laura Posada Taborda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `e878c98`

Muy buen trabajo: el código es correcto y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 20 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **84 / 100** |
| **Nota (0–5)** | **4.20** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- Indica desde qué tamaño divide y vencerás gana (n = 100) con tiempos medidos.
- Compara bien con el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia da `Θ(n)` y dividir no mejora nada.
- Recomienda divide y vencerás y declara que el valor para 1.000.000 de registros es una estimación.

**Lo que puede mejorar:**
- La estimación de fuerza bruta está mal: con su propio dato (2,27 s en n = 8000) y factor cuadrático (125² = 15.625), el resultado es cerca de 35.000 segundos, es decir, unas 10 horas, no "más de 35 horas".
- En la pregunta 3, la ventaja de divide y vencerás empieza a verse desde n = 50 en su tabla; hubiera sido bueno revisar también ese tamaño.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada parte.
- Aplica el método maestro y verifica que se cumple el caso 2.
- Justifica que la fuerza bruta es `Θ(n²)` por los dos ciclos anidados.

**Lo que puede mejorar:**
- Explique con más detalle por qué la suma de pasos de los ciclos da exactamente un orden `n²`.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos, no usa la fuerza bruta y no modifica la lista.
- Tiene anotaciones de tipos y docstrings en las funciones principales.

**Lo que puede mejorar:**
- El docstring de `medir_rendimiento` no sigue el formato Google (faltan `Args` y `Returns`) y no tiene línea en blanco bien ubicada.

## 4. Calidad del análisis de las gráficas (20 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños.
- Los factores al duplicar n (4,40 y 2,0) coinciden con la gráfica (fuerza bruta cerca de 0,5 s en n = 4000 y 2,3 s en n = 8000) y los contrasta con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los valores que cita para n = 100 no se pueden leer de la gráfica. Faltó una tabla con los tiempos medidos que los respaldara.
- Dice que la fuerza bruta crece "exponencialmente": crece de forma cuadrática, no exponencial.
- Cada medición se hizo una sola vez; repetirla y promediar daría datos más confiables.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` tiene todos los archivos pedidos, la gráfica se ve en el informe y cada parte enlaza su código.
- Hay tres commits descriptivos sobre el laboratorio.

**Lo que puede mejorar:**
- La instrucción para activar el entorno usa una ruta absoluta de Windows (`/venv/Scripts/activate`) que no sirve en otros equipos.
- Los datos aleatorios son decimales, y se pedían enteros entre -100 y 100.
- La nota de la Parte 2 habla de "funciones de ordenamiento" y no dice si repitió las mediciones.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos soluciones coinciden en mis pruebas adicionales y `medicion.py` corre y genera la gráfica.

## Para el próximo laboratorio
- Revise las cuentas de las estimaciones antes de entregar.
- Repita cada medición varias veces y reporte el promedio.
- Agregue una tabla con los tiempos medidos para poder analizar los tamaños pequeños.
- Escriba las instrucciones de reproducción con rutas que funcionen en cualquier equipo.
- Complete los docstrings de todas las funciones con `Args` y `Returns`, y deje dos líneas en blanco entre funciones.
