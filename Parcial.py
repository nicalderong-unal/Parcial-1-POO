#Autor: Nicolás Alexander Calderón García

class Libro:
    def __init__(self, titulo, autor, isbn, categoria):
        self.__titulo = titulo 
        self.__autor = autor
        self.__isbn = isbn
        self.__categoria = categoria

    def get_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Categoría: {self.__categoria}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre 
        self.__id_usuario = id_usuario

    def get_info(self):
        return f"Nombre: {self.__nombre}, ID: {self.__id_usuario}"

class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catalogo_libros = []
        self.__lista_usuarios = []
        self.__categorias = ["Distopía", "Literatura Clásica", "Ciencia Ficción", "Historia"]

    def registrar_libro(self):
        print("\n|---              Registro de Nuevo Libro             ---|")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        print("Seleccione una categoría:")
        for i, cat in enumerate(self.__categorias):
            print(f"{i + 1}. {cat}")
        
        try:
            opcion_cat = int(input("Opción: "))
            if 1 <= opcion_cat <= len(self.__categorias):
                categoria_seleccionada = self.__categorias[opcion_cat - 1]
                nuevo_libro = Libro(titulo, autor, isbn, categoria_seleccionada)
                self.__catalogo_libros.append(nuevo_libro)
                print("Se ha registrado correctamente el libro.")
            else:
                print("Error: Opción de categoría no válida.")
        except ValueError: print("Error: Ingrese un número válido.")

    def registrar_usuario(self):
        print("\n|---            Registro de Nuevo Usuario             ---|")
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = input("Ingrese el ID del usuario (ej. Cédula): ")
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.__lista_usuarios.append(nuevo_usuario)
        print("Se registró correctamente el nuevo usuario.")

    def mostrar_libros(self):
        print("\n|---                Catálogo de Libros                ---|")
        if not self.__catalogo_libros:
            print("No hay libros registrados.")
        else:
            for libro in self.__catalogo_libros:
                print(libro.get_info())

    def mostrar_usuarios(self):
        print("\n|---                Lista de Usuarios                 ---|")
        if not self.__lista_usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self.__lista_usuarios:
                print(usuario.get_info())

def main():
    mi_biblioteca = Biblioteca("Biblioteca de Ingeniería - Virgilio Barco")

    while True:
        print("\n==========================================================")
        print(f"| Bienvenido a {mi_biblioteca._Biblioteca__nombre} |")
        print("==========================================================")
        print("1. Registrar nuevo libro")
        print("2. Registrar nuevo usuario")
        print("3. Mostrar todos los libros")
        print("4. Mostrar todos los usuarios")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mi_biblioteca.registrar_libro()
        elif opcion == '2':
            mi_biblioteca.registrar_usuario()
        elif opcion == '3':
            mi_biblioteca.mostrar_libros()
        elif opcion == '4':
            mi_biblioteca.mostrar_usuarios()
        elif opcion == '5':
            print("\nSí se pudo, my people.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
