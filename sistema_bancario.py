menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        try:
            valor = float(input('Digite o valor a ser depositado: '))
            
        except ValueError:
            print('Valor inválido')
            continue
        
        if valor > 0:
            saldo += valor

        else:
            print('Valor inválido')
            continue

        extrato += f'Depósito: R$ {valor:.2f}\n'   
        
        print(f'R$ {valor:.2f} depositado com sucesso')

    elif opcao == 's':

        if numero_saque >= LIMITE_SAQUES:
            print('Limite de saques diários atingido')
            continue
        try:
            valor = float(input('Digite o valor a ser sacado: '))
        except ValueError:
            print('Valor inválido')
            continue

        if valor > saldo:
            print('Saldo insuficiente')

        elif valor > limite:
            print('Valor acima do seu limite de saque')

        elif valor < 0:
            print('Valor inválido')

        else:

            saldo -= valor
            extrato += f'{numero_saque} - Saque: R$ {valor:.2f}\n'
            numero_saque += 1
            
            print(f'R$ {valor:.2f} sacado com sucesso')
    
    elif opcao == 'e':

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 'q':

        print('Obrigado por utilizar o nossos serviços')
        break

    else: 
        print('Opção inválida, por favor selecione uma opção válida')
