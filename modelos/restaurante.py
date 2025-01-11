class Restaurante:
    #utilizar o def __init__ para ser um construtor - Ou seja, quando o objeto for definido, deve ter as próprias informações
    #def é usado para definir o init como construtor
    #self é a referência à instância utilizada no momento, ou seja, permite entender que é daquela instância. É o padrão utilizado em python
    #nome e categoria, nesse caso, se tornam os requisitos obrigatórios a serem definidos
    #Dessa forma, se tentar criar um objeto sem essas informações, o código vai retornar um erro esperando por essa informação
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    # utilizado o método __str__ para que ele apresente o objeto em forma de texto. Ele deve receber um retorno, que irá buscar as informações dos atributos daquela instância para devolver em formato de texto 
    # como o método retorna string, é possível utilizar f-string para "estilizar" o retorno do texto 
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
#na hora de declarar o objeto, basta colocar seus atributos na ordem em que foram definidos no self do construtor
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

#Ao usar o método dir() conseguimos enxergar todas as informações relacionados ao objeto da classe, desde os métodos padrão até os atributos definidos pelo desenvolvedor
#Ao usar o método vars() conseguimos enxergar todas as informações contidas nos atributos definidos

print(restaurante_praca)
print(restaurante_pizza)


