from banco_de_dados.conexao_banco_de_dados import Conexao

class GrupoDAO:
    def __init__(self, nome_grupo, codigo_grupo):
        self._nome_grupo = nome_grupo
        self._codigo_grupo = codigo_grupo


    @classmethod
    @Conexao.consultar
    def ver_grupos(cls):
        obter_perguntas = "SELECT * FROM Grupo"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @Conexao.consultar
    def adicionar_grupo(cls, args):
        grupo = args[0]
        adicionar_grupo = "INSERT INTO Grupo(nome_grupo, codigo_grupo) VALUES(%s, %s)"
        valores = (grupo._nome_grupo, grupo._codigo_grupo)
        cls.consulta.execute(adicionar_grupo, valores)
        grupo._id_grupo = cls.consulta.lastrowid
        return None
    
    @classmethod
    @Conexao.consultar
    def procurar_grupo(cls, args):
        grupo = args[0]
        nome_grupo = grupo._nome_grupo
        codigo_grupo = grupo._codigo_grupo
        procurar = "SELECT * FROM Grupo WHERE codigo_grupo = %s OR nome_grupo = %s"
        valores = (codigo_grupo, nome_grupo)
        cls.consulta.execute(procurar, valores)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @Conexao.consultar
    def procurar_grupo_por_codigo(cls, args):
        codigo = args[0]
        procurar = "SELECT * FROM Grupo WHERE codigo_grupo = %s"
        valores = (codigo,)
        cls.consulta.execute(procurar, valores)
        resultado = cls.consulta.fetchall()
        return resultado
    

    @property
    def id(self):
        return self._id_grupo
    @property
    def nome(self):
        return self._nome_grupo
    @property
    def senha(self):
        return self._codigo_grupo