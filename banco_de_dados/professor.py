from banco_de_dados.conexao_banco_de_dados import Conexao

class ProfessorDAO:
    def __init__(self, usuario_professor, senha_professor, id_grupo):
        self._usuario_professor = usuario_professor
        self._senha_professor = senha_professor
        self._id_grupo = id_grupo

    @classmethod
    @Conexao.consultar
    def ver_professores(cls):
        obter_perguntas = "SELECT * FROM Professor"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @Conexao.consultar
    def adicionar_professor(cls, args):
        professor = args[0]
        adicionar_professor = "INSERT INTO Professor(usuario_professor, senha_professor, idGrupo) VALUES(%s,%s,%s)"
        valores = (professor._usuario_professor, professor._senha_professor, professor._id_grupo)
        cls.consulta.execute(adicionar_professor, valores)
        professor._id_professor = cls.consulta.lastrowid
        return None
    
    @classmethod
    @Conexao.consultar
    def vincular_grupo(cls,args):
        professor = args[0]
        id_grupo = professor.id_grupo
        id_professor = professor.id
        vincular_grupo = "UPDATE Professor SET idGrupo = %s WHERE idProfessor = %s"
        valores = (id_grupo, id_professor)
        cls.consulta.execute(vincular_grupo, valores)
        return None
    
    @classmethod
    @Conexao.consultar
    def consulta_professor(cls,args):
        professor = args[0]
        consultar_professor = "SELECT * FROM Professor WHERE usuario_professor = %s"
        valores = (professor._usuario_professor,)
        cls.consulta.execute(consultar_professor, valores)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @property
    def id(self):
        return self._id_professor
    @property
    def usuario(self):
        return self._usuario_professor
    @property
    def senha(self):
        return self._senha_professor
    @property
    def pontuacao(self):
        return self._pontuacao
    @pontuacao.setter
    def pontuacao(self, nova_pontuacao):
        self._pontuacao = nova_pontuacao