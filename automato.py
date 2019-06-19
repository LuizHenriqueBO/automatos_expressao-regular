from estado import *
from transicao import *


class Automato(object):
    def __init__(self, nome=None):
        if(nome != None):
            self.inicio           =  'q0'
            self.fim              =  'q1'
            self.lista_estado     =  [self.inicio,self.fim]
            transicao             =  Transicao(self.inicio, nome, self.fim)
            self.lista_transicao  =  [transicao]
            self.alfabeto         =  [transicao.nome]
            self.branco           =  'E'
        else:
            self.inicio           =  'q0'
            self.fim              =  ''
            self.lista_estado     =  ['q0']
            self.lista_transicao  =  []
            self.alfabeto         =  []
            self.branco           =  'E'


    # def criar_automato(self, nome):

    #     self.inicio           =  'q0'
    #     self.fim              =  'q1'
    #     self.lista_estado     =  [self.inicio,self.fim]
    #     transicao             =  Transicao(self.inicio, nome, self.fim)
    #     self.lista_transicao  =  [transicao]
    #     self.alfabeto         =  [transicao.nome]
    #     self.branco           =  'E'


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

        #print("transicao ja existe: ", "origem:  ",origem," nome: ", nome, "  destino: ", destino)
        return False


    # verifica se a origem e o destino ja existe na lista de transições
    def verifica_origem_e_destino_da_transicao(self, origem, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem == origem) and (transicao.destino == destino)):
                return True
        return False
    

    # def set_automato_final(self, final):
    #     self.fim = Estado(final)
    
    # def set_automato_inicial(self, inicio):
    #     self.inicio = Estado(inicio)

    # def get_automato_final(self):
    #     return self.fim
    
    # def get_automato_inicio(self):
    #     return self.inicio


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

    


# aut = Automato()
# ##aut2 = Automato()

# # aut = aut.criar_automato('a')
# # # aut.criar_automato
# aut.add_transicao('q0','a','q2')
# aut.imprimir_automato()
# aut.add_transicao('q3','E','q4')
# aut.add_transicao('q2','b','q3')
# aut.add_transicao('q2','b','q3')
# aut.set_automato_inicial('q0')
# aut.set_automato_final('q4')


# aut2.add_transicao('e2','b','e3')
# aut2.set_automato_final('e3')
# aut2.set_automato_inicial('e2')


# aut.imprimir_automato()
# aut2.imprimir_automato()




