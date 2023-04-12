#from minhaPilha import Pilha
from PilhaE import Pilha

pilha1 = Pilha()
pilha2 = Pilha()
pilha2.empilhar('B')
pilha2.empilhar('A')
print("Pilha2:", pilha2)
pilha1.empilhar(10)
pilha1.empilhar(20)
pilha1.empilhar(30)
pilha1.empilhar(40)
print("pilha1:", pilha1)
pilha1.desempilha()
print("pilha depois de desempilhar:", pilha1)
pilha1.concatena(pilha2)
print(pilha1)
pilha1.esvaziar
print(pilha1)
