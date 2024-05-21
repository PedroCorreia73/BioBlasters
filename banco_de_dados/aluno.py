from banco_de_dados.conexao_banco_de_dados import Conexao

class AlunoDAO:
    def __init__(self, nome_aluno, senha_aluno, id_grupo):
        self._nome_aluno = nome_aluno
        self._senha_aluno = senha_aluno
        self._id_grupo = id_grupo

    @classmethod
    @Conexao.consultar
    def ver_alunos(cls):
        obter_alunos = "SELECT * FROM aluno"
        cls.consulta.execute(obter_alunos)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @Conexao.consultar
    def adicionar_aluno(cls, args):
        aluno = args[0]
        adicionar_aluno = "INSERT INTO aluno(nome_aluno, senha_aluno, Grupos_idGrupo) VALUES(%s, %s, %s)"
        valores = (aluno._nome_aluno, aluno._senha_aluno, aluno._id_grupo)
        cls.consulta.execute(adicionar_aluno, valores)
        aluno._id_aluno = cls.consulta.lastrowid
        return None


    @property
    def id(self):
        return self._id_aluno
    @property
    def nome(self):
        return self._nome_aluno
    @property
    def senha(self):
        return self._senha_aluno
    @property
    def pontuacao(self):
        return self._pontuacao
    @pontuacao.setter
    def pontuacao(self, nova_pontuacao):
        self._pontuacao = nova_pontuacao