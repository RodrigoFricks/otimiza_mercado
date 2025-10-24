from vendas import VendasCRUD
import crud_produto 

def menu_vendas():
    vendas_crud = VendasCRUD()
    while True:
        print("""
==== MENU VENDAS ====
1. Cadastrar Venda
2. Listar Vendas
3. Atualizar Venda
4. Deletar Venda
0. Voltar
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vendas_crud.cadastrar_venda()
        elif opcao == "2":
            vendas_crud.listar_vendas()
        elif opcao == "3":
            vendas_crud.atualizar_venda()
        elif opcao == "4":
            vendas_crud.deletar_venda()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")


def main():
    while True:
        print("""
======== MENU PRINCIPAL ========
1. Fornecedores
2. Produtos
3. Clientes
4. Vendas
5. Relatórios
0. Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n🔧 Módulo de Fornecedores ainda não implementado.\n")
            # menu_fornecedores()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            print("\n🔧 Módulo de Clientes ainda não implementado.\n")
            # menu_clientes()
        elif opcao == "4":
            menu_vendas()
        elif opcao == "5":
            print("\n📊 Relatórios ainda não implementados.\n")
        elif opcao == "0":
            print("\n👋 Saindo do sistema... Até mais!")
            break
        else:
            print("\n❌ Opção inválida!\n")

def menu_produtos():
    
    while True:
        print("\n--- MENU PRODUTOS ---")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n-- CADASTRO DE PRODUTO --")
            try:
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
                fornecedor_id = int(input("ID do Fornecedor: "))
                crud_produtos.cadastrar_produto(nome, preco, estoque, fornecedor_id)
            except ValueError:
                print("ERRO: Preço, Estoque e ID devem ser números.")

        elif opcao == '2':
            crud_produtos.listar_produtos()
        
        elif opcao == '3':
            try:
                id_alvo = int(input("ID do Produto para atualizar: "))
                nome = input("Novo Nome: ")
                preco = float(input("Novo Preço: "))
                estoque = int(input("Nova Quantidade em Estoque: "))
                fornecedor_id = int(input("Novo ID do Fornecedor: "))
                crud_produtos.atualizar_produto(id_alvo, nome, preco, estoque, fornecedor_id)
            except ValueError:
                print("ERRO: ID, Preço, Estoque e ID Fornecedor devem ser números.")

        elif opcao == '4':
            try:
                id_alvo = int(input("ID do Produto para deletar: "))
                crud_produtos.deletar_produto(id_alvo)
            except ValueError:
                print("ERRO: O ID deve ser um número.")

        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
menu_produtos()
if __name__ == "__main__":
    main()