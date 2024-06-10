from banco_de_dados.conexao_banco_de_dados import Conexao

class AdministradorDAO:
    def __init__(self,usuario_administrador = None, senha_administrador = None):
        self._usuario_administrador = usuario_administrador
        self._senha_administrador = senha_administrador 

    @Conexao.consultar
    def consulta_administrador(self, consulta):
        usuario_administrador = self._usuario_administrador
        procurar_administrador = "SELECT * FROM Administrador WHERE usuario_administrador = %s"
        valores = (usuario_administrador,)
        consulta.execute(procurar_administrador, valores)
        resultado = consulta.fetchall()
        return resultado