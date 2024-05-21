from banco_de_dados.conexao_banco_de_dados import Conexao

class PerguntaDAO:
    @Conexao.consultar
    def ver_perguntas(cls):
        obter_perguntas = "SELECT * FROM pergunta"
        cls.consulta.execute(obter_perguntas)
        resultado = cls.consulta.fetchall()
        return resultado