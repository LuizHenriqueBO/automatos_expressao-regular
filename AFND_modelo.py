from transicao import *
from itertools import chain


class Automato:
    
    def __init__(self, nome=None):
        self.letra_estado         =  'q'
        self.inicio               =  self.letra_estado+(str(0))        
        if(nome != None):
            self.lista_fim        =  [self.letra_estado+(str(1))]
            self.lista_estado     =  [self.inicio, self.lista_fim[0]]
            transicao             =  Transicao(self.inicio, nome, self.lista_fim[0])
            self.lista_transicao  =  [transicao]
            self.alfabeto         =  [transicao.nome]
        else:
            self.lista_estado     =  []
            self.lista_transicao  =  list()
            self.alfabeto         =  list()
            self.lista_fim        =  list()



    @staticmethod
    def epsilon():
        return 'E'


    def add_estado(self, nome_estado):
        if(nome_estado in self.lista_estado):
            return False
        self.lista_estado.append(nome_estado)
        self.lista_fim = [nome_estado]
        return True


    def get_estado(self, nome_estado):
        for estado in self.lista_estado:
            if estado == nome_estado:
                return estado
        return False


    def add_transicao(self, origem, nome, destino):
        if isinstance(origem, int):
            origem = self.letra_estado+str(origem)
        if isinstance(destino, int):
            destino = self.letra_estado+str(destino)
        if(self.verifica_origem_e_destino_da_transicao(origem, nome, destino) == False):
            if(self.get_estado(origem) == False):
                self.add_estado(origem)
            if(self.get_estado(destino) == False):
                self.add_estado(destino)
            transicao = Transicao(origem, nome, destino)
            self.lista_transicao.append(transicao)
            if(transicao.nome != self.epsilon()):
                if(transicao.nome not in self.alfabeto):
                    self.alfabeto.append(transicao.nome)                
            return True
        return False


    def verifica_origem_e_destino_da_transicao(self, origem, nome, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem == origem) and (transicao.destino == destino) and (transicao.nome == nome)):
                return True
        return False
    

    def imprimir_automato(self):
        print(self.alfabeto)
        print(self.epsilon())
        print(self.inicio)
        for i in self.lista_fim:
            print(f'{i} ',end='')
        print() 
        for estados in self.lista_estado:
            print(estados, end =" ")
        print("")
        for i in self.lista_transicao:
            print(f'[{i.origem} {i.nome} {i.destino}]')
        print("\n")


    
    def get_transicao_destino(self, estado, palavra):

        transicoes = {}
        for i in range(len(self.lista_transicao)):
            origem = self.lista_transicao[i].origem
            destino = self.lista_transicao[i].destino
            nome = self.lista_transicao[i].nome
            if not transicoes.get(origem):
                transicoes[origem] = {}
            if not transicoes[origem].get(nome):
                transicoes[origem][destino] = {nome}
            else:
                transicoes[origem][destino].update([nome])

        if isinstance(estado, int): # mudar pra list
            estado = [estado]       
        todos_estados = set()
        for estado in estado:
            if estado in transicoes:
                for transicao in transicoes[estado]:
                    if palavra in transicoes[estado][transicao]:
                        todos_estados.add(transicao)
        return set(todos_estados)


    def get_estados_epsilon(self, estado_origem):
        
        transicoes = {}
        for i in range(len(self.lista_transicao)):
            origem = self.lista_transicao[i].origem
            destino = self.lista_transicao[i].destino
            nome = self.lista_transicao[i].nome
            if not transicoes.get(origem):
                transicoes[origem] = {}
            if not transicoes[origem].get(nome):
                transicoes[origem][destino] = {nome}
            else:
                transicoes[origem][destino].update([nome])

        todos_estados = set()
        origens = set([estado_origem])
        while len(origens) != 0:
            origem = origens.pop()
            todos_estados.add(origem)
            if origem in transicoes:
                for destino in transicoes[origem]:
                    if Automato.epsilon() in transicoes[origem][destino] and nome not in todos_estados:
                        origens.add(destino)
        return todos_estados




# aut = Automato('a')

# aut.add_transicao('q0','E','q2')
# aut.add_transicao('q0','E','q3')
# aut.add_transicao('q0','E','q4')
# aut.add_transicao('q2','E','q5')
# aut.add_transicao('q5','E','q6')
# aut.add_transicao('q5','E','q8')

# aut.imprimir_automato()

# print(aut.get_estados_epsilon2('q0'))
