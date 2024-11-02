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
        try:
            nombre_usuario = self.leer_entrada("Ingrese un nombre de usuario: ")
            if not nombre_usuario:
                raise ValueError("El nombre de usuario es obligatorio.")

            contraseña = self.leer_entrada("Ingrese una contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial): ")
            if not contraseña:
                raise ValueError("La contraseña es obligatoria.")

            if not self.sistema.validar_nueva_contraseña(contraseña):
                raise ValueError("La contraseña no cumple los requisitos.")

            if self.sistema.crear_cuenta_usuario(nombre_usuario, contraseña):
                self.mostrar_mensaje("Cuenta creada exitosamente.")
            else:
                self.mostrar_mensaje("Error al crear la cuenta. Verifique que el nombre de usuario esté disponible y que la contraseña cumpla los requisitos.")
        except ValueError as ve:
            self.mostrar_mensaje(f"Error: {ve}")
        except Exception as e:
            self.mostrar_mensaje(f"Error inesperado: {e}")

    def cambiar_contraseña(self, usuario: Usuario):
        try:
            contraseña_actual = self.leer_entrada("Ingrese su contraseña actual: ")
            if not contraseña_actual:
                raise ValueError("La contraseña actual es obligatoria.")

            if not self.sistema.validar_contraseña_actual(usuario, contraseña_actual):
                raise ValueError("La contraseña actual es incorrecta.")

            contraseña_nueva = self.leer_entrada("Ingrese su nueva contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial): ")
            if not contraseña_nueva:
                raise ValueError("La nueva contraseña es obligatoria.")

            if not self.sistema.validar_nueva_contraseña(contraseña_nueva):
                raise ValueError("La nueva contraseña no cumple los requisitos.")

            confirmar = self.leer_entrada("Confirme su nueva contraseña: ")
            if not confirmar:
                raise ValueError("La confirmación de la nueva contraseña es obligatoria.")

            if self.sistema.cambiar_contraseña(usuario, contraseña_actual, contraseña_nueva, confirmar):
                self.mostrar_mensaje("Contraseña cambiada correctamente.")
            else:
                self.mostrar_mensaje("Error al cambiar la contraseña. Verifique los datos ingresados.")
        except ValueError as ve:
            self.mostrar_mensaje(f"Error: {ve}")
        except Exception as e:
            self.mostrar_mensaje(f"Error inesperado: {e}")

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
        try:
            titulo = self.leer_entrada("Ingrese el título de la tarea: ")
            if not titulo:
                raise ValueError("El título es obligatorio.")

            descripcion = self.leer_entrada("Ingrese la descripción de la tarea: ")
            if not descripcion:
                raise ValueError("La descripción es obligatoria.")

            fecha_limite = self.leer_entrada("Ingrese la fecha límite de la tarea (YYYY-MM-DD): ")
            if not fecha_limite:
                raise ValueError("La fecha límite es obligatoria.")

            prioridad = self.leer_entrada("Ingrese la prioridad de la tarea (alta, media, baja): ")
            if not prioridad:
                raise ValueError("La prioridad es obligatoria.")

            categoria_nombre = self.leer_entrada("Ingrese la categoría de la tarea (deje en blanco para ninguna): ")
            categoria = None
            if categoria_nombre:
                categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
                if not categoria:
                    self.mostrar_mensaje(f"Categoría '{categoria_nombre}' no encontrada. Creando nueva categoría.")
                    categoria = self.sistema.crear_categoria(categoria_nombre)

            tarea = self.sistema.crear_tarea(titulo, descripcion, fecha_limite, prioridad, categoria)
            self.mostrar_mensaje(f"Tarea creada: {tarea}")

        except ValueError as ve:
            self.mostrar_mensaje(f"Error: {ve}")
        except Exception as e:
            self.mostrar_mensaje(f"Error inesperado: {e}")

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

    def generar_informe_pdf(self):
        nombre_usuario = self.leer_entrada("Ingrese el nombre de usuario: ")
        archivo_pdf = self.leer_entrada("Ingrese el nombre del archivo PDF (con extensión .pdf): ")
        self.sistema.generar_informe_pdf(nombre_usuario, archivo_pdf)