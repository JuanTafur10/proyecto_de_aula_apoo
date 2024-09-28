import re

class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

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