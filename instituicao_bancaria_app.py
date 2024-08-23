
valor_conta = []

saldo = 0.0

nomes = {    
    'Nome':'',
    'CPF':'',
    'RG':'',
    'Data de Nascimento':'',
    'Sexo':'',
}

while True:
    print(f'{'='*10} Bem-vindo(a) a nossa instituição Bancária {'='*10}')
    print('1 - Criar conta.')
    print('2 - Consultar os dados pessoais da conta.')
    print('3 - Alterar os dados pessoais da conta.')
    print('4 - Excluir a conta.')
    print('5 - Consultar o saldo da conta.')
    print('6 - Depositar valor na conta.')
    print('7 - Sacar valor na conta.')
    print('8 - Sair do programa.')



    opcao = input('Informe opção desejada: ')

    match opcao:
        case '1':
            nomes['Nome'] = input('Informe seu Nome: ')
            nomes['CPF'] = input('Informe seu CPF: ')
            nomes['RG'] = input('Informe seu RG: ')
            nomes['Data de Nascimento'] = input('Informe sua Data de Nascimento: ')
            nomes['Sexo'] = input('Informe seu Sexo: ')

            #exibir dicionario 
            for chave in nomes:
                print(f'{chave}: {nomes.get(chave)}')
            continue

            # novo_nome = input('Informe o novo nome: ')
            # nomes.append(novo_nome)
            # print(f'Nome {novo_nome} cadastrado com sucesso.')
            
        case '2':
            for chave in nomes:
                print(f'{chave}: {nomes.get(chave)}')
                continue

        case '3':
            nomes['Nome'] = input('Informe novo Nome: ')
            nomes['CPF'] = input('Informe novo CPF: ')
            nomes['RG'] = input('Informe novo RG: ')
            nomes['Data de Nascimento'] = input('Informe nova Data de Nascimento: ')
            nomes['Sexo'] = input('Informe Sexo: ')
            continue

        case '4':
            del nomes['Nome']
            del nomes['CPF']
            del nomes['RG']
            del nomes['Data de Nascimento']
            del nomes['Sexo']
            continue

        case '5':
            print(f'Saldo: {saldo:,.2f}')
            continue

        case '6':
            valor = float(input('Digite o valor para depósito: '))
            saldo = saldo + valor
            print(f'Depósito de R${valor:,.2f} realizado com sucesso!')
            continue

        case '7':
            valor = float(input('Digite o valor para saque: '))
            if valor <= saldo:
                saldo = saldo - valor
                print(f'Saque de R${valor:,.2f} realizado com sucesso!')
            else:
                print('Saldo insuficiente!')
            continue

        case '8':
            print('Saindo do programa...')
            break

        case _:
            print('Opção inválida!')
            continue
            
