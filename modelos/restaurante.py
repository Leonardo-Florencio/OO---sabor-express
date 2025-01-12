from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    #utilizar o def __init__ para ser um construtor - Ou seja, quando o objeto for definido, deve ter as próprias informações
    #def é usado para definir o init como construtor
    #self é a referência à instância utilizada no momento, ou seja, permite entender que é daquela instância. É o padrão utilizado em python
    #nome e categoria, nesse caso, se tornam os requisitos obrigatórios a serem definidos
    #Dessa forma, se tentar criar um objeto sem essas informações, o código vai retornar um erro esperando por essa informação
    def __init__(self, nome, categoria):
        self._nome = nome.title() #o método de string title() é utilizado para deixar a primeira letra maiúscula, mostrando que não é necessario usar um property pra esse tipo de coisa
        self._categoria = categoria
        self._ativo = False #utilização do underline _ é para indicar que é um atributo privado, que não deve ser acessado
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #método append utilizado para que, cada instância da classe quando criada, seja adicionada no array restaurantes[]
    # utilizado o método __str__ para que ele apresente o objeto em forma de texto. Ele deve receber um retorno, que irá buscar as informações dos atributos daquela instância para devolver em formato de texto 
    # como o método retorna string, é possível utilizar f-string para "estilizar" o retorno do texto 
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod #@classmethod é para mostrar que o método é da Classe e não do Objeto que foi criado como instância. Coloca-se também 'cls" no argumento da função, como uma convenção
    def listar_restaurantes(cls): #método criado para listar os restaurantes contidos no array restaurantes[]. O for procura por restaurante dentro do array da classe e, para cada um, printa seu nome, categoria e ativo no f'string definido
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    #property é um decorator e é acessado por arroba @. O property permite modificar a forma como uma informação é lida - Ao invés de FALSE boolean, retornar, nesse cenário, inativo
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
#na hora de declarar o objeto, basta colocar seus atributos na ordem em que foram definidos no self do construtor
#restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('pizza express', 'Italiana')

#Ao usar o método dir() conseguimos enxergar todas as informações relacionados ao objeto da classe, desde os métodos padrão até os atributos definidos pelo desenvolvedor
#Ao usar o método vars() conseguimos enxergar todas as informações contidas nos atributos definidos

#Restaurante.listar_restaurantes()


