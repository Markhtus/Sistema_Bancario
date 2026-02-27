#Sistema bancário v1 (Um usário)
# Operação de depósito:
# O usuário deve informar o valor a ser depositado. O valor deve ser positivo.Todos depósitos devem ser armazenados em uma lista.
# Operação de saque:
# O usuário deve informar o valor a ser sacado. O valor deve ser positivo e menor ou igual ao saldo disponível. O usuário só pode realizar 3 saques por dia. Todos os saques devem ser armazenados em uma lista.
# Operação de extrato:
# O sistema deve exibir todas as operações de depósito e saque, bem como o saldo atual. Se não houver movimentações, exibir a mensagem "Não foram realizadas movimentações."
# O sistema deve exibir um menu de opções para o usuário escolher a operação desejada (sacar, depositar, extrato ou sair). O programa deve continuar rodando até que o usuário escolha a opção de sair. 
# Observações: 3 saques diários, limite de saque de R$500,00 por operação, depósito mínimo de R$1. Caso não tenha saldo suficiente para realizar um saque, exibir a mensagem "Saldo insuficiente." O sistema deve ser implementado utilizando funções para cada operação (sacar, depositar, extrato) e uma função principal para controlar o fluxo do programa.

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
