class Nodo:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        nuevo_nodo = Nodo(codigo, nombre, cantidad, precio)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_producto(self, codigo):
        actual = self.cabeza
        anterior = None
        while actual and actual.codigo != codigo:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            print("Producto no encontrado.")
        else:
            if anterior is None:
                self.cabeza = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente

    def buscar_producto(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def listar_productos(self):
        actual = self.cabeza
        while actual:
            print(f"Código: {actual.codigo}, Nombre: {actual.nombre}, Cantidad: {actual.cantidad}, Precio: {actual.precio}")
            actual = actual.siguiente

    def modificar_producto(self, codigo, nuevo_nombre, nueva_cantidad, nuevo_precio):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.cantidad = nueva_cantidad
            producto.precio = nuevo_precio
        else:
            print("Producto no encontrado.")

    def vaciar_inventario(self):
        self.cabeza = None

inventario = ListaEnlazada()
inventario.agregar_producto(1, "Manzana", 10, 2.5)
inventario.agregar_producto(2, "Banana", 15, 1.8)
inventario.agregar_producto(3, "Naranja", 8, 2)

inventario.listar_productos()

producto_encontrado = inventario.buscar_producto(2)
if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado.nombre}")

inventario.modificar_producto(2, "Plátano", 20, 2)
inventario.listar_productos()

inventario.eliminar_producto(1)
inventario.listar_productos()