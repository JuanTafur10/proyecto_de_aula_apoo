import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import ttk
from GestionDeTareas.model.GestionTareas import Categoria
from GestionDeTareas.model.GestionTareas import Usuario
from GestionDeTareas.model.GestionTareas import Tarea
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class UITkinter(tk.Tk):
    def __init__(self, sistema):
        super().__init__()
        self.sistema = sistema
        self.configure(bg="black")  # esto sirve para el fondo negro de la ventana principal
        self.title("Gestión de Tareas")
        self.geometry("800x600")  # tamanhio de la pantalla
        
        # Estilo general
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", padding=6, relief="flat", background="#333", foreground="white", font=("Helvetica", 12, "bold"))
        style.map("TButton", background=[("active", "#555")])

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        tk.Label(self, text=" Menú 📗", font=("Helvetica", 16, "bold"), bg="black", fg="white").pack(pady=10)

        botones = [
            ("Crear Cuenta de Usuario", self.crear_cuenta),
            ("Iniciar Sesión", self.iniciar_sesion),
            ("Cambiar Contraseña", self.cambiar_contraseña),
            ("Crear Tarea", self.crear_tarea),
            ("Editar Tarea", self.editar_tarea),
            ("Eliminar Tarea", self.eliminar_tarea),
            ("Crear Categoría", self.crear_categoria),
            ("Mostrar Tareas por Categoría", self.mostrar_tareas_por_categoria),
            ("Generar Informe en PDF", self.generar_informe_pdf),
            ("Salir ↩️", self.quit)
        ]

        for text, command in botones:
            btn = ttk.Button(self, text=text, command=command, style="TButton")
            btn.pack(pady=5, padx=20, fill="x")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_mensaje(self, mensaje: str):
        messagebox.showinfo("Mensaje", mensaje)

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error", mensaje)

    def leer_entrada(self, mensaje: str) -> str:
        return simpledialog.askstring("Entrada", mensaje)

    def crear_cuenta(self):
        try:
            nombre_usuario = self.leer_entrada("Ingrese un nombre de usuario:")
            if not nombre_usuario:
                raise ValueError("El nombre de usuario es obligatorio.")

            contraseña = self.leer_entrada("Ingrese una contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial):")
            if not contraseña:
                raise ValueError("La contraseña es obligatoria.")

            if not self.sistema.validar_nueva_contraseña(contraseña):
                raise ValueError("La contraseña no cumple los requisitos.")

            if self.sistema.crear_cuenta_usuario(nombre_usuario, contraseña):
                self.mostrar_mensaje("Cuenta creada exitosamente.")
            else:
                self.mostrar_error("Error al crear la cuenta. Verifique que el nombre de usuario esté disponible y que la contraseña cumpla los requisitos.")
        except ValueError as ve:
            self.mostrar_error(f"Error: {ve}")
        except Exception as e:
            self.mostrar_error(f"Error inesperado: {e}")

    def iniciar_sesion(self):
        try:
            nombre_usuario = simpledialog.askstring("Iniciar Sesión", "Ingrese nombre de usuario:")
            contraseña = simpledialog.askstring("Iniciar Sesión", "Ingrese contraseña:", show="*")

            if self.sistema.validar_credenciales(nombre_usuario, contraseña):
                messagebox.showinfo("Éxito", f"Sesión iniciada para {nombre_usuario}.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def cambiar_contraseña(self):
        try:
            nombre_usuario = self.leer_entrada("Ingrese su nombre de usuario:")
            if not nombre_usuario:
                raise ValueError("El nombre de usuario es obligatorio.")

            usuario = self.sistema.usuarios.get(nombre_usuario)
            if not usuario:
                raise ValueError("El usuario no existe.")

            contraseña_actual = self.leer_entrada("Ingrese su contraseña actual:")
            if not contraseña_actual:
                raise ValueError("La contraseña actual es obligatoria.")

            if not self.sistema.validar_contraseña_actual(usuario, contraseña_actual):
                raise ValueError("La contraseña actual es incorrecta.")

            contraseña_nueva = self.leer_entrada("Ingrese su nueva contraseña (mínimo 6 caracteres, con al menos una mayúscula, un número y un carácter especial):")
            if not contraseña_nueva:
                raise ValueError("La nueva contraseña es obligatoria.")

            if not self.sistema.validar_nueva_contraseña(contraseña_nueva):
                raise ValueError("La nueva contraseña no cumple los requisitos.")

            confirmar = self.leer_entrada("Confirme su nueva contraseña:")
            if not confirmar:
                raise ValueError("La confirmación de la nueva contraseña es obligatoria.")

            if self.sistema.cambiar_contraseña(usuario, contraseña_actual, contraseña_nueva, confirmar):
                self.mostrar_mensaje("Contraseña cambiada correctamente.")
            else:
                self.mostrar_error("Error al cambiar la contraseña. Verifique los datos ingresados.")
        except ValueError as ve:
            self.mostrar_error(f"Error: {ve}")
        except Exception as e:
            self.mostrar_error(f"Error inesperado: {e}")

    def crear_tarea(self):
        try:
            titulo = self.leer_entrada("Ingrese el título de la tarea:")
            if not titulo or titulo.isspace():
                raise ValueError("El título es obligatorio.")

            descripcion = self.leer_entrada("Ingrese la descripción de la tarea:")
            if not descripcion or descripcion.isspace():
                raise ValueError("La descripción es obligatoria.")

            fecha_limite = self.leer_entrada("Ingrese la fecha límite de la tarea (YYYY-MM-DD):")
            if not fecha_limite or fecha_limite.isspace():
                raise ValueError("La fecha límite es obligatoria.")

            prioridad = self.leer_entrada("Ingrese la prioridad de la tarea (alta, media, baja):")
            if not prioridad or prioridad.isspace():
                raise ValueError("La prioridad es obligatoria.")

            categoria_nombre = self.leer_entrada("Ingrese la categoría de la tarea (deje en blanco para ninguna):")
            categoria = None
            if categoria_nombre and not categoria_nombre.isspace():
                categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
                if not categoria:
                    self.mostrar_mensaje(f"Categoría '{categoria_nombre}' no encontrada. Creando nueva categoría.")
                    categoria = self.sistema.crear_categoria(categoria_nombre)

            tarea = self.sistema.crear_tarea(titulo, descripcion, fecha_limite, prioridad, categoria)
            self.mostrar_mensaje(f"Tarea creada: {tarea}")
        except ValueError as ve:
            self.mostrar_error(f"Error: {ve}")
        except Exception as e:
            self.mostrar_error(f"Error inesperado: {e}")

    def editar_tarea(self):
        try:
            tarea_id = simpledialog.askinteger("Editar Tarea", "Ingrese el ID de la tarea a editar:")
            if not tarea_id:
                return

            tarea = next((t for t in self.sistema.tareas if t.id == tarea_id), None)
            if not tarea:
                messagebox.showerror("Error", "Tarea no encontrada.")
                return

            titulo = simpledialog.askstring("Editar Tarea", "Nuevo título (deje en blanco para no cambiar):", initialvalue=tarea.titulo)
            descripcion = simpledialog.askstring("Editar Tarea", "Nueva descripción (deje en blanco para no cambiar):", initialvalue=tarea.descripcion)
            fecha_limite = simpledialog.askstring("Editar Tarea", "Nueva fecha límite (YYYY-MM-DD):", initialvalue=tarea.fecha_limite)
            prioridad = simpledialog.askstring("Editar Tarea", "Nueva prioridad (alta, media, baja):", initialvalue=tarea.prioridad)
            categoria_nombre = simpledialog.askstring("Editar Tarea", "Nueva categoría (deje en blanco para no cambiar):", initialvalue=tarea.categoria.nombre if tarea.categoria else "")

            categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
            if not categoria and categoria_nombre:
                categoria = self.sistema.crear_categoria(categoria_nombre)

            self.sistema.editar_tarea(tarea_id, titulo, descripcion, fecha_limite, prioridad, categoria)
            messagebox.showinfo("Éxito", "Tarea editada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al editar la tarea: {e}")

    def eliminar_tarea(self):
        try:
            tarea_id = simpledialog.askinteger("Eliminar Tarea", "Ingrese el ID de la tarea a eliminar:")
            if not tarea_id:
                return

            tarea = self.sistema.eliminar_tarea(tarea_id)
            if tarea:
                messagebox.showinfo("Éxito", f"Tarea eliminada: {tarea}")
            else:
                messagebox.showerror("Error", "Tarea no encontrada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar la tarea: {e}")

    def crear_categoria(self):
        try:
            nombre = simpledialog.askstring("Crear Categoría", "Ingrese el nombre de la categoría:")
            categoria = self.sistema.crear_categoria(nombre)
            messagebox.showinfo("Éxito", f"Categoría creada: {categoria}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al crear la categoría: {e}")

    def mostrar_tareas_por_categoria(self):
        try:
            nombre_categoria = simpledialog.askstring("Mostrar Tareas", "Ingrese el nombre de la categoría:")
            tareas = self.sistema.obtener_tareas_por_categoria(nombre_categoria)
            if tareas:
                tarea_str = "\n".join(str(t) for t in tareas)
                messagebox.showinfo(f"Tareas en '{nombre_categoria}'", tarea_str)
            else:
                messagebox.showinfo("Información", f"No hay tareas en la categoría '{nombre_categoria}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al mostrar las tareas: {e}")

    def generar_informe_pdf(self):
        try:
            nombre_usuario = self.leer_entrada("Ingrese el nombre de usuario:")
            if not nombre_usuario:
                raise ValueError("El nombre de usuario es obligatorio.")

            archivo_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if not archivo_pdf:
                return

            self.sistema.generar_informe_pdf(nombre_usuario, archivo_pdf)
            self.mostrar_mensaje(f"Informe generado en {archivo_pdf}")
        except ValueError as ve:
            self.mostrar_error(f"Error: {ve}")
        except Exception as e:
            self.mostrar_error(f"Error inesperado: {e}")
