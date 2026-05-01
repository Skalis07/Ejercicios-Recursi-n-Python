# Preparación para test de recursión estilo HackerRank

## Lo que te comunicaron

- El objetivo del test es evaluar **razonamiento y abstracción** usando **recursión**.
- **No** evalúan un lenguaje específico.
- **No** buscan soluciones iterativas.
- Las soluciones esperadas suelen ser **cortas**: entre **5 y 20 líneas**.
- Tendrás un máximo de **25 minutos por ejercicio**.
- La recomendación es contestar el test dentro de las próximas **48 horas**.
- Durante la prueba debes tener la **cámara encendida**.
- HackerRank monitorea irregularidades como:
  - cambios de pestaña o ventana,
  - uso de múltiples pantallas o dispositivos,
  - copiar y pegar desde otras fuentes,
  - ayuda de terceros o herramientas de IA.
- También existe **revisión humana**.

## Traducción práctica de eso

1. Te conviene practicar sobre problemas donde la recursión sea la solución natural.
2. Debes poder identificar rápidamente:
   - caso base,
   - llamada recursiva,
   - cómo se reduce el problema,
   - cuándo debes combinar resultados.
3. No pierdas tiempo escribiendo arquitecturas largas.
4. Piensa primero en la firma de función y en el caso más pequeño posible.
5. Si un problema parece pedir backtracking, igualmente empieza por la forma recursiva más simple.

## Qué patrones conviene dominar

- factorial
- fibonacci
- suma de dígitos
- reversa de string
- palíndromos
- conteo de caminos
- escaleras / staircases
- suma de arreglo
- máximo de arreglo
- listas enlazadas
- árboles binarios
- búsqueda binaria recursiva
- generación de subconjuntos o combinaciones

## Método mental rápido

### 1. Define qué representa la función
Ejemplo: `f(n)` devuelve la cantidad de maneras de subir `n` escalones.

### 2. Encuentra el caso base mínimo
Pregúntate: ¿qué devuelve la función cuando ya no queda nada que resolver?

### 3. Reduce el problema
Piensa: ¿cómo llamo a la misma función con un problema más pequeño?

### 4. Combina
A veces solo retornas una llamada; otras veces sumas, comparas o concatenas resultados.

### 5. Verifica que avance
Cada llamada recursiva debe acercarse claramente al caso base.

## Error comunes

- olvidar el caso base,
- crear recursión infinita,
- mezclar lógica iterativa cuando la prueba espera recursión,
- devolver el tipo incorrecto,
- usar variables globales innecesarias,
- resolver bien la idea pero no respetar la firma pedida.

## Cómo practicar este pack

Cada carpeta trae:
- `README.md`: enunciado estilo plataforma,
- `starter.py`: base para resolver,
- `solucion_explicada.md`: solución corta + explicación.

Mi sugerencia:
1. Lee solo el `README.md`.
2. Resuelve en `starter.py` o en una copia.
3. Recién después abre `solucion_explicada.md`.
