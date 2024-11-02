import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from GestionDeTareas.model.GestionTareas import Categoria

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

    def crear_cuenta(self):
        try:
            nombre_usuario = simpledialog.askstring("Crear Cuenta", "Ingrese nombre de usuario:")
            contraseña = simpledialog.askstring("Crear Cuenta", "Ingrese una contraseña:", show="*")

            if self.sistema.crear_cuenta_usuario(nombre_usuario, contraseña):
                messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
            else:
                messagebox.showerror("Error", "Error al crear la cuenta. Verifique los datos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

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
            nombre_usuario = simpledialog.askstring("Cambiar Contraseña", "Ingrese su nombre de usuario:")
            if nombre_usuario not in self.sistema.usuarios:
                messagebox.showerror("Error", "El usuario no existe.")
                return

            usuario = self.sistema.usuarios[nombre_usuario]
            contraseña_actual = simpledialog.askstring("Cambiar Contraseña", "Ingrese su contraseña actual:", show="*")
            nueva_contraseña = simpledialog.askstring("Cambiar Contraseña", "Ingrese su nueva contraseña:", show="*")
            confirmar = simpledialog.askstring("Cambiar Contraseña", "Confirme su nueva contraseña:", show="*")

            if self.sistema.cambiar_contraseña(usuario, contraseña_actual, nueva_contraseña, confirmar):
                messagebox.showinfo("Éxito", "Contraseña cambiada correctamente.")
            else:
                messagebox.showerror("Error", "Error al cambiar la contraseña.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def crear_tarea(self):
        try:
            titulo = simpledialog.askstring("Crear Tarea", "Ingrese el título:")
            descripcion = simpledialog.askstring("Crear Tarea", "Ingrese la descripción:")
            fecha_limite = simpledialog.askstring("Crear Tarea", "Ingrese la fecha límite (YYYY-MM-DD):")
            prioridad = simpledialog.askstring("Crear Tarea", "Ingrese la prioridad (alta, media, baja):")
            categoria_nombre = simpledialog.askstring("Crear Tarea", "Ingrese la categoría (deje en blanco para ninguna):")

            categoria = None
            if categoria_nombre:
                categoria = next((cat for cat in self.sistema.categorias if cat.nombre == categoria_nombre), None)
                if not categoria:
                    categoria = self.sistema.crear_categoria(categoria_nombre)

            tarea = self.sistema.crear_tarea(titulo, descripcion, fecha_limite, prioridad, categoria)
            messagebox.showinfo("Éxito", f"Tarea creada: {tarea}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al crear la tarea: {e}")

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
            nombre_usuario = simpledialog.askstring("Generar Informe", "Ingrese el nombre del usuario:")
            archivo_pdf = simpledialog.askstring("Generar Informe", "Ingrese el nombre del archivo PDF (con .pdf):")
            resultado = self.sistema.generar_informe_pdf(nombre_usuario, archivo_pdf)
            messagebox.showinfo("Resultado", resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el informe: {e}")
