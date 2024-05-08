from Banco_de_dados import acessar_banco

class Pergunta:
    @acessar_banco
    def ver_perguntas(cls):
        obter_perguntas = "SELECT * FROM pergunta"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado