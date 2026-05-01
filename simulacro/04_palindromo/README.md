# Ejercicio 04: Palindrome recursivo

## Enunciado
Retorna `True` si `texto` es palíndromo y `False` en caso contrario. Asume que ya viene normalizado, sin espacios ni mayúsculas.

## Debes completar
`es_palindromo(texto)`

## Firma esperada
```python
def es_palindromo(texto: str) -> bool:
```

## Formato esperado
- Entrada conceptual: Un string `texto`.
- Salida esperada: Booleano.

## Restricciones
- 0 <= len(texto) <= 10^5

## Ejemplos
### Ejemplo
- Entrada: `texto = "radar"`
- Salida: `True`

### Ejemplo
- Entrada: `texto = "cabra"`
- Salida: `False`

## Pista
Compara extremos y reduce el centro.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.