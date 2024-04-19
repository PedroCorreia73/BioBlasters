import mysql.connector
from _login_banco_de_dados import usuario, senha
from functools import wraps


banco_de_dados = mysql.connector.pooling.MySQLConnectionPool(
    host= "localhost",
    user= usuario,
    password= senha,
    database = "pi",
    pool_name="pool"
)

def consultar(cls, func):
    @wraps(func)
    def criar_consulta():
        acessar_banco = banco_de_dados.get_connection()
        cls.consulta = acessar_banco.cursor()
        cls.consulta.execute("USE pi")
        func()
        cls.consulta.close()
        acessar_banco.commit()
        acessar_banco.close()
    return criar_consulta
