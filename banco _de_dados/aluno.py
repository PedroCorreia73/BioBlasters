from conexao_banco_de_dados import consultar

class Aluno:

    @consultar
    def ver_alunos(cls):
        obter_perguntas = "SELECT * FROM aluno"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado