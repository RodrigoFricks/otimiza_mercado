class Produto:
    def __init__(self, id_produto, nome, preco, quantidade_estoque, fornecedor_id):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco 
        self.quantidade_estoque = quantidade_estoque
        self.fornecedor_id = fornecedor_id

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade_estoque": self.quantidade_estoque,
            "fornecedor_id": self.fornecedor_id
        }

    def __str__(self):
        return f"ID: {self.id_produto} | Nome: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.quantidade_estoque}"