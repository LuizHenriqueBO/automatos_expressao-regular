class Automato():
    

    def __init__(self):
        self.entrada     =  list()
        self.branco      =  'E'
        self.estados     =  list()
        self.inicio      =  ''
        self.fim         =  ''
        self.transicoes  =  list()
        
        

    ############# add ############
    def adicionar_automato(self, palavra, inicio ='q0', fim ='q1'):
        if(palavra not in self.entrada):
            self.entrada.append(palavra)
        if(inicio not in self.estados):
            self.estados.append(inicio)
        if(fim not in self.estados):
            self.estados.append(fim)
        self.transicoes.append([inicio, palavra, fim])



    ############# setters ############
    def set_inicio(self, inicio):
        self.inicio = inicio

    def set_fim(self, fim):
        self.fim = fim

    ############# getters ############
    def get_inicio(self):
        return self.inicio

    def get_fim(self):
        return self.fim


    def get_inicio_by_element(self, element):
        if(element in self.estados):
            return element
        return None

    ############# print ############
    def imprimir(self):
        for entrada in self.entrada:
            print(entrada, end =" ")
        print("\n")        
        print(self.branco)
        for estados in self.estados:
            print(estados, end =" ")
        print("\n")
        print(self.inicio)     
        print(self.fim)
        for transdicao in self.transicoes:
            print(transdicao)
        print("\n")



        