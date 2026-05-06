# 1. Clase Padre (necesaria para que funcione super())
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

# 2. Tu clase Electrónico
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    def activar(self):
        self._activado = True
        return f"{self._nombre} encendido."

    def set_precio(self, nuevo_precio):
        super().set_precio(nuevo_precio)
        if nuevo_precio > 1000:
            self._garantia_meses = max(self._garantia_meses, 24)

# 3. Código para tirar el PRINT
# Creamos una laptop con 12 meses de garantía
mi_laptop = Electronico("Asus", 900, 5, 12)

print(f"Producto: {mi_laptop._nombre}")
print(f"Garantía inicial: {mi_laptop._garantia_meses} meses")

# Subimos el precio para activar la lógica de garantía extendida
mi_laptop.set_precio(1500)

print(f"Nuevo precio: ${mi_laptop._precio}")
print(f"Garantía final: {mi_laptop._garantia_meses} meses (actualizada automáticamente)")
print(mi_laptop.activar())