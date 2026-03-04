# Sistema_Bancario

    Desafio de bootcamp para a montagem de um sistema bancário simples

## Versão 1
Sistema bancário v1 (Um usário)
    Operação de depósito:
        O usuário deve informar o valor a ser depositado. O valor deve ser positivo.Todos depósitos devem ser armazenados em uma lista.
    Operação de saque:
        O usuário deve informar o valor a ser sacado. O valor deve ser positivo e menor ou igual ao saldo disponível. O usuário só pode realizar 3 saques por dia. Todos os saques devem ser armazenados em uma lista.
    Operação de extrato:
        O sistema deve exibir todas as operações de depósito e saque, bem como o saldo atual. Se não houver movimentações, exibir a mensagem "Não foram realizadas movimentações."

    O sistema deve exibir um menu de opções para o usuário escolher a operação desejada (sacar, depositar, extrato ou sair). O programa deve continuar rodando até que o usuário escolha a opção de sair. 

    Observações: 3 saques diários, limite de saque de R$500,00 por operação, depósito mínimo de R$1. Caso não tenha saldo suficiente para realizar um saque, exibir a mensagem "Saldo insuficiente." O sistema deve ser implementado utilizando funções para cada operação (sacar, depositar, extrato) e uma função principal para controlar o fluxo do programa.


## Versão 2 - Sistema Bancário com POO

Esta versão implementa o sistema bancário utilizando **Programação Orientada a Objetos (POO)**, tornando o código mais organizado, flexível e fácil de manter. Os principais arquivos e componentes são:

- `desafio_3_1.py` – Define as principais classes do sistema:
    - `Cliente` e `PessoaFisica`: representam os usuários, seus dados e contas associadas.
    - `Conta` e `ContaCorrente`: modelam as contas bancárias, com métodos para saque, depósito e histórico de operações. `ContaCorrente` implementa limites de saque e quantidade de saques diários.
    - `Historico`: registra todas as transações realizadas na conta, com data e tipo.
    - `Transacao`, `Saque` e `Deposito`: abstraem as operações bancárias, facilitando a extensão para novos tipos de transação.

- `desafio_3_2.py` – Ponto de entrada do sistema, responsável pelo menu interativo e fluxo principal:
    - Permite cadastrar clientes, criar contas, realizar depósitos, saques e consultar extrato.
    - Utiliza as classes do sistema para manipular os dados e operações de forma orientada a objetos.
    - Funções como `depositar` e `sacar` foram simplificadas para evitar repetição, usando uma função genérica para transações.

### Funcionalidades principais

- Cadastro de clientes e contas vinculadas ao CPF.
- Depósito e saque com validações (valor positivo, limite de saque, máximo de saques diários).
- Histórico detalhado de transações por conta.
- Menu interativo para todas as operações.

### Observações

O uso de POO permite fácil expansão do sistema, como inclusão de novos tipos de conta ou regras específicas. O código está mais modular, facilitando testes e manutenção.

## Versão 3 - Orientação a Objetos (POO)

A terceira versão reescreve o sistema utilizando programação orientada a objetos. Os principais componentes e arquivos são:

- `desafio_3_1.py` – contém as classes que modelam clientes, contas, histórico e transações.
  - `Cliente` e `PessoaFisica` para representar os usuários e seus dados.
  - `Conta` como classe base com propriedades e métodos de saque, depósito e histórico.
  - `ContaCorrente` especializada com limite por saque e número máximo de saques diários.
  - `Historico` armazena as operações realizadas com timestamps.
  - `Transacao`, `Saque` e `Deposito` abstraem o comportamento de cada operação.
  - Uso de padrões como métodos de classe (`nova_conta`), propriedades e herança.

- `desafio_3_2.py` – ponto de entrada (ainda vazio neste repositório) responsável por criar objetos e exibir o menu interativo. Nesta versão o fluxo principal pode ser implementado criando instâncias de clientes e contas e utilizando objetos de transação para registrar operações.

### Funcionalidades mantidas

- Limite de saque de R$500 por operação e até 3 saques por dia.
- Depósito apenas com valores positivos.
- Histórico de transações exibido em extrato.
- Exibição de menu para depositar, sacar, ver extrato ou sair.

### Observações

A arquitetura orientada a objetos facilita extensão futura (novos tipos de conta, regras específicas) e melhora a organização do código. O README passa a documentar as classes básicas e como usá-las para configurar o sistema bancário na versão POO.

