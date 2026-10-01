## Ejercicio 3: La Paciencia de Marge con los Niños (Recursivo)

Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge. Recibe como parámetros dos números (naturales) 
`a` (interrupciones por hora) y `b` (horas de la tarde), y devuelve el total de interrupciones.

def total_interrupciones(a, b):
    if b == 0:
        return 0
    return a + total_interrupciones(a, b-1)
print(total_interrupciones(5, 4))