## Ejercicio 2: La Eficiencia de Homer en la Barbacoa (Iterativo)

Escribir una función iterativa que calcule la cantidad total de donas consumidas en una fiesta.
 Recibe como parámetros dos números (naturales) `a` (donas por persona) y `b` (cantidad de personas), y devuelve el total de donas consumidas.


def total_donas(a, b):
    total= 0
    x= 0
    while x < b:
        total = total + a
        x = x + 1
        return total
print(total_donas(3, 4))