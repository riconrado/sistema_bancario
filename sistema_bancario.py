menu = '''\n
========================= Menu =========================
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastro de Usuário
[c] Cadastro de Conta Corrente
[lu] Listar Usuários
[lc] Listar Contas
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
valor=0
numero_saque = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas = []
conta_sequencial = 1
AGENCIA = '0001'

def sacar(*, valor, saldo, extrato, numero_saque, limite, limite_saques):
    
        if numero_saque >= LIMITE_SAQUES:
            print('Limite de saques diários atingido')

        elif valor > saldo:
            print('Saldo insuficiente')

        elif valor > limite:
            print('Valor acima do seu limite de saque')

        elif valor < 0:
            print('Valor inválido')

        else:

            saldo -= valor
            numero_saque += 1
            extrato += f'{numero_saque} - Saque:\t R$ {valor:.2f}\n'
            
            print(f'R$ {valor:.2f} sacado com sucesso')
        
        return saldo, extrato, numero_saque

def depositar(saldo, valor, extrato, /):
        
    if valor > 0:
        saldo += valor

    else:
        print('Valor inválido')

    extrato += f'Depósito:\t R$ {valor:.2f}\n'
    
    print(f'R$ {valor:.2f} depositado com sucesso')

    return saldo, extrato

def func_extrato(saldo, /, *, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(nome, data_aniversario, cpf, cidade):
    global lista_usuarios

    if not usuario_existe(cpf):
        
        ususario_dict = {
            'cpf': cpf,
            'nome': nome,
            'data_aniversario': data_aniversario,
            'cidade': cidade
        }

        lista_usuarios.append(ususario_dict)

        print(f'Usuário {nome} cadastrado com sucesso')

    else:
        print('Usuário já cadastrado')


def criar_conta(cpf):
     global lista_contas
     global conta_sequencial
     global AGENCIA

     if usuario_existe(cpf):

        lista_contas.append({
            'agencia': AGENCIA,
            'conta': conta_sequencial,
            'cpf': cpf,
            'saldo': saldo,
            'limite': 500,
            'extrato': '',
            'numero_saque': 0
        })

        conta_sequencial += 1
        print('Conta criada com sucesso')

     else:
        print('Usuário ainda não cadastrado\nFavor relizar primeiro o cadastro')

def listar_usuarios():
    global lista_usuarios

    for usuario in lista_usuarios:
        print(usuario)

def func_listar_contas():
    global lista_contas 
    for conta in lista_contas:
        print(conta)

def usuario_existe(cpf):
    global lista_usuarios

    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            return True
    
    return False

def conta_existe(cpf, nro_conta):
    global lista_contas

    if usuario_existe(cpf):
        for conta in lista_contas:
            if conta['cpf'] == cpf and conta['conta'] == nro_conta:
                return True
        else:
            print('Conta não existe')
            return False
        
    else:
        print('Usuário não existe')
        return False


while True:
    opcao = input(menu)

    if opcao == 'd':
        conta = int(input('Digite o número da conta: '))
        cpf = int(input('Digite o CPF: '))

        if conta_existe(cpf, conta):

            try:
                valor = float(input('Digite o valor a ser depositado: '))
            except ValueError:
                print('Valor inválido')
            
            saldo, extrato = depositar(saldo,valor,extrato)

    elif opcao == 's':
        try:
            valor = float(input('Digite o valor a ser sacado: '))
        except ValueError:
            print('Valor inválido')

        saldo, extrato, numero_saque = sacar(valor=valor, saldo=saldo, extrato=extrato,
                                             numero_saque=numero_saque, limite=limite,
                                             limite_saques=LIMITE_SAQUES)
    
    elif opcao == 'e':

        func_extrato(saldo, extrato=extrato)

    elif opcao == 'u':
        nome = input('Digite o nome do usuário: ')
        data_aniversario = input('Digite a data de aniversário: ')
        cpf = int(input('Digite o CPF: '))
        cidade = input('Digite a cidade: ')

        criar_usuario(nome, data_aniversario, cpf, cidade)

    elif opcao == 'c':

        cpf = int(input('Digite o CPF do usuário: '))
        criar_conta(cpf)

    elif opcao == 'lu':
        listar_usuarios()

    elif opcao == 'lc':
        func_listar_contas()

    elif opcao == 'q':

        print('Obrigado por utilizar nossos serviços')
        break

    else: 
        print('Opção inválida, por favor selecione uma opção válida')
