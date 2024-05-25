from banco_de_dados.conexao_banco_de_dados import Conexao

class PerguntaDAO:
    @Conexao.consultar
    def ver_perguntas(cls, args):
        id_grupo = args[0]
        obter_perguntas = "SELECT * FROM Pergunta WHERE idGrupo = %s"
        valores = (id_grupo,)
        cls.consulta.execute(obter_perguntas, valores)
        resultado = cls.consulta.fetchall()
        return resultado