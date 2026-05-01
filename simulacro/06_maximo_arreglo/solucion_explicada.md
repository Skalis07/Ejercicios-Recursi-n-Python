# Solución explicada: Máximo recursivo de arreglo

## Idea

El caso base es el último elemento. Para los demás casos, se obtiene el máximo del resto y se compara con el valor actual.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def maximo_arreglo(arr: list[int], i: int = 0) -> int:
    if i == len(arr) - 1:
        return arr[i]
    resto = maximo_arreglo(arr, i + 1)
    return arr[i] if arr[i] > resto else resto
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
