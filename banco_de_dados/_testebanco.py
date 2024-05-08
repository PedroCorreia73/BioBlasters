from Atores import Grupo, Administrador, Aluno
from Grupo import Grupo



grupo = Grupo("grupo", "grupo")
Grupo.adicionar_grupo(grupo)
aluno = Aluno("nome", "senha", grupo.id)
aluno.realizar_cadastro()
print(aluno.id)
