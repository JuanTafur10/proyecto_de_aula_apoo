from GestionDeTareas.model.GestionTareas import Sistemas
from GestionDeTareas.view.console import UIConsola

def main():
    sistema = Sistemas()
    ui = UIConsola(sistema)

    while True:
        print("\n--- Menu ---")
        print("1. Crear Cuenta de Usuario")
        print("2. Iniciar Sesión")
        print("3. Cambiar Contraseña")
        print("4. Crear Tarea")
        print("5. Editar Tarea")
        print("6. Eliminar Tarea")
        print("7. Crear Categoría")
        print("8. Mostrar Tareas por Categoría")
        print("9. Generar Informe en PDF")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ui.crear_cuenta()
        elif opcion == "2":
            usuario = ui.iniciar_sesion()
            if usuario:
                print(f"Sesión iniciada para {usuario.nombre_usuario}.")
        elif opcion == "3":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            if nombre_usuario in sistema.usuarios:
                usuario = sistema.usuarios[nombre_usuario]
                ui.cambiar_contraseña(usuario)
            else:
                print("Error: El usuario no existe.")
        elif opcion == "4":
            ui.crear_tarea()
        elif opcion == "5":
            ui.editar_tarea()
        elif opcion == "6":
            ui.eliminar_tarea()
        elif opcion == "7":
            ui.crear_categoria()
        elif opcion == "8":
            ui.mostrar_tareas_por_categoria()
        elif opcion == "9":
            ui.generar_informe_pdf()
        elif opcion == "10":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            ui.mostrar_mensaje("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()