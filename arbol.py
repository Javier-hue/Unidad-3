class NodoFamilia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioFamilia:
    def __init__(self):
        self.raiz = None

    def agregar(self, nombre, madre=None, posicion="izquierdo"):
        nuevo_nodo = NodoFamilia(nombre)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            print(f"{nombre} agregada como la raíz del árbol.")
        else:
            madre_nodo = self.buscar(madre)
            if madre_nodo:
                if posicion == "izquierdo" and madre_nodo.izquierdo is None:
                    madre_nodo.izquierdo = nuevo_nodo
                    print(f"{nombre} agregada como hija izquierdo de {madre}.")
                elif posicion == "derecho" and madre_nodo.derecho is None:
                    madre_nodo.derecho = nuevo_nodo
                    print(f"{nombre} agregado como hijo derecho de {madre}.")
                else:
                    print(f"{posicion} ya está ocupado para {madre}.")
            else:
                print(f"madre {madre} no encontrada en el árbol.")

    def eliminar(self, nombre):
        def eliminar_nodo(nodo, nombre):
            if nodo is None:
                return nodo
            if nombre < nodo.nombre:
                nodo.izquierdo = eliminar_nodo(nodo.izquierdo, nombre)
            elif nombre > nodo.nombre:
                nodo.derecho = eliminar_nodo(nodo.derecho, nombre)
            else:
                if nodo.izquierdo is None:
                    return nodo.derecho
                elif nodo.derecho is None:
                    return nodo.izquierdo
                sucesor = self.minimo_nodo(nodo.derecho)
                nodo.nombre = sucesor.nombre
                nodo.derecho = eliminar_nodo(nodo.derecho, sucesor.nombre)
            return nodo

        self.raiz = eliminar_nodo(self.raiz, nombre)
        print(f"{nombre} eliminado del árbol.")

    def buscar(self, nombre):
        def buscar_nodo(nodo, nombre):
            if nodo is None or nodo.nombre == nombre:
                return nodo
            if nombre < nodo.nombre:
                return buscar_nodo(nodo.izquierdo, nombre)
            return buscar_nodo(nodo.derecho, nombre)

        resultado = buscar_nodo(self.raiz, nombre)
        if resultado:
            print(f"{nombre} encontrado en el árbol.")
        else:
            print(f"{nombre} no encontrado en el árbol.")
        return resultado

    def mostrar(self):
        def mostrar_arbol(nodo, nivel=0):
            if nodo is not None:
                mostrar_arbol(nodo.derecho, nivel + 1)
                print("    " * nivel + f"- {nodo.nombre}")
                mostrar_arbol(nodo.izquierdo, nivel + 1)

        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            mostrar_arbol(self.raiz)

arbol = ArbolBinarioFamilia()

arbol.agregar("Abuela")
arbol.agregar("madre", "Abuela", "izquierdo")
arbol.agregar("Tío", "Abuela", "derecho")
arbol.agregar("Hijo", "madre", "izquierdo")
arbol.agregar("Hija", "madre", "derecho")

print("\nÁrbol Familiar:")
arbol.mostrar()

arbol.buscar("Hijo")

arbol.eliminar("Tío")

print("\nÁrbol Familiar Actualizado:")
arbol.mostrar()
