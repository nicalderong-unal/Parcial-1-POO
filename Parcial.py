#Autor: Nicolás Alexander Calderón García

class New_book:
    def __init__ (self, titulo, categoria, autor, code):
        self.__titulo = titulo  
        self.__autor = autor
        self.__code = code
        self.__categoria = categoria
    
    def get_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, code: {self.__code}, Categoría: {self.__categoria}"

class New_user:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre # Atributo encapsulado
        self.__id_usuario = id_usuario

    def get_info(self):
        return f"Nombre: {self.__nombre}, ID: {self.__id_usuario}"

    def get_info(self):
        return f"Nombre: {self.__nombre}, ID: {self.__id_usuario}"


    def get_info(self):
        return f"Nombre: {self._nombre}, Usuario"

class Biblioteca:
    def __init__ (self,nuevo_usuario,nuevo_libro):
        self.nuevo_usuario=nuevo_usuario
        self.nuevo_libro=nuevo_libro



    


