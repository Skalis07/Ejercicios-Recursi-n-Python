# Solución explicada: Recursion: Fibonacci reducido

## Idea

El caso base ocurre cuando `n` es 0 o 1. Para cualquier otro valor, el problema se divide en los dos Fibonacci anteriores y se suman.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
