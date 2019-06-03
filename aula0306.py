from random import randint


"""
Validar arvore (metodo fora da classe arvore)
Remover


testar com

     17 - 19
      |
10 - 13 - 18

não é valida!!!!!!
"""

class No:
    def __init__(self, chave, valor=randint(0, 100)): 
        self.esquerda = None
        self.chave = chave
        self.valor = valor
        self.direita = None

class Arvore:
    def __init__(self):
        self.no_raiz = None

    def inserir(self, chave, valor=randint(0, 100)):
        if self.no_raiz is None: 
            self.no_raiz = No(chave, valor)
        else:
            self._inserir(chave, valor, self.no_raiz)

    def _inserir(self, chave, valor, no_atual):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave, valor)
            else:
                self._inserir(chave, valor, no_atual.esquerda)
        elif chave > no_atual.chave:
            if no_atual.direita is None:
                no_atual.direita = No(chave, valor)
            else:
                self._inserir(chave, valor, no_atual.direita)
        else:
            raise Exception('O valor ja está na árvore')

    def mostrar(self):
        if self.no_raiz is not None:
            self._mostrar(self.no_raiz)
    
    def _mostrar(self, no_atual):
        if no_atual is not None:
            self._mostrar(no_atual.esquerda)
            print(no_atual.chave)
            self._mostrar(no_atual.direita)

