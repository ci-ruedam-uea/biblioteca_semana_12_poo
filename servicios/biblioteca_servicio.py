from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros disponibles
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set de IDs únicos
        self.ids_usuarios = set()

    # -------------------------
    # LIBROS
    # -------------------------

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    # -------------------------
    # USUARIOS
    # -------------------------

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado correctamente.")

        else:
            print("Usuario no encontrado.")

    # -------------------------
    # PRESTAMOS
    # -------------------------

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:

            if libro.isbn == isbn:

                usuario.devolver_libro(libro)
                self.libros[isbn] = libro

                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # -------------------------
    # BUSQUEDAS
    # -------------------------

    def buscar_por_titulo(self, titulo):

        resultados = []

        for libro in self.libros.values():

            if titulo.lower() in libro.obtener_titulo().lower():
                resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor):

        resultados = []

        for libro in self.libros.values():

            if autor.lower() in libro.obtener_autor().lower():
                resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria):

        resultados = []

        for libro in self.libros.values():

            if categoria.lower() in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    # -------------------------
    # LISTAR LIBROS USUARIO
    # -------------------------

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return []

        return self.usuarios[id_usuario].libros_prestados