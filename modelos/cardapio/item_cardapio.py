from abc import ABC, abstractmethod #import necessário para criação de classe abstrata

class ItemCardapio(ABC): #necessário colocar o ABC no argumento, para que o método abstrato possa ser utilizado
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    #criação de classe abstrata - Siginifica que todas as classes derivadas precisam ter esse método, mas a classe não precisa saber como ele funciona. Esses detalhes são definidos nas classes que recebem herança dessa classe
    # essa habilidade de um método poder ser diferente em diferentes classes se chama polimorfismo
    @abstractmethod
    def aplicar_desconto(self):
        pass