# main.py
from fornecedor import menu as menu_fornecedores
from produto import menu_produtos
from vendas import menu_vendas
from clientes import menu_clientes
import os


def menu_principal():
    try:
        while True:
            print("""
================= MENU PRINCIPAL =================
1 - Fornecedores
2 - Produtos
3 - Clientes
4 - Vendas
5 - Relatórios
0 - Voltar
==================================================
""")
            opcao = input("Escolha uma opção: ").strip()

            # Verificando se a opção é válida
            if opcao not in ["1", "2", "3", "4", "5", "0"]:
                print("\n❌ Opção inválida! Tente novamente.\n")
                continue

            # Tratando as opções do menu
            if opcao == "1":
                try:
                    menu_fornecedores()
                except Exception as e:
                    print(f"⚠️ Erro ao acessar Fornecedores: {e}")
                
            elif opcao == "2":
                try:
                    menu_produtos()
                except Exception as e:
                    print(f"⚠️ Erro ao acessar Produtos: {e}")
                    
            elif opcao == "3":
                try:
                    menu_clientes()
                except Exception as e:
                    print(f"⚠️ Erro ao acessar Clientes: {e}")
                    
            elif opcao == "4":
                try:
                    menu_vendas()
                except Exception as e:
                    print(f"⚠️ Erro ao acessar Vendas: {e}")
                    
            elif opcao == "5":
                print("\n📊 Relatórios ainda não implementados.\n")

            elif opcao == "0":
                print("\n👋 Saindo do sistema... Até mais!\n")
                break

    except KeyboardInterrupt:
        print("\n🛑 O sistema foi interrompido pelo usuário. Até logo!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}. Tente novamente mais tarde.")

if __name__ == "__main__":
    menu_principal()
