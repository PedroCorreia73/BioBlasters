from banco_de_dados.conexao_banco_de_dados import Conexao

class GrupoDAO:
    def __init__(self, nome_grupo = None, codigo_grupo = None):
        self._nome_grupo = nome_grupo
        self._codigo_grupo = codigo_grupo


    @Conexao.consultar
    def ver_grupos(self, consulta):
        obter_perguntas = "SELECT * FROM Grupo"
        consulta.execute(obter_perguntas)
        resultado = consulta.fetchall()
        return resultado

    @Conexao.consultar
    def adicionar_grupo(self, consulta):
        adicionar_grupo = "INSERT INTO Grupo(nome_grupo, codigo_grupo) VALUES(%s, %s)"
        valores = (self._nome_grupo, self._codigo_grupo)
        consulta.execute(adicionar_grupo, valores)
        self._id_grupo = consulta.lastrowid
        return None
    
    @Conexao.consultar
    def procurar_grupo(self, consulta):
        nome_grupo = self._nome_grupo
        codigo_grupo = self._codigo_grupo
        procurar = "SELECT * FROM Grupo WHERE codigo_grupo = %s OR nome_grupo = %s"
        valores = (codigo_grupo, nome_grupo)
        consulta.execute(procurar, valores)
        resultado = consulta.fetchall()
        return resultado
    
    @Conexao.consultar
    def procurar_grupo_por_codigo(self, consulta, args):
        codigo = args[0]
        procurar = "SELECT * FROM Grupo WHERE codigo_grupo = %s"
        valores = (codigo,)
        consulta.execute(procurar, valores)
        resultado = consulta.fetchall()
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