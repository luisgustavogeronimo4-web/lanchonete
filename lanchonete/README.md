# Sistema de Atendimento e Pedidos 

##  Informações 
- **Nome do Estudante:** Luís Gustavo Gerônimo
- **Disciplina:** Algoritmos e Programação
- **Título do Projeto:** Sistema de Atendimento e Pedidos para Lanchonete

##  Breve Descrição do Programa
Este programa consiste num sistema automatizado de atendimento e gestão de pedidos desenvolvido para uma lanchonete com o objetivo principal de substituir o registo manual por uma solução em Python que permite identificar o cliente, apresentar o cardapio, registar multiplos itens, calcular valores acumulados e descontos automaticos, alem de validar a forma de pagamento e apresentar um resumo final detalhado da compra.

## Principais Funcionalidades Implementadas
- **Identificação do Cliente:** Registo do nome do cliente no inicio do atendimento
- **Cardápio Interativo:** Exibição de produtos com codigos e preços fixos, desenvolvida sem a utilização de estruturas de dados avançadas
- **Acúmulo de Pedidos:** Controle de repetição via laço while, permitindo adicionar varios itens e quantidades sucessivamente
- **Cálculo Automático de Descontos:** Aplicação das regras de negocio sobre o valor total da compra:
  - Compras inferiores a R$ 50,00: sem desconto (0%)
  - Compras de R$ 50,00 ate R$ 99,99: 5% de desconto
  - Compras iguais ou superiores a R$ 100,00: 10% de desconto
- **Validação de Dados:** Utilização de estruturas de decisão (if/else e match-case) para validar a seleção do produto, quantidades e opções do menu, tratando opções invalidas sem comprometer os cálculos
- **Selecção da Forma de Pagamento:** Escolha validada entre Dinheiro, PIX e Cartão através da estrutura match-case
- **Resumo do Pedido:** Exibição final organizada contendo o nome do cliente, valor original, percentual e valor do desconto, valor final a pagar e forma de pagamento

##  Instruções Necessárias para Executar o Programa

### Pré-requisitos
- Ter o **Python 3.10** ou superior instalado no sistema

### Passo a Passo de Execução
1. Faça o clone deste repositório ou transfira os ficheiros do projeto
