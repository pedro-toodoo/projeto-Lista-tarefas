from interface import *
from funcoes import *

criar_tabela()

while True:
    resp = menuOpcao(
        ["Listar tarefas", "Adicionar nova tarefa", "Editar tarefa", "Concluir tarefa", "Apagar tarefa", "Sair"])

    if resp == 1:
        listar_tarefas()

    elif resp == 2:
        adicionar_tarefa()

    elif resp == 3:
        atualizar()

    elif resp == 4:
        concluir_tarefa()

    elif resp == 5:
        deletar_tarefa()

    elif resp == 6:
        sair()


