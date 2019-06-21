import os # biblioteca pra usar o método de limpar a tela
from gerenciador import *
from infixa_posfixa import *



# def leitor(file_name):
#     file_reader = open(file_name, 'r');
    
#     file_list = file_reader.readlines()
#     file_list = [ i.replace('\n', '') for i in file_list]
#     file_list = [ i.split(' ') for i in file_list]
    
#     file_reader.close()

#     return file_list


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
        print("[2] Converter ER para AFND")

        print("[3] Converter AFND para AFD")
        print("[4] Minimização de AFD")
        
        print("[5] Imprimir ER")
        print("[6] Imprimir AFND")
        print("[7] Imprimir AFD")
        print("[0] Sair")
        
        opcao = input(">> ")
        if(opcao == '1'):
            alfabeto_entrada = input("Digite o alfabeto de entrada: ")
            alfabeto_entrada = analise_expressao(alfabeto_entrada)
        if(opcao == '2'):
            AFND = converter__ER__AFND(alfabeto_entrada)
        
        
        # if(opcao == '3'):
        # if(opcao == '4'):
        if(opcao == '5'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(alfabeto_entrada)
            input()
        if(opcao == '6'):
            os.system('cls' if os.name == 'nt' else 'clear')
            if(type(AFND) != Automato):
                print("Não foi efetuado a conversão")
            else:
                AFND.imprimir_automato()
            input()
        # if(opcao == '7'):
        
      
if __name__ == '__main__':
	main()