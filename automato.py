from transicao import *

class Automato(object):
    
    def __init__(self, nome=None):
    
        self.letra_estado         =  'q'
        self.inicio               =  self.letra_estado+(str(0))
        self.branco               =  'E'
        if(nome != None):
            self.fim              =  self.letra_estado+(str(1))
            self.lista_estado     =  [self.inicio, self.fim]
            transicao             =  Transicao(self.inicio, nome, self.fim)
            self.lista_transicao  =  [transicao]
            self.alfabeto         =  [transicao.nome]
        else:
            self.fim              =  ''
            self.lista_estado     =  [self.inicio]
            self.lista_transicao  =  []
            self.alfabeto         =  []


    def add_estado(self, nome_estado):
        if(nome_estado in self.lista_estado):
            return False
        self.lista_estado.append(nome_estado)
        self.fim = nome_estado
        return True


    def get_estado(self, nome_estado):
        for estado in self.lista_estado:
            if estado == nome_estado:
                return estado
        return False


    def add_transicao(self, origem, nome, destino):
        if(self.verifica_origem_e_destino_da_transicao(origem, destino) == False):
            if(self.get_estado(origem) == False):
                self.add_estado(origem)
            if(self.get_estado(destino) == False):
                self.add_estado(destino)
            transicao = Transicao(origem, nome, destino)
            self.lista_transicao.append(transicao)
            if(transicao.nome != self.branco):
                if(transicao.nome not in self.alfabeto):
                    self.alfabeto.append(transicao.nome)                
            return True
        return False


    def verifica_origem_e_destino_da_transicao(self, origem, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem == origem) and (transicao.destino == destino)):
                return True
        return False
    

    def imprimir_automato(self):
        print(self.alfabeto)
        print(self.branco)
        print(self.inicio)
        print(self.fim)
        for estados in self.lista_estado:
            print(estados, end =" ")
        print("")
        for i in self.lista_transicao:
            print(f'[{i.origem} {i.nome} {i.destino}]')
        print("\n")
