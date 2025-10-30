import json
import os
import re

# Caminho dos arquivos
ARQUIVO_CLIENTES = os.path.join("dados", "clientes.json")
ARQUIVO_FORNECEDORES = os.path.join("dados", "fornecedores.json")
ARQUIVO_PRODUTOS = os.path.join("dados", "produtos.json")

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

def salvar_clientes(clientes):
    """Salva a lista de clientes no arquivo JSON."""
    with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def salvar_fornecedores(fornecedores):
    """Salva a lista de fornecedores no arquivo JSON."""
    with open(ARQUIVO_FORNECEDORES, "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def verificar_id_existe(id, lista):
    """Verifica se o ID já existe em qualquer lista."""
    for item in lista:
        if item["id"] == id:
            return True
    return False

# ===================== Funções de validação =====================

def validar_cpf(cpf):
    """Valida o formato do CPF."""
    cpf = re.sub(r'\D', '', cpf)  # Remove qualquer coisa que não seja número
    if len(cpf) != 11:
        return False
    return True

def validar_telefone(telefone):
    """Valida o formato do telefone (DDD + número)."""
    return bool(re.match(r'^\(\d{2}\)\s?\d{4,5}-\d{4}$', telefone))

def validar_email(email):
    """Valida o formato do e-mail."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# ===================== Funções CRUD =====================

def gerar_id(clientes):
    """Gera um novo ID com base no maior existente, validando a duplicidade."""
    new_id = max(c["id"] for c in clientes) + 1 if clientes else 1
    while verificar_id_existe(new_id, clientes):
        new_id += 1  # Garantir ID único
    return new_id

# Funções de cadastro para Clientes, Fornecedores e Produtos seguem a mesma lógica

def cadastrar_cliente(clientes):
    """Cadastra um novo cliente com validação de dados."""
    print("\n--- Cadastro de Cliente ---")
    
    nome = input("Nome: ").strip().upper()
    while not nome:
        print("⚠️ Nome não pode ser vazio!")
        nome = input("Nome: ").strip().upper()
    
    cpf = input("CPF: ").strip()
    while not validar_cpf(cpf):
        print("⚠️ CPF inválido! Deve ter 11 dígitos.")
        cpf = input("CPF: ").strip()

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

# Função de listagem, atualização e exclusão seguem a mesma lógica

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
    """Atualiza os dados de um cliente existente com validação de dados."""
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
    """Exclui um cliente pelo ID com confirmação."""
    listar_clientes(clientes)
    try:
        id_excluir = int(input("Digite o ID do cliente a excluir: "))
    except ValueError:
        print("⚠️ ID inválido!")
        return

    for c in clientes:
        if c["id"] == id_excluir:
            confirmacao = input(f"Você tem certeza que deseja excluir o cliente {c['nome']}? (s/n): ").strip().lower()
            if confirmacao == 's':
                clientes.remove(c)
                salvar_clientes(clientes)
                print("🗑️ Cliente excluído com sucesso!\n")
            else:
                print("⚠️ Exclusão cancelada.\n")
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
