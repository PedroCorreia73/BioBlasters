from banco_de_dados.conexao_banco_de_dados import Conexao

class ProfessorDAO:
    def __init__(self, usuario_professor = None, senha_professor = None, id_grupo = None):
        self._usuario_professor = usuario_professor
        self._senha_professor = senha_professor
        self._id_grupo = id_grupo

    @Conexao.consultar
    def ver_todos_professores(self, consulta):
        obter_perguntas = "SELECT usuario_professor, idGrupo FROM Professor"
        consulta.execute(obter_perguntas)
        resultado = consulta.fetchall()
        return resultado

    @Conexao.consultar
    def adicionar_professor(self, consulta):
        adicionar_professor = "INSERT INTO Professor(usuario_professor, senha_professor, idGrupo) VALUES(%s,%s,%s)"
        valores = (self._usuario_professor, self._senha_professor, self._id_grupo)
        consulta.execute(adicionar_professor, valores)
        self._id_professor = consulta.lastrowid
        return None
    
    @Conexao.consultar
    def vincular_grupo(self, consulta, args):
        id_grupo = args[0]
        id_professor = args[1]
        vincular_grupo = "UPDATE Professor SET idGrupo = %s WHERE idProfessor = %s"
        valores = (id_grupo, id_professor)
        consulta.execute(vincular_grupo, valores)
        return None
    
    @Conexao.consultar
    def consulta_professor(self, consulta):
        consultar_professor = "SELECT * FROM Professor WHERE usuario_professor = %s"
        valores = (self._usuario_professor,)
        consulta.execute(consultar_professor, valores)
        resultado = consulta.fetchall()
        return resultado
    
    @Conexao.consultar
    def obter_id_professor(self, consulta):
        obter_id_professor = "SELECT idProfessor FROM Professor WHERE usuario_professor = %s"
        valores = (self._usuario_professor,)
        consulta.execute(obter_id_professor, valores)
        resultado = consulta.fetchone()
        return resultado
    
    @Conexao.consultar
    def remover_professor(self, consulta, args):
        id_professor = args[0]
        remover_professor = "DELETE FROM Professor WHERE idProfessor = %s"
        valores = (id_professor,)
        consulta.execute(remover_professor, valores)
        return None
    
    @Conexao.consultar
    def atualizar_pontuacao(self, consulta, args):
        id_professor = args[0]
        pontuacao_da_jogada = args[1]
        atualizar_pontuacao = "UPDATE Professor SET maior_pontuacao_professor = %s WHERE idProfessor = %s"
        valores = (pontuacao_da_jogada, id_professor)
        consulta.execute(atualizar_pontuacao, valores)
        resultado = consulta.fetchone()
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