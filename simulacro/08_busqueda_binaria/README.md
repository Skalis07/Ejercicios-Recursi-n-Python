# Ejercicio 08: Binary Search recursiva

## Enunciado
Dado un arreglo ordenado ascendentemente, retorna el índice de `objetivo` usando búsqueda binaria recursiva. Si no existe, retorna `-1`.

## Debes completar
`busqueda_binaria(arr, objetivo, izq, der)`

## Firma esperada
```python
def busqueda_binaria(arr: list[int], objetivo: int, izq: int, der: int) -> int:
```

## Formato esperado
- Entrada conceptual: Lista ordenada `arr`, entero `objetivo` y rango inicial.
- Salida esperada: Índice o `-1`.

## Restricciones
- 0 <= len(arr) <= 10^5

## Ejemplos
### Ejemplo
- Entrada: `arr = [1,3,5,7], objetivo = 5`
- Salida: `2`

### Ejemplo
- Entrada: `arr = [1,3,5,7], objetivo = 4`
- Salida: `-1`

## Pista
Reduce a la mitad izquierda o derecha.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.