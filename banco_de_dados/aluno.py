from banco_de_dados.conexao_banco_de_dados import Conexao

class AlunoDAO:
    def __init__(self, usuario_aluno, senha_aluno, id_grupo):
        self._usuario_aluno = usuario_aluno
        self._senha_aluno = senha_aluno
        self._id_grupo = id_grupo

    @classmethod
    @Conexao.consultar
    def ver_alunos(cls):
        obter_alunos = "SELECT * FROM Aluno"
        cls.consulta.execute(obter_alunos)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @Conexao.consultar
    def adicionar_aluno(cls, args):
        aluno = args[0]
        adicionar_aluno = "INSERT INTO Aluno(usuario_aluno, senha_aluno, idGrupo) VALUES(%s, %s, %s)"
        valores = (aluno._usuario_aluno, aluno._senha_aluno, aluno._id_grupo)
        cls.consulta.execute(adicionar_aluno, valores)
        aluno._id_aluno = cls.consulta.lastrowid
        return None

    @classmethod
    @Conexao.consultar
    def consulta_aluno(cls, args):
        aluno = args[0]
        consulta_aluno = "SELECT * FROM Aluno WHERE usuario_aluno = %s"
        valores = (aluno._usuario_aluno,)
        cls.consulta.execute(consulta_aluno, valores)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @Conexao.consultar
    def vincular_grupo(cls,args):
        aluno = args[0]
        id_grupo = aluno.id_grupo
        id_aluno = aluno.id
        vincular_grupo = "UPDATE Aluno SET idGrupo = %s WHERE idAluno = %s"
        valores = (id_grupo, id_aluno)
        cls.consulta.execute(vincular_grupo, valores)
        return None
        
    @property
    def id(self):
        return self._id_aluno
    @property
    def usuario(self):
        return self._usuario_aluno
    @property
    def senha(self):
        return self._senha_aluno
    @property
    def pontuacao(self):
        return self._pontuacao
    @pontuacao.setter
    def pontuacao(self, nova_pontuacao):
        self._pontuacao = nova_pontuacao