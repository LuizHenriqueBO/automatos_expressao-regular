

class Transicao(object):

    def __init__(self, origem, nome, destino):
        self.nome = nome
        self.origem = origem
        self.destino = destino
        

    def get_transicao_nome(self):
        return self.nome

    def get_transicao_origem(self):
        return self.origem
    
    def get_transicao_destino(self):
        return self.destino

 


    def set_transicao_nome(self, nome):
        self.nome = nome

    def set_transicao_origem(self, origem):
        self.origem = origem

    def set_transicao_destino(self, destino):
        self.destino = destino
