saldo = 0
extrato = []
numero_saques = 0
LIMITES_SAQUES = 3


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito realizado com sucesso. Saldo atual: R${saldo:.2f}")
    else:
        print("Valor de depósito deve ser positivo.")


def sacar(valor):
    global saldo, numero_saques
    if valor > 0 and valor <= 500:
        if numero_saques < LIMITES_SAQUES:
            if saldo >= valor:
                saldo -= valor
                extrato.append(f"Saque: R${valor:.2f}")
                numero_saques += 1
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários excedido.")
    else:
        print("Valor de saque inválido. Deve ser positivo e menor ou igual a R$500,00.")


def visualizar_extrato():
    if extrato:
        print("\nExtrato:")
        for operacao in extrato:
            print(operacao)
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")


def main():
    while True:
        print("\nMenu:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Visualizar Extrato")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            sacar(valor)
        elif opcao == "3":
            visualizar_extrato()
        elif opcao == "4":
            print("Saindo do sistema. Obrigado por usar nosso serviço!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
