import sys
import string
#pl = sys.argv[1]
x = 0
minhapl = 'ab(c)*(aa(g(j)*)s+d)*b+bb(aa+s)*+p(ll)+pl+llllllll+l'
#minhapl = 'aa+b(c*)+ff+gk*'
lo = list()
popo = list()
ou = False
cont = 0


for i in range(len(minhapl)):
    lo.append(minhapl[i])
    if minhapl[i] == '(':
        x += 1

    elif minhapl[i] == ')':
        x -= 1

        if x == 0 and i+1 < len(minhapl)and minhapl[i+1] != '*':
            popo.append(lo.copy())
            lo.clear()

        if x == 0 and i == len(minhapl)-1:
            popo.append(lo.copy())
            lo.clear()

    elif x == 0 and minhapl[i] == '*' and ou == False and cont!=0:
        popo.append(lo.copy())
        lo.clear()

    elif minhapl[i] == '+':
        if x == 0:
            ou = True
            w = list()

            if len(lo) > 1:
                w = list(lo.pop())
                popo.append(lo.copy())

            else:
                w = lo.copy()
            popo.append(w.copy())
            lo.clear()
            cont += 1

    elif len(lo) == 1 and x == 0 and ou == False and cont!=0:
        popo.append(lo.copy())
        lo.clear()

    elif i == len(minhapl)-1:
        popo.append(lo.copy())
        lo.clear()


#minhapl = [i.replace('(aas)','') for i in minhapl]
for i in popo:
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
