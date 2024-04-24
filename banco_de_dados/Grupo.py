from urllib3 import Retry
from conexao_banco_de_dados import consultar

class Grupo:
    def __init__(self, nome_grupo, senha_grupo):
        self._nome_grupo = nome_grupo
        self._senha_grupo = senha_grupo
    

    @classmethod
    @consultar
    def ver_grupos(cls):
        obter_perguntas = "SELECT * FROM grupo"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @consultar
    def adicionar_grupo(cls, args):
        grupo = args[0]
        adicionar_grupo = "INSERT INTO grupo(nome_grupo, senha_grupo) VALUES(%s, %s)"
        valores = (grupo._nome_grupo, grupo._senha_grupo)
        cls.consulta.execute(adicionar_grupo, valores)
        grupo._id_grupo = cls.consulta.lastrowid
        return None
    

    @property
    def id(self):
        return self._id_grupo
    @property
    def nome(self):
        return self._nome_grupo
    @property
    def senha(self):
        return self._senha_grupo