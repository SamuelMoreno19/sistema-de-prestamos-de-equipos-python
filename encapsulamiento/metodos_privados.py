# --- TU CLASE ---
class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        # Se guarda la contraseña encriptada, nunca en texto plano
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        import hashlib
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        hash_ingresado = self.__generar_hash(contraseña_ingresada)
        return hash_ingresado == self._contraseña_hash

# --- CÓDIGO PARA EL PRINT ---
# 1. Creamos el usuario
user1 = Autenticador("samuel_dev", "12345")

# 2. Intentamos entrar
print("--- Sistema de Login ---")
intento1 = "9999"
print(f"¿Entra con '{intento1}'?: {user1.verificar_contraseña(intento1)}")

intento2 = "12345"
print(f"¿Entra con '{intento2}'?: {user1.verificar_contraseña(intento2)}")

# 3. Dato clave para la clase:
# Si intentas hacer esto: user1.__generar_hash("hola"), Python te dará un ERROR.
# Eso demuestra que el método está protegido.