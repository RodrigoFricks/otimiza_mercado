from vendas import VendasCRUD

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
            print("\n🔧 Módulo de Produtos ainda não implementado.\n")
            # menu_produtos()
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


if __name__ == "__main__":
    main()