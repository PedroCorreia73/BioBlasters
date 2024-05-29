from banco_de_dados.conexao_banco_de_dados import Conexao

class AdministradorDAO:
    def __init__(self,usuario_administrador, senha_administrador):
        self._usuario_administrador = usuario_administrador
        self._senha_administrador = senha_administrador 

    @classmethod
    @Conexao.consultar
    def consulta_administrador(cls, args):
        administrador = args[0]
        usuario_administrador = administrador._usuario_administrador
        procurar_administrador = "SELECT * FROM Administrador WHERE usuario_administrador = %s"
        valores = (usuario_administrador,)
        cls.consulta.execute(procurar_administrador, valores)
        resultado = cls.consulta.fetchall()
        return resultado