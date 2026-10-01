## Ejercicio 5: El Inventario del Kwik-E-Mart

Definir una clase `ProductoKwikE` que represente un artículo en venta en el Kwik-E-Mart. 
Contiene los datos:
*   `descripcion`: 'string'
*   `id_producto`: 'integer'
*   `fecha_vencimiento`: `date` (importar `datetime`)
*   `precio`: 'float'
*   `stock`: 'integer'

La clase debe contener métodos para facilitar:
*   Cambiar uno o varios datos del producto (descripción, precio, stock).
*   Calcular en cuántos días expira un producto. Si el método detecta que el producto ha expirado, deberá informar al usuario y marcar el stock como 0.

**Importante:** Pueden agregar más atributos y métodos si lo consideran necesario (ej: `categoria`).


import datetime

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria):
        self.descripcion
        self-id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    
    def cambiar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is note None: 
            self.descripcion = descripcion
        if precio is not None: 
            self.precio = precio
        if stock is not None:
            self.stock = stock