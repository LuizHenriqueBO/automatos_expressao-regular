
from automato import *
class Pilha(object):
    def __init__(self):
        self.tamanho = 0
        self.dado    = list()


    def get_pilha(self):
        self.tamanho -=1
        return self.dado.pop()


    def inserir_pilha(self, elemento):
        self.dado.append(elemento)
        self.tamanho +=1

