import json
import os

ARQUIVO_JSON = "fornecedores.json"

def carregar_fornecedores():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_fornecedores(fornecedores):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

def gerar_id(fornecedores):
    if not fornecedores:
        return 1
    return max(f["id"] for f in fornecedores) + 1

def cadastrar_fornecedor(fornecedores):
    print("\n--- Cadastro de Fornecedor ---")
    nome = input("Nome: ").strip().upper()
    cnpj = input("CNPJ: ").strip().upper()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip().upper()
    endereco_pais = input("País: ").strip().upper()
    endereco_estado = input("Estado: ").strip().upper()
    endereco_cidade = input("Cidade: ").strip().upper()
    endereco_bairro = input("Bairro: ").strip().upper()
    endereco_rua = input("Rua e Número: ").strip().upper()

    fornecedor = {
        "id": gerar_id(fornecedores),
        "nome": nome,
        "cnpj": cnpj,
        "telefone": telefone,
        "email": email,
        "pais": endereco_pais,
        "estado": endereco_estado,
        "cidade": endereco_cidade,
        "bairro": endereco_bairro,
        "rua_num": endereco_rua
    }

    fornecedores.append(fornecedor)
    salvar_fornecedores(fornecedores)
    print("✅ Fornecedor cadastrado com sucesso!\n")

def listar_fornecedores(fornecedores):
    print("\n--- Lista de Fornecedores ---")
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    for f in fornecedores:
        print(
            f"ID: {f['id']} | Nome: {f['nome']} | CNPJ: {f['cnpj']} | "f"Telefone: {f.get('telefone', 'N/A')} | Email: {f['email']} | País: {f['pais']} | Estado: {f['estado']}"
        )
    print()

def atualizar_fornecedor(fornecedores):
    listar_fornecedores(fornecedores)
    try:
        id_atualizar = int(input("Digite o ID do fornecedor a atualizar: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for f in fornecedores:
        if f["id"] == id_atualizar:
            print(f"\nEditando fornecedor: {f['nome']}")
            f["nome"] = input(f"Novo nome ({f['nome']}): ") or f["nome"]
            f["cnpj"] = input(f"Novo CNPJ ({f['cnpj']}): ") or f["cnpj"]
            f["telefone"] = input(f"Novo telefone ({f.get('telefone', 'N/A')}): ") or f.get("telefone", "")
            f["email"] = input(f"Novo e-mail ({f['email']}): ") or f["email"]
            f["pais"] = input(f"Novo país ({f['pais']}): ") or f["pais"]
            f["estado"] = input(f"Novo estado ({f['estado']}): ") or f["estado"]
            f["cidade"] = input(f"Nova cidade ({f['cidade']}): ") or f["cidade"]
            f["bairro"] = input(f"Novo bairro ({f['bairro']}): ") or f["bairro"]
            f["rua_num"] = input(f"Nova rua/número ({f['rua_num']}): ") or f["rua_num"]

            salvar_fornecedores(fornecedores)
            print("✅ Fornecedor atualizado com sucesso!\n")
            return
    print("⚠️ Fornecedor não encontrado.\n")

def excluir_fornecedor(fornecedores):
    listar_fornecedores(fornecedores)
    try:
        id_excluir = int(input("Digite o ID do fornecedor a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for f in fornecedores:
        if f["id"] == id_excluir:
            fornecedores.remove(f)
            salvar_fornecedores(fornecedores)
            print("🗑️ Fornecedor excluído com sucesso!\n")
            return
    print("⚠️ Fornecedor não encontrado.\n")

def menu():
    fornecedores = carregar_fornecedores()

    while True:
        print("""
========== MENU ==========
1 - Cadastrar fornecedor
2 - Listar fornecedores
3 - Atualizar fornecedor
4 - Excluir fornecedor
5 - Sair
==========================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_fornecedor(fornecedores)
        elif opcao == "2":
            listar_fornecedores(fornecedores)
        elif opcao == "3":
            atualizar_fornecedor(fornecedores)
        elif opcao == "4":
            excluir_fornecedor(fornecedores)
        elif opcao == "5":
            print("💾 Saindo e salvando dados...")
            salvar_fornecedores(fornecedores)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()