import json
import os
import re

ARQUIVO_JSON = os.path.join("dados", "fornecedores.json")

# ===================== Funções utilitárias =====================

def carregar_fornecedores():
    """Carrega os fornecedores do arquivo JSON."""
    if not os.path.exists(ARQUIVO_JSON):
        return []
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_fornecedores(fornecedores):
    """Salva a lista de fornecedores no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

def verificar_id_existe(id, fornecedores):
    """Verifica se o ID já existe em qualquer lista de fornecedores."""
    for f in fornecedores:
        if f["id"] == id:
            return True
    return False

def gerar_id(fornecedores):
    """Gera um novo ID baseado no maior existente, garantindo que seja único."""
    new_id = max(f["id"] for f in fornecedores) + 1 if fornecedores else 1
    while verificar_id_existe(new_id, fornecedores):
        new_id += 1  # Garantir que o ID seja único
    return new_id

# ===================== Funções de validação =====================

def validar_cnpj(cnpj):
    """Valida o formato do CNPJ."""
    cnpj = re.sub(r'\D', '', cnpj)  # Remove qualquer coisa que não seja número
    if len(cnpj) != 14:
        return False
    return True

def validar_telefone(telefone):
    """Valida o formato do telefone (DDD + número)."""
    return bool(re.match(r'^\(\d{2}\)\s?\d{4,5}-\d{4}$', telefone))

def validar_email(email):
    """Valida o formato do e-mail."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# ===================== Funções CRUD =====================

def cadastrar_fornecedor(fornecedores):
    """Cadastra um novo fornecedor com validação de dados e verificação de ID único."""
    print("\n--- Cadastro de Fornecedor ---")
    
    nome = input("Nome: ").strip().upper()
    while not nome:
        print("⚠️ Nome não pode ser vazio!")
        nome = input("Nome: ").strip().upper()
    
    cnpj = input("CNPJ: ").strip()
    while not validar_cnpj(cnpj):
        print("⚠️ CNPJ inválido!")
        cnpj = input("CNPJ: ").strip()

    telefone = input("Telefone: ").strip()
    while not validar_telefone(telefone):
        print("⚠️ Telefone inválido! Use o formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX")
        telefone = input("Telefone: ").strip()

    email = input("Email: ").strip().lower()
    while not validar_email(email):
        print("⚠️ E-mail inválido!")
        email = input("Email: ").strip().lower()

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
    """Lista todos os fornecedores cadastrados."""
    print("\n--- Lista de Fornecedores ---")
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    for f in fornecedores:
        print(
            f"ID: {f['id']} | Nome: {f['nome']} | CNPJ: {f['cnpj']} | "
            f"Telefone: {f.get('telefone', 'N/A')} | Email: {f['email']} | País: {f['pais']} | Estado: {f['estado']}"
        )
    print()

def atualizar_fornecedor(fornecedores):
    """Atualiza um fornecedor existente com validação de dados e verificação de ID único."""
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
    """Exclui um fornecedor pelo ID com confirmação."""
    listar_fornecedores(fornecedores)
    try:
        id_excluir = int(input("Digite o ID do fornecedor a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for f in fornecedores:
        if f["id"] == id_excluir:
            confirmacao = input(f"Você tem certeza que deseja excluir o fornecedor {f['nome']}? (s/n): ").strip().lower()
            if confirmacao == 's':
                fornecedores.remove(f)
                salvar_fornecedores(fornecedores)
                print("🗑️ Fornecedor excluído com sucesso!\n")
            else:
                print("⚠️ Exclusão cancelada.\n")
            return
    print("⚠️ Fornecedor não encontrado.\n")

# ===================== MENU =====================

def menu():
    fornecedores = carregar_fornecedores()

    while True:
        print("""
========== MENU ===========
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
