from GestionDeTareas.model.GestionTareas import Sistemas
from GestionDeTareas.model.GestionTareas import Usuario
from GestionDeTareas.model.GestionTareas import Tarea

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

    def iniciar_sesion(self):
            nombre_usuario = self.leer_entrada("Ingrese su nombre de usuario: ")
            contraseña = self.leer_entrada("Ingrese su contraseña: ")

            if self.sistema.validar_credenciales(nombre_usuario, contraseña):
                self.mostrar_mensaje(self.sistema.autenticar_usuario(nombre_usuario))
                return self.sistema.usuarios[nombre_usuario]
            else:
                self.mostrar_mensaje("Error: Las credenciales son incorrectas.")
                return None
            
    
    def crear_tarea(self):
        titulo = self.leer_entrada("Ingrese el título de la tarea: ")
        descripcion = self.leer_entrada("Ingrese la descripción de la tarea: ")
        fecha_limite = self.leer_entrada("Ingrese la fecha límite de la tarea (YYYY-MM-DD): ")
        prioridad = self.leer_entrada("Ingrese la prioridad de la tarea (alta, media, baja): ")
        categoria_nombre = self.leer_entrada("Ingrese la categoría de la tarea (deje en blanco para ninguna): ")
        categoria = None
        if categoria_nombre:
            categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
            if not categoria:
                self.mostrar_mensaje(f"Categoría '{categoria_nombre}' no encontrada. Creando nueva categoría.")
                categoria = self.sistema.crear_categoria(categoria_nombre)
        tarea = self.sistema.crear_tarea(titulo, descripcion, fecha_limite, prioridad, categoria)
        self.mostrar_mensaje(f"Tarea creada: {tarea}")

    def editar_tarea(self):
        tarea_id = int(self.leer_entrada("Ingrese el ID de la tarea a editar: "))
        titulo = self.leer_entrada("Ingrese el nuevo título de la tarea (deje en blanco para no cambiar): ")
        descripcion = self.leer_entrada("Ingrese la nueva descripción de la tarea (deje en blanco para no cambiar): ")
        fecha_limite = self.leer_entrada("Ingrese la nueva fecha límite de la tarea (YYYY-MM-DD) (deje en blanco para no cambiar): ")
        prioridad = self.leer_entrada("Ingrese la nueva prioridad de la tarea (alta, media, baja) (deje en blanco para no cambiar): ")
        categoria_nombre = self.leer_entrada("Ingrese la nueva categoría de la tarea (deje en blanco para no cambiar): ")
        categoria = None
        if categoria_nombre:
            categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
            if not categoria:
                self.mostrar_mensaje(f"Categoría '{categoria_nombre}' no encontrada. Creando nueva categoría.")
                categoria = self.sistema.crear_categoria(categoria_nombre)
        tarea = self.sistema.editar_tarea(tarea_id, titulo or None, descripcion or None, fecha_limite or None, prioridad or None, categoria)
        if tarea:
            self.mostrar_mensaje(f"Tarea editada: {tarea}")

    def eliminar_tarea(self):
        tarea_id = int(self.leer_entrada("Ingrese el ID de la tarea a eliminar: "))
        tarea = self.sistema.eliminar_tarea(tarea_id)
        if tarea:
            self.mostrar_mensaje(f"Tarea eliminada: {tarea}")

    def crear_categoria(self):
        nombre = self.leer_entrada("Ingrese el nombre de la nueva categoría: ")
        categoria = self.sistema.crear_categoria(nombre)
        self.mostrar_mensaje(f"Categoría creada: {categoria}")

    def mostrar_tareas_por_categoria(self):
        nombre_categoria = self.leer_entrada("Ingrese el nombre de la categoría: ")
        tareas = self.sistema.obtener_tareas_por_categoria(nombre_categoria)
        if tareas:
            self.mostrar_mensaje(f"Tareas en la categoría '{nombre_categoria}':")
            for tarea in tareas:
                self.mostrar_mensaje(str(tarea))
        else:
            self.mostrar_mensaje(f"No hay tareas en la categoría '{nombre_categoria}'.")

    def asignar_categoria_a_tarea(self):
        tarea_id = int(self.leer_entrada("Ingrese el ID de la tarea a la que desea asignar una categoría: "))
        categoria_nombre = self.leer_entrada("Ingrese el nombre de la categoría: ")
        categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
        if not categoria:
            self.mostrar_mensaje(f"Categoría '{categoria_nombre}' no encontrada.")
            return
        tarea = self.sistema.editar_tarea(tarea_id, categoria=categoria)
        if tarea:
            self.mostrar_mensaje(f"Tarea actualizada con nueva categoría: {tarea}")