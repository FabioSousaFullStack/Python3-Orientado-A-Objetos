class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
         return f'{self._nome} - {self.ano} - {self.duracao} minutos- {self.likes} likes'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'

class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
palylist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

for programa in filmes_e_series:
    print(programa)