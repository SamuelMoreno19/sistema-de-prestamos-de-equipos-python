# Versión inicial con atributos públicos
class ProductoV1:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Versión intermedia con getters y setters
class ProductoV2:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_precio(self):
        return self._precio

    def set_precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# Versión final con propiedades
class ProductoV3:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

# -------------------------
# PRUEBAS

# ProductoV1
p1 = ProductoV1("Mouse", 50)
print("ProductoV1:")
print(p1.nombre)
print(p1.precio)

# ProductoV2
p2 = ProductoV2("Teclado", 100)
print("\nProductoV2:")
print(p2.get_nombre())
print(p2.get_precio())

p2.set_precio(120)
print("Nuevo precio:", p2.get_precio())

# ProductoV3
p3 = ProductoV3("Monitor", 300)
print("\nProductoV3:")
print(p3.nombre)
print(p3.precio)

p3.precio = 350
print("Nuevo precio:", p3.precio)        