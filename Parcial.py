#Autor: Nicolás Alexander Calderón García

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://biblioteca--poo-default-rtdb.firebaseio.com/'
})


#Referencias a la base de datos
ref_libros = db.reference('libros')
ref_usuarios = db.reference('usuarios')


#Clases
class Libro:
    def __init__(self, titulo, autor, isbn, categoria):
        self.__titulo = titulo 
        self.__autor = autor
        self.__isbn = isbn
        self.__categoria = categoria

    def get_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Categoría: {self.__categoria}"
    
    def to_dict(self):
        "Convierte el libro a diccionario para Firebase"
        return {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'isbn': self.__isbn,
            'categoria': self.__categoria
        }
    
    @staticmethod
    def from_dict(data):
        "Crea un objeto Libro desde un diccionario de Firebase"
        return Libro(data['titulo'], data['autor'], data['isbn'], data['categoria'])


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre 
        self.__id_usuario = id_usuario

    def get_info(self):
        return f"Nombre: {self.__nombre}, ID: {self.__id_usuario}"
    
    def to_dict(self):
        "Convierte el usuario a diccionario para Firebase"
        return {
            'nombre': self.__nombre,
            'id_usuario': self.__id_usuario
        }
    
    @staticmethod
    def from_dict(data):
        "Crea un objeto Usuario desde un diccionario de Firebase"
        return Usuario(data['nombre'], data['id_usuario'])


class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__categorias = ["Distopía", "Literatura Clásica", "Ciencia Ficción", "Historia"]

    #métodos CRUD pa libros
    
    def agregar_libro(self):
        "CREATE - Agregar nuevo libro a Firebase"
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
                
                #guardado direbase usando ISBN como clave única
                ref_libros.child(isbn).set(nuevo_libro.to_dict())
                print("Se ha registrado correctamente el libro en Firebase.")
            else:
                print("Error: Opción de categoría no válida.")
        except ValueError: 
            print("Error: Ingrese un número válido.")

    def ver_libros(self):
        "READ - Ver todos los libros desde Firebase"
        print("\n|---                Catálogo de Libros                ---|")
        libros_data = ref_libros.get()
        
        if not libros_data:
            print("No hay libros registrados.")
        else:
            for isbn, data in libros_data.items():
                libro = Libro.from_dict(data)
                print(f"ISBN: {isbn} - {libro.get_info()}")

    def actualizar_libro(self):
        "UPDATE - Actualizar información de un libro"
        print("\n|---              Actualizar Libro                    ---|")
        isbn = input("Ingrese el ISBN del libro a actualizar: ")
        
        libro_data = ref_libros.child(isbn).get()
        
        if not libro_data:
            print("No se encontró un libro con ese ISBN.")
            return
        
        print(f"\nLibro actual: {Libro.from_dict(libro_data).get_info()}")
        print("\n¿Qué desea actualizar?")
        print("1. Título")
        print("2. Autor")
        print("3. Categoría")
        print("4. Todo")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            nuevo_titulo = input("Nuevo título: ")
            ref_libros.child(isbn).update({'titulo': nuevo_titulo})
        elif opcion == '2':
            nuevo_autor = input("Nuevo autor: ")
            ref_libros.child(isbn).update({'autor': nuevo_autor})
        elif opcion == '3':
            print("Seleccione nueva categoría:")
            for i, cat in enumerate(self.__categorias):
                print(f"{i + 1}. {cat}")
            try:
                opcion_cat = int(input("Opción: "))
                if 1 <= opcion_cat <= len(self.__categorias):
                    ref_libros.child(isbn).update({'categoria': self.__categorias[opcion_cat - 1]})
            except ValueError:
                print("Opción inválida.")
                return
        elif opcion == '4':
            titulo = input("Nuevo título: ")
            autor = input("Nuevo autor: ")
            print("Seleccione nueva categoría:")
            for i, cat in enumerate(self.__categorias):
                print(f"{i + 1}. {cat}")
            try:
                opcion_cat = int(input("Opción: "))
                if 1 <= opcion_cat <= len(self.__categorias):
                    ref_libros.child(isbn).update({
                        'titulo': titulo,
                        'autor': autor,
                        'categoria': self.__categorias[opcion_cat - 1]
                    })
            except ValueError:
                print("Opción inválida.")
                return
        else:
            print("Opción no válida.")
            return
        
        print("Libro actualizado correctamente.")

    def eliminar_libro(self):
        "DELETE - Eliminar un libro de Firebase"
        print("\n|---              Eliminar Libro                      ---|")
        isbn = input("Ingrese el ISBN del libro a eliminar: ")
        
        libro_data = ref_libros.child(isbn).get()
        
        if not libro_data:
            print("No se encontró un libro con ese ISBN.")
            return
        
        print(f"\nLibro a eliminar: {Libro.from_dict(libro_data).get_info()}")
        confirmacion = input("¿Está seguro? (sí/no): ").lower()
        
        if confirmacion == 's':
            ref_libros.child(isbn).delete()
            print("Libro eliminado correctamente.")
        else:
            print("Operación cancelada.")

    #métodos CRUD pa' usuarios
    
    def agregar_usuario(self):
        "CREATE - Agregar nuevo usuario a Firebase"
        print("\n|---            Registro de Nuevo Usuario             ---|")
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = input("Ingrese el ID del usuario (ej. Cédula): ")
        
        nuevo_usuario = Usuario(nombre, id_usuario)
        
        #guardado en direbase usando ID como clave única
        ref_usuarios.child(id_usuario).set(nuevo_usuario.to_dict())
        print("Se registró correctamente el nuevo usuario en Firebase.")

    def ver_usuarios(self):
        """READ - Ver todos los usuarios desde Firebase"""
        print("\n|---                Lista de Usuarios                 ---|")
        usuarios_data = ref_usuarios.get()
        
        if not usuarios_data:
            print("No hay usuarios registrados.")
        else:
            for id_u, data in usuarios_data.items():
                usuario = Usuario.from_dict(data)
                print(f"ID: {id_u} - {usuario.get_info()}")

    def actualizar_usuario(self):
        "UPDATE - Actualizar información de un usuario"
        print("\n|---              Actualizar Usuario                  ---|")
        id_usuario = input("Ingrese el ID del usuario a actualizar: ")
        
        usuario_data = ref_usuarios.child(id_usuario).get()
        
        if not usuario_data:
            print("No se encontró un usuario con ese ID.")
            return
        
        print(f"\nUsuario actual: {Usuario.from_dict(usuario_data).get_info()}")
        nuevo_nombre = input("Nuevo nombre: ")
        
        ref_usuarios.child(id_usuario).update({'nombre': nuevo_nombre})
        print("Usuario actualizado correctamente.")

    def eliminar_usuario(self):
        "DELETE - Eliminar un usuario de Firebase"
        print("\n|---              Eliminar Usuario                    ---|")
        id_usuario = input("Ingrese el ID del usuario a eliminar: ")
        
        usuario_data = ref_usuarios.child(id_usuario).get()
        
        if not usuario_data:
            print("No se encontró un usuario con ese ID.")
            return
        
        print(f"\nUsuario a eliminar: {Usuario.from_dict(usuario_data).get_info()}")
        confirmacion = input("¿Está seguro? (sí/no): ").lower()
        
        if confirmacion == 's':
            ref_usuarios.child(id_usuario).delete()
            print("Usuario eliminado correctamente.")
        else:
            print("Operación cancelada.")

    #método para el menú
    
    def mostrar_menu(self):
        "Método para mostrar el menú principal"
        while True:
            print("\n==========================================================")
            print(f"| Bienvenido a {self.__nombre} |")
            print("==========================================================")
            print("--- GESTIÓN DE LIBROS ---")
            print("1. Agregar nuevo libro")
            print("2. Ver todos los libros")
            print("3. Actualizar libro")
            print("4. Eliminar libro")
            print("\n--- GESTIÓN DE USUARIOS ---")
            print("5. Agregar nuevo usuario")
            print("6. Ver todos los usuarios")
            print("7. Actualizar usuario")
            print("8. Eliminar usuario")
            print("\n9. Salir")
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.agregar_libro()
            elif opcion == '2':
                self.ver_libros()
            elif opcion == '3':
                self.actualizar_libro()
            elif opcion == '4':
                self.eliminar_libro()
            elif opcion == '5':
                self.agregar_usuario()
            elif opcion == '6':
                self.ver_usuarios()
            elif opcion == '7':
                self.actualizar_usuario()
            elif opcion == '8':
                self.eliminar_usuario()
            elif opcion == '9':
                print("\nSí se pudo, my people.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")


#main (ya limpio)
def main():
    mi_biblioteca = Biblioteca("Biblioteca de Ingeniería - CYT")
    mi_biblioteca.mostrar_menu()


if __name__ == "__main__":
    main()
