from GestionDeTareas.model.GestionTareas import Sistemas

class UIConsola:
    def __init__(self, sistema: Sistemas):
        self.sistema = sistema

    def mostrar_mensaje(self, mensaje: str):
        print(mensaje)

    def leer_entrada(self, mensaje: str) -> str:
        return input(mensaje)

    def crear_cuenta(self):
        nombre_usuario = self.leer_entrada("Ingrese un nombre de usuario: ")
        contraseña = self.leer_entrada("Ingrese una contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial): ")

        if self.sistema.crear_cuenta_usuario(nombre_usuario, contraseña):
            self.mostrar_mensaje("Registro realizado apropiadamente. Cuenta creada.")
            self.redirigir_a_perfil(nombre_usuario)
        else:
            self.mostrar_mensaje("Error al crear la cuenta. Asegúrese de que el nombre de usuario no esté en uso y que la contraseña sea válida.")

    def redirigir_a_perfil(self, nombre_usuario: str):
        self.mostrar_mensaje(f"Redirigiendo a la pantalla de bienvenida de {nombre_usuario}...")