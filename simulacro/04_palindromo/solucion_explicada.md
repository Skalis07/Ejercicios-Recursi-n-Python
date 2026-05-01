# Solución explicada: Palindrome recursivo

## Idea

Si los extremos no coinciden, no es palíndromo. Si coinciden, el problema se reduce al substring interno. Strings de largo 0 o 1 siempre son palíndromos.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def es_palindromo(texto: str) -> bool:
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return es_palindromo(texto[1:-1])
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
