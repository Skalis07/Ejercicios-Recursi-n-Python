def fibonacci(n: int) -> int:
    # Escribe tu solución recursiva aquí
    if n >= 0 and n <= 30:    
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    else:
        raise ValueError("n debe ser un número entero entre 0 y 30 inclusive.")
    
print(fibonacci(8))
