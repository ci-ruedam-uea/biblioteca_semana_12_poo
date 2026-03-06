from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n===== BIBLIOTECA DIGITAL =====")

        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar por titulo")
        print("8. Buscar por autor")
        print("9. Buscar por categoria")
        print("10. Listar libros de usuario")
        print("11. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID usuario: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":

            titulo = input("Titulo: ")
            resultados = biblioteca.buscar_por_titulo(titulo)

            for libro in resultados:
                print(libro)

        elif opcion == "8":

            autor = input("Autor: ")
            resultados = biblioteca.buscar_por_autor(autor)

            for libro in resultados:
                print(libro)

        elif opcion == "9":

            categoria = input("Categoria: ")
            resultados = biblioteca.buscar_por_categoria(categoria)

            for libro in resultados:
                print(libro)

        elif opcion == "10":

            id_usuario = input("ID usuario: ")
            libros = biblioteca.listar_libros_usuario(id_usuario)

            for libro in libros:
                print(libro)

        elif opcion == "11":

            print("Saliendo del sistema...")
            break

        else:

            print("Opcion invalida")


if __name__ == "__main__":
    menu()