## Ejercicio 6: La Etiqueta de los Productos del Kwik-E-Mart (Sobrecarga de Métodos)

Sobrecargar los siguientes métodos en la clase `ProductoKwikE`:
*   `__str__`: Para representar el producto de forma legible (ej: "Producto: Donuts Glaseadas | ID: 123 | Precio: $1.50 | Stock: 50").
*   `__eq__`: Para comparar si dos productos son iguales basándose en su `id_producto` y `descripcion`.


def __str__(self):
    return f"producto: {self.descripcion} | Id: {self.id_producto} | Precio: {self.precio}$ | Stock: {self.stock}"

def __eq__(self, other):
    if not isinstance(other, ProductoKwikE):
        return False
    return self.id_producto == other.id_producto and self.descripcion == other.descripcion