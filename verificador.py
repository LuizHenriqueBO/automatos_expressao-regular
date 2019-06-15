import sys
import re

alfabeto_entrada = list(sys.argv[1])

#alfabeto_entrada = alfabeto_entrada[::-1]

print(alfabeto_entrada)

expressao = ['(',')','*','+','.']

pilha = list()

palavra = list()
palavra = alfabeto_entrada[:]

subpalavra = list()

lista_ponteiro = list()
posicao_inicio = list()
posicao_fim = list()

posicao = 0
for alfabeto in alfabeto_entrada:
    
    if alfabeto in expressao[0]:
        pilha.append(alfabeto)
        posicao_inicio.append(posicao)
        
        print(" posicao inicio = ", posicao_inicio, " pilha :",pilha)
    
    if alfabeto in expressao[1]:    
        del(pilha[-1])
        posicao_fim.append(posicao)
        
        subpalavra = palavra[posicao_inicio[-1]+1:posicao_fim[0]]
        del(posicao_inicio[-1])
        del(posicao_fim[0])
        #print(posicao inicial)
        ppp = str(alfabeto_entrada)
        jjj = str(subpalavra)
        
        ppp= re.sub(jjj,"",ppp)

        alfabeto_entrada = list(ppp.split().copy())
        print("subpalavra: ",jjj)
        
        subpalavra = []

    posicao +=1
        
