# Ejercicio 03: Recursive Digit Sum simple

## Enunciado
Retorna la suma de los dígitos de un entero no negativo `n` usando recursión.

## Debes completar
`sumar_digitos(n)`

## Firma esperada
```python
def sumar_digitos(n: int) -> int:
```

## Formato esperado
- Entrada conceptual: Un entero `n`.
- Salida esperada: La suma de sus dígitos.

## Restricciones
- 0 <= n <= 10^18

## Ejemplos
### Ejemplo
- Entrada: `n = 5024`
- Salida: `11`

### Ejemplo
- Entrada: `n = 9`
- Salida: `9`

## Pista
Separa último dígito y resto con `%` y `//`.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.