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

## Versão 2

O repositório contém os seguintes arquivos de código:

- `desafio_1.py` – implementação inicial do sistema bancário (Versão 1) com as funcionalidades básicas de depósito, saque (com limite diário de 3 saques e limite de R$500 por operação) e visualização de extrato. Usa variáveis globais e funções simples, rodando em loop no console até o usuário escolher sair.
- `desafio_2.py` – versão ampliada que adiciona cadastro de usuários e criação de contas vinculadas a um CPF, mantendo lista de usuários e contas. Também refatora os métodos de saque e depósito com argumentos posicionais e nomeados, e preserva limite diário de saques e extrato em string.