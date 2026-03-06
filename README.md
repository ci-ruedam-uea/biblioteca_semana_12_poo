# biblioteca_semana_12_poo
Repositorio único para la biblioteca

### Modelos
Contienen las clases que representan las entidades del sistema.

- **Libro**: representa un libro dentro de la biblioteca.
- **Usuario**: representa un usuario registrado.

### Servicios
Contiene la lógica del negocio del sistema.

- **BibliotecaServicio**: gestiona libros, usuarios, préstamos y búsquedas.

### Punto de entrada
- **main.py**: ejecuta el sistema y proporciona un menú interactivo para probar las funcionalidades.

---

## Funcionalidades del Sistema

El sistema permite realizar las siguientes operaciones:

- Añadir libros al catálogo
- Eliminar libros
- Registrar usuarios
- Eliminar usuarios
- Prestar libros
- Devolver libros
- Buscar libros por:
  - Título
  - Autor
  - Categoría
- Listar los libros prestados a un usuario

---

## Uso de Colecciones en Python

El sistema utiliza diferentes estructuras de datos para gestionar la información:

| Estructura | Uso en el sistema |
|-------------|------------------|
| Tupla | Almacenar el título y autor del libro |
| Lista | Guardar los libros prestados a un usuario |
| Diccionario | Gestionar el catálogo de libros usando el ISBN |
| Set | Mantener IDs únicos de usuarios |

---

## Requisitos

- Python 3.x
- Cualquier IDE o editor de código (VS Code, PyCharm, etc.)

---

## Ejecución del Programa

1. Clonar el repositorio o descargar el proyecto.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el archivo principal:

```bash
python main.py
