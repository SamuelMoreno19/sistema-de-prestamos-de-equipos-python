class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        # Creamos un objeto Persona
ana = Persona("Ana García", 28)

# Python internamente hace algo equivalente a:
# Persona.__init__(ana, "Ana García", 28)
# Creamos dos objetos Persona
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35