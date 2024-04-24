from conexao_banco_de_dados import *
from Aluno import Aluno
from Grupo import Grupo


grupo = Grupo("nome","senha")
Grupo.adicionar_grupo(grupo)
aluno = Aluno("Guilherme", 123123, grupo.id)
Aluno.adicionar_aluno(aluno)
print(Grupo.ver_grupos())
print(Aluno.ver_alunos())