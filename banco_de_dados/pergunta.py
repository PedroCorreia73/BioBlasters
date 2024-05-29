from banco_de_dados.conexao_banco_de_dados import Conexao

class PerguntaAlternativasDAO:
    @classmethod
    @Conexao.consultar
    def ver_previa_perguntas(cls, args):
        id_grupo = args[0]
        obter_perguntas = """SELECT idPerguntaAlternativas, texto_enunciado 
                            FROM "Pergunta-Alternativas" AS pa INNER JOIN Pergunta AS p
                                                        ON pa.idPergunta = p.idPergunta
                            WHERE idGrupo = %s"""
        valores = (id_grupo,)
        cls.consulta.execute(obter_perguntas, valores)
        resultado = cls.consulta.fetchall()
        return resultado
    
    @classmethod
    @Conexao.consultar
    def adicionar_pergunta(cls, args):
        id_pergunta = cls.obter_id_pergunta(cls.consulta)
        id_grupo = args[0]
        enunciado = args[1]
        alternativas = args[2]
        id_enunciado = PerguntaDAO.adicionar_enunciado(enunciado)
        id_tentativa = TentativaDAO.criar_tentativas()
        dados = []
        for i in range(len(alternativas)):
            if i == 0:
                id_alternativa = AlternativaDAO.adicionar_alternativa(alternativas[i])
                valores = (id_pergunta,id_grupo,id_enunciado, id_alternativa, id_tentativa, 1)
                dados.append(valores)
            else:
                id_alternativa = AlternativaDAO.adicionar_alternativa(alternativas[i])
                valores = (id_pergunta,id_grupo,id_enunciado, id_alternativa, id_tentativa, 0)
                dados.append(valores)
        adicionar_pergunta_alternativas = """INSERT INTO "Pergunta-Alternativas"(idPerguntaAlternativas, idGrupo, idPergunta, idAlternativa, idTentativa, alternativa_correta)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
        cls.consulta.executemany(adicionar_pergunta_alternativas,dados)
        return None
    
    @classmethod
    def obter_id_pergunta(cls, cursor):
        obter_id_pergunta = """SELECT MAX(idPerguntaAlternativas) FROM "Pergunta-Alternativas" """
        cursor.execute(obter_id_pergunta,)
        resultado = cursor.fetchall()
        if resultado[0][0] == None:
            return 1
        return resultado[0][0] + 1


        
class AlternativaDAO:
    @classmethod
    @Conexao.consultar
    def adicionar_alternativa(cls, args):
        alternativa = args[0]
        adicionar_alternativa = "INSERT INTO Alternativa (alternativa) VALUES (%s)"
        valores = (alternativa,)
        cls.consulta.execute(adicionar_alternativa, valores)
        id_alternativa = cls.consulta.lastrowid
        return id_alternativa
    
class PerguntaDAO:
    @classmethod
    @Conexao.consultar
    def adicionar_enunciado(cls, args):
        enunciado = args[0]
        adicionar_enunciado = "INSERT INTO Pergunta (texto_enunciado) VALUES (%s)"
        valores = (enunciado,)
        cls.consulta.execute(adicionar_enunciado, valores)
        id_enunciado = cls.consulta.lastrowid
        return id_enunciado
    
class TentativaDAO:
    @classmethod
    @Conexao.consultar
    def criar_tentativas(cls):
        criar_tentativas = "INSERT INTO Tentativa (numero_tentativas, numero_acertos) VALUES (%s, %s)"
        valores = (0,0)
        cls.consulta.execute(criar_tentativas, valores)
        id_tentativa = cls.consulta.lastrowid
        return id_tentativa