# Solución explicada: Reversa recursiva de string

## Idea

Se va colocando al frente el último carácter del string actual y luego se repite con el resto hasta llegar a tamaño 0 o 1.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
def reversa(texto: str) -> str:
    if len(texto) <= 1:
        return texto
    return texto[-1] + reversa(texto[:-1])
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
