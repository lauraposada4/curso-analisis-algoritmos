#Script de partida - antes
# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
# 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))


# Refactorización PEP 8 y agregar type hints.

def calcular_promedio(lista: list) -> float:
    """Calcula el promedio de una lista de números.
    
    Args:
        lista: lista de números a promediar.
        
    Returns:
        El promedio calculado.
    """
    suma = 0
    for x in lista:
        suma = suma + x
    return suma / len(lista)


def main() -> None:
    """Punto de entrada del script."""
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()