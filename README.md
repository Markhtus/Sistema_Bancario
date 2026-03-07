# Sistema_Bancario

    Desafio de bootcamp para a montagem de um sistema bancário 

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

## Versão 4 - Decoradores, Iteradores e Geradores

Esta versão aprimora o sistema bancário com conceitos avançados de Python: decoradores, iteradores e geradores. O arquivo principal é `version_4.py`, que integra essas funcionalidades ao sistema POO existente.

### Principais Componentes e Funcionalidades

- **Decorador de Log**: 
  - Aplicado a todas as funções de transações (depósito, saque, criação de conta, etc.).
  - Registra (imprime) a data e hora de cada transação, bem como o tipo de transação.
  - Implementado via [`log_transacao`], um decorador parametrizado que aceita o tipo de transação.

- **Gerador de Relatório**:
  - Implementado no método [`gerar_relatorio`] da classe [`Historico`]
  - Permite iterar sobre as transações de uma conta, retornando-as uma a uma.
  - Suporta filtragem por tipo de transação (ex.: apenas saques ou apenas depósitos), utilizando o parâmetro opcional `tipo`.

- **Iterador Personalizado**:
  - Classe [`ContaIterador`] para iterar sobre todas as contas do banco.
  - Retorna informações básicas de cada conta (número, agência, titular, saldo) em cada iteração.
  - Utilizado na função [`listar_contas`] para exibir a lista de contas.

### Funcionalidades Adicionadas ou Aprimoradas

- Menu simplificado com extrato único, sem opção de relatório separado; os detalhes de transações aparecem diretamente no extrato.
- Logs automáticos para todas as transações, melhorando a rastreabilidade.
- Relatórios gerados sob demanda, com possibilidade de filtro, utilizando geradores para eficiência de memória.
- Iteração personalizada sobre contas, facilitando operações em lote ou exibições.

### Observações

Esta versão demonstra o uso prático de decoradores para logging, geradores para relatórios eficientes e iteradores para navegação customizada de dados. Mantém a compatibilidade com versões anteriores, focando em aprimoramentos funcionais e educacionais. O código é mais conciso e performático, especialmente em operações com grandes volumes de dados.

## Versão 5 - Limites e contagens diárias de transações

A quinta versão adiciona controles mais sofisticados sobre a quantidade de operações realizadas por conta em um único dia, reforçando regras de negócio e ampliando a rastreabilidade.

### Principais melhorias

- **Limite diário de transações**: cada conta agora possui um atributo `_limite_transacoes_diarias` que restringe o número total de operações (saques ou depósitos) por dia.
- **Contagem de transações**: implementação de `_contar_transacoes_diarias` na classe `Conta` que verifica quantas transações já foram feitas na data atual.
- **Validação nas transações**: os métodos `registrar` de `Saque` e `Deposito` consultam o contador diário e impedem novas operações quando o limite é atingido, exibindo mensagem de erro apropriada.
- **Integração com decoradores**: o decorador `log_transacao` continua registrando data/hora e tipo, agora também aplicado nos métodos `registrar` para maior rastreabilidade.
- **Atributo de limite no conta corrente**: `ContaCorrente` herda o limite diário e mantém restrições de valores e quantidade de saques, garantindo múltiplos níveis de validação.

As demais funcionalidades de cliente, menu interativo, histórico, gerador de relatórios e iterador de contas permanecem presentes, garantindo compatibilidade com versões anteriores enquanto adicionam regras de negócio mais robustas.

## Versão 6 - Log em Arquivo, Padrão Strategy e Melhorias na Iteração

A sexta versão consolidada aprimora significativamente o sistema bancário com persistência de logs em arquivo, implementação completa do padrão Strategy e refinamentos na iteração e filtragem de dados.

### Principais Implementações

- **Decorador de Log com Persistência em Arquivo**:
  - Novo decorador `log_transacao` que registra automaticamente todas as transações (saques e depósitos) em um arquivo `log.txt`.
  - Captura informações detalhadas: data/hora (`dd-mm-aaaa HH:MM:SS`), nome da função, argumentos passados e valor retornado.
  - Aplicado automaticamente aos métodos `sacar`, `depositar` e `registrar` das classes de transação.
  - Facilita auditoria e rastreamento de todas as operações do banco.

- **Padrão Strategy com Classes Abstratas**:
  - Classe abstrata `Transacao` definida com `ABC` (Abstract Base Class) e `@abstractmethod`.
  - Define contrato claro: propriedade `valor` e método `registrar(conta)` que toda transação deve implementar.
  - Classes `Saque` e `Deposito` implementam o contrato abstrato, encapsulando lógica específica de cada operação.
  - Facilita a extensão para novos tipos de transação no futuro, mantendo flexibilidade e segurança de tipo.

- **Iterator Customizado para Contas**:
  - Classe `ContaIterador` implementa protocolos `__iter__()` e `__next__()` para iteração customizada.
  - Retorna dicionário com informações básicas: número, agência, titular e saldo da conta.
  - Função `listar_contas()` utiliza o iterator para exibir todas as contas de forma elegante e organizada.
  - Exemplifica boas práticas de design iterável em Python.

- **Gerador para Relatórios com Filtro**:
  - Método `gerar_relatorio(tipo=None)` em `Historico` usa `yield` para retornar transações uma a uma.
  - Suporta filtro opcional por tipo: `Saque`, `Deposito` ou todas as transações (quando `tipo=None`).
  - Função `exibir_relatorio()` no menu permite ao usuário filtrar relatórios por tipo de operação.
  - Economia de memória em contas com muitas transações.

- **Método Privado para Contagem de Transações Diárias**:
  - Método `_contar_transacoes_diarias()` na classe `Conta` verifica limite diário (10 transações).
  - Utiliza compreensão de lista com filtro de data para contar operações do dia atual.
  - Validação ocorre em ambos os métodos `registrar` de `Saque` e `Deposito`, garantindo consistência.

- **Propriedades (`@property`) para Encapsulamento**:
  - Atributos privados (`_saldo`, `_numero`, `_agencia`, `_cliente`, `_historico`) acessados apenas via propriedades.
  - Garante validação e controle centralizado sobre dados sensíveis da conta.
  - Implementação de boas práticas de encapsulamento e proteção de dados.

- **Método de Classe (`@classmethod`) para Criação**:
  - Método `nova_conta()` em `Conta` exemplo de método de classe para construir instâncias de forma padronizada.
  - Facilita criação consistent de contas e permite lógica customizada em subclasses.

- **Menu Interativo Expandido**:
  - Opção `[r]` para exibir **Relatório de transações** com filtro opcional por tipo (Saque/Depósito).
  - Opção `[lc]` para **Listar contas** com visualização formatada de todas as contas e seus saldos.
  - Menu mantém compatibilidade com versões anteriores (depósito, saque, extrato).

### Funcionalidades Mantidas

- Cadastro de clientes (PessoaFisica) e contas (ContaCorrente) vinculadas ao CPF.
- Limites de saque (R$500) e máximo de saques diários (10).
- Limite total de 10 transações por dia (saques + depósitos).
- Histórico detalhado de todas as operações com timestamps.
- Sistema de log com decoradores para rastreamento de execução.

### Observações

A versão 6 representa uma consolidação madura do sistema bancário, demonstrando domínio de conceitos avançados de Python como decoradores parametrizados, classes abstratas, iteradores customizados, geradores e padrões de design. O código é altamente extensível, mantível e segue as melhores práticas de engenharia de software. A persistência de logs em arquivo agrega valor significativo para auditoria e conformidade.

