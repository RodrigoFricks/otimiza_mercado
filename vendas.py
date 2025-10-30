import json
import os

ARQUIVO_CLIENTES = os.path.join("dados", "clientes.json")
ARQUIVO_PRODUTOS = os.path.join("dados", "produtos.json")
ARQUIVO_VENDAS = os.path.join("dados", "vendas.json")

# ========== Funções utilitárias ==========

def carregar_clientes():
    """Carrega os clientes do arquivo JSON."""
    if not os.path.exists(ARQUIVO_CLIENTES):
        return []
    with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_produtos():
    """Carrega os produtos do arquivo JSON."""
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []
    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_vendas():
    """Carrega as vendas do arquivo JSON."""
    if not os.path.exists(ARQUIVO_VENDAS):
        return []
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_clientes(clientes):
    """Salva a lista de clientes no arquivo JSON."""
    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def salvar_vendas(vendas):
    """Salva a lista de vendas no arquivo JSON."""
    with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as f:
        json.dump(vendas, f, indent=4, ensure_ascii=False)

def verificar_id_existe(id, vendas):
    """Verifica se o ID já existe em qualquer lista de vendas."""
    for v in vendas:
        if v["id_venda"] == id:
            return True
    return False

def gerar_id(vendas):
    """Gera um novo ID baseado no maior existente, garantindo que seja único."""
    new_id = max(v["id_venda"] for v in vendas) + 1 if vendas else 1
    while verificar_id_existe(new_id, vendas):
        new_id += 1  # Garantir que o ID seja único
    return new_id

# ========== Funções de Validação e Cadastro de Venda ==========

def listar_clientes(clientes):
    """Lista todos os clientes cadastrados."""
    if not clientes:
        print("Não há clientes cadastrados.")
        return []
    print("\n--- Clientes Cadastrados ---")
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nome: {cliente['nome']}")
    print()
    return clientes

def listar_produtos(produtos):
    """Lista todos os produtos cadastrados."""
    if not produtos:
        print("Não há produtos cadastrados.")
        return []
    print("\n--- Produtos Cadastrados ---")
    for produto in produtos:
        print(f"ID: {produto['id_produto']} | Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Estoque: {produto['estoque']}")
    print()
    return produtos

def cadastrar_venda(vendas, clientes, produtos):
    """Cadastra uma nova venda com validação de ID único."""
    print("\n--- Cadastro de Venda ---")
    
    clientes = listar_clientes(clientes)
    if not clientes:
        return
    while True:
        try:
            id_cliente = int(input("Escolha o ID do Cliente: "))
            cliente = next((c for c in clientes if c["id"] == id_cliente), None)
            if cliente:
                break
            else:
                print("ID de cliente inválido, tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ID do Cliente.")

    produtos = listar_produtos(produtos)
    if not produtos:
        return
    while True:
        try:
            id_produto = int(input("Escolha o ID do Produto: "))
            produto = next((p for p in produtos if p["id_produto"] == id_produto), None)
            if produto:
                break
            else:
                print("ID de produto inválido, tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido para o ID do Produto.")

    while True:
        try:
            quantidade = int(input(f"Quantidade de {produto['nome']} (estoque disponível: {produto['estoque']}): "))
            if 0 < quantidade <= produto['estoque']:
                break
            else:
                print(f"Quantidade inválida, deve ser maior que 0 e não exceder o estoque ({produto['estoque']}).")
        except ValueError:
            print("Erro: Por favor, insira um número válido para a Quantidade.")

    valor_total = produto["preco"] * quantidade

    venda = {
        "id_venda": gerar_id(vendas),
        "id_cliente": id_cliente,
        "id_produto": id_produto,
        "quantidade": quantidade,
        "valor_produto": produto["preco"],
        "valor_total": valor_total,
    }

    # Atualizar o estoque do produto
    produto['estoque'] -= quantidade
    salvar_produtos(produtos)  # Atualiza o arquivo de produtos

    vendas.append(venda)
    salvar_vendas(vendas)

    # Formatação mais bonita para o retorno
    print(f"\nVenda Cadastrada com Sucesso! 🎉\n")
    print(f"Venda ID: {venda['id_venda']}")
    print(f"Cliente: {cliente['nome']} (ID: {venda['id_cliente']})")
    print(f"Produto: {produto['nome']} (ID: {venda['id_produto']})")
    print(f"Preço Unitário: R${venda['valor_produto']:.2f}")
    print(f"Quantidade: {venda['quantidade']}")
    print(f"Total: R${venda['valor_total']:.2f}")
    print("\n")

# ========== MENU ==========

def menu_vendas():
    clientes = carregar_clientes()
    produtos = carregar_produtos()
    vendas = carregar_vendas()

    while True:
        print("""
========== MENU VENDAS ===========
1 - Cadastrar venda
2 - Listar vendas
3 - Voltar
================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_venda(vendas, clientes, produtos)
        elif opcao == "2":
            listar_vendas(vendas)
        elif opcao == "3":
            print("Voltando ao menu principal...\n")
            salvar_vendas(vendas)
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def listar_vendas(vendas):
    print("\n--- Lista de Vendas ---")
    if not vendas:
        print("Não há vendas cadastradas.")
        return
    for v in vendas:
        print(
            f"ID: {v['id_venda']} | Cliente: {v['id_cliente']} | Produto: {v['id_produto']} | "
            f"Qtd: {v['quantidade']} | Total: R${v['valor_total']:.2f}"
        )
    print()

# Função principal para iniciar o programa
if __name__ == "__main__":
    menu_vendas()
