# Ejercicios de Recursión en Python

Pack de práctica para prepararte para un **test de recursión estilo HackerRank**.

La idea NO es memorizar código. La idea es entrenar lo que de verdad suelen medir en este tipo de pruebas: **abstracción, casos base, reducción del problema y combinación de resultados**.

Aunque el repositorio usa **Python** en los archivos `starter.py`, el enfoque es **conceptual** y te sirve aunque luego rindas en otro lenguaje.

## Objetivo del repositorio

Este material está pensado para practicar ejercicios donde la **recursión es la solución natural**, con problemas cortos y directos, similares al formato mental que suelen exigir las plataformas técnicas.

En particular, este pack te ayuda a entrenar:

- identificación rápida del **caso base**,
- definición clara de la **firma de la función**,
- reducción del problema a una versión más pequeña,
- combinación correcta de resultados,
- escritura de soluciones **cortas** y enfocadas.

## Qué tipo de prueba simula

Según la guía del repo, este tipo de test suele priorizar:

- **razonamiento y abstracción** usando recursión,
- soluciones breves, normalmente entre **5 y 20 líneas**,
- ejercicios con un límite cercano a **25 minutos por problema**,
- enfoque recursivo por encima de soluciones iterativas.

Dicho de forma simple: aquí NO ganas por escribir más. Ganas por **pensar mejor**.

## Contenido del simulacro

Dentro de `simulacro/` tienes 10 ejercicios:

1. `01_fibonacci`
2. `02_factorial`
3. `03_sumar_digitos`
4. `04_palindromo`
5. `05_suma_arreglo`
6. `06_maximo_arreglo`
7. `07_staircase`
8. `08_busqueda_binaria`
9. `09_reversa_string`
10. `10_altura_arbol`

Estos problemas cubren patrones clásicos de recursión como:

- factorial,
- fibonacci,
- suma de dígitos,
- reversa de strings,
- palíndromos,
- suma y máximo de arreglos,
- conteo de caminos / staircases,
- búsqueda binaria recursiva,
- recorridos o propiedades de estructuras como árboles.

## Estructura de cada ejercicio

Cada carpeta trae:

- `README.md` → enunciado estilo plataforma,
- `starter.py` → base para resolver,
- `solucion_explicada.md` → solución corta con explicación.

## Cómo usar este repo

La forma correcta de practicar es esta:

1. Entra a un ejercicio.
2. Lee **solo** el `README.md`.
3. Resuélvelo en `starter.py` o en una copia.
4. Recién después compara con `solucion_explicada.md`.

Si miras la solución demasiado pronto, te engañas. Y ese tipo de autoengaño es EXACTAMENTE lo que después te explota en una prueba real.

## Método mental recomendado

Antes de escribir código, responde estas 5 preguntas:

1. **¿Qué representa la función?**
2. **¿Cuál es el caso base más pequeño posible?**
3. **¿Cómo reduzco el problema?**
4. **¿Qué hago con el resultado recursivo?**
5. **¿Cada llamada avanza de verdad hacia el caso base?**

Si no puedes responder eso, todavía NO entiendes el problema. Estás intentando teclear antes de pensar.

## Errores comunes que este pack busca corregir

- olvidar el caso base,
- provocar recursión infinita,
- mezclar una solución iterativa cuando el ejercicio pide recursión,
- devolver un tipo incorrecto,
- usar variables globales sin necesidad,
- entender la idea pero romper la firma pedida.

## Material original e inspiración

El contenido del repositorio está **redactado desde cero** y **no copia enunciados completos** de plataformas.

Sí toma inspiración del estilo de problemas públicos muy conocidos, por ejemplo:

- HackerRank – Interview Preparation Kit – Recursion and Backtracking,
- familias clásicas como Fibonacci, Staircase y Recursive Digit Sum,
- colecciones públicas de práctica de GeeksforGeeks sobre recursión, árboles, listas, palíndromos, búsqueda y subconjuntos.

La intención no es clonar una plataforma. La intención es simular **el tipo de pensamiento** que esa plataforma te exige.

## Documentos base del repo

En la raíz del proyecto tienes dos archivos de contexto:

- `reglas_y_guia_test_recursion.md` → explica el formato esperado del test y cómo conviene practicar.
- `fuentes_publicas_inspiracion.md` → aclara el origen de la inspiración y el criterio de redacción del material.

## Recomendación final

Si vas a rendir una prueba de este estilo, entrena para reconocer patrones, no para copiar recetas.

**Concepto primero. Código después.**
