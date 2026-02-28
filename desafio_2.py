usuarios = []
contas = []

AGENCIA_FIXA = "0001"
NUMERO_CONTA = 1

saldo = 0
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

def cadastrar_usuario(nome, cpf, data_nascimento, endereco):
    global usuarios
    cpf_numeros = ''.join(filter(str.isdigit, cpf)) [:11] # Extrai apenas os números do CPF e limita a 11 dígitos
    
    if any(usuario['cpf'] == cpf_numeros for usuario in usuarios):
        print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF mais de uma vez.")
        return
    
    usuario = {
        'nome': nome,
        'cpf': cpf_numeros,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def criar_conta(cpf):

    global contas, NUMERO_CONTA

    cpf_numeros = ''.join(filter(str.isdigit, cpf))[:11]

    usuario_existe = False

    for usuario in usuarios:
        if usuario['cpf'] == cpf_numeros:
            usuario_existe = True

    if not usuario_existe:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    conta = {
        'numero_conta': NUMERO_CONTA,
        'agencia': AGENCIA_FIXA,
        'titular': cpf_numeros
    }

    contas.append(conta)

    print(f"Conta criada com sucesso. Número da conta: {NUMERO_CONTA}")

    NUMERO_CONTA += 1

def depositar(valor, /):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso. Saldo atual: R${saldo:.2f}")
    else:
        print("Valor de depósito deve ser positivo.")

def sacar(*, valor):
    global saldo, numero_saques, extrato
    if valor > 0 and valor <= 500:
        if numero_saques < LIMITES_SAQUES:
            if saldo >= valor:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários excedido.")
    else:
        print("Valor de saque inválido. Deve ser positivo e menor ou igual a R$500,00.")

def visualizar_extrato(*args, **kwargs):
    if extrato:
        print("\nExtrato:")
        print(extrato)
        
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")
 
def main():
        while True:
            print("\n=== Menu ===")
            print("1. Cadastrar usuário")
            print("2. Criar conta")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Visualizar extrato")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                cpf = input("CPF (somente números): ")[:11] 
                data_nascimento = input("Data de nascimento: ")

                rua = input("Rua: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado (sigla): ").upper()[:2]
                endereco = f"{rua}, {numero}, {bairro}, {cidade}, {estado}"

                cadastrar_usuario(nome, cpf, data_nascimento, endereco)
            elif opcao == "2":
                cpf = input("CPF do titular da conta: ")
                criar_conta(cpf)
            elif opcao == "3":
                valor = float(input("Valor do depósito: "))
                depositar(valor)
            elif opcao == "4":
                valor = float(input("Valor do saque: "))
                sacar(valor=valor)
            elif opcao == "5":
                visualizar_extrato()
            elif opcao == "6":
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()