# Ejercicio 07: Davis Staircase simplificado

## Enunciado
Una persona puede subir una escalera avanzando 1, 2 o 3 escalones por vez. Retorna cuántas formas distintas hay de llegar exactamente al escalón `n`.

## Debes completar
`formas_escalera(n)`

## Firma esperada
```python
def formas_escalera(n: int) -> int:
```

## Formato esperado
- Entrada conceptual: Un entero `n`.
- Salida esperada: Cantidad de formas.

## Restricciones
- 0 <= n <= 25

## Ejemplos
### Ejemplo
- Entrada: `n = 3`
- Salida: `4`

### Ejemplo
- Entrada: `n = 4`
- Salida: `7`

## Pista
Piensa en las formas de llegar desde `n-1`, `n-2` y `n-3`.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.