from crud import agregar_producto, eliminar_producto, actualizar_producto, mostrar_inventario
import os

if __name__ == "__main__":
# Mensaje de bienvenida
    print("🛒 Sistema de Control de Inventario")

    def menu():
        """
        Muestra el menú de opciones y gestiona la interacción del usuario.
        """
        while True:
            print("\nOpciones:")
            print("1 - Agregar producto")
            print("2 - Actualizar producto")
            print("3 - Eliminar producto")
            print("4 - Mostrar inventario")
            print("0 - Salir")

            opcion = input("Elija una opción: ")
            
            os.system("cls" if os.name == "nt" else "clear")

            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                actualizar_producto()
            elif opcion == "3":
                producto_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().title()
                eliminar_producto(producto_eliminar)
            elif opcion == "4":
                mostrar_inventario()
            elif opcion == "0":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n❌ ¡Opción inválida! Elija una opción del 1 al 4.")

    # Llamando al menú para iniciar el sistema
    menu()
