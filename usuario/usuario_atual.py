from abc import abstractmethod
from abc import ABC

class Usuario(ABC):
    def __init__(self):
        self._id_usuario = None
        self._nome_usuario = None
        self._senha_usuario = None
        

    @abstractmethod
    def entrar_menu():
        pass
    @property
    def id(self):
        return self._id_usuario
    @id.setter
    def id(self, novo_id):
        self._id_usuario = novo_id
    @property
    def nome(self):
        return self._nome_usuario
    @nome.setter
    def nome(self, nome_usuario):
        self._nome_usuario = nome_usuario
    @property
    def senha(self):
        return self._senha_usuario
    @senha.setter
    def senha(self, senha_usuario):
        self._senha_usuario = senha_usuario 


class Aluno(Usuario):
    def __init__(self):
        super().__init__()
        self._id_grupo = None
    
    def entrar_menu(self, menu):
        return menu.aluno(self)
    @property
    def id_grupo(self):
        return self._id_grupo
    @id_grupo.setter
    def id_grupo(self, novo_id):
        self._id_grupo = novo_id
    
    
    
class Professor(Usuario):
    def __init__(self):
        super().__init__()
        self._id_grupo = None
    def entrar_menu(self, menu):
        return menu.professor(self)
    @property
    def id_grupo(self):
        return self._id_grupo
    @id_grupo.setter
    def id_grupo(self, novo_id):
        self._id_grupo = novo_id
    

class Administrador(Usuario):
    def __init__(self):
        super().__init__()
    def entrar_menu(self, menu):
        return menu.administrador(self)