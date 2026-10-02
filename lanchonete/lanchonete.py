def exibir_cardapio():
    print("=" * 35)
    print("         CARDÁPIO DE LANCHES       ")
    print("=" * 35)
    print("Código | Produto            | Preço ")
    print("  1    | X-Burguer          | R$ 15.00")
    print("  2    | X-Salada           | R$ 18.00")
    print("  3    | Batata Frita       | R$ 12.00")
    print("  4    | Refrigerante Lata  | R$  6.00")
    print("  5    | Suco Natural       | R$  8.00")
    print("=" * 35)


def obter_nome_cliente():
    nome = input("Digite o nome do cliente: ")
    return nome


def obter_preco_produto(codigo):
    match codigo:
        case 1:
            return 15.00  
        case 2:
            return 18.00  
        case 3:
            return 12.00  
        case 4:
            return 6.00   
        case 5:
            return 8.00   
        case _:
            return None   


def realizar_pedidos():
    exibir_cardapio()
    
    total_compra = 0.0
    continuar = "s"
    
    while continuar.lower() == "s":
        codigo = int(input("\nDigite o código do produto desejado: "))
        preco = obter_preco_produto(codigo)
        
        # Validação do código do produto
        if preco is None:
            print("Código de produto inválido! Tente novamente.")
            continue
            
        quantidade = int(input("Digite a quantidade desejada: "))
        
        # Validação da quantidade
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero! Tente novamente.")
            continue
            
        subtotal = preco * quantidade
        total_compra += subtotal
        
        print(f"Item adicionado! Subtotal do item: R$ {subtotal:.2f}")
        print(f"Total acumulado até agora: R$ {total_compra:.2f}")
        
        continuar = input("\nDeseja adicionar outro produto? (s/n): ").strip()
        
    return total_compra


def calcular_desconto(total_compra):
    if total_compra < 50.0:
        percentual = 0
    elif total_compra < 100.0:
        percentual = 5
    else:
        percentual = 10
        
    valor_desconto = total_compra * (percentual / 100)
    valor_final = total_compra - valor_desconto
    
    return percentual, valor_desconto, valor_final


def selecionar_forma_pagamento():
    print("\n--- FORMA DE PAGAMENTO ---")
    print("1. Dinheiro")
    print("2. PIX")
    print("3. Cartão")
    
    while True:
        opcao = int(input("Escolha a forma de pagamento (1, 2 ou 3): "))
        
        match opcao:
            case 1:
                return "Dinheiro"
            case 2:
                return "PIX"
            case 3:
                return "Cartão"
            case _:
                print("Opção inválida! Escolha 1, 2 ou 3.")


def exibir_resumo_final(nome_cliente, valor_original, percentual_desconto, valor_desconto, valor_final, forma_pagamento):
    print("\n" + "=" * 40)
    print("         RESUMO FINAL DO PEDIDO        ")
    print("=" * 40)
    print(f"Cliente: {nome_cliente}")
    print(f"Valor Original: R$ {valor_original:.2f}")
    print(f"Desconto Aplicado: {percentual_desconto}% (R$ {valor_desconto:.2f})")
    print(f"Valor Final a Pagar: R$ {valor_final:.2f}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print("=" * 40)
    print("Obrigado pela preferência! Volte sempre.")


def main():
    nome_cliente = obter_nome_cliente()
    
    total_original = realizar_pedidos()
    
    if total_original == 0:
        print("\nNenhum produto foi selecionado. Atendimento encerrado.")
        return
        
    percentual, valor_desc, valor_final = calcular_desconto(total_original)
    
    forma_pagamento = selecionar_forma_pagamento()
    
    exibir_resumo_final(nome_cliente, total_original, percentual, valor_desc, valor_final, forma_pagamento)


if __name__ == "__main__":
    main()