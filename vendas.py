import json
import os

ARQUIVO_VENDAS = os.path.join("dados", "vendas.json")

# ========== Funções utilitárias ==========
def carregar_vendas():
    if not os.path.exists(ARQUIVO_VENDAS):
        return []
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_vendas(vendas):
    with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as f:
        json.dump(vendas, f, indent=4, ensure_ascii=False)

def gerar_id(vendas):
    if not vendas:
        return 1
    return max(v["id_venda"] for v in vendas) + 1

# ========== CRUD ==========
def cadastrar_venda(vendas):
    print("\n--- Cadastro de Venda ---")
    try:
        id_cliente = int(input("ID do Cliente: "))
        id_produto = int(input("ID do Produto: "))
        quantidade = int(input("Quantidade: "))
        valor_total = float(input("Valor Total: "))
    except ValueError:
        print("⚠️ Valores inválidos! Use apenas números onde necessário.")
        return

    venda = {
        "id_venda": gerar_id(vendas),
        "id_cliente": id_cliente,
        "id_produto": id_produto,
        "quantidade": quantidade,
        "valor_total": valor_total
    }

    vendas.append(venda)
    salvar_vendas(vendas)
    print("✅ Venda cadastrada com sucesso!\n")

def listar_vendas(vendas):
    print("\n--- Lista de Vendas ---")
    if not vendas:
        print("Nenhuma venda cadastrada.")
        return
    for v in vendas:
        print(
            f"ID: {v['id_venda']} | Cliente: {v['id_cliente']} | Produto: {v['id_produto']} | "
            f"Qtd: {v['quantidade']} | Total: R${v['valor_total']:.2f}"
        )
    print()

def atualizar_venda(vendas):
    listar_vendas(vendas)
    try:
        id_alvo = int(input("Digite o ID da venda a atualizar: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for v in vendas:
        if v["id_venda"] == id_alvo:
            print(f"\nEditando venda ID {v['id_venda']}")
            novo_cliente = input(f"Novo ID Cliente ({v['id_cliente']}): ") or v["id_cliente"]
            novo_produto = input(f"Novo ID Produto ({v['id_produto']}): ") or v["id_produto"]
            nova_qtd = input(f"Nova Quantidade ({v['quantidade']}): ")
            novo_valor = input(f"Novo Valor Total ({v['valor_total']}): ")

            v["id_cliente"] = int(novo_cliente)
            v["id_produto"] = int(novo_produto)
            v["quantidade"] = int(nova_qtd) if nova_qtd else v["quantidade"]
            v["valor_total"] = float(novo_valor) if novo_valor else v["valor_total"]

            salvar_vendas(vendas)
            print("✅ Venda atualizada com sucesso!\n")
            return
    print("⚠️ Venda não encontrada.\n")

def excluir_venda(vendas):
    listar_vendas(vendas)
    try:
        id_excluir = int(input("Digite o ID da venda a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for v in vendas:
        if v["id_venda"] == id_excluir:
            vendas.remove(v)
            salvar_vendas(vendas)
            print("🗑️ Venda excluída com sucesso!\n")
            return
    print("⚠️ Venda não encontrada.\n")

# ========== MENU ==========
def menu_vendas():
    vendas = carregar_vendas()

    while True:
        print("""
========== MENU VENDAS ==========
1 - Cadastrar venda
2 - Listar vendas
3 - Atualizar venda
4 - Excluir venda
5 - Voltar
=================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_venda(vendas)
        elif opcao == "2":
            listar_vendas(vendas)
        elif opcao == "3":
            atualizar_venda(vendas)
        elif opcao == "4":
            excluir_venda(vendas)
        elif opcao == "5":
            print("💾 Saindo do menu de vendas...")
            salvar_vendas(vendas)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu_vendas()
