from GestionDeTareas.model.GestionTareas import Sistemas
from GestionDeTareas.model.GestionTareas import Usuario

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
            self.mostrar_mensaje("Cuenta creada exitosamente.")
        else:
            self.mostrar_mensaje("Error al crear la cuenta. Verifique que el nombre de usuario esté disponible y que la contraseña cumpla los requisitos.")

    def cambiar_contraseña(self, usuario: Usuario):
        contraseña_actual = self.leer_entrada("Ingrese su contraseña actual: ")
        contraseña_nueva = self.leer_entrada("Ingrese su nueva contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial): ")
        confirmar = self.leer_entrada("Confirme su nueva contraseña: ")

        if self.sistema.cambiar_contraseña(usuario, contraseña_actual, contraseña_nueva, confirmar):
            self.mostrar_mensaje("Contraseña cambiada correctamente.")
        else:
            self.mostrar_mensaje("Error al cambiar la contraseña. Verifique los datos ingresados.")