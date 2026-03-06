class Libro:
    """
    Clase que representa un libro dentro del sistema de biblioteca.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla obligatoria para titulo y autor
        self.titulo_autor = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.titulo_autor[0]

    def obtener_autor(self):
        return self.titulo_autor[1]

    def __str__(self):
        return f"{self.obtener_titulo()} - {self.obtener_autor()} | Categoria: {self.categoria} | ISBN: {self.isbn}"