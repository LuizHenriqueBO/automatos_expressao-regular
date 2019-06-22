import os # biblioteca pra usar o método de limpar a tela
from ER_AFND import *
from infixa_posfixa import *
from AFND_AFD import *

def main():
    print("EXPRESSÃO REGUAR VS AUTOMATOS")
    alfabeto_entrada = ''
    AFND = ''
    AFD = ''
    opcao = -1
    while(opcao != '0'):

        # limpa a tela no Windows ou Linux
        os.system('cls' if os.name == 'nt' else 'clear')

        print("FUNCIONALIDADES: ")
        print("[1] Inserir ER")
        print("[2] Imprimir ER")
        print("[3] Imprimir AFND")
        print("[4] Imprimir AFD")
        #print("[5] Imprimir AFD MINIMIZADO")
        print("[0] Sair")
        
        opcao = input(">> ")
        if(opcao == '1'):                                            # 'a*+c*.(q*.w*.e*)+t*+(m*.y*)+o*'
            # alfabeto_entrada = 'a*+c*.(q*.w*.e*)+t*+(m*.y*)+o*'  
            alfabeto_entrada = input('INSIRA A EXPRESSÃO REGULAR : ')    
            alfabeto_entrada = analise_expressao(alfabeto_entrada)
            AFND = converter__ER__AFND(alfabeto_entrada)
            AFD = conversao_AFND_AFD(AFND)

        if(opcao == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(alfabeto_entrada)
            input()
        if(opcao == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            AFND.imprimir_automato()
            input()
        if(opcao == '4'):
            os.system('cls' if os.name == 'nt' else 'clear')
            AFD.imprimir_automato()
            input()
        # if(opcao == '5'):
        #     os.system('cls' if os.name == 'nt' else 'clear')
            
        #     input()        
      
if __name__ == '__main__':
	main()