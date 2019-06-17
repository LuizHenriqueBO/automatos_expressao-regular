from automato import *

class Transformacao():
    def __init__(self):
        self.lista_estados = list()
        self.lista_alfabeto = list()
        self.i = 0



    def transformacao_concatenacao(self, symbol_a, symbol_b, *symbol_n):  
        sub_automato = Automato()
        i = self.i
        sub_automato.set_inicio(f'c{i}')
        sub_automato.adicionar_automato(symbol_a,f'c{i}',f'c{i+1}')
        sub_automato.adicionar_automato(sub_automato.branco,f'c{i+1}',f'c{i+2}')
        sub_automato.adicionar_automato(symbol_b,f'c{i+2}',f'c{i+3}')
        i += 3
        for symbol in symbol_n:
            sub_automato.adicionar_automato(sub_automato.branco,f'c{i}',f'c{i+1}')
            sub_automato.adicionar_automato(symbol,f'c{i+1}',f'c{i+2}')
            i += 2
        sub_automato.set_fim(f'c{i}')
        
        self.i = i
        return sub_automato



    def transformacao_uniao(self, alfabeto):  
        sub_automato = Automato()
        sub_automato.set_inicio('u0')
        sub_automato.set_fim('u5')
        alfabeto = alfabeto.split('+')
        sub_automato.adicionar_automato(sub_automato.branco,'u0','u1')
        sub_automato.adicionar_automato(sub_automato.branco,'u0','u2')
        sub_automato.adicionar_automato(alfabeto[0],'u1','u3')
        sub_automato.adicionar_automato(alfabeto[1],'u2','u4')
        sub_automato.adicionar_automato(sub_automato.branco,'u3','u5')
        sub_automato.adicionar_automato(sub_automato.branco,'u4','u5')

        return sub_automato






    def transformacao_fecho_kleene(self, alfabeto):
        
        sub_automato = Automato()

        sub_automato.set_inicio('K0')
        sub_automato.set_fim('K3')

        sub_automato.adicionar_automato(sub_automato.branco,'K0','K1')

        i = self.i
        if len(alfabeto) > 1:
            for a in alfabeto.split("+"):
                sub_automato.adicionar_automato(a,'K1','K2')

        else:
            sub_automato.adicionar_automato(alfabeto,'K1','K2')
        
        sub_automato.adicionar_automato(sub_automato.branco,'K2','K1')
        sub_automato.adicionar_automato(sub_automato.branco,'K2','K3')        
        sub_automato.adicionar_automato(sub_automato.branco,sub_automato.get_inicio(), sub_automato.get_fim())        

        return sub_automato




tr = Transformacao()
if(tr.lista_alfabeto == []):
    print("vazia")

print("\n fecho de Kleene:")
# kleene = tr.transformacao_fecho_kleene('a.b.c')
#kleene2 = tr.transformacao_fecho_kleene('b')
# kleene.imprimir()
#kleene2.imprimir()


# concatenacao = tr.transformacao_concatenacao(*list('abcde'))
concatenacao = tr.transformacao_concatenacao(*'a.b.c.d.e'.split('.'))

concatenacao.imprimir()

# uniao = tr.transformacao_uniao('a+b')
# uniao.imprimir()



# a b               alfabeto entrada
# E                 palavra vazia
# q0 q1 q2 q3       estados
# q0                estado inicial
# q2                estado final
# q0 a q1           transições
# q0 b q0
# q1 a q3
# q1 b q2
# q2 a q3
# q2 b q2
# q3 a q3
# q3 b q2



