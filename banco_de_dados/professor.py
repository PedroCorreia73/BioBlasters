from banco_de_dados.conexao_banco_de_dados import Conexao

class ProfessorDAO:
    def __init__(self, usuario_professor = None, senha_professor = None, id_grupo = None):
        self._usuario_professor = usuario_professor
        self._senha_professor = senha_professor
        self._id_grupo = id_grupo

    @Conexao.consultar
    def ver_professores(consulta):
        obter_perguntas = "SELECT * FROM Professor"
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