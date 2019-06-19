from automato import *

class Main(object):
    def __init__(self):
        self.qtd = 0
        self.letra_estado = 'q'


    def renomeia_estados_automato(self, automato1, automato2):
        qtd = len(automato1.lista_estado)
        new_automato = Automato()
        for i in automato2.lista_transicao:
            _origem = self.letra_estado+str(qtd + int(i.origem[1:]))
            _destino = self.letra_estado+str(qtd + int(i.destino[1:]))
            new_automato.add_transicao(_origem,i.nome,_destino)
        _inicio = self.letra_estado+str(qtd + int(automato2.inicio[1:]))
        new_automato.inicio = _inicio
        return new_automato


    def concatenacao(self, automato1, automato2): 
        if(type(automato1) is Automato) and (type(automato2) is Automato):
            automato = Automato()
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem, i.nome, i.destino)
            automato2 = self.renomeia_estados_automato(automato, automato2)
            automato.add_transicao(automato1.fim, automato.branco, automato2.inicio)
            for i in automato2.lista_transicao:
                automato.add_transicao(i.origem, i.nome, i.destino)

            return automato
        print("\n\n erro, não é autômato\n\n")
        return False


    def uniao(self, automato1, automato2): 
        if(type(automato1) is Automato) and (type(automato2) is Automato):
            automato = Automato()
            automato1 = self.renomeia_estados_automato(automato,automato1)
            automato.add_transicao(automato.inicio, automato.branco, automato1.inicio)
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem, i.nome, i.destino)
            automato2 = self.renomeia_estados_automato(automato1, automato2)
            automato.add_transicao(automato.inicio, automato.branco,automato2.inicio)
            for i in automato2.lista_transicao:
                automato.add_transicao(i.origem, i.nome, i.destino)
            automato.add_estado(self.letra_estado + str(1+int(automato2.fim[1:])))
            automato.add_transicao(automato1.fim, automato.branco, automato.fim)
            automato.add_transicao(automato2.fim, automato.branco, automato.fim)            
            return automato
        print("\n\n erro, não é autômato\n\n")
        return False



    def fecho_kleene(self, automato1):
        if(type(automato1) is Automato):
            automato = Automato()
            automato1 = self.renomeia_estados_automato(automato, automato1)
            automato.add_transicao(automato.inicio, automato.branco, automato1.inicio)
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem, i.nome, i.destino)
            automato.add_transicao(automato1.fim, automato.branco, automato1.inicio)
            automato.add_estado(self.letra_estado + str(1+(int(automato1.fim[1:]))))
            automato.add_transicao(automato1.fim, automato.branco, automato.fim)
            automato.add_transicao(automato.inicio, automato.branco, automato.fim)
            return automato
        print("\n\n erro, não é autômato\n\n")
        return False