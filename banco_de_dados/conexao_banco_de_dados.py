import mysql.connector
from _login_banco_de_dados import usuario, senha
from functools import wraps

class Conexao:
    banco_de_dados = mysql.connector.pooling.MySQLConnectionPool(
        host= "bio-blasters-bio-blasters.h.aivencloud.com",
        user= usuario,
        password= senha,
        database = "defaultdb",
        port= "22073",
        pool_name="mypool"
    )

    def consultar(func):
        """Todas as funções que utilizam uma conexão com o banco de dados devem ter essa função como decorator.
        @consultar é responsável por abrir e fechar uma pool de conexão com o banco de dados."""
        @wraps(func)
        def criar_consulta(cls, *args):        
            acessar_banco = Conexao.banco_de_dados.get_connection()
            cls.consulta = acessar_banco.cursor()
            if len(args) == 0:
                resultado = func(cls)   
            else:
                resultado = func(cls, args)
            cls.consulta.close()
            acessar_banco.commit()
            acessar_banco.close()
            return resultado
        return criar_consulta