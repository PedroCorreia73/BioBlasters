from Banco_de_dados import acessar_banco

class Grupo:
    def __init__(self, nome_grupo, senha_grupo):
        self._nome_grupo = nome_grupo
        self._senha_grupo = senha_grupo
    

    @classmethod
    @acessar_banco
    def consultar_grupos(cls):
        obter_perguntas = "SELECT * FROM grupo"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @acessar_banco
    def adicionar_grupo(cls, args):
        professor = args[0]
        grupo = args[1]
        
        adicionar_grupo = "INSERT INTO grupo(nome_grupo, senha_grupo) VALUES(%s, %s)"
        valores = (grupo._nome_grupo, grupo._senha_grupo)
        cls.consulta.execute(adicionar_grupo, valores)
        grupo._id_grupo = cls.consulta.lastrowid
        adicionar_id_grupo_no_prof = "UPDATE professor SET idGrupo = %s WHERE idProfessor = %s"
        cls.consulta.execute(adicionar_id_grupo_no_prof, (grupo.id, professor.id))
    

    @property
    def id(self):
        return self._id_grupo
    @property
    def nome(self):
        return self._nome_grupo
    @property
    def senha(self):
        return self._senha_grupo