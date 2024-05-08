from Usuario import Usuario
from Grupo import Grupo
from Banco_de_dados import acessar_banco 


class Aluno(Usuario):
    def __init__(self, nome_aluno, senha_aluno, id_grupo):
        super().__init__(nome_aluno, senha_aluno, id_grupo)

    def realizar_cadastro(self):
        Administrador.adicionar_aluno(self)


class Professor(Aluno):
    def __init__(self, nome_professor, senha_professor):
        super().__init__(nome_professor, senha_professor, None)

    @acessar_banco
    def criar_grupo(self, nome_grupo, senha_grupo):
        grupo_desejado = Grupo(nome_grupo,senha_grupo)
        try:
            Grupo.adicionar_grupo(self, grupo_desejado)
        except:
            raise Exception
        else:
            self._id_grupo = grupo_desejado.id
        
    @classmethod
    @acessar_banco
    def consultar_alunos_do_grupo(cls):
        pass

        

class Administrador(Professor):
    def __init__(self, nome_administrador, senha_administrador):
        super().__init__(nome_administrador, senha_administrador, None)
    
    @classmethod
    @acessar_banco
    def consultar_alunos(cls):
        obter_alunos = "SELECT * FROM aluno"
        cls.consulta.execute(obter_alunos)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @acessar_banco
    def adicionar_aluno(cls, args):
        aluno = args[0]
        
        adicionar_aluno = "INSERT INTO aluno(nome_aluno, senha_aluno, Grupos_idGrupo) VALUES(%s, %s, %s)"
        valores = (aluno._nome, aluno._senha, aluno._id_grupo)
        cls.consulta.execute(adicionar_aluno, valores)
        aluno._id = cls.consulta.lastrowid
        
    
    @classmethod
    @acessar_banco
    def consultar_professores(cls):
        obter_perguntas = "SELECT * FROM professor"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado

    @classmethod
    @acessar_banco
    def adicionar_professor(cls, nome_professor, senha_professor):
        pass
