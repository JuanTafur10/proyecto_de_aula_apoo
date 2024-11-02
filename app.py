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
        print("6. Salir")
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
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()