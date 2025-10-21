import json
import os

# Caminho do arquivo onde as vendas serão armazenadas
ARQUIVO_VENDAS = os.path.join("dados", "vendas.json")


class Venda:
    def __init__(self, id_venda, id_cliente, id_produto, quantidade, valor_total):
        self.id_venda = id_venda
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.valor_total = valor_total

    def to_dict(self):
        return {
            "id_venda": self.id_venda,
            "id_cliente": self.id_cliente,
            "id_produto": self.id_produto,
            "quantidade": self.quantidade,
            "valor_total": self.valor_total,
        }


class VendasCRUD:
    def __init__(self):
        os.makedirs("dados", exist_ok=True)
        if not os.path.exists(ARQUIVO_VENDAS):
            with open(ARQUIVO_VENDAS, "w") as f:
                json.dump([], f)

    def carregar_vendas(self):
        with open(ARQUIVO_VENDAS, "r") as f:
            return json.load(f)

    def salvar_vendas(self, vendas):
        with open(ARQUIVO_VENDAS, "w") as f:
            json.dump(vendas, f, indent=4)

    def cadastrar_venda(self):
        vendas = self.carregar_vendas()

        id_venda = len(vendas) + 1
        id_cliente = input("ID do Cliente: ")
        id_produto = input("ID do Produto: ")
        quantidade = int(input("Quantidade: "))
        valor_total = float(input("Valor Total: "))

        venda = Venda(id_venda, id_cliente, id_produto, quantidade, valor_total)
        vendas.append(venda.to_dict())

        self.salvar_vendas(vendas)
        print("\n✅ Venda cadastrada com sucesso!\n")

    def listar_vendas(self):
        vendas = self.carregar_vendas()
        if not vendas:
            print("\n❌ Nenhuma venda cadastrada.\n")
            return

        print("\n📋 Lista de Vendas:")
        for v in vendas:
            print(f"ID: {v['id_venda']} | Cliente: {v['id_cliente']} | Produto: {v['id_produto']} | "
                  f"Qtd: {v['quantidade']} | Total: R${v['valor_total']:.2f}")
        print()

    def atualizar_venda(self):
        vendas = self.carregar_vendas()
        self.listar_vendas()
        id_venda = int(input("Digite o ID da venda a ser atualizada: "))

        for v in vendas:
            if v["id_venda"] == id_venda:
                print("\nDeixe em branco se não quiser alterar o campo.\n")
                novo_cliente = input(f"Novo ID Cliente ({v['id_cliente']}): ") or v["id_cliente"]
                novo_produto = input(f"Novo ID Produto ({v['id_produto']}): ") or v["id_produto"]
                nova_quantidade = input(f"Nova Quantidade ({v['quantidade']}): ")
                novo_valor = input(f"Novo Valor Total ({v['valor_total']}): ")

                v["id_cliente"] = novo_cliente
                v["id_produto"] = novo_produto
                v["quantidade"] = int(nova_quantidade) if nova_quantidade else v["quantidade"]
                v["valor_total"] = float(novo_valor) if novo_valor else v["valor_total"]

                self.salvar_vendas(vendas)
                print("\n✅ Venda atualizada com sucesso!\n")
                return

        print("\n❌ Venda não encontrada.\n")

    def deletar_venda(self):
        vendas = self.carregar_vendas()
        self.listar_vendas()
        id_venda = int(input("Digite o ID da venda a ser deletada: "))

        nova_lista = [v for v in vendas if v["id_venda"] != id_venda]
        if len(nova_lista) == len(vendas):
            print("\n❌ Venda não encontrada.\n")
            return

        self.salvar_vendas(nova_lista)
        print("\n🗑️ Venda deletada com sucesso!\n")


# Permite testar o CRUD de forma independente
if __name__ == "__main__":
    crud = VendasCRUD()

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
            crud.cadastrar_venda()
        elif opcao == "2":
            crud.listar_vendas()
        elif opcao == "3":
            crud.atualizar_venda()
        elif opcao == "4":
            crud.deletar_venda()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")
