import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# Decorador de log
def log_transacao(tipo):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] Transação: {tipo}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @log_transacao("Saque")
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nSaldo insuficiente para realizar a transação.")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso.")
            return True
        else:
            print("\nValor inválido para saque.")
        return False

    @log_transacao("Depósito")
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso.")
        else:
            print("\nValor inválido para depósito.")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=10):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @log_transacao("Saque")
    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    @property
    def limite_saques(self):
        return self._limite_saques

    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    # Gerador de relatório
    def gerar_relatorio(self, tipo=None):
        for transacao in self._transacoes:
            if tipo is None or transacao["tipo"] == tipo:
                yield transacao


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @log_transacao("Saque")
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @log_transacao("Depósito")
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Iterador personalizado para contas
class ContaIterador:
    def __init__(self, contas):
        self._contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._contas):
            conta = self._contas[self._index]
            self._index += 1
            return {
                "numero": conta.numero,
                "agencia": conta.agencia,
                "titular": conta.cliente.nome,
                "saldo": conta.saldo,
            }
        raise StopIteration


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [r]\tRelatório de transações
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nO cliente não possui conta.")
        return
    return cliente.contas[0]


def realizar_transacao(clientes, transacao_cls, valor_msg):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input(valor_msg))
    transacao = transacao_cls(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    realizar_transacao(clientes, Deposito, "Informe o valor do depósito: ")


def sacar(clientes):
    realizar_transacao(clientes, Saque, "Informe o valor do saque: ")


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\nEXTRATO".center(30, "="))
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} | {transacao['data']}\n"

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("=" * 30)


def exibir_relatorio(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    tipo = input(
        "Filtrar por tipo de transação (Saque/Deposito) ou deixe vazio para todas: "
    )
    tipo = tipo.capitalize() if tipo else None

    print("\nRELATÓRIO DE TRANSAÇÕES".center(40, "="))
    for transacao in conta.historico.gerar_relatorio(tipo):
        print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f} | {transacao['data']}")
    print("=" * 40)


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\nJá existe um cliente cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )
    clientes.append(cliente)
    print("\nCliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("\nConta criada com sucesso!")


def listar_contas(contas):
    print("\nLISTA DE CONTAS".center(50, "="))
    for info in ContaIterador(contas):
        print(
            f"Agência: {info['agencia']} | Conta: {info['numero']} | Titular: {info['titular']} | Saldo: R$ {info['saldo']:.2f}"
        )
    print("=" * 50)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "r":
            exibir_relatorio(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break


if __name__ == "__main__":
    main()
