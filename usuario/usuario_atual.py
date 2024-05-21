class Usuario:
    def __init__(self):
        self._nome_usuario = ""
        self._senha_usuario = ""
        self._id_usuario = -1
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
    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, novo_id):
        self._id_usuario = novo_id


class Aluno(Usuario):
    pass
    
class Professor(Usuario):
    pass

class Administrador(Usuario):
    pass