from conexao_banco_de_dados import consultar

class Pergunta:
    @consultar
    def ver_perguntas(cls):
        obter_perguntas = "SELECT * FROM pergunta"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado