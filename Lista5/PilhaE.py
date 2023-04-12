class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class No():
    def __init__(self, carga: any):
        self.__carga = carga
        self.__prox = None
    
    def getCarga(self):
        return self.__carga
    
    def getProximo(self)-> 'No':
        return self.__prox
    
    def setProximo(self, novoprox: 'No'):
        self.__prox = novoprox
    
    def temProximo(self)->bool:
        return self.__prox == None

    def __str__(self):
        return f'{self.__carga}'

class Pilha():
    def __init__(self):
        self.__topo = None
        self.__tam = 0
    
    def estaVazia(self)-> bool:
        return self.__topo == None
    
    def tamanho(self) -> int:
        return self.__tam
    
    def __len__(self):
        return self.__tam
    
    def elemento(self, posicao:int)->any:
        if posicao <= 0 or posicao > self.tamanho():
            raise PilhaException(f"Posicao invalida. A pilha so tem {self.__tam} elementos.")
        
        contador = 1 
        cursor = self.__topo
        while(cursor != None):
            if contador == posicao:
                return cursor.getCarga()
            cursor = cursor.getProximo()
            contador += 1
        
                
    def busca(self, key:any)->int:
        contador = 1
        cursor = self.__topo
        while(cursor != None):
            if key == cursor.getCarga():
                return contador
            cursor = cursor.getProximo()
            contador += 1

        raise PilhaException(f"A chave {key} não está na pilha.")
    
    def empilhar(self, carga:any):
        no = No(carga)
        no.setProximo(self.__topo)
        self.__topo = no
        self.__tam += 1

    def desempilha(self):
        if self.__topo is None:
            raise PilhaException('Não há elementos para remoção. Pilha Vazia')
        carga = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tam -= 1
        return carga
    
    def topo(self):
        if self.__topo is None:
            raise PilhaException("Pilha Vazia")
        return self.__topo.getCarga
    
    def esvaziar(self):
        while (self.__tam > 0):
           self.desempilha

    def concatena( self, pilha2: 'Pilha'):
        while (pilha2.tamanho() > 0):
           self.empilhar(pilha2.desempilha())

    #def inverter(self)-> bool:
        #while not self.estaVazia():
            #self.empilhar(self.desempilha())
        
    def imprime(self):
        print(self.__str__())
        
    def __str__(self)->str:
        s = 'topo->[ '
        cursor = self.__topo
        while(cursor != None):
            s += f'{cursor.getCarga()}'
            if cursor.getProximo() is not None:
                s+= ', '
            cursor = cursor.getProximo()
        return s + "]"
    
    def clone(self) ->'Pilha': 
        clone = Pilha()
        for posicao in range(self.__len__(),0,-1):
            clone.empilha(self.elemento(posicao))
        return clone
            






