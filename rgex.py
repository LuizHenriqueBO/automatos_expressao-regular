import sys
import string
#pl = sys.argv[1]
num_parenteses = 0
#expressao = 'aba+c*+l'
expressao = 'a*ab(a+b+c*)ff(g)*iok*n*'
sub_xprs = list()
full_xprs = list()
ou = False


for i in range(len(expressao)):

    sub_xprs.append(expressao[i])
    '''adiciona o simbolo na sub expressao'''

    if expressao[i] == '(':
        '''se o simbolo for abre parenteses'''
        num_parenteses += 1

    elif expressao[i] == ')':
        '''se o simbolo for fecha parenteses'''
        num_parenteses -= 1

        if num_parenteses == 0 and i == len(expressao)-1:
            '''se nao estiver entre parenteses, e for o ultimo simbolo'''
            if ou == True:
                full_xprs.append(sub_xprs.copy())
            else:
                if len(full_xprs)>0:
                    full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
                else:
                    full_xprs.append(sub_xprs.copy())
            '''expressao completa recebe a sub expressao ate o fecha parenteses'''
            sub_xprs.clear()
            '''apaga a sub expressao'''

    elif expressao[i] == '*' and i-1 >= 0 and expressao[i-1] != ')' and ou == False:
        '''se nao estiver entre parenteses, o simbolo for * , simbolo anterior nao for fecha parenteses, e nao estiver em uniao externa'''
        h = list()
        h.append(sub_xprs.pop())
        '''h recebe simbolo *'''
        if len(sub_xprs)>0:
            h.append(sub_xprs.pop())
            '''h recebe simbolo antes do simbolo *'''
        h.reverse()
        '''inverte a ordem de h'''
        sub_xprs.append(h.copy())
        '''h adicionado em sub expressao'''
        if ou == False and len(sub_xprs) > 0:
            '''se nao estiver em uniao externa e houver sub expressao para adicionar'''
            if len(full_xprs)>0:
                full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
            else:
                full_xprs.append(sub_xprs.copy())
            '''expressao completa recebe sub expressao'''
        sub_xprs.clear()
        '''apaga a sub expressao'''

    elif num_parenteses == 0 and expressao[i] == '*' and ou == False :
        '''se nao estiver entre parenteses, simbolo for * e nao estiver em uniao externa'''
        if len(full_xprs)>0:
            full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
        else:
            full_xprs.append(sub_xprs.copy())
        '''expressao completa recebe a sub expressao ate o fecha parenteses'''
        sub_xprs.clear()
        '''apaga a sub expressao'''
    
    elif num_parenteses == 0 and expressao[i] == '*' and ou == True:
        if len(full_xprs)>0:
            full_xprs.append(sub_xprs.copy())
        else:
            full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
        sub_xprs.clear()
        

    elif expressao[i] == '+':
        '''se simbolo for +'''
        if num_parenteses == 0:
            '''se nao estiver entre parenteses'''
            ou = True

            w = list(sub_xprs.pop()) 
            '''w recebe simbolo +'''
            if len(sub_xprs) > 1:
                '''se havia simbolos para salvar antes do +'''
                if len(full_xprs)>0 and'+' not in full_xprs[len(full_xprs)-1] :
                    full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
                else:
                    full_xprs.append(sub_xprs.copy())
                '''expressao completa recebe o resto da sub expressao'''

            full_xprs.append(w.copy()) 
            '''expressao completa recebe simbolo +'''
            sub_xprs.clear() 
            '''apaga sub expressao'''
        else:
            ou=False

    elif num_parenteses == 0 and ou ==True and '+' not in full_xprs[len(full_xprs)-1] :
        '''simbolo unico fora de parenteses'''
        ''' se for um unico simbolo, nao estiver entre parenteses e estiver em uniao externa'''
        if len(full_xprs)>0 and expressao[i+1]!='*':
            full_xprs[len(full_xprs)-1]+=sub_xprs
        else:
            full_xprs.append(sub_xprs.copy())
        '''expressao completa recebe a sub expressao ate o fecha parenteses'''
        sub_xprs.clear()
        '''apaga a sub expressao'''

    elif i==len(expressao)-1:
        '''se for o ultimo simbolo da expressao'''
        if ou == True:
            full_xprs.append(sub_xprs.copy())
        else:
            full_xprs[len(full_xprs)-1]+=sub_xprs.copy()
        '''expressao completa recebe a sub expressao ate o fecha parenteses'''
        sub_xprs.clear()
        '''apaga a sub expressao'''
    


#expressao = [i.replace('(aas)','') for i in expressao]
for i in full_xprs:
    print(i)

'''
class transformacao():
    
    # def __init__(self):
    #     self.inicio = 0
    #     self.fim = 1

    def transformacao_basica(self, letra, inicio=None, fim=None):

        if(inicio == None):
            estado_inicio = 'q0'
        else:
            estado_inicio = 'q'+str(inicio)

        if(fim == None):
            estado_final  = 'q1'
        else:
            estado_final = 'q'+str(fim)
        
        automato = list()
        automato.append(letra)
        automato.append('E')
        automato.append([estado_inicio,estado_final])
        automato.append(estado_inicio)
        automato.append(estado_final)
        automato.append([estado_inicio, letra, estado_final])
        
        return automato
        
       


      
    def transformacao_fecho_kleene(self, letra):
        
        subautomato = self.transformacao_basica(letra, self.inicio+1, self.fim+1)
        estado_inicio = 'q'+str(self.inicio)
        estado_final  = 'q'+str(self.fim+2)

        automato = list()
        automato.append(subautomato)
        automato.append([subautomato[2], 'E', subautomato[0]])
        automato.append([estado_inicio, 'E', subautomato[0]])
        automato.append([estado_inicio, 'E', estado_final])
        automato.append([subautomato[2],'E', estado_final])

        return automato


    def transformacao_concatenacao(self, letra1, letra2):
        automato = list()
        subautomato1 = self.transformacao_basica(letra1, self.inicio, self.fim)
        automato.append(subautomato1)
        estado_final  = 'q'+str(self.fim+1)
        automato.append([subautomato1[2], 'E', estado_final])
        subautomato2 = self.transformacao_basica(letra2, self.fim+1, self.fim+2)
        automato.append(subautomato2)
        
        return automato


tr = transformacao()

autom = list()
autom = tr.transformacao_basica('d')
# autom = tr.transformacao_concatenacao('a','b')

for i in autom:
    print(i)



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
'''
