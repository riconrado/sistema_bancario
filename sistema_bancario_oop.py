from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:

    def __init__(self, nome, cpf, cidade, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._cidade = cidade
        self._data_nascimento = data_nascimento
        self.contas = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def criar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"{self._nome} ({self._cpf})"
    

class Conta:
    def __init__(self, nro_conta, cliente):
        self._saldo = 0
        self._nro_conta = nro_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, nro_conta): # 'cls' retorna uma instância do Obj Conta
        return cls(nro_conta, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def nro_conta(self):
        return self._nro_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor, limite=500, LIMITE_SAQUES=3):
        saldo = self._saldo

        numero_saque = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
    
        if numero_saque >= LIMITE_SAQUES:
            print('Limite de saques diários atingido')

        elif valor > saldo:
            print('Saldo insuficiente')

        elif valor > limite:
            print('Valor acima do seu limite de saque')

        elif valor < 0:
            print('Valor inválido')

        else:

            self._saldo -= valor
            numero_saque += 1
            
            print(f'R$ {valor:.2f} sacado com sucesso')
            
            return True
        
        return False

    def depositar(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print(f'R$ {valor:.2f} depositado com sucesso')
            return True

        else:
            print('Valor inválido')

        return False


    def __str__(self):
        return f"{self.agencia} {self.nro_conta} - {self.cliente.nome}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)