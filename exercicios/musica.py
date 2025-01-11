class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    def __str__(self):
        return(f'{self.nome} | {self.artista} | {self.duracao}')
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
    
musica_bmth = Musica('Antivist','Bring Me the Horizon',203)
musica_emicida = Musica('Acabou, mas tem...','Emicida',235)
musica_LP = Musica('Casualty','Linkin Park',141)

Musica.listar_musicas()