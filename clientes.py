import json
import os

ARQUIVO_CLIENTES = os.path.join("dados", "clientes.json")

# ===================== Funções utilitárias =====================

def carregar_clientes():
    """Carrega os clientes do arquivo JSON."""
    if not os.path.exists(ARQUIVO_CLIENTES):
        return []
    with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_clientes(clientes):
    """Salva a lista de clientes no arquivo JSON."""
    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def gerar_id(clientes):
    """Gera um novo ID com base no maior existente."""
    if not clientes:
        return 1
    return max(c["id"] for c in clientes) + 1

# ===================== CRUD =====================

def cadastrar_cliente(clientes):
    """Cadastra um novo cliente."""
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ").strip().upper()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip().lower()
    endereco_pais = input("País: ").strip().upper()
    endereco_estado = input("Estado: ").strip().upper()
    endereco_cidade = input("Cidade: ").strip().upper()
    endereco_bairro = input("Bairro: ").strip().upper()
    endereco_rua = input("Rua e Número: ").strip().upper()

    cliente = {
        "id": gerar_id(clientes),
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "pais": endereco_pais,
        "estado": endereco_estado,
        "cidade": endereco_cidade,
        "bairro": endereco_bairro,
        "rua_num": endereco_rua
    }

    clientes.append(cliente)
    salvar_clientes(clientes)
    print("✅ Cliente cadastrado com sucesso!\n")

def listar_clientes(clientes):
    """Lista todos os clientes cadastrados."""
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for c in clientes:
        print(
            f"ID: {c['id']} | Nome: {c['nome']} | CPF: {c['cpf']} | "
            f"Telefone: {c.get('telefone', 'N/A')} | Email: {c['email']} | "
            f"Cidade: {c['cidade']} - {c['estado']} ({c['pais']})"
        )
    print()

def atualizar_cliente(clientes):
    """Atualiza os dados de um cliente existente."""
    listar_clientes(clientes)
    try:
        id_alvo = int(input("Digite o ID do cliente a atualizar: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for c in clientes:
        if c["id"] == id_alvo:
            print(f"\nEditando cliente: {c['nome']}")
            c["nome"] = input(f"Novo nome ({c['nome']}): ").strip().upper() or c["nome"]
            c["cpf"] = input(f"Novo CPF ({c['cpf']}): ").strip() or c["cpf"]
            c["telefone"] = input(f"Novo telefone ({c['telefone']}): ").strip() or c["telefone"]
            c["email"] = input(f"Novo email ({c['email']}): ").strip().lower() or c["email"]
            c["pais"] = input(f"Novo país ({c['pais']}): ").strip().upper() or c["pais"]
            c["estado"] = input(f"Novo estado ({c['estado']}): ").strip().upper() or c["estado"]
            c["cidade"] = input(f"Nova cidade ({c['cidade']}): ").strip().upper() or c["cidade"]
            c["bairro"] = input(f"Novo bairro ({c['bairro']}): ").strip().upper() or c["bairro"]
            c["rua_num"] = input(f"Nova rua/número ({c['rua_num']}): ").strip().upper() or c["rua_num"]

            salvar_clientes(clientes)
            print("✅ Cliente atualizado com sucesso!\n")
            return
    print("⚠️ Cliente não encontrado.\n")

def excluir_cliente(clientes):
    """Exclui um cliente pelo ID."""
    listar_clientes(clientes)
    try:
        id_excluir = int(input("Digite o ID do cliente a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for c in clientes:
        if c["id"] == id_excluir:
            clientes.remove(c)
            salvar_clientes(clientes)
            print("🗑️ Cliente excluído com sucesso!\n")
            return
    print("⚠️ Cliente não encontrado.\n")

# ===================== MENU =====================

def menu_clientes():
    clientes = carregar_clientes()

    while True:
        print("""
========== MENU CLIENTES ==========
1 - Cadastrar cliente
2 - Listar clientes
3 - Atualizar cliente
4 - Excluir cliente
5 - Voltar
===================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            atualizar_cliente(clientes)
        elif opcao == "4":
            excluir_cliente(clientes)
        elif opcao == "5":
            print("💾 Saindo do menu de clientes...")
            salvar_clientes(clientes)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.\n")

# ===================== Execução direta =====================

if __name__ == "__main__":
    menu_clientes()
