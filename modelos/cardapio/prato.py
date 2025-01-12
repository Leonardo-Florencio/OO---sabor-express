from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #colocando a classe mãe "ItemCardápio" no argumento dessa classe, garante que a classe Prato receba herança da classe mãe, conectando uma a outra
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #super é um objeto especial, que permite acessar os atributos de outra classe a partir de uma classe diferente
        self.descricao = descricao
        
    def __str__(self):
        return self._nome