import mysql.connector
from functools import wraps
from banco_de_dados._login_banco_de_dados import usuario, senha

class Conexao:
    banco_de_dados = {
        "host": "bio-blasters-bio-blasters.h.aivencloud.com",
        "user": usuario,
        "password": senha,
        "database": "defaultdb",
        "port": "22073",
    }

    def consultar(func):
        """Todas as funções que utilizam uma conexão com o banco de dados devem ter essa função como decorator.
        @consultar é responsável por abrir e fechar uma conexão com o banco de dados."""
        @wraps(func)
        def criar_consulta(cls, *args):        
            with mysql.connector.connect(**Conexao.banco_de_dados) as acessar_banco:
                cls.consulta = acessar_banco.cursor()
                if len(args) == 0:
                    resultado = func(cls)   
                else:
                    resultado = func(cls, args)
                cls.consulta.close()
                acessar_banco.commit()
                return resultado
        return criar_consulta