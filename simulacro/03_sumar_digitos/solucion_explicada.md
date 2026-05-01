# Solución explicada: Recursive Digit Sum simple

## Idea

En cada paso tomas el último dígito y llamas a la función con el resto del número. Cuando queda un solo dígito, ese valor se retorna.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def sumar_digitos(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sumar_digitos(n // 10)
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
