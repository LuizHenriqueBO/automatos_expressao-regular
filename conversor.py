


def busca_dados(pilha):
    return len(pilha) and pilha[len(pilha) - 1]


operador_precedente = {'+': 0,'.': 1,'*': 2}


def pos_fixo(expressao):
    saida = ''
    operador_pilha = []

    for token in expressao:
        if (token == '.' or token == '+' or token == '*'):
            while(len(operador_pilha) and busca_dados(operador_pilha) != '(' and operador_precedente[busca_dados(operador_pilha)] >= operador_precedente[token]):
                saida += operador_pilha.pop()
            operador_pilha.append(token)

        elif (token == '(' or token == ')'):
            if(token == '('):
                operador_pilha.append(token)
            else:
                while(busca_dados(operador_pilha) != '('):
                    saida += operador_pilha.pop()
                operador_pilha.pop()
            
        else:
            saida += token
        
    

    while(len(operador_pilha)):
        saida += operador_pilha.pop()

    return saida


# c = 'a.(b.t)+(c.d)*'
# dado  = insertExplicitConcatOperator(c)
# dado2 = pos_fixo(c)

# print(dado)
# print(dado2)