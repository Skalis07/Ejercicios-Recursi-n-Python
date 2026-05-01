# Solución explicada: Altura de árbol binario

## Idea

El árbol vacío mide `-1`. Para cualquier nodo real, la altura es 1 más la mayor altura entre sus hijos izquierdo y derecho.

## Caso base

El caso base debe cortar la recursión en el punto más pequeño válido del problema.

## Reducción del problema

Cada llamada recursiva trabaja con una versión más pequeña del mismo problema, hasta llegar al caso base.

## Solución en Python

```python
class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def altura(raiz: "Nodo | None") -> int:
    if raiz is None:
        return -1
    return 1 + max(altura(raiz.izq), altura(raiz.der))
```

## Por qué funciona

Porque la definición de la función respeta exactamente la estructura del problema original y en cada llamada avanza hacia el caso base.
