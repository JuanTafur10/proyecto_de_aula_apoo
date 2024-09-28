import re

class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def ingresar_contraseña_actual(self, contraseña_actual: str) -> bool:
        return self.contraseña == contraseña_actual

    def ingresar_nueva_contraseña(self, contraseña_nueva: str):
        self.contraseña = contraseña_nueva

class Sistemas:
    def __init__(self):
        self.usuarios = {}

    def validar_nombre_usuario(self, nombre_usuario: str) -> bool:
        return nombre_usuario not in self.usuarios

    def validar_contraseña(self, contraseña: str) -> bool:
        if len(contraseña) < 6:
            return False
        if (not re.search(r'[A-Z]', contraseña) or
            not re.search(r'\d', contraseña) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña)):
            return False
        return True

    def crear_cuenta_usuario(self, nombre_usuario: str, contraseña: str) -> bool:
        if self.validar_nombre_usuario(nombre_usuario) and self.validar_contraseña(contraseña):
            nuevo_usuario = Usuario(nombre_usuario, contraseña)
            self.usuarios[nombre_usuario] = nuevo_usuario  
            return True
        return False
    
    def validar_contraseña_actual(self, usuario: Usuario, contraseña_actual: str) -> bool:
        return usuario.ingresar_contraseña_actual(contraseña_actual)
    
    def validar_nueva_contraseña(self, contraseña_nueva: str) -> bool:
        if len(contraseña_nueva) < 6:
            return False
        if (not re.search(r'[A-Z]', contraseña_nueva) or
            not re.search(r'\d', contraseña_nueva) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña_nueva)):
            return False
        return True
    
    def cambiar_contraseña(self, usuario: Usuario, contraseña_actual: str, contraseña_nueva: str, confirmar: str) -> bool:
        if not self.validar_contraseña_actual(usuario, contraseña_actual):
            print("Error: La contraseña actual es incorrecta.")
            return False

        if not self.validar_nueva_contraseña(contraseña_nueva):
            print("Error: La nueva contraseña no cumple los requisitos.")
            return False

        if contraseña_nueva != confirmar:
            print("Error: La confirmación de la nueva contraseña no coincide.")
            return False

        usuario.ingresar_nueva_contraseña(contraseña_nueva)
        self.confirmar_cambio_contraseña()
        self.redirigir_a_perfil(usuario.nombre_usuario)
        return True

    def confirmar_cambio_contraseña(self):
        print("La contraseña ha sido cambiada correctamente.")

    def redirigir_a_perfil(self, nombre_usuario: str):
        print(f"Redirigiendo al perfil de {nombre_usuario}...")