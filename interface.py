def linha():
    print("-"*30)

def cabecalho(msg):
    linha()
    print(msg.center(30))
    linha()

def leiaInt():
    while True:
        try:
            opcao = int(input("Opção: "))
        except (ValueError, TypeError):
            print("ERRO! Tipos de dados inválidos... ")
        except (KeyboardInterrupt):
            print("ERRO. Execução encerrada...")
        else:
            return opcao

def menuOpcao(lista):
    i = 1
    cabecalho("LISTA DE TAREFAS")
    for l in lista:
        print(f"{i} - {l}")
        i += 1
    linha()
    opcao = leiaInt()
    return opcao

