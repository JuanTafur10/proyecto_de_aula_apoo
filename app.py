from GestionDeTareas.model.GestionTareas import Sistemas
from GestionDeTareas.view.console import UIConsola


def main():
    sistema = Sistemas()
    ui = UIConsola(sistema)

    while True:
        print("\n--- Menu ---")
        print("1. Crear Cuenta de Usuario")
        print("2. Cambiar Contraseña")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ui.crear_cuenta()
        elif opcion == "2":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            if nombre_usuario in sistema.usuarios:
                usuario = sistema.usuarios[nombre_usuario]
                ui.cambiar_contraseña(usuario)
            break
        elif opcion == "3":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            ui.mostrar_mensaje("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()