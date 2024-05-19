from conexao_banco_de_dados import Conexao

class GrupoDAO:
    def __init__(self, nome_grupo, senha_grupo):
        self._nome_grupo = nome_grupo
        self._senha_grupo = senha_grupo


    @classmethod
    @Conexao.consultar
    def ver_grupos(cls):
        obter_perguntas = "SELECT * FROM grupo"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @Conexao.consultar
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