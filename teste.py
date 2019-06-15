class transformacao():
    
    # def __init__(self):
    #     self.inicio = 0
    #     self.fim = 1



    def transformacao_basica(self, letra):

        estado_inicio = 'q0'
        estado_final  = 'q1'

        automato = list()
        automato.append(letra)
        automato.append('E')
        automato.append([estado_inicio,estado_final])
        automato.append(estado_inicio)
        automato.append(estado_final)
        automato.append([estado_inicio, letra, estado_final])

        return automato



    def transformacao_fecho_kleene(self, letra):

        estado_inicio = 'q0'
        estado_final  = 'q3'

        automato = list()
        automato.append(letra)
        automato.append('E')
        automato.append([estado_inicio,'q1','q2',estado_final])
        automato.append(estado_inicio)
        automato.append(estado_final)
        automato.append(['q0', 'E', 'q1'])
        automato.append(['q1', letra, 'q2'])
        automato.append(['q2', 'E', 'q1'])
        automato.append(['q2', 'E', 'q3'])
        automato.append([estado_inicio,'E', estado_final])

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
autom2 = list()
autom3 = list()

autom = tr.transformacao_basica('d')
autom2 = tr.transformacao_fecho_kleene('d')
#autom3 = tr.transformacao_concatenacao('a','b')

print("\n basico:")
for i in autom:
    print(i)

print("\n fecho de Kleene:")
for i in autom2:
    print(i)

# print("\n concatenacao:")
# for i in autom3:
#     print(i)


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



