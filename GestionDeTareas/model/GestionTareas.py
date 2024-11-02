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
        self.tareas = []

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
        if nombre_usuario in self.usuarios:
            return False 
        self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contraseña)
        return True
    
    def validar_credenciales(self, nombre_usuario: str, contraseña: str) -> bool:
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.contraseña == contraseña:
            return True
        return False
    
    def autenticar_usuario(self, nombre_usuario: str) -> str:
        return (f"Bienvenido {nombre_usuario}.")
    
    def validar_contraseña_actual(self, usuario: Usuario, contraseña_actual: str) -> bool:
        return usuario.ingresar_contraseña_actual(contraseña_actual)

    def cambiar_contraseña(self, usuario: Usuario, contraseña_actual: str, contraseña_nueva: str, confirmar: str) -> bool:
        if not self.validar_contraseña_actual(usuario, contraseña_actual):
            print('Error: La contraseña actual es incorrecta.')
            return False

        if not self.validar_nueva_contraseña(contraseña_nueva):
            print('Error: La nueva contraseña no cumple los requisitos.')
            return False

        if contraseña_nueva != confirmar:
            print('Error: La confirmación de la nueva contraseña no coincide.')
            return False

        usuario.ingresar_nueva_contraseña(contraseña_nueva)
        self.confirmar_cambio_contraseña()
        self.redirigir_a_perfil(usuario.nombre_usuario)
        return True
    
    def validar_nueva_contraseña(self, contraseña_nueva: str) -> bool:
        if len(contraseña_nueva) < 6:
            return False
        if (not re.search(r'[A-Z]', contraseña_nueva) or
            not re.search(r'\d', contraseña_nueva) or
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña_nueva)):
            return False
        return True
    
    def crear_tarea(self, titulo: str, descripcion: str, fecha_limite: str, prioridad: str):
        nueva_tarea = Tarea(titulo, descripcion, fecha_limite, prioridad)
        self.tareas.append(nueva_tarea)
        print("Tarea creada exitosamente.")
        return nueva_tarea

class Tarea:
    def __init__(self, titulo: str, descripcion: str, fecha_limite: str, prioridad: str):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
    def __str__(self):
        return f"Tarea(titulo={self.titulo}, descripcion={self.descripcion}, fecha_limite={self.fecha_limite}, prioridad={self.prioridad})"
    


def confirmar_cambio_contraseña(self):
    print("La contraseña ha sido cambiada correctamente.")

def redirigir_a_perfil(self, nombre_usuario: str):
    print(f"Redirigiendo al perfil de {nombre_usuario}...")
    print("Error: Las credenciales son incorrectas.")

def mostrar_mensaje_error(self):
    print("Error: Las credenciales son incorrectas.")

    