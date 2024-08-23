nomes = []
valor_conta = []

while True:
    print(f'{'='*10} Bem-vindo(a) a nossa instituição Bancária {'='*10}')
    print('1 - Criar conta.')
    print('2 - Consultar o saldo da conta.')
    print('3 - Alterar os dados pessoais da conta.')
    print('4 - Excluir a conta.')

    opcao = input('Informe opção desejada: ')

    match opcao:
        case '1':
            novo_nome = input('Informe o novo nome: ')
            nomes.append(novo_nome)
            print(f'Nome {novo_nome} cadastrado com sucesso.')
            continue
        case '2':
            for saldo_conta in range(len(valor_conta)):
                print(valor_conta)
                continue
        case '3':
            inserir_valor = input('Informe valor a ser depositado: ')
            valor_conta.append(inserir_valor)
            print('\nValor depositado com sucesso.')
            continue
        case '4':
            sacar_valor = input('Informe índice a ser retirado: ')
            del valor_conta[sacar_valor]
            print('\nItem retirado com sucesso.')
            continue
        case '5':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida!')
            continue
      
            # print('2 - Consultar os dados pessoais da conta.')
            # print('3 - Alterar os dados pessoais da conta.')
            # print('4 - Excluir a conta.')
            # print('5 - Sair do Prograna.')
