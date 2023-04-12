class PilhaExeption(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Pilha:

    def __init__(self):
        self.__colecao = []

    def empilhar(self, carga:any):
        self.__colecao.append(carga)

    def desempilha(self):
        if self.estaVazia():
            raise PilhaExeption("A pilha está vazia")
        return self.__colecao.pop()
    
    def tamanho(self):
        return len(self.__colecao)
    
    def topo(self):
        if self.estaVazia():
            raise PilhaExeption("A pilha está vazia")
        return self.__colecao[-1]

    def estavazia(self):
        return len(self.__colecao) == 0
    
    def inverter(self):
        self.__colecao.reverse()

    def estaVazia(self):
        while (len(self.__colecao) > 0):
            self.desempilha
    
    def concatena( self, pilha2: any):
        while (pilha2.tamanho() > 0):
            self.empilhar(pilha2.desempilha())

    def concatenaPilhas( cls, pilha1, pilha2 ):
        pass

    def __str__(self)->str:
        s="["
        for i in range(len(self.__colecao)):
            s += f'{self.__colecao[i]}, '
        return s[:-2] + '] <-topo'

