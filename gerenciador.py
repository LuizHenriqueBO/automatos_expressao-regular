

from conversor import *
from pilha import *
from main import *
from transicao import *

transformacao = Main()
alfabeto_entrada = 'a.(b+t)*+(c+(d+e)*)+g.h*'
alfabeto_pos_fixo = pos_fixo(alfabeto_entrada)
print(alfabeto_pos_fixo)
pilha_alfabeto = Pilha()



for i in range(len(alfabeto_pos_fixo)):
    if(alfabeto_pos_fixo[i] != '.' and alfabeto_pos_fixo[i] != '+' and alfabeto_pos_fixo[i] != '*'):
        automato = Automato(alfabeto_pos_fixo[i])
        pilha_alfabeto.inserir_pilha(automato)
    
    if(alfabeto_pos_fixo[i] == '.'):
        dado2 = pilha_alfabeto.get_pilha()
        dado1 = pilha_alfabeto.get_pilha()
        pilha_alfabeto.inserir_pilha(transformacao.concatenacao(dado1,dado2))
    
    if(alfabeto_pos_fixo[i] == '+'):
        dado2 = pilha_alfabeto.get_pilha()
        dado1 = pilha_alfabeto.get_pilha()
        pilha_alfabeto.inserir_pilha(transformacao.uniao(dado1,dado2))

    if(alfabeto_pos_fixo[i] == '*'):
        dado = pilha_alfabeto.get_pilha()
        pilha_alfabeto.inserir_pilha(transformacao.fecho_kleene(dado))

    print("-------------------nova pilha: ----------------------------")
    print(alfabeto_pos_fixo)
    pilha_alfabeto.imprimir_pilha()
    print("-----------------------------------------------------------")

automato = pilha_alfabeto.get_pilha()
automato.imprimir_automato()

