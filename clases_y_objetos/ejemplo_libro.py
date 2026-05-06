class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        # Encapsulamiento: agrupamos el estado 'cerrado' dentro del objeto
        self._esta_abierto = False 

    # Abstracción: Solo llamamos a abrir(), no nos importa cómo cambia el estado interno
    def abrir(self):
        self._esta_abierto = True
        print(f"El libro '{self.titulo}' ahora está abierto.")

    def leer(self):
        if self._esta_abierto:
            print(f"Leyendo: {self.titulo} de {self.autor}...")
        else:
            print(f"No puedes leer '{self.titulo}', el libro está cerrado.")

# --- Instancias (Reutilización y Modelado) ---
libro_python = Libro("Python Básico", "Guido van Rossum")
novela_fantasia = Libro("El Señor de los Anillos", "J.R.R. Tolkien")

print("--- Demostración de Abstracción ---")
libro_python.leer()  # Intentamos leer sin preocuparnos de la lógica interna
libro_python.abrir() # Acción simple
libro_python.leer()  # Ahora sí funciona