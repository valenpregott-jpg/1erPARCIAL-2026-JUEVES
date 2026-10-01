class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def agregar(self, dato):
        nuevo = Nodo(dato)
        actual = self.header

        while actual._nxt is not None:
            actual = actual._nxt

        actual._nxt = nuevo

    def buscar(self, id_producto):
        actual = self.header._nxt

        while actual is not None:
            if actual._elem.id_producto == id_producto:
                return actual._elem

            actual = actual._nxt

        return None

    def eliminar(self, id_producto):
        anterior = self.header
        actual = self.header._nxt

        while actual is not None:
            if actual._elem.id_producto == id_producto:
                anterior._nxt = actual._nxt
                return

            anterior = actual
            actual = actual._nxt

    def __iter__(self):
        return IteradorLista(self)


class IteradorLista:
    def __init__(self, lista):
        self.actual = lista.header._nxt

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        dato = self.actual._elem
        self.actual = self.actual._nxt

        return dato


class KwikEMart:
    def __init__(self):
        self.bebidas = ListaEnlazada()
        self.snacks = ListaEnlazada()
        self.conveniencia = ListaEnlazada()

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
        self._pasillo(nombre_pasillo).agregar(producto)

    def buscar_producto(self, id_producto):
        for lista in self._todas_las_listas():
            producto = lista.buscar(id_producto)

            if producto is not None:
                return producto

        return None

    def remover_producto(self, id_producto):
        for lista in self._todas_las_listas():
            producto = lista.buscar(id_producto)

            if producto is not None:
                lista.eliminar(id_producto)
                return

    def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_producto(id_producto)

        if producto is None:
            print("No existe el producto", id_producto)
        else:
            producto.cambiar_datos(stock=nuevo_stock)

    def descartar_por_vencer(self):
        cantidad = 0

        for lista in self._todas_las_listas():
            productos_a_eliminar = []

            for producto in lista:
                if producto.dias_para_vencer() <= 1:
                    productos_a_eliminar.append(producto.id_producto)

            for id_producto in productos_a_eliminar:
                lista.eliminar(id_producto)
                cantidad = cantidad + 1

        return cantidad