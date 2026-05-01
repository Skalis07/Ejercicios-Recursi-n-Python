# Solución explicada: Suma recursiva de arreglo

## Idea

La función suma el elemento actual y delega la suma del resto del arreglo a la siguiente llamada. Cuando el índice sale del rango, se retorna 0.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def sumar_arreglo(arr: list[int], i: int = 0) -> int:
    if i == len(arr):
        return 0
    return arr[i] + sumar_arreglo(arr, i + 1)
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
