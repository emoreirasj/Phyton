# Array de tarefas
tarefas = []
tarefasConcluidas = []
tarefaConcluida = 0

while True:
    print('Opções:')
    print('1. Adicionar tarefa')
    print('2. Mostrar tarefas')
    print('3. Tarefa concluída')
    print('4. Lista de Tarefas concluídas')
    print('5. Sair')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
    elif escolha == '2':
        print('Tarefas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')
    elif escolha == '3':
        tarefaConcluida = (int(input('Digite o número da tarefa concluída:'))) - 1
        tarefasConcluidas.append(tarefas[tarefaConcluida])
        tarefas.remove(tarefas[tarefaConcluida])
    elif escolha == '4':
        print('Tarefas Concluidas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefasConcluidas}')
    elif escolha == '5':
        break
    else:
        print('Opção inválida. Tente novamente.')
