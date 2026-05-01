# Solución explicada: Binary Search recursiva

## Idea

En cada llamada se revisa el elemento del medio. Si coincide, se retorna el índice. Si no, se descarta la mitad imposible y se continúa con la otra.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def busqueda_binaria(arr: list[int], objetivo: int, izq: int, der: int) -> int:
    if izq > der:
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:
        return medio
    if objetivo < arr[medio]:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    return busqueda_binaria(arr, objetivo, medio + 1, der)
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
