# Ejercicio 05: Suma recursiva de arreglo

## Enunciado
Retorna la suma de todos los elementos de `arr` usando recursión. Usa `i` como índice actual.

## Debes completar
`sumar_arreglo(arr, i)`

## Firma esperada
```python
def sumar_arreglo(arr: list[int], i: int = 0) -> int:
```

## Formato esperado
- Entrada conceptual: Una lista de enteros `arr`.
- Salida esperada: La suma total.

## Restricciones
- 0 <= len(arr) <= 10^4

## Ejemplos
### Ejemplo
- Entrada: `arr = [3, 1, 4]`
- Salida: `8`

### Ejemplo
- Entrada: `arr = []`
- Salida: `0`

## Pista
Cuando `i` llega al largo, ya no quedan elementos.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.