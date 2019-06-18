from estado import *
from transicao import *


class Automato(object):
    def __init__(self):
        self.lista_transicao  = list()
        self.lista_estado     = list()
        self.inicio           = Estado('q0')
        self.fim              = Estado('q1')
        self.alfabeto         = list()
        self.branco           = 'E'




    def criar_automato(self, nome):
        if(nome != None):
            if(nome != self.branco):
                self.inicio = Estado('q0')
                self.fim    = Estado('q1')
                transicao = Transicao(self.inicio, nome, self.fim)
                self.lista_transicao = [transicao]
                self.lista_estado = [self.inicio, self.fim]
                self.alfabeto = [transicao.nome]
                return True
            else:
                print("erro: nome esta sendo utilizado como caracter branco")
                return False
        else:
            print("erro: nome não informado")
            return False




    def add_estado(self, nome_estado):
        for estado in self.lista_estado:
            if(estado.get_estado_nome() == nome_estado):
                return estado
        estado = Estado(nome_estado)
        self.lista_estado.append(estado)
        return estado

    
    def add_transicao(self, origem, nome_trasicao, destino):
        if(self.verifica_origem_e_destino_da_transicao(origem, destino) == False):
            _origem = self.add_estado(origem)
            _destino = self.add_estado(destino)
            transicao = Transicao(_origem, nome_trasicao, _destino)
            self.lista_transicao.append(transicao)
            if(transicao.nome != self.branco):
                if(transicao.nome not in self.alfabeto):
                    self.alfabeto.append(transicao.nome)    
            return True
        
        return False



    # verifico se a origem e destino já existem no grafo
    def verifica_origem_e_destino_da_transicao(self, origem, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem.nome == origem) and (transicao.destino.nome == destino)):
                return True
        return False
    

    def set_automato_final(self, final):
        self.fim = Estado(final)
    
    def set_automato_inicial(self, inicio):
        self.inicio = Estado(inicio)

    def get_automato_final(self):
        return self.fim
    
    def get_automato_inicio(self):
        return self.inicio


    def imprimir_automato(self):
        print(self.alfabeto)
        print(self.branco)
        print(self.inicio.nome)
        print(self.fim.nome)
        for estados in self.lista_estado:
            print(estados.nome, end =" ")
        print("")
        for i in self.lista_transicao:
            print(f'[{i.origem.nome} {i.nome} {i.destino.nome}]')
        print("\n")

    


# aut = Automato()
# aut2 = Automato()

# aut.add_transicao('q0','a','q2')
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




