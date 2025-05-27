from modelos.cardapio.item_cardapio import Item_Cardapio

class Prato(Item_Cardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
