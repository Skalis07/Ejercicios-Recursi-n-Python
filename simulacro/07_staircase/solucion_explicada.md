# Solución explicada: Davis Staircase simplificado

## Idea

Para llegar al escalón `n`, el último salto pudo haber sido de 1, 2 o 3. Por eso se suman las formas de llegar a `n-1`, `n-2` y `n-3`. Llegar justo a 0 cuenta como una forma válida.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def formas_escalera(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return formas_escalera(n - 1) + formas_escalera(n - 2) + formas_escalera(n - 3)
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
