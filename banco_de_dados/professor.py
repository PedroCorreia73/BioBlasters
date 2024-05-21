from banco_de_dados.conexao_banco_de_dados import Conexao

class ProfessorDAO:
    @Conexao.consultar
    def ver_professores(cls):
        obter_perguntas = "SELECT * FROM professor"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado

    @Conexao.consultar
    def adicionar_professor(cls, nome_professor, senha_professor):
        pass