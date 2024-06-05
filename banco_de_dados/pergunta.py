from banco_de_dados.conexao_banco_de_dados import Conexao

class PerguntaAlternativasDAO:
    @Conexao.consultar
    def ver_previa_perguntas(self, consulta, args):
        id_grupo = args[0]
        obter_perguntas = """SELECT idPerguntaAlternativas, ANY_VALUE(p.texto_enunciado) 
                            FROM Pergunta_Alternativas AS pa INNER JOIN Pergunta AS p
                                                        ON pa.idPergunta = p.idPergunta
                            WHERE idGrupo = %s
                            GROUP BY pa.idPerguntaAlternativas"""
        valores = (id_grupo,)
        consulta.execute(obter_perguntas, valores)
        resultado = consulta.fetchall()
        return resultado
    
    @Conexao.consultar
    def adicionar_pergunta(self, consulta, args):
        alternativadao = AlternativaDAO()
        perguntadao = PerguntaDAO()
        tentativadao = TentativaDAO()

        id_grupo = args[0]
        id_pergunta = self.obter_id_pergunta(consulta, id_grupo)
        enunciado = args[1]
        alternativas = args[2]
        id_enunciado = perguntadao.adicionar_enunciado(enunciado)
        id_tentativa = tentativadao.criar_tentativas()
        dados = []
        for i in range(len(alternativas)):
            if i == 0:
                id_alternativa = alternativadao.adicionar_alternativa(alternativas[i])
                valores = (id_pergunta,id_grupo,id_enunciado, id_alternativa, id_tentativa, 1)
                dados.append(valores)
            else:
                id_alternativa = alternativadao.adicionar_alternativa(alternativas[i])
                valores = (id_pergunta,id_grupo,id_enunciado, id_alternativa, id_tentativa, 0)
                dados.append(valores)
        adicionar_pergunta_alternativas = """INSERT INTO Pergunta_Alternativas (idPerguntaAlternativas, idGrupo, idPergunta, idAlternativa, idTentativa, alternativa_correta)
                                VALUES(%s,%s,%s,%s,%s,%s)"""
        consulta.executemany(adicionar_pergunta_alternativas,dados)
        return None
    
    def obter_id_pergunta(self, cursor, id_grupo):
        obter_id_pergunta = """SELECT MAX(idPerguntaAlternativas) FROM Pergunta_Alternativas WHERE idGrupo = %s"""
        cursor.execute(obter_id_pergunta, (id_grupo,))
        resultado = cursor.fetchall()
        if resultado[0][0] == None:
            return 1
        return resultado[0][0] + 1
    
    @Conexao.consultar
    def obter_ids_perguntas(self, consulta, args):
        id_grupo = args[0]
        obter_ids_perguntas = """SELECT idPerguntaAlternativas 
                                 FROM Pergunta_Alternativas
                                 WHERE idGrupo = %s
                                 GROUP BY idPerguntaAlternativas"""
        valores = (id_grupo,)
        consulta.execute(obter_ids_perguntas,valores)
        resultado = consulta.fetchall()
        return resultado
        
    @Conexao.consultar
    def obter_enunciado_e_tentativa(self, consulta, args):
        id_pergunta_alternativas = args[0]
        id_grupo = args[1]
        obter_enunciado_e_tentativa = """SELECT idPerguntaAlternativas, ANY_VALUE(texto_enunciado) AS texto_enunciado, 
                                                ANY_VALUE(numero_tentativas) AS numero_tentativas, ANY_VALUE(numero_acertos) AS numero_acertos
                            FROM Pergunta_Alternativas AS pa INNER JOIN Pergunta AS p
                                                        ON pa.idPergunta = p.idPergunta
                                                        INNER JOIN Tentativa AS t
                                                        ON pa.idTentativa = t.idTentativa
                            WHERE pa.idPerguntaAlternativas = %s AND idGrupo = %s
                            GROUP BY pa.idPerguntaAlternativas"""
        valores = (id_pergunta_alternativas, id_grupo)
        consulta.execute(obter_enunciado_e_tentativa, valores)
        resultado = dict(zip(consulta.column_names, consulta.fetchone()))
        return resultado
    
    @Conexao.consultar
    def editar_pergunta(self, consulta, args):
        alternativadao = AlternativaDAO()
        perguntadao = PerguntaDAO()

        id_pergunta_alternativas = args[0]
        id_grupo = args[1]
        enunciado = args[2]
        alternativas = args[3]
        obter_ids = "SELECT idPergunta, idAlternativa, idTentativa FROM Pergunta_Alternativas WHERE idPerguntaAlternativas = %s AND idGrupo = %s ORDER BY 1"
        valores = (id_pergunta_alternativas, id_grupo)
        consulta.execute(obter_ids, valores)
        resultado = consulta.fetchall()
        perguntadao.editar_enunciado(resultado[0][0], enunciado)
        for i in range(len(alternativas)):
            if alternativas[i] == "":
                if len(resultado) >= i + 1:
                    consulta.execute("DELETE FROM Pergunta_Alternativas WHERE idPerguntaAlternativas = %s AND idGrupo = %s AND idAlternativa = %s",
                                        (id_pergunta_alternativas, id_grupo, resultado[i][1]))
                else:
                    continue
            elif alternativas[i] != "" and len(resultado) < i + 1:
                id_alternativa = alternativadao.adicionar_alternativa(alternativas[i])
                consulta.execute("""INSERT INTO Pergunta_Alternativas (idPerguntaAlternativas, idGrupo, idPergunta, idAlternativa, idTentativa, alternativa_correta)
                                VALUES(%s,%s,%s,%s,%s,0)""", 
                                (id_pergunta_alternativas, id_grupo, resultado[0][0], id_alternativa, resultado[0][2]))
            else:
                alternativadao.editar_alternativa(resultado[i][1], alternativas[i])
        return None

    @Conexao.consultar
    def remover_pergunta(self, consulta, args):
        id_pergunta_alternativas = args[0]
        id_grupo = args[1]
        remover_pergunta = "DELETE FROM Pergunta_Alternativas WHERE idPerguntaAlternativas = %s AND idGrupo = %s"
        valores = (id_pergunta_alternativas, id_grupo)
        consulta.execute(remover_pergunta, valores)
        return None
        

        
class AlternativaDAO:
    @Conexao.consultar
    def adicionar_alternativa(self, consulta, args):
        alternativa = args[0]
        adicionar_alternativa = "INSERT INTO Alternativa (alternativa) VALUES (%s)"
        valores = (alternativa,)
        consulta.execute(adicionar_alternativa, valores)
        id_alternativa = consulta.lastrowid
        return id_alternativa
    
    @Conexao.consultar
    def obter_alternativas(self, consulta, args):
        id_pergunta_alternativas = args[0]
        id_grupo = args[1]
        obter_alternativas = """SELECT alternativa, alternativa_correta
                                FROM Alternativa AS a INNER JOIN Pergunta_Alternativas AS pa
                                                      ON a.idAlternativa = pa.idAlternativa
                                WHERE pa.idPerguntaAlternativas = %s AND idGrupo = %s"""
        valores = (id_pergunta_alternativas, id_grupo)
        consulta.execute(obter_alternativas,valores)
        resultado = consulta.fetchall()
        return resultado
    
    @Conexao.consultar
    def editar_alternativa(self, consulta,args):
        id_alternativa = args[0]
        alternativa = args[1]
        editar_enunciado = "UPDATE Alternativa SET alternativa = %s WHERE idAlternativa = %s"
        valores = (alternativa, id_alternativa)
        consulta.execute(editar_enunciado, valores)
        return None
    
    
class PerguntaDAO:
    @Conexao.consultar
    def adicionar_enunciado(self, consulta, args):
        enunciado = args[0]
        adicionar_enunciado = "INSERT INTO Pergunta (texto_enunciado) VALUES (%s)"
        valores = (enunciado,)
        consulta.execute(adicionar_enunciado, valores)
        id_enunciado = consulta.lastrowid
        return id_enunciado
    
    @Conexao.consultar
    def editar_enunciado(self, consulta,args):
        id_pergunta = args[0]
        enunciado = args[1]
        editar_enunciado = "UPDATE Pergunta SET texto_enunciado = %s WHERE idPergunta = %s"
        valores = (enunciado, id_pergunta)
        consulta.execute(editar_enunciado, valores)
        return None
        
    
class TentativaDAO:
    @Conexao.consultar
    def criar_tentativas(self, consulta):
        criar_tentativas = "INSERT INTO Tentativa (numero_tentativas, numero_acertos) VALUES (%s, %s)"
        valores = (0,0)
        consulta.execute(criar_tentativas, valores)
        id_tentativa = consulta.lastrowid
        return id_tentativa
    
    