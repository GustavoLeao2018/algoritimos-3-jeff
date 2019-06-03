class No:
    def __init__(self, valor=None):
        self.esquerda = None
        self.chave = None
        self.valor = valor
        self.direita = None

class Arvore:
    def __init__(self):
        self.no_raiz = None
    
    def inserir(self, valor):
        if self.no_raiz is None:
            self.no_raiz = No(valor=valor)
        else:
            self._inserir(valor=valor, no_atual=self.no_raiz)
    
    def _inserir(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor=valor)
            else:
                self._inserir(valor=valor, no_atual=no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor=valor)
            else:
                self._inserir(valor=valor, no_atual=no_atual.direita)
        else:
            print("Valor já está na na árvore!")


    def mostrar(self):
        if self.no_raiz is not None:
            self._mostrar(self.no_raiz)

    def _mostrar(self, no_atual):
        if no_atual is not None:
            self._mostrar(no_atual=no_atual.esquerda)
            print(f"{no_atual.valor}")
            self._mostrar(no_atual=no_atual.direita)    

    
    
    def pesquisar(self, valor):
        if self.no_raiz is not None:
            return self._pesquisar(valor, self.no_raiz)
        else:
            return False

    def _pesquisar(self, valor,  no_atual):
        if  valor == no_atual.valor:
            return True
        elif valor < no_atual.valor and no_atual.esquerda is not None:
            return self._pesquisar(valor, no_atual.esquerda)
        elif valor > no_atual.valor and no_atual.direita is not None:
            return self._pesquisar(valor, no_atual.direita)
        else:
            return False

    def pre_ordem(self, no, visit):
        if no is None: return 0
        visit(no)
        self.pre_ordem(no.esquerda, visit)
        self.pre_ordem(no.direita, visit)

    def em_ordem(self, no, visit):
        if no is None: return 0
        self.em_ordem(no.esquerda, visit)
        visit(no)
        self.em_ordem(no.direita, visit)

        
    def pos_ordem(self, no, visit):
        if no is None: return 0
        self.pos_ordem(no.esquerda, visit)
        self.pos_ordem(no.direita, visit)
        visit(no)

    def altura(self, no):
        if no is None: return 0
        h_esquerda = self.altura(no.esquerda)
        h_direita = self.altura(no.direita)
        return 1+max(h_esquerda, h_direita)


if __name__ == "__main__":
    from random import randint
    arvore = Arvore()
    for i in range(0, 230):
        arvore.inserir(randint(0, 100))
    
    arvore.mostrar()
    print(f"Pesquisar: {arvore.pesquisar(randint(0, 100))}")

    
    

    