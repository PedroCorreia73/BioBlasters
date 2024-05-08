import mysql.connector
from _login_banco_de_dados import usuario, senha


conexao = mysql.connector.pooling.MySQLConnectionPool(
    host= "bio-blasters-bio-blasters.h.aivencloud.com",
    user= usuario,
    password= senha,
    database = "defaultdb",
    port= "22073",
    pool_name="pool"
)


def tratar_excecoes(func):
    """Caso ocorra alguma exceção durante a conexão com o banco de dados, ou durante a alteração de dados
    esse decorator tratará as Exceptions"""
    def verificar_excecoes(cls, *args):
        try:
            func(cls, args)
        except:    
            print("teste")  
    return verificar_excecoes

def acessar_banco(func):
    """Todas as funções que desejam alterar algo no banco de dados devem ter essa função como decorator.
    @acessar_banco é responsável por fornecer uma conexão com o banco de dados"""
    def criar_alteracao(cls, *args):        
        acessar_banco = conexao.get_connection()
        cls.consulta = acessar_banco.cursor()
        if len(args) == 0:
            resultado = func(cls)   
        else:
            resultado = func(cls, args)
        cls.consulta.close()
        acessar_banco.commit()
        acessar_banco.close()
        return resultado
    return criar_alteracao




