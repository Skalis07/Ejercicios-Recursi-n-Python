# Ejercicio 09: Reversa recursiva de string

## Enunciado
Retorna el string `texto` invertido usando recursión.

## Debes completar
`reversa(texto)`

## Firma esperada
```python
def reversa(texto: str) -> str:
```

## Formato esperado
- Entrada conceptual: Un string.
- Salida esperada: El string al revés.

## Restricciones
- 0 <= len(texto) <= 10^4

## Ejemplos
### Ejemplo
- Entrada: `texto = "hola"`
- Salida: `"aloh"`

### Ejemplo
- Entrada: `texto = ""`
- Salida: `""`

## Pista
Toma el último carácter y resuelve el resto.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.