# Ejercicio 10: Altura de árbol binario

## Enunciado
Implementa una función recursiva que retorne la altura de un árbol binario. La altura de un árbol vacío es `-1` y la de un nodo hoja es `0`.

## Debes completar
`altura(raiz)`

## Firma esperada
```python
def altura(raiz: "Nodo | None") -> int:
```

## Formato esperado
- Entrada conceptual: La raíz `raiz` de un árbol binario.
- Salida esperada: La altura.

## Restricciones
- 0 <= cantidad de nodos <= 10^5

## Ejemplos
### Ejemplo
- Entrada: `árbol vacío`
- Salida: `-1`

### Ejemplo
- Entrada: `raíz con dos hijos hoja`
- Salida: `1`

## Pista
La altura depende del máximo entre subárbol izquierdo y derecho.

## Nota estilo HackerRank
Concéntrate en implementar solo la función pedida. La plataforma normalmente se encarga del I/O principal.