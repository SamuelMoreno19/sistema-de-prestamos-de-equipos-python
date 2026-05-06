class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validación: Si el precio es menor a 0, lanza un error
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

# --- MOSTRAR EN PANTALLA ---
print("--- Creando productos ---")

# Caso exitoso
p1 = Producto("Monitor Asus", 1500000)
print(f"Producto: {p1._nombre} | Precio: ${p1._precio}")

# Caso con error (comentado para que no se detenga el programa)
print("--- Intento de crear producto con precio negativo ---")
try:
    p2 = Producto("Teclado", -50000)
except ValueError as e:
    print(f"Error de validación: {e}")