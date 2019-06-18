
from automato import *

class Main(object):
    def __init__(self):
        self.qtd = 0
        self.letra_estado = 'q'


    def renomeia_estados_automato(self, automato1, automato2):
        qtd = len(automato1.lista_estado)
        new_automato = Automato()
        for i in automato2.lista_transicao:
            _origem = self.letra_estado+str(qtd + int(i.origem.nome[1]))
            _destino = self.letra_estado+str(qtd + int(i.destino.nome[1]))
            new_automato.add_transicao(_origem,i.nome,_destino)
        _inicio = self.letra_estado+str(qtd + int(automato2.inicio.nome[1]))
        _fim = self.letra_estado+str(qtd + int(automato2.fim.nome[1]))
        new_automato.set_automato_inicial(_inicio)
        new_automato.set_automato_final(_fim)
        return new_automato


    def concatenacao(self, automato1, automato2): 
        if(type(automato1) is Automato) and (type(automato2) is Automato):
            automato = Automato()
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem.nome, i.nome, i.destino.nome)
            automato2 = self.renomeia_estados_automato(automato1, automato2)
            automato.add_transicao(automato1.fim.nome, automato.branco, automato2.inicio.nome)
            for i in automato2.lista_transicao:
                automato.add_transicao(i.origem.nome, i.nome, i.destino.nome)
            automato.set_automato_inicial(automato1.inicio.nome)
            automato.set_automato_final(automato2.fim.nome)

            return automato
        print("\n\n erro, não é autômato\n\n")
        return False


    def uniao(self, automato1, automato2): 
        if(type(automato1) is Automato) and (type(automato2) is Automato):
            automato = Automato()
            # automato1 = automato.criar_automato(automato.branco)
            automato1 = self.renomeia_estados_automato(automato1,automato1)
            automato.add_transicao(automato.inicio.nome, automato.branco, automato1.inicio.nome)
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem.nome, i.nome, i.destino.nome)
            automato2 = self.renomeia_estados_automato(automato1, automato2)
            automato.add_transicao(automato.inicio.nome,automato.branco,automato2.inicio.nome)
            for i in automato2.lista_transicao:
                automato.add_transicao(i.origem.nome, i.nome, i.destino.nome)
            automato.set_automato_final(automato.add_estado(self.letra_estado + str(1+int(automato2.fim.nome[1:]))).nome)
            automato.add_transicao(automato1.fim.nome, automato.branco, automato.fim.nome)
            automato.add_transicao(automato2.fim.nome, automato.branco, automato.fim.nome)            
            return automato
        print("\n\n erro, não é autômato\n\n")
        return False


    def fecho_kleene(self, automato1):
        if(type(automato1) is Automato):
            automato = Automato()
            automato.add_estado('q0')
            automato1 = self.renomeia_estados_automato(automato,automato1)
            automato.add_transicao(automato.inicio.nome, automato.branco, automato1.inicio.nome)
            for i in automato1.lista_transicao:
                automato.add_transicao(i.origem.nome, i.nome, i.destino.nome)

            automato.add_transicao(automato1.fim.nome, automato.branco, automato1.inicio.nome)
            automato.set_automato_inicial(automato.inicio.nome)
            automato.set_automato_final(automato.add_estado(self.letra_estado + str(1+(int(automato1.fim.nome[1:])))).nome)
            automato.add_transicao(automato1.fim.nome, automato.branco, automato.fim.nome)
            automato.add_transicao(automato.inicio.nome, automato.branco, automato.fim.nome)
            return automato
        print("\n\n erro, não é autômato\n\n")
        return False





# teste = Main()

# automato = Automato()
# aut1 = automato.criar_automato('a')
# aut2 = automato.criar_automato('b')
# aut3 = automato.criar_automato('t')
# aut4 = automato.criar_automato('c')
# aut5 = automato.criar_automato('d')

# aut2 = teste.concatenacao(aut2,aut3)
# aut1 = teste.concatenacao(aut1,aut2)

# aut3 = teste.concatenacao(aut4,aut5)
# aut3 = teste.fecho_kleene(aut3)

# aut1 = teste.uniao(aut1,aut3)

# # aut1 = teste.concatenacao(aut4,aut5)

# aut1.imprimir_automato()


# automato = teste.concatenacao(aut,aut2)


# exp = "a.b.c.d+a.b"
# group = exp.split("+")
# first = group.pop(0).split(".")
# aut.add_transicao('q0',first.pop(0),'q1')
# for s in first:
#     aut2 = Automato()
#     aut2.add_transicao("x", s, "y")
#     aut = teste.concatenacao(aut, aut2)

# if group:

#     for exp in group:

# aut = teste.concatenacao(aut, aut2)

# aut.imprimir_automato()


    # automato = teste.uniao(aut,aut2)
    # automato.imprimir_automato()
# aut3.add_transicao('q0','c','q1')
# aut4.add_transicao('q0','d','q1')
# aut5.add_transicao('q0','e','q1')
# aut6.add_transicao('q0','f','q1')

# automato = teste.concatenacao(aut, aut2)
# automato2 = teste.concatenacao(aut3, aut4)
# automato3 = teste.concatenacao(aut5, aut6)


# automato_1 = teste.concatenacao(automato,automato2)
# automato_total = teste.concatenacao(automato_1,automato3)
# automato.imprimir_automato()
