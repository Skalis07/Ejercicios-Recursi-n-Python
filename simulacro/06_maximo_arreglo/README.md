# Ejercicio 06: Máximo recursivo de arreglo

## Enunciado
Retorna el valor máximo de un arreglo no vacío usando recursión.

## Debes completar
`maximo_arreglo(arr, i)`

## Firma esperada
```python
def maximo_arreglo(arr: list[int], i: int = 0) -> int:
```

## Formato esperado
- Entrada conceptual: Una lista de enteros `arr` no vacía.
- Salida esperada: El mayor valor.

## Restricciones
- 1 <= len(arr) <= 10^4

## Ejemplos
### Ejemplo
- Entrada: `arr = [7, 2, 9, 4]`
- Salida: `9`

### Ejemplo
- Entrada: `arr = [-3, -7, -1]`
- Salida: `-1`

## Pista
Compara el actual con el máximo del resto.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.