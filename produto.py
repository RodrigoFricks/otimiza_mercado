import json
import os

ARQUIVO_PRODUTOS = os.path.join("dados", "produtos.json")

# ===================== Funções utilitárias =====================

def carregar_produtos():
    """Carrega os produtos do arquivo JSON."""
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []
    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def gerar_id(produtos):
    """Gera um novo ID baseado no maior existente."""
    if not produtos:
        return 1
    return max(p["id_produto"] for p in produtos) + 1

# ===================== CRUD =====================

def cadastrar_produto(produtos):
    """Cadastra um novo produto."""
    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do Produto: ").strip().upper()
    try:
        preco = float(input("Preço (R$): "))
        estoque = int(input("Quantidade em Estoque: "))
        fornecedor_id = int(input("ID do Fornecedor: "))
    except ValueError:
        print("⚠️ Erro: valores numéricos inválidos.")
        return

    produto = {
        "id_produto": gerar_id(produtos),
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "fornecedor_id": fornecedor_id
    }

    produtos.append(produto)
    salvar_produtos(produtos)
    print("✅ Produto cadastrado com sucesso!\n")

def listar_produtos(produtos):
    """Lista todos os produtos cadastrados."""
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(
            f"ID: {p['id_produto']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | "
            f"Estoque: {p['estoque']} | Fornecedor ID: {p['fornecedor_id']}"
        )
    print()

def atualizar_produto(produtos):
    """Atualiza um produto existente."""
    listar_produtos(produtos)
    try:
        id_alvo = int(input("Digite o ID do produto a atualizar: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for p in produtos:
        if p["id_produto"] == id_alvo:
            print(f"\nEditando produto: {p['nome']}")
            novo_nome = input(f"Novo nome ({p['nome']}): ").strip().upper() or p["nome"]
            novo_preco = input(f"Novo preço ({p['preco']}): ").strip()
            novo_estoque = input(f"Novo estoque ({p['estoque']}): ").strip()
            novo_forn = input(f"Novo ID Fornecedor ({p['fornecedor_id']}): ").strip()

            p["nome"] = novo_nome
            p["preco"] = float(novo_preco) if novo_preco else p["preco"]
            p["estoque"] = int(novo_estoque) if novo_estoque else p["estoque"]
            p["fornecedor_id"] = int(novo_forn) if novo_forn else p["fornecedor_id"]

            salvar_produtos(produtos)
            print("✅ Produto atualizado com sucesso!\n")
            return
    print("⚠️ Produto não encontrado.\n")

def excluir_produto(produtos):
    """Exclui um produto pelo ID."""
    listar_produtos(produtos)
    try:
        id_excluir = int(input("Digite o ID do produto a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for p in produtos:
        if p["id_produto"] == id_excluir:
            produtos.remove(p)
            salvar_produtos(produtos)
            print("🗑️ Produto excluído com sucesso!\n")
            return
    print("⚠️ Produto não encontrado.\n")

# ===================== MENU =====================

def menu_produtos():
    produtos = carregar_produtos()

    while True:
        print("""
========== MENU PRODUTOS ==========
1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
5 - Voltar
===================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            atualizar_produto(produtos)
        elif opcao == "4":
            excluir_produto(produtos)
        elif opcao == "5":
            print("💾 Saindo do menu de produtos...")
            salvar_produtos(produtos)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.\n")

# ===================== Execução direta =====================

if __name__ == "__main__":
    menu_produtos()
