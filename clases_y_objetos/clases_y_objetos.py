class Coche:
     # Aquí definiremos los atributos y métodos
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año

# Creamos dos objetos de tipo Coche
mi_coche = Coche("BMW", "rojo", 2020)
coche_de_amigo = Coche("Toyota", "gris", 2015)

print("--- Datos de mi coche ---")
print(f"Marca: {mi_coche.marca}")
print(f"Color: {mi_coche.color}")
print(f"Año: {mi_coche.año}")

