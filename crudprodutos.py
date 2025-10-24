import json
from produto import Produto 

ARQUIVO = 'dados_produtos.json'

def _ler_dados():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def _salvar_dados(dados):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4) 

def _gerar_novo_id(dados):
    if not dados:
        return 1
    return max(item['id_produto'] for item in dados) + 1

def cadastrar_produto(nome, preco, quantidade_estoque, fornecedor_id):
    dados = _ler_dados()
    novo_id = _gerar_novo_id(dados)
    novo_produto_obj = Produto(novo_id, nome, preco, quantidade_estoque, fornecedor_id)
    dados.append(novo_produto_obj.to_dict())
    _salvar_dados(dados)
    print(f"\n✅ Produto '{nome}' (ID: {novo_id}) cadastrado com sucesso.")

def listar_produtos():
    dados = _ler_dados()
    if not dados:
        print("\n Nenhum produto cadastrado.")
        return
    
    print("\n--- LISTA DE PRODUTOS ---")
    for produto_dict in dados:
        print(Produto(**produto_dict))

def atualizar_produto(id_alvo, novo_nome, novo_preco, nova_quantidade, novo_fornecedor_id):
    dados = _ler_dados()
    encontrado = False
    for produto in dados:
        if produto['id_produto'] == id_alvo:
            produto['nome'] = novo_nome
            produto['preco'] = novo_preco
            produto['quantidade_estoque'] = nova_quantidade
            produto['fornecedor_id'] = novo_fornecedor_id
            encontrado = True
            break
            
    if encontrado:
        _salvar_dados(dados)
        print(f"\n Produto ID {id_alvo} atualizado com sucesso.")
    else:
        print(f"\n Erro: Produto com ID {id_alvo} não encontrado.")

def deletar_produto(id_alvo):
    dados_atuais = _ler_dados()
    dados_apos_delecao = [p for p in dados_atuais if p['id_produto'] != id_alvo]

    if len(dados_atuais) > len(dados_apos_delecao):
        _salvar_dados(dados_apos_delecao)
        print(f"\n Produto ID {id_alvo} deletado com sucesso.")
    else:
        print(f"\n Erro: Produto com ID {id_alvo} não encontrado.")