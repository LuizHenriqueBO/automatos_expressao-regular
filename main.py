from automato import *

def renomeia_estados_automato(automato1, automato2):
    qtd = len(automato1.lista_estado)
    automato = Automato()
    for i in automato2.lista_transicao:
        automato.add_transicao(automato.letra_estado+str(qtd + int(i.origem[1:])), i.nome, automato.letra_estado+str(qtd + int(i.destino[1:])))
    automato.inicio = automato.letra_estado+str(qtd + int(automato2.inicio[1:]))
    return automato


def concatenacao(automato1, automato2): 
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato2 = renomeia_estados_automato(automato, automato2)
        automato.add_transicao(automato1.fim, automato.branco, automato2.inicio)
        for i in automato2.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False


def uniao(automato1, automato2): 
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()
        automato1 = renomeia_estados_automato(automato,automato1)
        automato.add_transicao(automato.inicio, automato.branco, automato1.inicio)
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato2 = renomeia_estados_automato(automato1, automato2)
        automato.add_transicao(automato.inicio, automato.branco,automato2.inicio)
        for i in automato2.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato.add_estado(automato.letra_estado + str(1+int(automato2.fim[1:])))
        automato.add_transicao(automato1.fim, automato.branco, automato.fim)
        automato.add_transicao(automato2.fim, automato.branco, automato.fim)            
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False


def fecho_kleene(automato1):
    if(type(automato1) is Automato):
        automato = Automato()
        automato1 = renomeia_estados_automato(automato, automato1)
        automato.add_transicao(automato.inicio, automato.branco, automato1.inicio)
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato.add_transicao(automato1.fim, automato.branco, automato1.inicio)
        automato.add_estado(automato.letra_estado + str(1+(int(automato1.fim[1:]))))
        automato.add_transicao(automato1.fim, automato.branco, automato.fim)
        automato.add_transicao(automato.inicio, automato.branco, automato.fim)
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False