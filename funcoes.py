import sqlite3
from datetime import datetime, date

banco = sqlite3.connect('Lista_de_Tarefas.db')
cursor = banco.cursor()
todas_tarefas = cursor.fetchall()


def criar_tabela():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS tarefas(id integer primary key autoincrement,tarefa text,data date,status text)')
    banco.commit()


def adicionar_tarefa():
    tarefa = str(input('Tarefa a ser realizada: '))
    data = input("Data limite (DD/MM/AAAA): ")
    while True:
        try:

            datetime.strptime(data, "%d/%m/%Y")
            hoje = datetime.today().strftime('%d/%m/%Y')
            dia_dig, mes_dig, ano_dig = data.split('/')
            dia_hoje, mes_hoje, ano_hoje = hoje.split('/')

            if ano_dig < ano_hoje:
                print('Não é possivel adicionar data no passado, tente novamente:')
                data = input("Data limite (DD/MM/AAAA): ")

            else:
                if dia_dig < dia_hoje and mes_dig < mes_hoje:
                    print('Não é possivel adicionar data no passado, tente novamente:')
                    data = input("Data limite (DD/MM/AAAA): ")
                elif mes_dig < mes_hoje:
                    print('Não é possivel adicionar data no passado, tente novamente:')
                    data = input("Data limite (DD/MM/AAAA): ")
                elif mes_dig == mes_hoje and dia_dig < dia_hoje:
                    print('Não é possivel adicionar data no passado, tente novamente:')
                    data = input("Data limite (DD/MM/AAAA): ")
                else:
                    data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
                    status = 'Pendente'
                    cursor.execute(
                        f"INSERT INTO tarefas(tarefa, data, status) VALUES('{tarefa}','{data_convertida}', '{status}')")
                    banco.commit()
                    print('\033[32mTarefa Adicionada!\033[m')
                    break

        except ValueError:
            print("\033[31mERRO. Data no formato errado!\033[m")


def listar_tarefas():
    cursor.execute('SELECT id, tarefa, data, status from tarefas ORDER BY date(data) asc')
    todas_tarefas = cursor.fetchall()
    if len(todas_tarefas) == 0:
        print('Lista de tarefas vazia!')

    else:
        print('-' * 50)
        print(f'{"Id":^5} {"Tarefa":^20} {"Data":^10} {"Status":^15}')
        for i, v in enumerate(todas_tarefas):
            print(f'\n{v[0]:^5} {v[1]:^20} {v[2]:^10} {v[3]:^15}\n')

    return todas_tarefas


def atualizar():
    todas = listar_tarefas()
    achar = False
    try:
        id_tarefa = int(input("Qual tarefa deseja editar? "))
    except ValueError:
        print('Insira apenas números')
    else:
        for t in todas:
            if id_tarefa == t[0]:
                achar = True
                opcao = int(input(
                    "O que deseja alterar? \n[1 - Tarefa / 2 - Data / 3 - Alterar os dois / 4 - Alterar status]\n> "))

                if opcao == 1:
                    nova_tarefa = input("Tarefa alterada: ")
                    cursor.execute(f"UPDATE tarefas SET tarefa = '{nova_tarefa}' WHERE id = '{id_tarefa}'")

                elif opcao == 2:
                    nova_data = input("Data alterada: ")
                    data_convertida = datetime.strptime(nova_data, "%d/%m/%Y").date()
                    cursor.execute(f"UPDATE tarefas SET data = '{data_convertida}' WHERE id = '{id_tarefa}'")

                elif opcao == 3:
                    nova_tarefa = input("Tarefa alterada: ")
                    nova_data = input("Data alterada: ")
                    data_convertida = datetime.strptime(nova_data, "%d/%m/%Y").date()
                    cursor.execute(
                        f"UPDATE tarefas SET tarefa = '{nova_tarefa}', data = '{data_convertida}' WHERE id = '{id_tarefa}'")
                else:
                    print('Opção incorreta')
        if not achar:
            print('ID não encontrado')
    banco.commit()


def concluir_tarefa():
    todas = listar_tarefas()
    achar = False
    try:
        id_tarefa = int(input("Qual tarefa deseja concluir? "))
    except ValueError:
        print('Informe somente números!')
    else:
        for t in todas:
            if id_tarefa == t[0]:
                achar = True
                status_novo = 'Concluido'
                cursor.execute(f"UPDATE tarefas SET status = '{status_novo}' WHERE id = '{id_tarefa}'")
                print(f'\033[32mTarefa com ID {id_tarefa} alterada para concluida!\033[m')
        if not achar:
            print('ID não encontrado')


def deletar_tarefa():
    todas = listar_tarefas()
    achar = False
    try:
        id_tarefa = int(input("Qual tarefa deseja deletar? "))
    except ValueError:
        print('Informe somente números!')
    else:
        for t in todas:

            if id_tarefa == t[0]:
                achar = True
                op = input('Tem certeza que deseja deletar? [S/N]: ').strip().upper()

                if op == 'S':
                    cursor.execute(f"DELETE FROM tarefas WHERE id = '{id_tarefa}'")
                    print(f'\033[32mTarefa com ID {id_tarefa} deletada!\033[m')
                elif op == 'N':
                    break

                else:
                    print('Digito inválido')

        if not achar:
            print('ID não encontrado')
        banco.commit()


def sair():
    import sys
    print('Encerrando o programa...')
    sys.exit()


def deletar_tabela():
    cursor.execute('DROP TABLE tarefas')
    banco.commit()
