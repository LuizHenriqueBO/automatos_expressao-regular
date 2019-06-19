from conversor import *
from pilha import *
from main import *
from transicao import *

alfabeto_entrada = '(a.b*+(b.a)*).a.b+c*+(1.5+p)*+(q+r+l).(z*+r.v.m*)*'
alfabeto_pos_fixo = pos_fixo(alfabeto_entrada)
# print(alfabeto_entrada)
# print(alfabeto_pos_fixo)
pilha_alfabeto = Pilha()


for i in range(len(alfabeto_pos_fixo)):
    if(alfabeto_pos_fixo[i] != '.' and alfabeto_pos_fixo[i] != '+' and alfabeto_pos_fixo[i] != '*'):
        automato = Automato(alfabeto_pos_fixo[i])
        pilha_alfabeto.inserir_pilha(automato)
    else:
        if(alfabeto_pos_fixo[i] == '.'):
            dado2 = pilha_alfabeto.get_pilha()
            dado1 = pilha_alfabeto.get_pilha()
            pilha_alfabeto.inserir_pilha(concatenacao(dado1, dado2))
        if(alfabeto_pos_fixo[i] == '+'):
            dado2 = pilha_alfabeto.get_pilha()
            dado1 = pilha_alfabeto.get_pilha()
            pilha_alfabeto.inserir_pilha(uniao(dado1,dado2))
        if(alfabeto_pos_fixo[i] == '*'):
            dado = pilha_alfabeto.get_pilha()
            pilha_alfabeto.inserir_pilha(fecho_kleene(dado))


automato = pilha_alfabeto.get_pilha()
automato.imprimir_automato()

