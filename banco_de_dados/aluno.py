from banco_de_dados.conexao_banco_de_dados import Conexao

class AlunoDAO:
    def __init__(self, usuario_aluno = None, senha_aluno = None, id_grupo = None):
        self._usuario_aluno = usuario_aluno
        self._senha_aluno = senha_aluno
        self._id_grupo = id_grupo

    @Conexao.consultar
    def ver_todos_alunos(self, consulta):
        obter_alunos = "SELECT usuario_aluno, idGrupo FROM Aluno"
        consulta.execute(obter_alunos)
        resultado = consulta.fetchall()
        return resultado

    @Conexao.consultar
    def adicionar_aluno(self, consulta):
        adicionar_aluno = "INSERT INTO Aluno(usuario_aluno, senha_aluno, idGrupo) VALUES(%s, %s, %s)"
        valores = (self._usuario_aluno, self._senha_aluno, self._id_grupo)
        consulta.execute(adicionar_aluno, valores)
        self._id_aluno = consulta.lastrowid
        return None

    @Conexao.consultar
    def consulta_aluno(self, consulta):
        consulta_aluno = "SELECT * FROM Aluno WHERE usuario_aluno = %s"
        valores = (self._usuario_aluno,)
        consulta.execute(consulta_aluno, valores)
        resultado = consulta.fetchall()
        return resultado
    
    @Conexao.consultar
    def vincular_grupo(self, consulta, args):
        id_grupo = args[0]
        id_aluno = args[1]
        vincular_grupo = "UPDATE Aluno SET idGrupo = %s WHERE idAluno = %s"
        valores = (id_grupo, id_aluno)
        consulta.execute(vincular_grupo, valores)
        return None
    
    @Conexao.consultar
    def ver_alunos_do_grupo(self, consulta, args):
        id_grupo = args[0]
        ver_alunos_do_grupo = "SELECT usuario_aluno FROM Aluno WHERE idGrupo = %s"
        valores = (id_grupo,)
        consulta.execute(ver_alunos_do_grupo,valores)
        resultado = consulta.fetchall()
        return resultado
        
    @Conexao.consultar
    def remover_aluno_do_grupo(self, consulta, args):
        id_aluno = args[0]
        remover_aluno_do_grupo = "UPDATE Aluno SET idGrupo = NULL WHERE idAluno = %s"
        valores = (id_aluno,)
        consulta.execute(remover_aluno_do_grupo, valores)
        return None
    
    @Conexao.consultar
    def remover_aluno(self, consulta, args):
        id_aluno = args[0]
        remover_aluno = "DELETE FROM Aluno WHERE idAluno = %s"
        valores = (id_aluno,)
        consulta.execute(remover_aluno, valores)
        return None
    
    @Conexao.consultar 
    def obter_id_aluno(self, consulta):
        obter_id_aluno = "SELECT idAluno FROM Aluno WHERE usuario_aluno = %s"
        valores = (self._usuario_aluno,)
        consulta.execute(obter_id_aluno, valores)
        resultado = consulta.fetchone()
        return resultado
    
    @Conexao.consultar
    def atualizar_pontuacao(self, consulta, args):
        id_aluno = args[0]
        pontuacao_da_jogada = args[1]
        atualizar_pontuacao = "UPDATE Aluno SET maior_pontuacao_aluno = %s WHERE idAluno = %s"
        valores = (pontuacao_da_jogada, id_aluno)
        consulta.execute(atualizar_pontuacao, valores)
        resultado = consulta.fetchone()
        return resultado
    
    @Conexao.consultar
    def alterar_senha(self, consulta, args):
        id_aluno = args[0]
        nova_senha = args[1]
        alterar_senha = "UPDATE Aluno SET senha_aluno = %s WHERE idAluno = %s"
        valores = (nova_senha, id_aluno)
        consulta.execute(alterar_senha, valores)
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