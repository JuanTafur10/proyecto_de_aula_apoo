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
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ui.crear_cuenta()
        elif opcion == "2":
            usuario = ui.iniciar_sesion()
            if usuario:
                # Si se inicia sesión correctamente, puedes implementar otras funcionalidades aquí
                print(f"Sesión iniciada para {usuario.nombre_usuario}.")
                # Puedes continuar con otras acciones de usuario, como cambiar contraseña
        elif opcion == "3":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            if nombre_usuario in sistema.usuarios:
                usuario = sistema.usuarios[nombre_usuario]
                ui.cambiar_contraseña(usuario)
            else:
                print("Error: El usuario no existe.")
        elif opcion == "4":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            ui.mostrar_mensaje("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()