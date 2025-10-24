# main.py
from fornecedor import menu as menu_fornecedores
from produto import menu_produtos
from vendas import menu_vendas
from clientes import menu_clientes


def main():
    while True:
        print("""
================= MENU PRINCIPAL =================
1 - Fornecedores
2 - Produtos
3 - Clientes
4 - Vendas
5 - Relatórios
0 - Sair
==================================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            
            menu_fornecedores()

        elif opcao == "2":
            
            menu_produtos()

        elif opcao == "3":
        
            menu_clientes()

        elif opcao == "4":
            
            menu_vendas()

        elif opcao == "5":
            print("\n📊 Relatórios ainda não implementados.\n")

        elif opcao == "0":
            print("\n👋 Saindo do sistema... Até mais!\n")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
