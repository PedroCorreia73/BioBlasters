from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.grupo import GrupoDAO


grupo = GrupoDAO("nome","senha")
GrupoDAO.adicionar_grupo(grupo)
aluno = AlunoDAO("Guilherme", 123123, grupo.id)
AlunoDAO.adicionar_aluno(aluno)
print(GrupoDAO.ver_grupos())
print(AlunoDAO.ver_alunos())