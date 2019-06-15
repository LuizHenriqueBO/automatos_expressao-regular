class transformacao():
    
    def __init__(self):
        self.inicio = 0
        self.fim = 1

    def transformacao_basica(self, letra, inicio=None, fim=None):

        if(inicio == None):
            estado_inicio = 'q'+str(self.inicio)
        else:
            estado_inicio = 'q'+str(inicio)

        if(fim == None):
            estado_final  = 'q'+str(self.fim)
        else:
            estado_final = 'q'+str(fim)
            
        automato = [estado_inicio, letra, estado_final]
        
        return automato
        
       


      
    def transformacao_fecho_kleene(self, letra):
        
        automato = list()
        subautomato = self.transformacao_basica(letra, self.inicio+1, self.fim+1)
        estado_inicio = 'q'+str(self.inicio)
        estado_final  = 'q'+str(self.fim+2)

        automato.append(subautomato)
        automato.append([subautomato[2], 'E', subautomato[0]])
        automato.append([estado_inicio, 'E', subautomato[0]])
        automato.append([estado_inicio, 'E', estado_final])
        automato.append([subautomato[2],'E', estado_final])
        return automato


tr = transformacao()

autom = list()
autom = tr.transformacao_fecho_kleene('d')

print(autom)



# a b
# B
# q0 q1 q2 q3
# q0
# q2
# q0 a q1
# q0 b q0
# q1 a q3
# q1 b q2
# q2 a q3
# q2 b q2
# q3 a q3
# q3 b q2



