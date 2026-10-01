## Ejercicio 7: La Gestión del Kwik-E-Mart

Crear una clase `KwikEMart`, la cual estará representada (atributos internos) mediante varias listas de objetos del tipo `ProductoKwikE`. 
Cada lista corresponde a un pasillo o sección del mercado (ej: "Bebidas", "Snacks", "Conveniencia").

La clase debe contener métodos para facilitar:
*   Controlar el stock de productos (añadir un nuevo producto a un pasillo, remover un producto del inventario, actualizar stock).
*   Calcular cuántos productos expiran en las próximas 24 horas y removerlos del inventario (simulando que Apu los desecha).

**Importante:** Pueden agregar más atributos y métodos si lo consideran necesario (ej: método para buscar un producto por su ID).


import datetime


class ProductoKwikE:

    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def cambiar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_para_vencer(self):
        hoy = datetime.date.today()
        dias = (self.fecha_vencimiento - hoy).days

        if dias < 0:
            print("El producto", self.descripcion, "esta vencido. Stock en 0.")
            self.stock = 0

        return dias

    def __str__(self):
        return f"producto: {self.descripcion} | Id: {self.id_producto} | Precio: {self.precio}$ | Stock: {self.stock}"

    def __eq__(self, other):
        if not isinstance(other, ProductoKwikE):
            return False
        return self.id_producto == other.id_producto and self.descripcion == other.descripcion


class KwikEMart:

    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

    def _pasillo(self, nombre):
        if nombre == "Bebidas":
            return self.bebidas
        elif nombre == "Snacks":
            return self.snacks
        elif nombre == "Conveniencia":
            return self.conveniencia
        else:
            raise ValueError("Pasillo Inexistente")

    def _todas_las_listas(self):
        return [self.bebidas, self.snacks, self.conveniencia]

    def agregar_producto(self, nombre_pasillo, producto):
        self._pasillo(nombre_pasillo).append(producto)

    def buscar_producto(self, id_producto):
        for lista in self._todas_las_listas():
            for p in lista:
                if p.id_producto == id_producto:
                    return p
        return None

    def remover_producto(self, id_producto):
        for lista in self._todas_las_listas():
            i = len(lista) - 1

            while i >= 0:
                if lista[i].id_producto == id_producto:
                    lista.pop(i)
                i = i - 1

    def actualizar_stock(self, id_producto, nuevo_stock):
        p = self.buscar_producto(id_producto)

        if p is None:
            print("No existe el producto", id_producto)
        else:
            p.cambiar_datos(stock=nuevo_stock)

    def descartar_por_vencer(self):
        cantidad = 0

        for lista in self._todas_las_listas():
            i = len(lista) - 1

            while i >= 0:
                if lista[i].dias_para_vencer() <= 1:
                    lista.pop(i)
                    cantidad = cantidad + 1

                i = i - 1

        return cantidad


producto1 = ProductoKwikE("Donuts", 1, datetime.date(2026, 10, 5), 1500.0, 20, "Snacks")

producto2 = ProductoKwikE("Coca Cola", 2, datetime.date(2026, 10, 20), 2000.0, 10, "Bebidas")

mart = KwikEMart()

mart.agregar_producto("Snacks", producto1)
mart.agregar_producto("Bebidas", producto2)

print("Producto buscado:")
print(mart.buscar_producto(1))

print("Stock antes:")
print(producto1.stock)

mart.actualizar_stock(1, 50)

print("Stock después:")
print(producto1.stock)

print("Cantidad descartada:")
print(mart.descartar_por_vencer())