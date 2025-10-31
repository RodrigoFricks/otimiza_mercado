import json
import os
import re

ARQUIVO_PRODUTOS = os.path.join("dados", "produtos.json")
ARQUIVO_FORNECEDORES = os.path.join("dados", "fornecedores.json")

# ===================== Funções utilitárias =====================

def carregar_fornecedores():
    """Carrega os fornecedores do arquivo JSON."""
    if not os.path.exists(ARQUIVO_FORNECEDORES):
        return []
    with open(ARQUIVO_FORNECEDORES, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

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

def salvar_fornecedores(fornecedores):
    """Salva a lista de fornecedores no arquivo JSON."""
    with open(ARQUIVO_FORNECEDORES, "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

def verificar_id_existe(id, produtos):
    """Verifica se o ID já existe em qualquer lista de produtos."""
    for p in produtos:
        if p["id_produto"] == id:
            return True
    return False

def gerar_id(produtos):
    """Gera um novo ID baseado no maior existente, garantindo que seja único."""
    new_id = max(p["id_produto"] for p in produtos) + 1 if produtos else 1
    while verificar_id_existe(new_id, produtos):  # Garantir que o ID seja único
        new_id += 1
    return new_id

# ===================== Funções de validação =====================

def validar_cnpj(cnpj):
    """Valida o formato do CNPJ."""
    cnpj = re.sub(r'\D', '', cnpj)  # Remove qualquer coisa que não seja número
    if len(cnpj) != 14:
        return False
    return True

# def validar_telefone(telefone):
#     """Valida o formato do telefone (DDD + número)."""
#     return bool(re.match(r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$', telefone))

def validar_email(email):
    """Valida o formato do e-mail."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# ===================== Funções CRUD =====================

def listar_fornecedores(fornecedores):
    """Lista todos os fornecedores cadastrados."""
    print("\n--- Fornecedores Cadastrados ---")
    if not fornecedores:
        print("Não há fornecedores cadastrados.")
        return []
    for f in fornecedores:
        print(f"ID: {f['id']} | Nome: {f['nome']}")
    print()
    return fornecedores

def cadastrar_produto(produtos, fornecedores):
    """Cadastra um novo produto com fornecedor associado."""
    print("\n--- Cadastro de Produto ---")
    
    # Listar fornecedores para seleção
    fornecedores = listar_fornecedores(fornecedores)
    if not fornecedores:
        return

    while True:
        try:
            id_fornecedor = int(input("Escolha o ID do Fornecedor: "))
            fornecedor = next((f for f in fornecedores if f["id"] == id_fornecedor), None)
            
            # Verifica se o fornecedor com o ID escolhido existe
            if fornecedor:
                break  # ID de fornecedor válido
            else:
                print("⚠️ ID de fornecedor inválido ou não existente. Tente novamente.")
        except ValueError:
            print("⚠️ Erro: Por favor, insira um número válido para o ID do Fornecedor.")
    
    # Garantir que o nome do produto não seja vazio
    while True:
        nome = input("Nome do Produto: ").strip().upper()
        if nome:  # Verifica se o nome não está vazio
            break
        else:
            print("⚠️ Nome do produto não pode ser vazio! Tente novamente.")

    try:
        preco = float(input("Preço (R$): "))
        estoque = int(input("Quantidade em Estoque: "))
    except ValueError:
        print("⚠️ Erro: valores numéricos inválidos.")
        return

    produto = {
        "id_produto": gerar_id(produtos),
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "fornecedor_id": id_fornecedor  # Associando o fornecedor
    }

    produtos.append(produto)
    salvar_produtos(produtos)
    print(f"✅ Produto '{nome}' cadastrado com sucesso!\n")

def listar_produtos(produtos, fornecedores):
    """Lista todos os produtos cadastrados com informações do fornecedor."""
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Não há produtos cadastrados.")
        return
    for p in produtos:
        # Verifica se o fornecedor existe
        fornecedor = next((f for f in fornecedores if f["id"] == p["fornecedor_id"]), None)
        if fornecedor:
            print(
                f"\nID: {p['id_produto']} | Nome: {p['nome']}\n"
                f"Preço: R${p['preco']:.2f}\nEstoque: {p['estoque']}\n"
                f"Fornecido por: {fornecedor['nome']} (ID: {fornecedor['id']})\n"
                
            )

def atualizar_produto(produtos, fornecedores):
    """Atualiza um produto existente com validação de dados e verificação de ID único."""
    listar_produtos(produtos, fornecedores)  # Só chama a listagem aqui, depois de alterar
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

def excluir_produto(produtos, fornecedores):
    """Exclui um produto pelo ID."""
    listar_produtos(produtos, fornecedores)  # Só chama a listagem aqui, depois de excluir
    try:
        id_excluir = int(input("Digite o ID do produto a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for p in produtos:
        if p["id_produto"] == id_excluir:
            produtos.remove(p)
            salvar_produtos(produtos)
            print(f"🗑️ Produto '{p['nome']}' excluído com sucesso!\n")
            return
    print("⚠️ Produto não encontrado.\n")

# ===================== MENU =====================

def menu_produtos():
    fornecedores = carregar_fornecedores()
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
            cadastrar_produto(produtos, fornecedores)
        elif opcao == "2":
            listar_produtos(produtos, fornecedores)
        elif opcao == "3":
            atualizar_produto(produtos, fornecedores)
        elif opcao == "4":
            excluir_produto(produtos, fornecedores)
        elif opcao == "5":
            print("💾 Saindo do menu de produtos...")
            salvar_produtos(produtos)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.\n")

# ===================== Execução direta =====================

if __name__ == "__main__":
    menu_produtos()
